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
videoPID    = sys.argv[2]
audioPID    = sys.argv[3]
serviceId   = sys.argv[4]
fName       = sys.argv[5]
aitPid      = sys.argv[6]

# program: 0xE00 (3584) => FVX Test

pmt = program_map_section(

        # +-TableType: program_map_section (0/0)
        #   +-table_id: 0x2 (2) => program_map_section
        #   +-section_syntax_indicator: 0x1 (1)
        #   +-private_indicator: 0x0 (0)
        #   +-section_length: 0x2E (46)
        #   +-table_id_extension: 0xE00 (3584)
        #   +-version: 0x3 (3)
        #   +-current_next_indicator: 0x1 (1) => current
        #   +-section_number: 0x0 (0)
        #   +-last_section_number: 0x0 (0)
        #   +-private_data: 0xFFFFF0000BE021F01252012913050000000300660601060101000005E3DEF0056F005201AAFF34FA5B "......!..R.).......f............o.R...4.["
        #   +-PMT_PID: 0xC1C (3100)
        #   +-PCR_PID: 0x1FFF (8191)
        #   +-program_info_length: 0x0 (0)

        program_number = int(serviceId),
        PCR_PID = int(videoPID), 
        program_info_descriptor_loop = [],
        stream_loop = [
			stream_loop_item(
				stream_type = 0x1B, # avc video stream type
				elementary_PID = int(videoPID),
				element_info_descriptor_loop = [
                    stream_identifier_descriptor(
                        component_tag = 0xB,
                    )
                ]
			),
            
			stream_loop_item(
				stream_type = 0x0F, # aac audio stream type
				elementary_PID = int(audioPID),
				element_info_descriptor_loop = []
			),
            
            # --- AIT ---

            # +-component (ITU-T Rec. H.222.0 | ISO/IEC 13818-1 private_sections)
            #   +-stream_type: 0x5 (5) => ITU-T Rec. H.222.0 | ISO/IEC 13818-1 private_sections
            #   +-elementary_PID: 0x3DE (990)
            #   +-ES_info_length: 0x5 (5)
            #   +-component_descriptors: 2 entries
            #     +-Descriptor: application_signalling_descriptor: 0x6F (111)
            #     | +-descriptor_tag: 0x6F (111) => application_signalling_descriptor
            #     | +-descriptor_length: 0x0 (0)
            #     | +-descriptor_data: -
            #     +-Descriptor: stream_identifier_descriptor: 0x52 (82)
            #       +-descriptor_tag: 0x52 (82) => stream_identifier_descriptor
            #       +-descriptor_length: 0x1 (1)
            #       +-descriptor_data: 0xAA "."
            #       +-component_tag: 0xAA (170)
      
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

#os.system('rm ./tmp/' + fName + '.sec')
