FILEIN="$1"
NAMEOUT="${FILEIN%.*}"
MPDOUT="$NAMEOUT/.mpd"

echo "Manifest out: $MPDOUT"


mkdir -p tmp
rm -rf tmp/*


# ---Strip metadata and subs ---

ffmpeg -i FILEIN -map_metadata -1 -vcodec copy -acodec copy -map 0:0 -map 0:1  tmp/stripped.mp4


# --- scale and crop, aac audio ---
 ffmpeg -i tmp/stripped.mp4 -vf "scale=-1:1080, crop=1920:1080" -c:v libx264 -r 24 -profile:v main -preset fast -c:a aac -ac 1  -movflags +faststart tmp/source.mp4


# --- Split AV ---
ffmpeg -i tmp/source.mp4 -map_metadata -1 -map 0:0 -c:v copy -an tmp/video.mp4
ffmpeg -i tmp/source.mp4 -map_metadata -1 -c:a copy -vn tmp/audio.m4a


# --- Sanity check
ffmpeg -i tmp/video.mp4 -i tmp/audio.m4a -c copy tmp/checkpt_1.mp4


# --- Scale and GOP align! ---
ffmpeg -i tmp/video.mp4 -c:v libx264 -b:v 4630k -x264opts keyint=96:min-keyint=96:no-scenecut -profile:v main -preset medium -movflags +faststart tmp/valigned_1.mp4

ffmpeg -i tmp/video.mp4 -vf "scale=1280:720" -c:v libx264 -b:v 2594k -x264opts keyint=96:min-keyint=96:no-scenecut -profile:v main -preset medium -movflags +faststart tmp/valigned_2.mp4

ffmpeg -i tmp/video.mp4 -vf "scale=896:504" -c:v libx264 -b:v 1384k -x264opts keyint=96:min-keyint=96:no-scenecut -profile:v main -preset medium -movflags +faststart tmp/valigned_3.mp4

ffmpeg -i tmp/video.mp4 -vf "scale=704:396" -c:v libx264 -b:v 823k -x264opts keyint=96:min-keyint=96:no-scenecut -profile:v main -preset medium -movflags +faststart tmp/valigned_4.mp4

ffmpeg -i tmp/video.mp4 -vf "scale=512:288" -c:v libx264 -b:v 438k -x264opts keyint=96:min-keyint=96:no-scenecut -profile:v main -preset medium -movflags +faststart tmp/valigned_5.mp4


# Clean up again (some reason a sub track gets added...?!)
ffmpeg -i tmp/valigned_1.mp4 -map_metadata -1 -map 0:0 -c:v copy -an tmp/v1.mp4
ffmpeg -i tmp/valigned_2.mp4 -map_metadata -1 -map 0:0 -c:v copy -an tmp/v2.mp4
ffmpeg -i tmp/valigned_3.mp4 -map_metadata -1 -map 0:0 -c:v copy -an tmp/v3.mp4
ffmpeg -i tmp/valigned_4.mp4 -map_metadata -1 -map 0:0 -c:v copy -an tmp/v4.mp4
ffmpeg -i tmp/valigned_5.mp4 -map_metadata -1 -map 0:0 -c:v copy -an tmp/v5.mp4


# Sanity check
ffmpeg -i tmp/v5.mp4 -i tmp/audio.m4a -c copy tmp/checkpt_2.mp4
ffmpeg -i tmp/v1.mp4 -i tmp/audio.m4a -c copy tmp/checkpt_3.mp4

# ffplay tmp/checkpt_3.mp4


# --- Check frames ---

ffprobe -show_frames -print_format compact tmp/v1.mp4 > tmp/frames_1.txt
ffprobe -show_frames -print_format compact tmp/v2.mp4 > tmp/frames_2.txt
ffprobe -show_frames -print_format compact tmp/v3.mp4 > tmp/frames_3.txt
ffprobe -show_frames -print_format compact tmp/v4.mp4 > tmp/frames_4.txt
ffprobe -show_frames -print_format compact tmp/v5.mp4 > tmp/frames_5.txt

# cat tmp/frames_1.txt | awk -F '|' '($2 == "media_type=video") {if ($4 == "key_frame=1") print $6}' | awk -F '=' '{ print $2 * 1000 / 3840, i; ++i }'
# cat tmp/frames_2.txt | awk -F '|' '($2 == "media_type=video") {if ($4 == "key_frame=1") print $6}' | awk -F '=' '{ print $2 * 1000 / 3840, i; ++i }'
# cat tmp/frames_3.txt | awk -F '|' '($2 == "media_type=video") {if ($4 == "key_frame=1") print $6}' | awk -F '=' '{ print $2 * 1000 / 3840, i; ++i }'
# cat tmp/frames_4.txt | awk -F '|' '($2 == "media_type=video") {if ($4 == "key_frame=1") print $6}' | awk -F '=' '{ print $2 * 1000 / 3840, i; ++i }'
# cat tmp/frames_5.txt | awk -F '|' '($2 == "media_type=video") {if ($4 == "key_frame=1") print $6}' | awk -F '=' '{ print $2 * 1000 / 3840, i; ++i }'


# --- dash ---

MP4Box -dash 3840 -rap  -frag-rap -bs-switching inband -profile dashavc264:live -segment-name $RepresentationID$/SEG$Number$ -out MPDOUT tmp/audio.m4a tmp/v1.mp4 tmp/v2.mp4 tmp/v3.mp4 tmp/v4.mp4 tmp/v5.mp4 

