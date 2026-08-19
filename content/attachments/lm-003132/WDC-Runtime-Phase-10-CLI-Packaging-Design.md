# WDC Runtime Phase 10 CLI / Packaging Design

## Goal

Turn the Phase 0–9 Python kernel into an installable, scriptable local runtime surface without adding new cognitive semantics.

## Chosen Approach

Use the Python standard-library `argparse` stack and JSON I/O. A global `--root` identifies a WDC runtime workspace; complex command payloads use either inline JSON or `@path/to/file.json`. Commands print machine-readable JSON to stdout and human-readable errors to stderr with non-zero exit status.

This is preferred over Typer/Click because Phase 10 is a packaging surface, not a UI framework project. Zero new runtime dependencies keeps the v0.1 reference implementation portable and makes fresh-venv verification deterministic.

## Alternatives Rejected

1. **Typer/Click CLI** — nicer ergonomics and help formatting, but adds dependencies and another behavior layer before the runtime semantics are stable.
2. **REST service first** — useful later, but requires process lifecycle, networking, authentication, serialization and deployment decisions that are unnecessary for the local v0.1 surface.

## Architecture

### Runtime Workspace

A workspace contains:

```text
<root>/
  wdc.sqlite3
  blobs/
```

`RuntimeContext.open(root)` creates/opens these resources and exposes thin handles to existing services. It does not create a second business-logic layer.

### CLI Modules

```text
src/wdc/runtime.py       workspace/bootstrap context
src/wdc/cli_json.py      JSON input/output conversion helpers
src/wdc/cli.py           argparse parser + command dispatch
src/wdc/__main__.py      python -m wdc entry point
```

### Installation Surface

`pyproject.toml` adds:

```toml
[project.scripts]
wdc = "wdc.cli:main"
```

Both of these must work after installation:

```text
wdc --help
python -m wdc --help
```

## Command Surface

Global:

```text
wdc --root PATH <group> <command>
```

Workspace:

```text
wdc init
wdc status
```

TCD / candidates:

```text
wdc tcd init --json ...
wdc tcd show
wdc tcd assimilate --json ...
wdc tcd sediment --json ...
wdc candidate create --json ...
wdc candidate list
```

Worlds:

```text
wdc world create --json ...
wdc world show WORLD_ID
wdc world run-create WORLD_ID --json ...
```

Evidence:

```text
wdc evidence claim-create --json ...
wdc evidence packet-add --json ...
wdc evidence aggregate CLAIM_ID
wdc evidence counterexamples CLAIM_ID
```

Governor / portfolio:

```text
wdc governor state WORLD_ID
wdc governor allocate WORLD_ID --json ...
wdc governor kill WORLD_ID --reason ...
wdc governor promote WORLD_ID --level N --reason ...
wdc portfolio route --json ...
```

Commit:

```text
wdc commit assess --json ...
wdc commit show COMMIT_ID
wdc commit sandbox-execute COMMIT_ID --json ...
```

Learning:

```text
wdc learning component-init --json ...
wdc learning active COMPONENT
wdc learning source-anchor --json ...
wdc learning propose --json ...
wdc learning validate EVENT_ID --json ...
wdc learning rollback EVENT_ID --reason ...
wdc learning health --json ...
```

Demos:

```text
wdc demo branching-grid
wdc demo governed-evidence
wdc demo tri-temporal
wdc demo learning
```

## JSON Rules

`--json` accepts:

```text
'{"key":"value"}'
@payload.json
```

All CLI output is JSON. Dataclasses, enums, tuples and mappings are recursively normalized.

## Error Handling

Expected domain errors (`KeyError`, `ValueError`, budget/authority/history/learning conflicts) become:

```json
{"error":"<ExceptionName>","message":"..."}
```

on stderr with exit code `2`.

Unexpected exceptions are not silently translated into success.

## Packaging Rules

- No new runtime dependencies.
- `src/` layout remains authoritative.
- Installed console script must work outside the repository directory.
- Examples are copied into the package-independent source archive, but `wdc demo` calls the existing example modules through normal installed/runtime import rules.

## Test Strategy

1. Runtime workspace bootstrap creates DB/blob roots and is stable across reopen.
2. Parser/help works through both `main([...])` and `python -m wdc`.
3. TCD/candidate/world/evidence/Governor/portfolio commands round-trip through one workspace.
4. Commit/TCD sedimentation/learning commands preserve existing authority/history/source gates.
5. All four demos run through the CLI.
6. Build/install into a fresh virtual environment; verify `wdc --help`, `python -m wdc --help`, and a demo from outside the repo.
7. Full legacy suite remains green.

## Non-Goals

- network server;
- daemon/service manager;
- interactive TUI;
- auth/account system;
- remote scheduler;
- new world model adapters;
- new evidence or learning algorithms.
