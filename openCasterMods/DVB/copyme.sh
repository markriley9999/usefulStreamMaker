#!/bin/bash

if [ ! -f "/usr/lib/python2.7/dist-packages/dvbobjects/DVB/~~~~Descriptors.py" ]; then
    echo "Make a copy first"
    mv /usr/lib/python2.7/dist-packages/dvbobjects/DVB/Descriptors.py /usr/lib/python2.7/dist-packages/dvbobjects/DVB/~~~~Descriptors.py
fi

cp Descriptors.py /usr/lib/python2.7/dist-packages/dvbobjects/DVB/