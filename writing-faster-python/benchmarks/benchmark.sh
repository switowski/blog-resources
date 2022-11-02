#!/usr/bin/env bash

# Exit on error, unset variables or failed pipe command - good practice for any bash script
set -o errexit
set -o nounset
set -o pipefail

# Python versions that we will test
PYENV_VERSIONS=(3.7.14 3.8.14 3.9.14 3.10.7 3.11.0)
# PYENV_VERSIONS=(3.7.14 3.11.0)

# Setup code and the actual functions that we will benchmark
COMMANDS=(
    "-s 'from permission_vs_forgiveness import test_permission2' 'test_permission2()'"
    "-s 'from permission_vs_forgiveness import test_forgiveness2' 'test_forgiveness2()'"
    "-s 'from permission_vs_forgiveness2 import test_permission3' 'test_permission3()'"
    "-s 'from permission_vs_forgiveness2 import test_forgiveness3' 'test_forgiveness3()'"
    "-s 'from find_item import count_numbers' 'count_numbers()'"
    "-s 'from find_item import generator' 'generator()'"
    "-s 'from filter_list import for_loop' 'for_loop()'"
    "-s 'from filter_list import list_comprehension' 'list_comprehension()'"
    "-s 'from sorting import test_sort' 'test_sort()'"
    "-s 'from sorting import test_sorted' 'test_sorted()'"
    "-s 'from duplicates import test_for_loop' 'test_for_loop()'"
    "-s 'from duplicates import test_set' 'test_set()'"
    "-s 'from bubble_sort import bubble_sort' 'bubble_sort()'"
    "-s 'from pi_estimation import estimate_pi' 'estimate_pi()'"
)
#########################################################################################
# Version 1: For each Python version run all functions and print the results one by one #
#########################################################################################
# for v in ${PYENV_VERSIONS[@]}
# do
#     echo "Python version: $v"
#     # Go through each command, print what function is called and then the benchmark of timeit
#     for (( i = 0; i < ${#COMMANDS[@]} ; i++ ))
#     do
#         # String operator that will trim everything from current COMMAND item until last whitespace and print the rest
#         echo -n "${COMMANDS[$i]##*\ } "
#         eval "/Users/switowski/.pyenv/versions/$v/bin/python -m timeit ${COMMANDS[$i]}"
#     done
# done

############################################
# Version 2: Display benchmarks in a table #
############################################
OUTPUT="Function,"
# Create a header with version numbers
for v in ${PYENV_VERSIONS[@]}
do
    OUTPUT+="$v,"
done

# Last column will contain difference between 1st and last version of Python in the PYENV_VERSIONS
OUTPUT+="${PYENV_VERSIONS[0]}/${PYENV_VERSIONS[${#PYENV_VERSIONS[@]}-1]}"
OUTPUT+="\n"

# To make creation of the table easier, this time we swap the order of PYENV_VERSION and COMMAND loops
for (( i = 0; i < ${#COMMANDS[@]} ; i++ ))
do
    # Remove the single quotes from function name
    OUTPUT+=$(echo ${COMMANDS[$i]##*\ } | tr -d "'")

    for v in ${PYENV_VERSIONS[@]}
    do
        OUTPUT+=","
        OUTPUT+=$(eval "/Users/switowski/.pyenv/versions/$v/bin/python -m timeit ${COMMANDS[$i]}" | sed -e 's/.*: \(.*\) per loop/\1/')
    done
    # Divide timings for the first and last Python version and add it in the last column
    v1=$(eval "/Users/switowski/.pyenv/versions/${PYENV_VERSIONS[0]}/bin/python -m timeit ${COMMANDS[$i]}" | sed -e 's/.*: \(.*\) per loop/\1/' -e 's/[^0-9\.]//g')
    v2=$(eval "/Users/switowski/.pyenv/versions/${PYENV_VERSIONS[${#PYENV_VERSIONS[@]}-1]}/bin/python -m timeit ${COMMANDS[$i]}" | sed -e 's/.*: \(.*\) per loop/\1/' -e 's/[^0-9\.]//g')
    difference=$(echo "scale=2; $v1 / $v2" | bc)
    OUTPUT+=",$difference"

    OUTPUT+="\n"
done

# Print in a table-like format
printf "$OUTPUT" | column -ts,
