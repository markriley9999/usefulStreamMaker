import os

from dvbobjects.PSI.PAT import *
from dvbobjects.PSI.NIT import *
from dvbobjects.PSI.SDT import *
from dvbobjects.PSI.PMT import *
from dvbobjects.DVB.Descriptors import *
from dvbobjects.MPEG.Descriptors import *
from dvbobjects.MHP.AIT import *
from dvbobjects.HBBTV.Descriptors import *



pat = program_association_section(

 
    transport_stream_id = 0x1000,

    program_loop = [
 
 program_loop_item(
            program_number = 4000,
            PID = 3400,
        ),  
    ],

    version_number = 1,
    section_number = 0,
    last_section_number = 0,
)


out = open("./tmp/pat.sec", "wb")
out.write(pat.pack())
out.close

out = open("./tmp/pat.sec", "wb") # python flush bug
out.close

os.system('/usr/bin/sec2ts 0 < ./tmp/pat.sec > ./tmp/pat.ts')

#os.system('rm ./tmp/pat.sec')

