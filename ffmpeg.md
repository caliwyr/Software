

# timelapse video

My post... https://medium.com/@hiiamyes/using-ffmpeg-to-make-time-lapse-video-391f5ea8cc6b

[scale](https://stackoverflow.com/questions/44634765/ffmpeg-aspect-ratio-of-image-in-a-slideshow)

```
ffmpeg -f image2 -pattern_type glob -framerate 30 -i 'G0*.JPG' -vf "scale=3840x2160:force_original_aspect_ratio=decrease,pad=3840:2160:(ow-iw)/2:(oh-ih)/2,setsar=1" -vcodec libx264 -pix_fmt yuv420p test6.mp4
```


```
ffmpeg -f image2 -pattern_type glob -framerate 30 -i 'G0*.JPG' -s 3840x2160 -vcodec libx264 -pix_fmt yuv420p test4.mp4
```

[Why won't video from ffmpeg show in QuickTime, iMovie or quick preview?](https://apple.stackexchange.com/questions/166553/why-wont-video-from-ffmpeg-show-in-quicktime-imovie-or-quick-preview)

In short, you (often) need to include the argument `-pix_fmt yuv420p` when using ffmpeg to generate H.264 content for Apple software/devices, and a bunch of other decoders that don't handle yuv444p.

```
ffmpeg -i input.avi -pix_fmt yuv420p output.mp4
```

This is not mentioned in the output when using the defaults, but can be found in their Encode/H.264 guide.

[Convert sequence of JPEG images to MP4 video](https://gist.github.com/alexellis/bbf2bc2a6789480fcd0031f99800df9c)

`ffmpeg  -r 24 -pattern_type glob -i '*.JPG' -i DSC_%04d.JPG -s hd1080 -vcodec libx264 timelapse.mp4`

- `-r 24` - output frame rate
- `-pattern_type glob -i '*.JPG'` - all JPG files in the current directory
- `-i DSC_%04d.JPG` - e.g. DSC_0397.JPG
- `-s hd1080` - 1920x1080 resolution


[Padding]
[FFMPEG scale video to 720px, add black fields at the top and bottom and output 720x1280 (portrait) [duplicate]](https://superuser.com/questions/1271758/ffmpeg-scale-video-to-720px-add-black-fields-at-the-top-and-bottom-and-output-7)

The method below assumes that the source aspect ratio isn't greater than 720/1280.

```
ffmpeg -i in.mp4 -vf scale=720:1280:force_original_aspect_ratio=decrease,pad=720:1280:(ow-iw)/2:(oh-ih)/2,setsar=1 out.mp4
```

The force_original_aspect_ratio in the scale 'fits' the video within the dimensions specified. The pad then expands the canvas to get the size desired.
