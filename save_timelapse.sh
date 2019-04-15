ffmpeg -r 30 -i ./images/%04d.jpeg -s hd480 -vcodec libx264 -pix_fmt yuv420p time-lapse.mp4
