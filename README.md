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

| Day  | Python    | Rust      |
| ---- | --------- | --------- |
| `01` | `  19 ms` | `   4 ms` |
