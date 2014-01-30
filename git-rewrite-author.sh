#!/bin/sh

# Script to rewrite author emails in the event of accidental 
# commits with the wrong Git config. 
#
# Do not use after pushing!

OLDEMAIL="old@examplecom"
NEWEMAIL="new@example.com"

git filter-branch --commit-filter '
if [ "$GIT_COMMITTER_NAME" = "<Old Name>" ]; then
    GIT_COMMITTER_NAME="<New Name>";
    GIT_AUTHOR_NAME="<New Name>";
    GIT_COMMITTER_EMAIL="<New Email>";
    GIT_AUTHOR_EMAIL="<New Email>";
    git commit-tree "$@";
else
    git commit-tree "$@";
fi' HEAD
