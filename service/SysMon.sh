#!/bin/bash

TARGET_PATH="/server/chroot"


while true; do
    inotifywait -m -e close_write,moved_to -r $TARGET_PATH |
    while read dir action file; do
    python /bin/upload_filter/filter.py ${TARGET_PATH}/${file}
    done
done
