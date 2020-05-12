#!/bin/bash
# not my work
# https://unix.stackexchange.com/questions/570586/bash-script-to-sort-files-into-alphabetical-folders
# by Kusalananda♦

shopt -s nullglob  # makes the loop not loop at all if there are no files

for name in *; do
    if [[ -d $name ]] && [[ $name == ? ]]; then
        # skip directories that have single character names
        continue
    fi

    # get first character in filename
    first=${name:0:1}

    # compute destination directory name from this first
    # character by uppercasing it
    destdir=${first^}

    # make that directory if it does not already exist
    mkdir -p -- "$destdir"

    # move the file into place (name collisions not checked for)
    mv -- "$name" "$destdir"
done
