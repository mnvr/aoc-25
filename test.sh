#!/bin/sh

set -o errexit

diff <(cat inputs/01 | python 01.py) <(echo "1097 7101")
diff <(cat inputs/02 | python 02.py) <(echo "13108371860 22471660255")
diff <(cat inputs/03 | python 03.py) <(echo "17031 168575096286051")
diff <(cat inputs/04 | python 04.py) <(echo "1604")

diff <(rustc 01.rs && cat inputs/01 | ./01) <(echo "1097 7101")
