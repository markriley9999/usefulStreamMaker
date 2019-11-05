#!/bin/bash

mkdir -p tmp
mkdir -p output

rm -rf tmp/*

ffmpeg -y -i ~/source/keep-CosmosLaundromat.mp4 -c copy -ss 00:06:30 -t 90 tmp/av.mp4

ffmpeg -y -i tmp/av.mp4  -vf "scale=-1:480, crop=720:480" -c:v libx264 -x264opts keyint=12:min-keyint=12:no-scenecut -c:a aac -ac 2 tmp/av2.mp4

ffmpeg -y -i tmp/av2.mp4 -i spanner.png -filter_complex "overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2" -codec:a copy tmp/av3.mp4

ffmpeg -y -i tmp/av3.mp4 -vf "scale=-1:480, crop=720:480" -c:v libx264 -b:v 823k -maxrate:0 823k -minrate:0 823k -bufsize:0 1000000 -x264opts keyint=12:min-keyint=12:no-scenecut -c:a aac -ac 2 -ab 128000 -ar 48000 -b:a 128k -maxrate:1 128k -minrate:1 128k -bufsize:1 200000 -muxrate 1200000 -fflags +genpts -f mpegts -mpegts_original_network_id 1 -mpegts_transport_stream_id 1 -mpegts_service_id 4000 -mpegts_pmt_start_pid 3400 -streamid 0:3402 -streamid 1:3403 -metadata service_provider="CHANGEME" -metadata service_name="CHANGEME" -map 0:0 -map 0:1 tmp/spts.ts 

tsmask tmp/spts.ts -0 -16 -17 -3400 > tmp/spts-nosi.ts




python ./make_pmt_av.py "3400" "3402" "3403" "4000" "pmt-user1"   "3401"

python ./make_singleapp_nit.py

python ./make_singleapp_pat.py
python ./make_singleapp_sdt.py


python ./make_ait.py "3401" "100" "http://ait.cloud.digitaluk.co.uk/" "UserApp"    "appbyip.html"    "ait-user1"


tsmask ~/source/Suitest_Channel.ts \
    -0 \
    -16 \
    -17 \
    > tmp/suitest_stripped.ts



tscbrmuxer \
    c:1200000 tmp/spts-nosi.ts \
    b:3008 tmp/nit.ts \
    b:3008 tmp/pat.ts \
    b:1500 tmp/sdt.ts \
    b:3008 tmp/pmt-user1.ts \
    b:1400 tmp/ait-user1.ts \
    > output/appbyip_stream.ts

    

# clear up
#rm tmp/*.ts



if [ "$1" == "--xfer" ]; then
   # Backup
   cp output/*.ts ~/out/

   # cp *.sh *.py ~/out/

   cd ~/out/
   aws s3 sync . s3://duk-contentmaker-out

   # cp ~/duk-scot/*.py ~/duk-scot/*.sh ~/generalScripts/content/duk-scot/
fi


echo "*** Done ***"
