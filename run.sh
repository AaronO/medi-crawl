#!/bin/bash

JSON_FILE=$1
SCRIPT="python ./gen_sh.py"
CMD="${SCRIPT} ${JSON_FILE}"

# Make directories
echo "Making directories"
$CMD | grep mkdir | bash

# Download images
echo "Downloading slides"
$CMD | grep curl | xargs -P 50 -I{} bash -c '{}'

# Download videos
echo "Downloading videos"
$CMD | grep rtmpdump | xargs -P 30 -I{} bash -c '{}'
