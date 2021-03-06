import os

from dvbobjects.PSI.PAT import *
from dvbobjects.PSI.NIT import *
from dvbobjects.PSI.SDT import *
from dvbobjects.PSI.PMT import *
from dvbobjects.DVB.Descriptors import *
from dvbobjects.MPEG.Descriptors import *
from dvbobjects.MHP.AIT import *
from dvbobjects.HBBTV.Descriptors import *


import sys


pmtPID      = sys.argv[1]
serviceId   = sys.argv[2]
fName       = sys.argv[3]
aitPid      = sys.argv[4]

pmt = program_map_section(
        program_number = int(serviceId),
        PCR_PID = 8191,
        program_info_descriptor_loop = [],
        stream_loop = [
            stream_loop_item(
                stream_type = 5,
                elementary_PID = int(aitPid),
                element_info_descriptor_loop = [
                        application_signalling_descriptor(
                        application_type = 0x0010,
                        AIT_version = 1,
                    ),
                ]
            ),
        ],

        version_number = 1,
        section_number = 0,
        last_section_number = 0,
    )


out = open("./tmp/" + fName + ".sec", "wb")
out.write(pmt.pack())
out.close

out = open("./tmp/" + fName + ".sec", "wb") # python flush bug
out.close

os.system('/usr/bin/sec2ts ' + str(pmtPID) + ' < ./tmp/' + fName + '.sec > ./tmp/' + fName + '.ts')

os.system('rm ./tmp/' + fName + '.sec')
