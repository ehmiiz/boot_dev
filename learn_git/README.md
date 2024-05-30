# Learn Git!

plumming and porcline

## internals

Git stores data in 2 ways

tree: git's way of storing a directory
blob: git's way of storing a file

git log displays the commit hash

View the tree -> blob to see file changes with

git cat-file <hash>


## Config

Config files in 5 locations

Syste -> /etc/gitconfig

Global for the user -> ~/.gitconfig

Local (project) -> .git/config

Worktree (part of the project) -> .git/config.worktree


git config --list



cat .git/config