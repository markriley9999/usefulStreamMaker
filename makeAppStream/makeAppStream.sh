#!/bin/bash

mkdir -p tmp
mkdir -p output

rm -rf tmp/*


python ./make_pmt.py "3100" "3584" "pmt1" "3105"
python ./make_pmt.py "3200" "3585" "pmt2" "3205"
python ./make_pmt.py "3300" "3586" "pmt3" "3305"

python ./make_pmt.py "3400" "4000" "pmt-user1"   "3401"
python ./make_pmt.py "3402" "4001" "pmt-user2"   "3403"
python ./make_pmt.py "3404" "4002" "pmt-user3"   "3405"
python ./make_pmt.py "3406" "4003" "pmt-user4"   "3407"
python ./make_pmt.py "3408" "4004" "pmt-user5"   "3409"
python ./make_pmt.py "3410" "4005" "pmt-user6"   "3411"
python ./make_pmt.py "3412" "4006" "pmt-user7"   "3413"
python ./make_pmt.py "3414" "4007" "pmt-user8"   "3415"
python ./make_pmt.py "3416" "4008" "pmt-user9"   "3417"
python ./make_pmt.py "3418" "4009" "pmt-user10"  "3419"
python ./make_pmt.py "3420" "4010" "pmt-user11"  "3421"
python ./make_pmt.py "3422" "4011" "pmt-user12"  "3423"
python ./make_pmt.py "3424" "4012" "pmt-user13"  "3425"
python ./make_pmt.py "3426" "4013" "pmt-user14"  "3427"
python ./make_pmt.py "3428" "4014" "pmt-user15"  "3429"
python ./make_pmt.py "3430" "4015" "pmt-user16"  "3431"

python ./make_nit.py

python ./make_pat.py
python ./make_sdt.py



python ./make_ait.py "3105" "10" "http://discoveryapp-test.cloud.digitaluk.co.uk/"      "Freeview Explore"     "?nids%5B%5D=65535&lloc=lcn"    "ait1"
python ./make_ait.py "3205" "11" "http://discoveryapp-staging.cloud.digitaluk.co.uk/"   "Freeview Explore"     "?nids%5B%5D=65535&lloc=lcn"    "ait2"
python ./make_ait.py "3305" "12" "http://discoveryapp-preprod.cloud.digitaluk.co.uk/"   "FVX Pre-Production"   "?nids%5B%5D=65535&lloc=lcn"    "ait3"

python ./make_ait.py "3401" "100" "http://ec2-35-176-80-199.eu-west-2.compute.amazonaws.com/" "UserApp1"    "redirect01.html"    "ait-user1"
python ./make_ait.py "3403" "101" "http://ec2-35-176-80-199.eu-west-2.compute.amazonaws.com/" "UserApp2"    "redirect02.html"    "ait-user2"
python ./make_ait.py "3405" "102" "http://ec2-35-176-80-199.eu-west-2.compute.amazonaws.com/" "UserApp3"    "redirect03.html"    "ait-user3"
python ./make_ait.py "3407" "103" "http://ec2-35-176-80-199.eu-west-2.compute.amazonaws.com/" "UserApp4"    "redirect04.html"    "ait-user4"
python ./make_ait.py "3409" "104" "http://ec2-35-176-80-199.eu-west-2.compute.amazonaws.com/" "UserApp5"    "redirect05.html"    "ait-user5"
python ./make_ait.py "3411" "105" "http://ec2-35-176-80-199.eu-west-2.compute.amazonaws.com/" "UserApp6"    "redirect06.html"    "ait-user6"
python ./make_ait.py "3413" "106" "http://ec2-35-176-80-199.eu-west-2.compute.amazonaws.com/" "UserApp7"    "redirect07.html"    "ait-user7"
python ./make_ait.py "3415" "107" "http://ec2-35-176-80-199.eu-west-2.compute.amazonaws.com/" "UserApp8"    "redirect08.html"    "ait-user8"
python ./make_ait.py "3417" "108" "http://ec2-35-176-80-199.eu-west-2.compute.amazonaws.com/" "UserApp9"    "redirect09.html"    "ait-user9"
python ./make_ait.py "3419" "109" "http://ec2-35-176-80-199.eu-west-2.compute.amazonaws.com/" "UserApp10"   "redirect10.html"   "ait-user10"
python ./make_ait.py "3421" "110" "http://ec2-35-176-80-199.eu-west-2.compute.amazonaws.com/" "UserApp11"   "redirect11.html"   "ait-user11"
python ./make_ait.py "3423" "111" "http://ec2-35-176-80-199.eu-west-2.compute.amazonaws.com/" "UserApp12"   "redirect12.html"   "ait-user12"
python ./make_ait.py "3425" "112" "http://ec2-35-176-80-199.eu-west-2.compute.amazonaws.com/" "UserApp13"   "redirect13.html"   "ait-user13"
python ./make_ait.py "3427" "113" "http://ec2-35-176-80-199.eu-west-2.compute.amazonaws.com/" "UserApp14"   "redirect14.html"   "ait-user14"
python ./make_ait.py "3429" "114" "http://ec2-35-176-80-199.eu-west-2.compute.amazonaws.com/" "UserApp15"   "redirect15.html"   "ait-user15"
python ./make_ait.py "3431" "115" "http://ec2-35-176-80-199.eu-west-2.compute.amazonaws.com/" "UserApp16"   "redirect16.html"   "ait-user16"



tsmask ~/source/Suitest_Channel.ts \
    -0 \
    -16 \
    -17 \
    > tmp/suitest_stripped.ts

    
# bitrate: 0xAE7E6C (11435628)
tscbrmuxer \
    c:11435628 ~/tmp/suitest_stripped.ts \
    b:3008 tmp/nit.ts \
    b:3008 tmp/pat.ts \
    b:1500 tmp/sdt.ts \
    b:3008 tmp/pmt1.ts \
    b:3008 tmp/pmt2.ts \
    b:3008 tmp/pmt3.ts \
    b:3008 tmp/pmt-user1.ts \
    b:3008 tmp/pmt-user2.ts \
    b:3008 tmp/pmt-user3.ts \
    b:3008 tmp/pmt-user4.ts \
    b:3008 tmp/pmt-user5.ts \
    b:3008 tmp/pmt-user6.ts \
    b:3008 tmp/pmt-user7.ts \
    b:3008 tmp/pmt-user8.ts \
    b:3008 tmp/pmt-user9.ts \
    b:3008 tmp/pmt-user10.ts \
    b:3008 tmp/pmt-user11.ts \
    b:3008 tmp/pmt-user12.ts \
    b:3008 tmp/pmt-user13.ts \
    b:3008 tmp/pmt-user14.ts \
    b:3008 tmp/pmt-user15.ts \
    b:3008 tmp/pmt-user16.ts \
    b:1400 tmp/ait1.ts \
    b:1400 tmp/ait2.ts \
    b:1400 tmp/ait3.ts \
    b:1400 tmp/ait-user1.ts \
    b:1400 tmp/ait-user2.ts \
    b:1400 tmp/ait-user3.ts \
    b:1400 tmp/ait-user4.ts \
    b:1400 tmp/ait-user5.ts \
    b:1400 tmp/ait-user6.ts \
    b:1400 tmp/ait-user7.ts \
    b:1400 tmp/ait-user8.ts \
    b:1400 tmp/ait-user9.ts \
    b:1400 tmp/ait-user10.ts \
    b:1400 tmp/ait-user11.ts \
    b:1400 tmp/ait-user12.ts \
    b:1400 tmp/ait-user13.ts \
    b:1400 tmp/ait-user14.ts \
    b:1400 tmp/ait-user15.ts \
    b:1400 tmp/ait-user16.ts \
    > output/app_stream.ts

    

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
