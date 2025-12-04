# AoC 2025

[Advent of Code 2025](https://adventofcode.com/2025/) in Python.

## Python

Install [Python 3](https://python.org), then:

```sh
cat examples/01 | python 01.py
```

## Rust

Install [Rust](https://rust-lang.org/), then:

```sh
rustc 01.rs && cat examples/01 | ./01
```

## Benchmarks

```sh
hyperfine --input inputs/01 'python 01.py'
hyperfine --input inputs/01 ./01
```

| Day | Python | Rust |
| --- | -----: | ---: |
| 1   |  19 ms | 4 ms |
| 2   | 110 ms |    - |

## Ahas

- **[Day 1](https://mastodon.social/@jukkasuomela.fi@bsky.brid.gy/115650037243506402)** - "Always rotate right, flip the dial if needed"

- **[Day 2](https://www.reddit.com/r/adventofcode/comments/1pc0le8/2025_day_2_part_2_time_to_reach_for_that_trusty/nrup8b2/)** - "You only have to construct the values that are made out of repeated digit strings and then see if the result is the range, not check every number in the range to see if it's made of repeated digit strings"
