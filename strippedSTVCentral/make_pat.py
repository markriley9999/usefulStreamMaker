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

        # Transport Stream 8209
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


    transport_stream_id = 8209,

    program_loop = [
        # +-program (STV)
          # +-program_number: 0x2051 (8273)
          # +-program_map_PID: 0x6A4 (1700)
        program_loop_item(
            program_number = 8273,
            PID = 1700,
        ),  
        # +-program (STV+1)
          # +-program_number: 0x20B5 (8373)
          # +-program_map_PID: 0x76C (1900)
        program_loop_item(
            program_number = 8373,
            PID = 1900,
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

