#!/bin/bash

mkdir -p tmp
mkdir -p output

rm -rf tmp/*


python ./make_pmt.py "3400" "4000" "pmt-user1"   "3401"

python ./make_singleapp_nit.py

python ./make_singleapp_pat.py
python ./make_singleapp_sdt.py


python ./make_ait.py "3401" "100" "http://ec2-35-176-80-199.eu-west-2.compute.amazonaws.com/" "UserApp1"    "appbyip.html"    "ait-user1"



# bitrate: 0xAE7E6C (11435628)
tscbrmuxer \
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
