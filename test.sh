#!/bin/sh

set -o errexit

diff <(cat inputs/01 | python 01.py) <(echo "1097 7101")
diff <(cat inputs/02 | python 02.py) <(echo "13108371860 22471660255")

rustc 01.rs && cat inputs/01 | ./01
