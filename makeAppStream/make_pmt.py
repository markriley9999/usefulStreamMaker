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
        PCR_PID = 8191, 
        program_info_descriptor_loop = [],
        stream_loop = [
 
            # --- MHEG ---

            stream_loop_item(

                # +-component (ISO/IEC 13818-6 type B)
                # | +-stream_type: 0xB (11) => ISO/IEC 13818-6 type B
                # | +-elementary_PID: 0x21 (33)
                # | +-ES_info_length: 0x12 (18)

                stream_type = 11, # DSMCC stream type
                elementary_PID = 33,      
                element_info_descriptor_loop = [ 
                
                    #association_tag_descriptor(
                    #    association_tag = 0xB, 
                    #    use = 0,                        # some default values follow, don't change them
                    #    selector_lenght = 0,            # ...
                    #    transaction_id = 0x80000000,    # ...
                    #    timeout = 0xFFFFFFFF,           # ...
                    #    private_data = "",
                    #),
               
                    # | +-component_descriptors: 3 entries
                    # |   +-Descriptor: stream_identifier_descriptor: 0x52 (82)
                    # |   | +-descriptor_tag: 0x52 (82) => stream_identifier_descriptor
                    # |   | +-descriptor_length: 0x1 (1)
                    # |   | +-descriptor_data: 0x29 
                    # |   | +-component_tag: 0x29 (41)

                    stream_identifier_descriptor(
                        component_tag = 0x29, 
                    ),
                            
                    # |   +-Descriptor: DSM-CC Carousel_Identifier_descriptor: 0x13 (19)
                    # |   | +-descriptor_tag: 0x13 (19) => DSM-CC Carousel_Identifier_descriptor
                    # |   | +-descriptor_length: 0x5 (5)
                    # |   | +-descriptor_data: 0x0000000300 "....."
                    # |   | +-carousel_id: 0x3 (3)
                    # |   | +-format_id: 0x0 (0) => standard boot
                    # |   | +-private_data_byte: -

                    carousel_identifier_descriptor(
                        carousel_ID = 3, 
                        format_ID = 0, 
                        private_data = "",
                    ),        
                    
                    # |   +-Descriptor: data_broadcast_id_descriptor: 0x66 (102)
                    # |     +-descriptor_tag: 0x66 (102) => data_broadcast_id_descriptor
                    # |     +-descriptor_length: 0x6 (6)
                    # |     +-descriptor_data: 0x010601010000 "......"
                    # |     +-data_broadcast_id: 0x106 (262) => The Digital Network
                    # |     +-MHEG5 Applications: 1 entries
                    # |       +-MHEG5ApplicationType
                    # |         +-application_type_code: 0x101 (257) => UK_PROFILE_LAUNCH
                    # |         +-boot_priority_hint: 0x0 (0)
                    # |         +-application_specific_data_length: 0x0 (0)
                    # |         +-application_specific_data_byte: -

                    data_broadcast_id_descriptor(
                        data_broadcast_ID = 262,
                        ID_selector_bytes = "\001\001\000\000", 
                    ),
                        
                ]
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
