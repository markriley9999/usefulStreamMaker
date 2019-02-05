#!/bin/bash

mkdir -p tmp
mkdir -p output

rm -rf tmp/*



tsmask ~/source/STVCentral_PSB2.ts \
    -0 \
    -16 \
    -17 \
    -1100 \
    -1101 \
    -1102 \
    -1103 \
    -1131 \
    -1200 \
    -1201 \
    -1202 \
    -1203 \
    -1231 \
    -1300 \
    -1301 \
    -1302 \
    -1303 \
    -1331 \
    -1400 \
    -1401 \
    -1402 \
    -1403 \
    -1431 \
    -1500 \
    -1501 \
    -1502 \
    -1503 \
    -1531 \
    -1600 \
    -1601 \
    -1602 \
    -1603 \
    -1631 \
    -1800 \
    -1801 \
    -1802 \
    -1803 \
    -1831 \
    -2000 \
    -2001 \
    -2002 \
    -2003 \
    -2031 \
    -2200 \
    -3001 \
    -3002 \
    -3003 \
    -3004 \
    -3005 \
    -8000 \
    -8191 \
    > tmp/stripped.ts
    

python ./make_nit.py

python ./make_pat.py
python ./make_sdt.py


# bitrate: 0x517D03 (5340419)
tscbrmuxer \
    c:5340419 tmp/stripped.ts \
    b:3008 tmp/nit.ts \
    b:3008 tmp/pat.ts \
    b:1500 tmp/sdt.ts \
    > output/strippedSTVCentral.ts


tspcrmeasure output/strippedSTVCentral.ts 5340419


if [ "$1" == "--fixav" ]; then
    # 2nd stream with new AV

    ffmpeg -y -i ~/source/keep-CosmosLaundromat.mp4 -c copy -ss 00:06:30 -t 90 tmp/av.mp4

    ffmpeg -y -i tmp/av.mp4  -vf "scale=-1:480, crop=720:480" -c:v libx264 -x264opts keyint=12:min-keyint=12:no-scenecut -c:a aac -ac 2 tmp/av2.mp4

    ffmpeg -y -i tmp/av2.mp4 -i ~/source/STV_logo_2014_scale.png -filter_complex "overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2" -codec:a copy tmp/av3-stv.mp4
    ffmpeg -y -i tmp/av2.mp4 -i ~/source/STVplus1_logo_2014_scale.png -filter_complex "overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2" -codec:a copy tmp/av3-stvplus1.mp4

    ffmpeg -y -i tmp/av3-stv.mp4 -vf "scale=-1:480, crop=720:480" -c:v libx264 -b:v 823k -maxrate:0 823k -minrate:0 823k -bufsize:0 1000000 -x264opts keyint=12:min-keyint=12:no-scenecut -c:a aac -ac 2 -ab 128000 -ar 48000 -b:a 128k -maxrate:1 128k -minrate:1 128k -bufsize:1 200000 -muxrate 1200000 -fflags +genpts -f mpegts -mpegts_original_network_id 1 -mpegts_transport_stream_id 1 -mpegts_service_id 8273 -mpegts_pmt_start_pid 1700 -streamid 0:1701 -streamid 1:1702 -metadata service_provider="CHANGEME" -metadata service_name="CHANGEME" -map 0:0 -map 0:1 tmp/spts-stv.ts 

    ffmpeg -y -i tmp/av3-stvplus1.mp4 -vf "scale=-1:480, crop=720:480" -c:v libx264 -b:v 823k -maxrate:0 823k -minrate:0 823k -bufsize:0 1000000 -x264opts keyint=12:min-keyint=12:no-scenecut -c:a aac -ac 2 -ab 128000 -ar 48000 -b:a 128k -maxrate:1 128k -minrate:1 128k -bufsize:1 200000 -muxrate 1200000 -fflags +genpts -f mpegts -mpegts_original_network_id 1 -mpegts_transport_stream_id 1 -mpegts_service_id 8373 -mpegts_pmt_start_pid 1900 -streamid 0:1901 -streamid 1:1902 -metadata service_provider="CHANGEME" -metadata service_name="CHANGEME" -map 0:0 -map 0:1 tmp/spts-stvplus1.ts 


    tsmask tmp/spts-stv.ts -8191 -0 -16 -17 > tmp/spts-stv-nosi.ts
    tsmask tmp/spts-stvplus1.ts -8191 -0 -16 -17 > tmp/spts-stvplus1-nosi.ts



    # Strip out old AV
    tsmask output/strippedSTVCentral.ts -8191 -1700 -1701 -1702 -1703 -1731 -1900 -1901 -1902 -1903 -1931 > tmp/stripped-noav.ts



    tscbrmuxer c:12000000 tmp/stripped-noav.ts b:1200000 tmp/spts-stv-nosi.ts b:1200000 tmp/spts-stvplus1-nosi.ts > output/strippedSTVCentral-newAV.ts

fi




# clear up
#rm tmp/*.ts



if [ "$2" == "--xfer" ]; then
   # Backup
   cp output/*.ts ~/out/

   # cp *.sh *.py ~/out/

   cd ~/out/
   aws s3 sync . s3://duk-contentmaker-out

   # cp ~/duk-scot/*.py ~/duk-scot/*.sh ~/generalScripts/content/duk-scot/
fi


echo "*** Done ***"
