#!/usr/bin/env bash

# Exit on error, unset variables or failed pipe command - good practice for any bash script
set -o errexit
set -o nounset
set -o pipefail

PYENV_VERSIONS=(3.9.14 3.10.7 3.11.0)

for v in ${PYENV_VERSIONS[@]}
do
    echo "Python version: $v"
    echo "Without try/except block"
    eval "/Users/switowski/.pyenv/versions/$v/bin/python -m timeit -s 'from filter_list import for_loop' 'for_loop()'"
    eval "/Users/switowski/.pyenv/versions/$v/bin/python -m timeit -s 'from pi_estimation import estimate_pi' 'estimate_pi()'"
    eval "/Users/switowski/.pyenv/versions/$v/bin/python -m timeit -s 'from bubble_sort import bubble_sort' 'bubble_sort()'"

    echo "With try/except block"
    eval "/Users/switowski/.pyenv/versions/$v/bin/python -m timeit -s 'from zero_cost_exceptions import for_loop' 'for_loop()'"
    eval "/Users/switowski/.pyenv/versions/$v/bin/python -m timeit -s 'from zero_cost_exceptions import estimate_pi' 'estimate_pi()'"
    eval "/Users/switowski/.pyenv/versions/$v/bin/python -m timeit -s 'from zero_cost_exceptions import bubble_sort' 'bubble_sort()'"
done

############### Output when running on my laptop ##############################
# Python version: 3.9.14
# Without try/except block
# 10 loops, best of 5: 26.7 msec per loop
# 1 loop, best of 5: 18.4 sec per loop
# 1 loop, best of 5: 8.26 sec per loop
# With try/except block
# 10 loops, best of 5: 28.4 msec per loop
# 1 loop, best of 5: 19.2 sec per loop
# 1 loop, best of 5: 8.46 sec per loop
# Python version: 3.10.7
# Without try/except block
# 10 loops, best of 5: 26 msec per loop
# 1 loop, best of 5: 17.3 sec per loop
# 1 loop, best of 5: 7.96 sec per loop
# With try/except block
# 10 loops, best of 5: 27.1 msec per loop
# 1 loop, best of 5: 17.5 sec per loop
# 1 loop, best of 5: 8.06 sec per loop
# Python version: 3.11.0
# Without try/except block
# 20 loops, best of 5: 19.6 msec per loop
# 1 loop, best of 5: 14.1 sec per loop
# 1 loop, best of 5: 4.72 sec per loop
# With try/except block
# 10 loops, best of 5: 20.4 msec per loop
# 1 loop, best of 5: 14.3 sec per loop
# 1 loop, best of 5: 4.75 sec per loop
