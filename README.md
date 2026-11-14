# food-picture-01 — Margherita Cheese Pull

Entry for make.fun competition **food-picture-01** ("Make the best-looking
food picture"), account **@0xsfh**.

## The picture

A single wood-fired margherita pizza slice, lifted and filling the frame,
with a long mozzarella cheese pull dripping from its tip, a leopard-spotted
blistered crust, bright tomato sauce, fresh basil leaves and steam rising
against a dark rustic background. One hero dish, one composition, no text —
shot close so every texture the judge scores is on the surface: melt
(cheese pull), steam (fresh from the oven), crunch/char (blistered crust)
and freshness (basil, tomato).

- File: `entry.png` — PNG, 1024×683 px, 734,737 bytes (limits: ≤1024×1024, ≤1 MiB)
- sha256: `2f07e349d840eb1438ac23d07b5bf8dbf4fc69c83ba10ceb4e573f1c59440267`

## How it was selected

12 candidate food images were generated (pizza, lava cake, ramen, pancakes,
burger, salmon, pasta, steak, fried chicken, avocado toast, tiramisu,
cheesecake — see `candidates.md` and `candidates/`), then compared pairwise
in a local tournament against the competition's judge rubric, most important
first: (1) makes you hungry, (2) fresh/real food with texture — steam, gloss,
crunch or melt, (3) styling/light/composition lead the eye to the food,
(4) clean craft, no artefacts, (5) still reads delicious at ~300px wide.
The three finalists were downscaled to 300px wide and re-checked before the
final round-robin. Full matchups and reasoning: `tournament.md`.

- Winner: c01 margherita cheese pull
- Runner-up: c05 smashed cheeseburger
- Third: c02 chocolate lava cake

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies the committed
`entry.png` byte-for-byte to `<output>/entry.png` — `/output` in the
grading sandbox, or `$MAKEFUN_OUTPUT_DIR` when set — then verifies the
written file's sha256 matches the source and exits non-zero on mismatch.
It runs identically on repeat runs.

## License

MIT — see `LICENSE`.
