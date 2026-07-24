// AMRAL shared client-side rendering helpers.
// Requires marked + KaTeX + auto-render already loaded (see each page's <script> tags).

function amralEsc(s) {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

// Minimal CSV parser: handles quoted fields with embedded commas/quotes.
function amralParseCSV(text) {
  const rows = []; let row = [], field = "", inQuotes = false;
  const s = text.replace(/\r\n/g, "\n").trim();
  for (let i = 0; i < s.length; i++) {
    const c = s[i];
    if (inQuotes) {
      if (c === '"') { if (s[i + 1] === '"') { field += '"'; i++; } else inQuotes = false; }
      else field += c;
    } else if (c === '"') inQuotes = true;
    else if (c === ",") { row.push(field); field = ""; }
    else if (c === "\n") { row.push(field); rows.push(row); row = []; field = ""; }
    else field += c;
  }
  row.push(field); rows.push(row);
  return rows;
}

// Markdown -> HTML via `marked`, with $...$ / $$...$$ math spans stashed
// behind placeholders before inline parsing (so e.g. \lambda_{\min} never
// gets misread as markdown emphasis on the underscore), then restored for
// KaTeX auto-render to pick up afterwards.
function amralRenderDoc(md) {
  const stash = [];
  const withPlaceholders = md.replace(/\$\$[\s\S]+?\$\$|\$[^$\n]+?\$/g, (m) => {
    stash.push(m);
    return `${stash.length - 1}`;
  });
  let html = marked.parse(withPlaceholders);
  html = html.replace(/(\d+)/g, (_, i) => amralEsc(stash[Number(i)]));
  return html;
}

function amralRenderMath(container) {
  renderMathInElement(container, {
    delimiters: [{ left: "$$", right: "$$", display: true }, { left: "$", right: "$", display: false }],
    throwOnError: false,
  });
}

async function amralFetchText(path) {
  const r = await fetch(path);
  if (!r.ok) throw new Error(path + ": HTTP " + r.status);
  return r.text();
}
