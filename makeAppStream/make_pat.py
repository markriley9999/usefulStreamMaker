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

        # Transport Stream 0x1000
    # +-TableType: program_association_section (0/0)
      # +-table_id: 0x0 (0) => program_association_section
      # +-section_syntax_indicator: 0x1 (1)
      # +-private_indicator: 0x0 (0)
      # +-section_length: 0x21 (33)
      # +-table_id_extension: 0x2011 (8209)
      # +-version: 0x5 (5)
      # +-current_next_indicator: 0x1 (1) => current
      # +-section_number: 0x0 (0)
      # +-last_section_number: 0x0 (0)
      # +-private_data: 0x0001E0C80002E12C0E00EC1C0E01EC1C2051E6A420B5E76CF3F094E8 ".......,........ Q.. ..l...."


    transport_stream_id = 0x1000,

    # +-programs: 6 entries
    program_loop = [
        # +-program (the.suite.st)
          # +-program_number: 0x1 (1)
          # +-program_map_PID: 0xC8 (200)
        program_loop_item(
            program_number = 0x1,
            PID = 200,
        ),  
        # +-program (staging.suite.st)
          # +-program_number: 0x2 (2)
          # +-program_map_PID: 0x12C (300)
        program_loop_item(
            program_number = 0x2,
            PID = 300,
        ),  
        # +-program (FVX Test)
          # +-program_number: 0xE00 (3584)
          # +-program_map_PID: 0xC1C (3100)
        program_loop_item(
            program_number = 3584,
            PID = 3100,
        ),  
        # +-program (FVX Staging)
          # +-program_number: 0xE01 (3585)
          # +-program_map_PID: 0xC1C (3200)  FIXED!!!
        program_loop_item(
            program_number = 3585,
            PID = 3200,
        ),  
        # +-program (FVX Pre-Production)
          # +-program_number: 0xE02 (3586)
          # +-program_map_PID: 0xCe4 (3300)  
        program_loop_item(
            program_number = 3586,
            PID = 3300,
        ),  
        # +-program (User App 1)
        program_loop_item(
            program_number = 4000,
            PID = 3400,
        ),  
        # +-program (User App 2)
        program_loop_item(
            program_number = 4001,
            PID = 3402,
        ),  
        # +-program (User App 3)
        program_loop_item(
            program_number = 4002,
            PID = 3404,
        ),  
        # +-program (User App 4)
        program_loop_item(
            program_number = 4003,
            PID = 3406,
        ),  
        # +-program (User App 5)
        program_loop_item(
            program_number = 4004,
            PID = 3408,
        ),  
        # +-program (User App 6)
        program_loop_item(
            program_number = 4005,
            PID = 3410,
        ),  
        # +-program (User App 7)
        program_loop_item(
            program_number = 4006,
            PID = 3412,
        ),  
        # +-program (User App 8)
        program_loop_item(
            program_number = 4007,
            PID = 3414,
        ),  
        # +-program (User App 9)
        program_loop_item(
            program_number = 4008,
            PID = 3416,
        ),  
        # +-program (User App 10)
        program_loop_item(
            program_number = 4009,
            PID = 3418,
        ),  
        # +-program (User App 11)
        program_loop_item(
            program_number = 4010,
            PID = 3420,
        ),  
        # +-program (User App 12)
        program_loop_item(
            program_number = 4011,
            PID = 3422,
        ),  
        # +-program (User App 13)
        program_loop_item(
            program_number = 4012,
            PID = 3424,
        ),  
        # +-program (User App 14)
        program_loop_item(
            program_number = 4013,
            PID = 3426,
        ),  
        # +-program (User App 15)
        program_loop_item(
            program_number = 4014,
            PID = 3428,
        ),  
        # +-program (User App 16)
        program_loop_item(
            program_number = 4015,
            PID = 3430,
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

