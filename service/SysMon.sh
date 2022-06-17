#!/bin/bash

TARGET_PATH="/home"


while true; do
    inotifywait -m -e close_write,moved_to -r $TARGET_PATH |
    while read dir action file; do
    python3 /bin/SFTP-Filter/filter.py ${dir}/ ${file}
    done
done
