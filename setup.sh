#!/bin/bash

cp _locally/scripts/pre-commit.sh .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit

echo "Pre-commit hook configured successfully!"
