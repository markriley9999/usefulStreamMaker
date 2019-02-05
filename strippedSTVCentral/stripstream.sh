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
    > output/srippedSTVCentral.ts




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
