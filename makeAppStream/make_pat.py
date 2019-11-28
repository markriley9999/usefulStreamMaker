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
            program_number = 3584,
            PID = 3100,
        ),
        program_loop_item(
            program_number = 3585,
            PID = 3200,
        ),
        program_loop_item(
            program_number = 3586,
            PID = 3300,
        ),
        program_loop_item(
            program_number = 4000,
            PID = 3400,
        ),
        program_loop_item(
            program_number = 4001,
            PID = 3402,
        ),
        program_loop_item(
            program_number = 4002,
            PID = 3404,
        ),
        program_loop_item(
            program_number = 4003,
            PID = 3406,
        ),
        program_loop_item(
            program_number = 4004,
            PID = 3408,
        ),
        program_loop_item(
            program_number = 4005,
            PID = 3410,
        ),
        program_loop_item(
            program_number = 4006,
            PID = 3412,
        ),
        program_loop_item(
            program_number = 4007,
            PID = 3414,
        ),
        program_loop_item(
            program_number = 4008,
            PID = 3416,
        ),
        program_loop_item(
            program_number = 4009,
            PID = 3418,
        ),
        program_loop_item(
            program_number = 4010,
            PID = 3420,
        ),
        program_loop_item(
            program_number = 4011,
            PID = 3422,
        ),
        program_loop_item(
            program_number = 4012,
            PID = 3424,
        ),
        program_loop_item(
            program_number = 4013,
            PID = 3426,
        ),
        program_loop_item(
            program_number = 4014,
            PID = 3428,
        ),
        program_loop_item(
            program_number = 4015,
            PID = 3430,
        ),
        program_loop_item(
            program_number = 0x1,
            PID = 200,
        ),
        program_loop_item(
            program_number = 0x2,
            PID = 300,
        ),
        program_loop_item(
            program_number = 2580,
            PID = 3800,
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

os.system('rm ./tmp/pat.sec')
