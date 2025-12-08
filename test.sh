#!/bin/sh

set -o errexit

diff <(cat inputs/01 | python 01.py) <(echo "1097 7101")
diff <(cat inputs/02 | python 02.py) <(echo "13108371860 22471660255")
diff <(cat inputs/03 | python 03.py) <(echo "17031 168575096286051")
diff <(cat inputs/04 | python 04.py) <(echo "1604 9397")
diff <(cat inputs/05 | python 05.py) <(echo "664 350780324308385")
diff <(cat inputs/06 | python 06.py) <(echo "3785892992137 7669802156452")
diff <(cat inputs/07 | python 07.py) <(echo "1537 18818811755665")
diff <(cat inputs/08 | python 08.py) <(echo "102816")

diff <(rustc 01.rs && cat inputs/01 | ./01) <(echo "1097 7101")
