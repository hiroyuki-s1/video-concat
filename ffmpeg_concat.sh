#! /bin/bash
# ffmpeg -f concat -safe 0 -i concat.txt -acodec copy -vcodec h264_nvenc $1 # nvidia GPUを使うときはこっち
ffmpeg -f concat -safe 0 -i concat.txt -c copy - $1