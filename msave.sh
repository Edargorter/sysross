#!/bin/bash -e

git add -A
git commit
cat ~/projects/tokens/github_token | pbcopy
git push
