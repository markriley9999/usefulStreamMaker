#!/bin/bash

if [ ! -f "/usr/lib/python2.7/dist-packages/dvbobjects/DVB/~~~~Descriptors.py" ]; then
    echo "Make a copy first"
    sudo mv /usr/lib/python2.7/dist-packages/dvbobjects/DVB/Descriptors.py /usr/lib/python2.7/dist-packages/dvbobjects/DVB/~~~~Descriptors.py
fi

sudo cp Descriptors.py /usr/lib/python2.7/dist-packages/dvbobjects/DVB/

less /usr/lib/python2.7/dist-packages/dvbobjects/DVB/Descriptors.py

