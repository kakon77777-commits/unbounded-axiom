/**
 * CTCL — Common Temporal Coordinate Layer (MVP Worker)
 * Neo.K's whitepaper: 共同時間座標層 / CTCL_Agent_Time_API v0.1.
 *
 * A machine-readable REFERENCE + TRANSFORMATION layer for agents — not a universal
 * clock authority. "Same instant, different representations."
 *
 *   GET  /v1/now            verified reference instant (envelope §5)
 *   GET  /v1/timescales     supported timescales
 *   GET  /v1/encodings      supported encodings
 *   POST /v1/convert        convert a time value across encodings/timescales/timezones (§7)
 *   POST /v1/transform      map a reference value into a custom linear-rate system (§8-9,12)
 *   GET  /openapi.json      OpenAPI-ish resource map (§40)
 *   GET  /ai/ctcl.json      agent tool declaration (machine discovery — call this first)
 *   GET  /                  human page: live clock + playground + agent usage
 *
 * HONESTY (§16): a Worker's wall clock is millisecond-grade. We expose ns/us FIELDS
 * for format compatibility but never claim ns ACCURACY — quality.precision says so and
 * estimated_uncertainty_ns reflects the real ~ms ceiling. /convert preserves whatever
 * precision the CALLER supplies (BigInt nanoseconds), because that is offline math, not
 * the wall clock.
 */

const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
};
const API_VERSION = "v1";
// Leap-second-dependent offsets. NOT a live leap table — current values with a caveat.
const LEAP = { tai_minus_utc_s: 37, gps_minus_utc_s: 18, as_of: "2017-01-01",
  note: "Current offsets, not a live leap table. Verify for high-stakes/scientific use." };

const NS_PER = { s: 1000000000n, ms: 1000000n, us: 1000n, ns: 1n };

function jsonResp(obj, status = 200) {
  return new Response(JSON.stringify(obj, null, 2) + "\n",
    { status, headers: { "Content-Type": "application/json; charset=utf-8", ...CORS } });
}
function ok(data, meta = {}) {
  return jsonResp({ ok: true, data, meta: { api_version: API_VERSION, request_id: rid(), ...meta } });
}
function fail(code, message, details = {}, status = 400) {
  return jsonResp({ ok: false, error: { code, message, details }, meta: { api_version: API_VERSION, request_id: rid() } }, status);
}
function rid() { return "req_" + crypto.randomUUID().replace(/-/g, "").slice(0, 20); }
function instantId() { return "ctcl:instant:" + crypto.randomUUID(); }

// ---- time core -------------------------------------------------------------

// Parse a value+encoding to canonical BigInt nanoseconds since the Unix epoch (UTC).
function toNs(value, encoding) {
  const enc = (encoding || "unix_s").toLowerCase();
  if (enc === "rfc3339" || enc === "iso8601") {
    const s = String(value).trim();
    const base = Date.parse(s.replace(/(\.\d+)?(Z|[+\-]\d{2}:?\d{2})?$/, (m, frac, tz) => (tz || "Z")));
    if (Number.isNaN(base)) throw { code: "INVALID_TIME_VALUE", msg: `unparseable rfc3339: ${s}` };
    const fm = s.match(/\.(\d{1,9})/);
    const frac = fm ? BigInt(fm[1].padEnd(9, "0")) : 0n;
    // base already includes ms; strip its ms, re-add full-precision fractional seconds
    return BigInt(Math.floor(base / 1000)) * NS_PER.s + frac;
  }
  const unit = enc.replace(/^unix_/, "");
  if (!NS_PER[unit]) throw { code: "UNKNOWN_ENCODING", msg: `unknown encoding: ${encoding}` };
  const str = String(value).trim();
  if (!/^-?\d+(\.\d+)?$/.test(str)) throw { code: "INVALID_TIME_VALUE", msg: `not numeric: ${value}` };
  const [ip, fp = ""] = str.split(".");
  let ns = BigInt(ip) * NS_PER[unit];
  // fractional part of the unit -> nanoseconds (e.g. 0.5 unix_s = 5e8 ns), sign-aware
  if (fp) {
    const fracNs = BigInt(Math.round(Number("0." + fp) * Number(NS_PER[unit])));
    ns += ip.trimStart().startsWith("-") ? -fracNs : fracNs;
  }
  return ns;
}

// Encode canonical ns to a target encoding string. tz (IANA) only affects rfc3339.
function fromNs(ns, encoding, tz) {
  const enc = (encoding || "unix_s").toLowerCase();
  if (enc === "rfc3339" || enc === "iso8601") return rfc3339(ns, tz);
  const unit = enc.replace(/^unix_/, "");
  if (!NS_PER[unit]) throw { code: "UNKNOWN_ENCODING", msg: `unknown encoding: ${encoding}` };
  const whole = ns / NS_PER[unit];
  const rem = ns % NS_PER[unit];
  if (rem === 0n) return whole.toString();
  const fracDigits = String(NS_PER[unit]).length - 1;
  return whole.toString() + "." + (rem < 0n ? -rem : rem).toString().padStart(fracDigits, "0").replace(/0+$/, "");
}

function pad(n, w = 2) { return String(n).padStart(w, "0"); }

// Build an RFC3339 string (with up to 9 fractional digits) for canonical ns, optional IANA tz.
function rfc3339(ns, tz) {
  const ms = Number(ns / NS_PER.ms);
  const subMs = ns % NS_PER.ms; // 0..999999 ns
  const nanoStr = (ns % NS_PER.s < 0n ? 0n : ns % NS_PER.s).toString().padStart(9, "0").replace(/0+$/, "");
  const d = new Date(ms);
  if (!tz || tz.toUpperCase() === "UTC" || tz === "Z") {
    const iso = d.toISOString().replace(/\.\d+Z$/, "");
    return iso + (nanoStr ? "." + nanoStr : "") + "Z";
  }
  const off = tzOffsetMinutes(ms, tz);
  const local = new Date(ms + off * 60000);
  const sign = off >= 0 ? "+" : "-";
  const ao = Math.abs(off);
  const base = `${local.getUTCFullYear()}-${pad(local.getUTCMonth() + 1)}-${pad(local.getUTCDate())}` +
    `T${pad(local.getUTCHours())}:${pad(local.getUTCMinutes())}:${pad(local.getUTCSeconds())}`;
  return base + (nanoStr ? "." + nanoStr : "") + `${sign}${pad(Math.floor(ao / 60))}:${pad(ao % 60)}`;
}

// Offset (minutes) of an IANA tz at a given UTC ms, via the Intl formatToParts diff trick.
function tzOffsetMinutes(ms, tz) {
  const dtf = new Intl.DateTimeFormat("en-US", { timeZone: tz, hour12: false,
    year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit", second: "2-digit" });
  const p = {};
  for (const { type, value } of dtf.formatToParts(new Date(ms))) p[type] = value;
  const asUTC = Date.UTC(+p.year, +p.month - 1, +p.day, +(p.hour === "24" ? "0" : p.hour), +p.minute, +p.second);
  return Math.round((asUTC - ms) / 60000);
}

function nowEnvelope() {
  const ms = Date.now();
  const ns = BigInt(ms) * NS_PER.ms;
  const iso = new Date(ms).toISOString();
  return {
    instant: { id: instantId(), reference: { timescale: "utc", value: iso } },
    ...instantViews(ns),
    source: { class: "edge_wall_clock", protocol: "cloudflare-edge", provider: "cloudflare", sync_status: "synchronized" },
    quality: {
      precision: "millisecond_representation", estimated_uncertainty_ns: 5000000, synchronized: true,
      note: "ns/us fields are zero-padded from a millisecond source. precision != accuracy (whitepaper §16).",
    },
    policy: { leap_second: "posix_compatible", leap_table: LEAP },
  };
}

// ---- instant views (shared by /v1/now and the registry) -------------------
function instantViews(ns) {
  const iso = rfc3339(ns, "UTC");
  return {
    encodings: {
      unix_s: fromNs(ns, "unix_s"), unix_ms: fromNs(ns, "unix_ms"),
      unix_us: fromNs(ns, "unix_us"), unix_ns: fromNs(ns, "unix_ns"), rfc3339: iso,
    },
    timescales: {
      utc: iso, posix: fromNs(ns, "unix_s"),
      tai_approx: fromNs(ns + BigInt(LEAP.tai_minus_utc_s) * NS_PER.s, "unix_s"),
      gps_approx: fromNs(ns + BigInt(LEAP.gps_minus_utc_s) * NS_PER.s, "unix_s"),
    },
  };
}

// ---- Phase 2: KV-backed instant registry + persistent custom systems -------
// Instants (§6/§27): agent A registers a reference instant I*, agent B retrieves it
// by id and aligns on the SAME instant — the multi-agent temporal-alignment core.
// Systems (§10/§11): persistent custom linear-rate clocks (game worlds, accel sims).
// Graceful 503 when KV is unbound so /v1/now and the stateless endpoints still work.
function kvMissing() { return fail("REGISTRY_UNAVAILABLE", "KV registry not configured on this deployment", {}, 503); }
function uuidOf(id) { return String(id).replace(/^ctcl:instant:/, "").replace(/^instant:/, ""); }

async function registerInstant(req, env) {
  if (!env || !env.CTCL_KV) return kvMissing();
  let body = {};
  try { body = await req.json(); } catch { /* empty body -> register the current instant */ }
  let ns;
  try { ns = body.value != null ? toNs(body.value, body.encoding) : BigInt(Date.now()) * NS_PER.ms; }
  catch (e) { return fail(e.code || "INVALID_TIME_VALUE", e.msg || String(e)); }
  const id = instantId();
  const rec = {
    id, unix_ns: ns.toString(), reference_timescale: body.timescale || "utc",
    registered_at: new Date().toISOString(), label: body.label || null, meta: body.meta || null,
    from_wall_clock: body.value == null,
  };
  await env.CTCL_KV.put("instant:" + uuidOf(id), JSON.stringify(rec));
  return ok({ ...rec, retrieve: `/v1/instant/${id}`, ...instantViews(ns) },
    { note: "Registered. Any agent can GET /v1/instant/{id} to align on this exact instant (§27). Store the id in memory, not a bare number." });
}

async function getInstant(id, env) {
  if (!env || !env.CTCL_KV) return kvMissing();
  const raw = await env.CTCL_KV.get("instant:" + uuidOf(id));
  if (!raw) return fail("UNKNOWN_INSTANT", `no registered instant: ${id}`, {}, 404);
  const rec = JSON.parse(raw);
  return ok({ ...rec, ...instantViews(BigInt(rec.unix_ns)) });
}

async function createSystem(req, env) {
  if (!env || !env.CTCL_KV) return kvMissing();
  let body;
  try { body = await req.json(); } catch { return fail("INVALID_TIME_VALUE", "body must be JSON"); }
  const sys = body.system || body;
  if (!sys.id) return fail("INVALID_TIME_VALUE", "system.id required (e.g. user:game_world)");
  const rate = Number(sys.rate?.value ?? sys.rate ?? 1);
  if (!Number.isFinite(rate)) return fail("UNSUPPORTED_POLICY", "rate must be a finite number");
  const rec = {
    id: sys.id, parent: sys.parent || "ctcl:system:unix",
    epoch: sys.epoch || { parent_value: "0", encoding: "unix_s" },
    rate: { type: "constant", value: rate }, offset: Number(sys.offset ?? 0),
    calendar: sys.calendar || null, created_at: new Date().toISOString(),
  };
  await env.CTCL_KV.put("system:" + sys.id, JSON.stringify(rec));
  return ok({ ...rec, now: `/v1/systems/${encodeURIComponent(sys.id)}/now` });
}

async function getSystem(id, env) {
  if (!env || !env.CTCL_KV) return kvMissing();
  const raw = await env.CTCL_KV.get("system:" + id);
  if (!raw) return fail("UNKNOWN_SYSTEM", `no such system: ${id}`, {}, 404);
  return ok(JSON.parse(raw));
}

async function systemNow(id, env) {
  if (!env || !env.CTCL_KV) return kvMissing();
  const raw = await env.CTCL_KV.get("system:" + id);
  if (!raw) return fail("UNKNOWN_SYSTEM", `no such system: ${id}`, {}, 404);
  const sys = JSON.parse(raw);
  let epochNs;
  try { epochNs = toNs(sys.epoch?.parent_value ?? 0, sys.epoch?.encoding || "unix_s"); }
  catch { epochNs = 0n; }
  const nowNs = BigInt(Date.now()) * NS_PER.ms;
  const localSec = sys.rate.value * (Number(nowNs) / 1e9 - Number(epochNs) / 1e9) + (sys.offset || 0);
  let calendar = null;
  const cal = sys.calendar;
  if (cal && cal.day_seconds && cal.year_days) {
    const days = Math.floor(localSec / cal.day_seconds);
    calendar = { world_year: Math.floor(days / cal.year_days), world_day: (days % cal.year_days) + 1,
      seconds_into_day: Math.floor(((localSec % cal.day_seconds) + cal.day_seconds) % cal.day_seconds) };
  }
  return ok({ system_id: sys.id, reference: { timescale: "utc", value: rfc3339(nowNs, "UTC") },
    system_time: String(localSec), unit: "second", rate: sys.rate.value, calendar });
}

// ---- endpoints -------------------------------------------------------------

async function handleConvert(req) {
  let body;
  try { body = await req.json(); } catch { return fail("INVALID_TIME_VALUE", "body must be JSON"); }
  const input = body.input || {};
  const output = body.output || {};
  let ns;
  try { ns = toNs(input.value, input.encoding); }
  catch (e) { return fail(e.code || "INVALID_TIME_VALUE", e.msg || String(e), { input }); }
  let outValue;
  try { outValue = fromNs(ns, output.encoding || "rfc3339", output.timezone); }
  catch (e) { return fail(e.code || "UNKNOWN_ENCODING", e.msg || String(e), { output }); }
  // lossless only if the output encoding can represent the canonical ns without truncation
  const outUnit = (output.encoding || "rfc3339").toLowerCase().replace(/^unix_/, "");
  const lossless = (outUnit === "ns") || (NS_PER[outUnit] && ns % NS_PER[outUnit] === 0n) ||
    ((output.encoding || "rfc3339").match(/rfc3339|iso8601/) && ns % NS_PER.ns === 0n);
  return ok({
    input, output: { value: outValue, encoding: output.encoding || "rfc3339", timescale: output.timescale || "utc", timezone: output.timezone || "UTC" },
    canonical_unix_ns: ns.toString(),
    transform: { path: [(input.timescale || "posix"), (output.timescale || "utc")], type: "encoding_timescale" },
    quality: { lossless: !!lossless, loss: lossless ? null : { type: "precision_truncation" } },
  });
}

async function handleTransform(req) {
  let body;
  try { body = await req.json(); } catch { return fail("INVALID_TIME_VALUE", "body must be JSON"); }
  const sys = body.system || {};
  const rate = Number(sys.rate?.value ?? sys.rate ?? 1);
  const offset = Number(sys.offset ?? 0);
  const epochEnc = sys.epoch?.encoding || body.value_encoding || "unix_s";
  let parentNs, epochNs;
  try {
    parentNs = toNs(body.value, body.value_encoding || "unix_s");
    epochNs = toNs(sys.epoch?.parent_value ?? sys.epoch ?? 0, epochEnc);
  } catch (e) { return fail(e.code || "INVALID_TIME_VALUE", e.msg || String(e)); }
  if (!(rate > 0) && rate !== 0) return fail("UNSUPPORTED_POLICY", "rate must be a finite number");
  // local_seconds = rate * (parent_seconds - epoch_seconds) + offset
  const parentSec = Number(parentNs) / 1e9, epochSec = Number(epochNs) / 1e9;
  const localSec = rate * (parentSec - epochSec) + offset;
  let calendar = null;
  if (sys.calendar?.day_seconds && sys.calendar?.year_days) {
    const day = sys.calendar.day_seconds, year = sys.calendar.year_days;
    const days = Math.floor(localSec / day);
    calendar = { world_year: Math.floor(days / year), world_day: (days % year) + 1,
      seconds_into_day: Math.floor(localSec % day) };
  }
  return ok({
    system: { id: sys.id || "user:custom", parent: sys.parent || "ctcl:system:unix", rate, offset },
    value: String(localSec), unit: "second", transform_type: "linear_rate",
    formula: "local = rate*(parent - epoch) + offset", calendar,
    quality: { lossless: false, note: "float64 seconds; sub-ms and long-range precision limited" },
  });
}

function toolDeclaration(origin) {
  return {
    schema: "aicl-tool/0.1", service: "CTCL", version: "0.1",
    title: "Common Temporal Coordinate Layer",
    summary: "Verified reference instant + heterogeneous time transformation for agents. Read this, then call the endpoints. Same instant, different representations.",
    base_url: origin, runtime_enabled: true,
    core_rule: "Do not ask only 'what time is it'. Ask: which reference instant, under which timescale, from which source, transformed into which local system.",
    honesty: "Source is a millisecond-grade edge wall clock. ns/us fields are format-padding; check quality.precision + estimated_uncertainty_ns before trusting sub-ms.",
    tools: [
      { name: "now", method: "GET", path: "/v1/now", desc: "Verified reference instant: encodings, timescales, source, uncertainty, policy, a stable instant_id.", input: {}, output: "instant+encodings+timescales+source+quality+policy" },
      { name: "timescales", method: "GET", path: "/v1/timescales", desc: "Supported timescales.", input: {}, output: "list" },
      { name: "encodings", method: "GET", path: "/v1/encodings", desc: "Supported encodings.", input: {}, output: "list" },
      { name: "convert", method: "POST", path: "/v1/convert", desc: "Convert a time value across encodings/timescales/timezones (precision-preserving).",
        input: { input: { value: "string", encoding: "unix_s|unix_ms|unix_us|unix_ns|rfc3339", timescale: "utc|posix" }, output: { encoding: "…", timezone: "IANA (optional)" } },
        output: "output.value + canonical_unix_ns + quality.lossless" },
      { name: "transform", method: "POST", path: "/v1/transform", desc: "Map a reference (parent) time into a custom linear-rate system (game world / accelerated sim / child clock).",
        input: { value: "string (parent time)", value_encoding: "unix_s", system: { parent: "ctcl:system:unix", epoch: { parent_value: "unix_s" }, rate: { value: "number" }, offset: "number", calendar: { day_seconds: "int", year_days: "int" } } },
        output: "system time + optional world calendar" },
      { name: "register-instant", method: "POST", path: "/v1/instants", desc: "Register a reference instant I* (the current instant, or a given value) → get a shareable id. THE multi-agent primitive: another agent GETs that id and aligns on the exact same instant.",
        input: { value: "string? (default: now)", encoding: "unix_s|…?", timescale: "utc?", label: "string?", meta: "object?" }, output: "instant_id + retrieve URL + all encodings/timescales" },
      { name: "get-instant", method: "GET", path: "/v1/instant/{id}", desc: "Retrieve a registered instant by id — aligns you on the same I* another agent registered.",
        input: { id: "ctcl:instant:… or bare uuid" }, output: "instant record + all encodings/timescales" },
      { name: "create-system", method: "POST", path: "/v1/systems", desc: "Persist a custom linear-rate time system (game world / accelerated sim / child clock) for reuse.",
        input: { id: "user:game_world", parent: "ctcl:system:unix", epoch: { parent_value: "unix_s" }, rate: { value: "number" }, offset: "number?", calendar: { day_seconds: "int", year_days: "int" } }, output: "system record + /now URL" },
      { name: "get-system", method: "GET", path: "/v1/systems/{id}", desc: "Retrieve a stored system definition.", input: { id: "string" }, output: "system record" },
      { name: "system-now", method: "GET", path: "/v1/systems/{id}/now", desc: "Current time in a stored custom system (+ world calendar).", input: { id: "string" }, output: "system_time + reference instant + calendar" },
    ],
    memory_contract: "For long-term memory: store instant_id + timescale + encoding + source_quality (do not store only a bare number). Distinguish event / write / recall instants (§10.4, §23).",
    not_a: ["universal clock authority", "timing/NTP replacement", "guaranteed ns-accurate global sync"],
    whitepaper: "CTCL_Agent_Time_API v0.1 (Neo.K / EveMissLab)",
  };
}

function openapi(origin) {
  return {
    openapi: "3.0.0",
    info: { title: "CTCL — Common Temporal Coordinate Layer", version: "0.1",
      description: "Reference + transformation layer for agents. MVP." },
    servers: [{ url: origin }],
    paths: {
      "/v1/now": { get: { summary: "Verified reference instant", responses: { 200: { description: "instant envelope" } } } },
      "/v1/timescales": { get: { summary: "List timescales", responses: { 200: { description: "ok" } } } },
      "/v1/encodings": { get: { summary: "List encodings", responses: { 200: { description: "ok" } } } },
      "/v1/convert": { post: { summary: "Convert time value", responses: { 200: { description: "ok" }, 400: { description: "error" } } } },
      "/v1/transform": { post: { summary: "Map into a custom linear-rate system", responses: { 200: { description: "ok" } } } },
      "/v1/instants": { post: { summary: "Register a reference instant (multi-agent I*)", responses: { 200: { description: "ok" }, 503: { description: "registry unavailable" } } } },
      "/v1/instant/{id}": { get: { summary: "Retrieve a registered instant", responses: { 200: { description: "ok" }, 404: { description: "unknown instant" } } } },
      "/v1/systems": { post: { summary: "Create a persistent custom system", responses: { 200: { description: "ok" } } } },
      "/v1/systems/{id}": { get: { summary: "Get a system definition", responses: { 200: { description: "ok" }, 404: { description: "unknown system" } } } },
      "/v1/systems/{id}/now": { get: { summary: "Current time in a custom system", responses: { 200: { description: "ok" } } } },
    },
  };
}

// ---- router ----------------------------------------------------------------

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const p = url.pathname.replace(/\/+$/, "") || "/";
    const origin = url.origin;
    if (request.method === "OPTIONS") return new Response(null, { headers: CORS });

    if (p === "/v1/now") return ok(nowEnvelope(), { server_observed_at: new Date().toISOString() });
    if (p === "/v1/timescales") return ok({ timescales: [
      { id: "utc", type: "reference", note: "Civil reference; includes leap seconds." },
      { id: "posix", type: "encoding", note: "Unix time; POSIX ignores leap seconds." },
      { id: "tai", type: "reference", note: `Atomic; ≈ UTC + ${LEAP.tai_minus_utc_s}s (${LEAP.as_of}). Offset caveat applies.` },
      { id: "gps", type: "reference", note: `≈ UTC + ${LEAP.gps_minus_utc_s}s (${LEAP.as_of}). Offset caveat applies.` },
    ], leap_table: LEAP });
    if (p === "/v1/encodings") return ok({ encodings: [
      "unix_s", "unix_ms", "unix_us", "unix_ns", "rfc3339", "iso8601",
    ], note: "convert preserves caller-supplied precision via BigInt nanoseconds." });
    if (p === "/v1/convert" && request.method === "POST") return handleConvert(request);
    if (p === "/v1/transform" && request.method === "POST") return handleTransform(request);
    if (p === "/v1/instants" && request.method === "POST") return registerInstant(request, env);
    if (p.startsWith("/v1/instant/")) return getInstant(decodeURIComponent(p.slice(12)), env);
    if (p === "/v1/systems" && request.method === "POST") return createSystem(request, env);
    if (p.startsWith("/v1/systems/")) {
      const rest = decodeURIComponent(p.slice(12));
      if (rest.endsWith("/now")) return systemNow(rest.slice(0, -4), env);
      return getSystem(rest, env);
    }
    if (p === "/openapi.json") return jsonResp(openapi(origin));
    if (p === "/ai/ctcl.json" || p === "/.well-known/ctcl.json") return jsonResp(toolDeclaration(origin));
    if (p === "/" || p === "/index.html") return new Response(page(origin), { headers: { "Content-Type": "text/html; charset=utf-8", ...CORS } });

    return fail("NOT_FOUND", `no route: ${p}`, { try: ["/v1/now", "/ai/ctcl.json", "/"] }, 404);
  },
};

// ---- human page ------------------------------------------------------------

function page(origin) {
  return `<!doctype html><html lang="zh-Hant"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>CTCL · Common Temporal Coordinate Layer</title>
<meta name="description" content="共同時間座標層 — 給 agent 的驗證參考瞬間與異質時間轉換層。Same instant, different representations.">
<style>
:root{--bg:#0b0d10;--ink:#e8e6df;--dim:#9aa0a6;--faint:#6b7178;--gold:#c9a227;--line:#20242a;--surf:#12151a;--mono:'SF Mono',ui-monospace,'Cascadia Code',Menlo,Consolas,monospace}
*{margin:0;padding:0;box-sizing:border-box}
body{background:var(--bg);color:var(--ink);font:15px/1.65 ui-sans-serif,system-ui,'Segoe UI',sans-serif;-webkit-font-smoothing:antialiased}
.wrap{max-width:880px;margin:0 auto;padding:clamp(1.4rem,4vw,3rem)}
.eyebrow{font:600 .7rem/1 var(--mono);letter-spacing:.24em;text-transform:uppercase;color:var(--faint)}
h1{font-size:clamp(1.7rem,5vw,2.6rem);font-weight:650;letter-spacing:-.01em;margin:.5rem 0 .3rem}
.lede{color:var(--dim);max-width:60ch;margin:.4rem 0 0}
.clock{margin:2rem 0;padding:1.3rem 1.4rem;border:1px solid var(--line);border-radius:.7rem;background:var(--surf)}
.clock .row{display:flex;justify-content:space-between;gap:1rem;flex-wrap:wrap;font-family:var(--mono);font-size:.9rem;padding:.28rem 0}
.clock .k{color:var(--faint)}.clock .v{color:var(--gold);word-break:break-all;text-align:right}
h2{font-size:1.15rem;margin:2.4rem 0 .8rem;font-weight:620}
p{color:var(--dim);margin:.7rem 0}
code,pre{font-family:var(--mono);font-size:.85em}
code{background:#1a1e24;padding:.1em .4em;border-radius:4px;color:var(--ink)}
pre{background:#0f1216;border:1px solid var(--line);border-radius:.6rem;padding:1rem 1.1rem;overflow-x:auto;margin:.8rem 0;color:var(--ink);line-height:1.55}
.grid{display:grid;gap:.7rem;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));margin:.8rem 0}
.ep{border:1px solid var(--line);border-radius:.5rem;padding:.7rem .8rem;background:var(--surf)}
.ep .m{font:600 .68rem/1 var(--mono);letter-spacing:.1em;color:var(--gold)}
.ep .path{font-family:var(--mono);font-size:.82rem;margin:.25rem 0}
.ep .d{font-size:.8rem;color:var(--faint)}
button{font:inherit;background:var(--gold);color:#141414;border:0;border-radius:.4rem;padding:.5rem 1rem;font-weight:600;cursor:pointer}
.muted{color:var(--faint);font-size:.85rem}
a{color:var(--gold)}
footer{margin:3rem 0 1rem;color:var(--faint);font-size:.82rem;border-top:1px solid var(--line);padding-top:1.2rem}
</style></head><body><div class="wrap">
<div class="eyebrow">EveMissLab · Agent Time Infrastructure</div>
<h1>共同時間座標層 · CTCL</h1>
<p class="lede">給 agent 的<b>驗證參考瞬間</b>與異質時間轉換層。不是「現在幾點」，而是「我們共同指向哪一個參考瞬間，它在你的世界裡如何表示」。<br><span class="muted">Same instant, different representations. A reference layer, not a clock authority.</span></p>

<div class="clock" id="clock">
  <div class="row"><span class="k">CTCL /v1/now (edge, verified)</span><span class="v" id="c-utc">…</span></div>
  <div class="row"><span class="k">unix_ns (ms-padded)</span><span class="v" id="c-ns">…</span></div>
  <div class="row"><span class="k">instant_id</span><span class="v" id="c-id">…</span></div>
  <div class="row"><span class="k">你的瀏覽器本機時間</span><span class="v" id="c-local">…</span></div>
  <div class="row"><span class="k">兩者差 (drift)</span><span class="v" id="c-drift">…</span></div>
</div>
<p class="muted">↑ 三個時鐘：CTCL 邊緣參考、你的本機、與其漂移。這正是「異質時間系統需要共同參考層」的最小演示。精度誠實標為毫秒級（§16）。</p>

<h2>端點 Endpoints</h2>
<div class="grid">
  <div class="ep"><div class="m">GET</div><div class="path">/v1/now</div><div class="d">驗證參考瞬間（含來源、不確定度、instant_id）</div></div>
  <div class="ep"><div class="m">POST</div><div class="path">/v1/convert</div><div class="d">跨編碼/時標/時區轉換（保精度）</div></div>
  <div class="ep"><div class="m">POST</div><div class="path">/v1/transform</div><div class="d">映射到自定義倍速世界時間</div></div>
  <div class="ep"><div class="m">POST</div><div class="path">/v1/instants</div><div class="d">登記共同瞬間 I*，回可共享 id（多 agent 對齊）</div></div>
  <div class="ep"><div class="m">GET</div><div class="path">/v1/instant/{id}</div><div class="d">取回別的 agent 登記的同一瞬間</div></div>
  <div class="ep"><div class="m">POST</div><div class="path">/v1/systems</div><div class="d">建立持久自定義世界時鐘</div></div>
  <div class="ep"><div class="m">GET</div><div class="path">/v1/systems/{id}/now</div><div class="d">該世界當前時間＋世界曆</div></div>
  <div class="ep"><div class="m">GET</div><div class="path">/v1/timescales</div><div class="d">支援的時標</div></div>
  <div class="ep"><div class="m">GET</div><div class="path">/v1/encodings</div><div class="d">支援的編碼</div></div>
  <div class="ep"><div class="m">GET</div><div class="path">/ai/ctcl.json</div><div class="d">agent 工具宣告（先讀這個）</div></div>
</div>

<h2>本地 agent 怎麼調用</h2>
<p>Agent 先讀 <code>/ai/ctcl.json</code> 發現能力，再呼叫端點。取得驗證瞬間：</p>
<pre>curl -s ${origin}/v1/now</pre>
<p>把一個 Unix 奈秒值轉成台北時間（保精度）：</p>
<pre>curl -s ${origin}/v1/convert -H 'content-type: application/json' -d '{
  "input":  {"value":"1783420000.123456789","encoding":"unix_s"},
  "output": {"encoding":"rfc3339","timezone":"Asia/Taipei"}
}'</pre>
<p>映射到一個 12 倍速、一年 400 天的遊戲世界：</p>
<pre>curl -s ${origin}/v1/transform -H 'content-type: application/json' -d '{
  "value":"1783420000","value_encoding":"unix_s",
  "system":{"parent":"ctcl:system:unix","epoch":{"parent_value":"1780000000"},
            "rate":{"value":12},"calendar":{"day_seconds":72000,"year_days":400}}
}'</pre>

<h2>試一下 Playground</h2>
<p class="muted">轉換：把左邊的 Unix 秒轉成右邊時區的 RFC3339。</p>
<div style="display:flex;gap:.6rem;flex-wrap:wrap;align-items:center;margin:.6rem 0">
  <input id="pv" value="1783420000.5" style="font-family:var(--mono);background:#0f1216;border:1px solid var(--line);color:var(--ink);border-radius:.4rem;padding:.5rem .6rem;width:190px">
  <input id="ptz" value="Asia/Taipei" style="font-family:var(--mono);background:#0f1216;border:1px solid var(--line);color:var(--ink);border-radius:.4rem;padding:.5rem .6rem;width:150px">
  <button onclick="tryConvert()">convert →</button>
</div>
<pre id="pout" style="min-height:2.5em">…</pre>

<footer>
CTCL v0.1 · MVP · <a href="/openapi.json">OpenAPI</a> · <a href="/ai/ctcl.json">agent tool decl</a><br>
Neo.K / 一言諾科技有限公司 · EveMissLab. Reference + transformation layer, not a timing authority.
</footer>
</div>
<script>
const O=location.origin;
async function tick(){
 try{
  const t0=performance.now();
  const r=await (await fetch(O+'/v1/now')).json();
  const rtt=(performance.now()-t0);
  const d=r.data;
  document.getElementById('c-utc').textContent=d.instant.reference.value;
  document.getElementById('c-ns').textContent=d.encodings.unix_ns;
  document.getElementById('c-id').textContent=d.instant.id;
  const localMs=Date.now(), srvMs=Number(d.encodings.unix_ms);
  document.getElementById('c-local').textContent=new Date(localMs).toISOString();
  const drift=localMs-srvMs;
  document.getElementById('c-drift').textContent=(drift>=0?'+':'')+drift+' ms (± RTT '+rtt.toFixed(0)+'ms)';
 }catch(e){document.getElementById('c-utc').textContent='(offline)';}
}
async function tryConvert(){
 const body={input:{value:document.getElementById('pv').value,encoding:'unix_s'},
  output:{encoding:'rfc3339',timezone:document.getElementById('ptz').value}};
 try{
  const r=await (await fetch(O+'/v1/convert',{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify(body)})).json();
  document.getElementById('pout').textContent=JSON.stringify(r.ok?r.data:r,null,2);
 }catch(e){document.getElementById('pout').textContent=String(e);}
}
tick(); setInterval(tick,2000);
</script></body></html>`;
}
