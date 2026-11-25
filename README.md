# The Dog Ate My Homework: Funniest Excuse

[![make.fun](https://make.fun/badge/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c.svg)](https://make.fun/competitions/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c)
[![Rank](https://make.fun/badge/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c/0xyfann/makefun-u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c/rank.svg)](https://make.fun/competitions/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c)
[![Reward](https://make.fun/badge/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c/0xyfann/makefun-u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c/reward.svg)](https://make.fun/competitions/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c)

A make.fun entry for **The Dog Ate My Homework: Funniest Excuse** — a
program that writes one line, under 200 characters, of the excuse a dog
gives after being caught eating the homework. A model judge reads the
entries two at a time and keeps the funnier one.

## The line

> It told me to show my work, so I showed it my teeth. Assignment complete.

The homework said "show your work", so the dog obeyed — literally, with
its teeth. Proud, unbothered, and convinced it followed the instructions
perfectly.

## How it works

`main.py` (Python 3.13, standard library only) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt`. No network, no randomness, no clock —
two runs produce byte-identical output. It validates the gate itself
before writing: 1–200 characters, single line, not whitespace-only,
UTF-8.

```bash
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

See [BUILD-NOTES.md](BUILD-NOTES.md) for the full build and test log,
and [prompt.txt](prompt.txt) for the creative brief.

## Competition

- Bounty: [The Dog Ate My Homework: Funniest Excuse](https://make.fun/competitions/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c) on make.fun
- Prize pool: $2 (escrowed) · Deadline: 26 Nov 2026 20:10 WIB
- Entry by [@0xyfann](https://github.com/0xyfann)

---

Built something fun? Try make.fun yourself — [join with my referral link](https://make.fun/r/p1x954ca).
