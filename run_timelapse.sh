FRAMES=$1
streamer -c /dev/video1 -o 0000.jpeg -s 300x200 -j 100 -t $FRAMES -r 1

