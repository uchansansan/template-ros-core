#!/bin/bash

set -e

# YOUR CODE BELOW THIS LINE
# ----------------------------------------------------------------------------
echo "This is an empty launch script. Update it to launch your application."
roscore &
sleep 5
rosrun circle_drive circle_drive.py
