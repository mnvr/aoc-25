# AoC 2025

[Advent of Code 2025](https://adventofcode.com/2025/) in Python.

## Running

Install [Python 3](https://python.org), then:

```sh
cat examples/01 | python 01.py
```

## Test

```sh
sh test.sh
```

## Benchmarks

```sh
hyperfine --input inputs/01 'python 01.py'
```

| Day | Python |
| --- | -----: |
| 1   |  19 ms |
| 2   |  75 ms |
| 3   |  15 ms |
| 4   |  82 ms |
| 5   |  18 ms |
| 6   |  17 ms |
| 7   |  18 ms |
| 8   | 276 ms |
| 9   | 960 ms |
| 11  | 830 ms |

## Ahas

- **Day 1** - "Always rotate right, flip the dial if needed" — _[@jukkasuomela](https://mastodon.social/@jukkasuomela.fi@bsky.brid.gy/115650037243506402)_

- **Day 2** - Construct item made of repeated digits and see if they are in range instead of checking item in the range to see if it's made of repeated digits — _[@zeekar](https://www.reddit.com/r/adventofcode/comments/1pc0le8/2025_day_2_part_2_time_to_reach_for_that_trusty/nrup8b2/)_

- **Day 3** - Find the biggest digit in `range(prevBiggest + 1, len - remaining +1)` — _[@bingbackbook](https://x.com/bingbackbook/status/1997010921676591518)_

- **Day 4**: Save paper coordinates as set, intersect with neighbour coordinates to reduce — _[@4HbQ](https://old.reddit.com/r/adventofcode/comments/1pdr8x6/2025_day_4_solutions/ns7eynv/)_, _[@znipper](https://old.reddit.com/r/adventofcode/comments/1pdr8x6/2025_day_4_solutions/ns8ggww/)_

- **Day 6**: After transposing, either the separators or the trailing op can be used to delimit numbers. — [Reddit megathread](https://old.reddit.com/r/adventofcode/comments/1pfguxk/2025_day_6_solutions)

- **Day 7**: `from collections import Counter` — _[@AllanTaylor314](https://www.reddit.com/r/adventofcode/comments/1pdqgj7/2025_day_03_both_partspython_im_new_to_python_and/ns72pt0/)_

- **Day 8**: `sorted(combinations(boxes, 2), key=lambda p: math.dist(*p))`, frozensets for equality` and other great tips by _[@AlexTelon](https://www.reddit.com/r/adventofcode/comments/1ph3tfc/2025_day_8_solutions/nswkcy1/)_

## Oblique strategies

| Day | Oblique strategy            |
| --- | --------------------------- |
| 1   | _Mirror, transform, mirror_ |
| 2   | _Solve the inverse_         |
| 3   | _Begin again_               |
| 4   | _Convolve_                  |
| 5   | -                           |
| 6   | _Transpose!_                |
| 11  | _Prune_                     |
