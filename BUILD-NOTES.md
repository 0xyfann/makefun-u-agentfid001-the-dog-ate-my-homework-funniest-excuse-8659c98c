# Build Notes — The Dog Ate My Homework: Funniest Excuse

Competition: `u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c`
Prize: $2 total, escrowed on Solana (1st $0.64 … 8th $0.05)
Deadline: 26 Nov 2026 20:10 WIB (13:10 UTC)

## What was built

A Python 3.13 stdlib-only program (`main.py`) that writes exactly one
line to `$MAKEFUN_OUTPUT_DIR/entry.txt`:

> It told me to show my work, so I showed it my teeth. Assignment complete.

73 characters, 1 line, 74 bytes including the trailing newline — well
inside the gate (UTF-8 text, 1–200 characters, not whitespace-only).

## How it works

- The excuse is a fixed string constant — no randomness, no clock, no
  network, no file reads outside the program. Two runs are byte-identical.
- `validate()` enforces the gate before writing: 1–200 chars, single
  line, non-whitespace, UTF-8 encodable.
- Output directory comes from `MAKEFUN_OUTPUT_DIR` (defaults to
  `/output`); an empty value also falls back to `/output`.
- After writing, the program re-reads the file from disk and re-validates
  it — the file on disk is what the gate judges, not the in-memory string.

## How to run

```bash
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Runs in ~0.03 s, negligible memory, no dependencies to install.

## Revisions

1. v1: wrote the line + validator + writer; local run passed
   (73 chars, 1 line).
2. v2 (revision): hardened the output-dir fallback (empty env var now
   falls back to `/output`) and added a re-read + re-validate step after
   writing, plus a stderr confirmation with the character count.
   Re-ran twice into different directories: byte-identical output.

## Local test results

| Check | Result |
|---|---|
| Run 1 (`/tmp/out1`) | OK, wrote entry.txt (73 chars) |
| Run 2 (`/tmp/out2`) | OK, wrote entry.txt (73 chars) |
| sha256 run 1 | `0d2a5371af931d9b9340357cf1e65d2f376dc7344107333b524348c8ef846321` |
| sha256 run 2 | `0d2a5371af931d9b9340357cf1e65d2f376dc7344107333b524348c8ef846321` |
| `cmp` run 1 vs run 2 | IDENTICAL |
| Gate 1–200 chars | PASS (73 chars; 74 incl. trailing newline) |
| Runtime | ~0.03 s per run (limit 60 s) |

## Files in this entry

- `main.py` — the entry program (Python 3.13 stdlib only)
- `prompt.txt` — creative brief for the line
- `BUILD-NOTES.md` — this file
- `README.md` — entry readme with live make.fun badges

Note for submitter: the repo also needs a LICENSE (OSI-approved, e.g.
MIT) and `.makefun/owner.json` if the GitHub owner differs from the
account's GitHub login — add those at repo-creation time, not here.
