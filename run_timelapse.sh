FRAMES=$1
streamer -c /dev/video1 -o ./images/0000.jpeg -s 1280x720 -j 100 -t $FRAMES -r 1

