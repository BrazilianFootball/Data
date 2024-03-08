#!/bin/bash

printf "\e[33;1m%s\e[0m\n" 'Running Python Formatter and Linter (Pre-Commit)'

staged_py_files="$(git diff --name-only --cached --diff-filter=d -- "*.py" | sort)"

if [ -n "${staged_py_files}" ]; then
    black $staged_py_files
    if [ $? -eq 0 ]; then
        git add $staged_py_files
    else
        echo 'Error running Python Formatter'
        exit 1
    fi

    flake8 $staged_py_files

    if [ $? -eq 0 ]; then
        printf "\e[32;1m%s\e[0m\n" 'Python Linting Passed'
    else
        printf "\e[31;1m%s\e[0m\n" 'Python Linting Failed'
        exit 1
    fi
fi

printf "\e[33;1m%s\e[0m\n" 'Finished running Python Formatter and Linter (Pre-Commit)'
