import os

from dvbobjects.PSI.PAT import *
from dvbobjects.PSI.NIT import *
from dvbobjects.PSI.SDT import *
from dvbobjects.PSI.PMT import *
from dvbobjects.DVB.Descriptors import *
from dvbobjects.MPEG.Descriptors import *
from dvbobjects.MHP.AIT import *
from dvbobjects.HBBTV.Descriptors import *


# transport stream: 8209
# +-TableType: service_description_section - actual_transport_stream (0/0)
  # +-table_id: 0x42 (66) => service_description_section - actual_transport_stream
  # +-section_syntax_indicator: 0x1 (1)
  # +-private_indicator: 0x1 (1)
  # +-section_length: 0x97 (151)
  # +-table_id_extension: 0x2011 (8209)
  # +-version: 0x16 (22)
  # +-current_next_indicator: 0x1 (1) => current
  # +-section_number: 0x0 (0)
  # +-last_section_number: 0x0 (0)
  # +-private_data: 0x233AFF2051FF80144806010003535456730A7777772E7374762E747620B5FF801648080100055354562B31730A7777772E7374762E74760E00FC800D480B0C000846565820546573740E01FC8010480E0C000B4656582053746167696E670001FC801148 "#:. Q...H....STVs.www.stv.tv ....H....STV+1s.www.stv.tv.....H....FVX Test.....H....FVX Staging.....H"
  # +-original_network_id: 0x233A (9018) => UK Digital Terrestrial Television
sdt = service_description_section(
	transport_stream_id = 8209,
	original_network_id = 9018,

    # +-services_loop: 6 entries
    service_loop = [
        # +-service (STV)
           # +-service_id: 0x2051 (8273)
           # +-reserved_future_use: 0x3F (63)
           # +-EIT_schedule_flag: 0x1 (1) => EIT schedule information present in TS
           # +-EIT_present_following_flag: 0x1 (1) => EIT_present_following information present in TS
           # +-running_status: 0x4 (4) => running
           # +-free_CA_mode: 0x0 (0) => clear
           # +-service_descriptors_length: 0x14 (20)
           # +-service_descriptors: 2 entries
             # +-Descriptor: service_descriptor: 0x48 (72)
                # +-descriptor_tag: 0x48 (72) => service_descriptor
                # +-descriptor_length: 0x6 (6)
                # +-descriptor_data: 0x010003535456 "...STV"
                # +-service_type: 0x1 (1) => digital television service
                # +-service_provider_name_encoding: -
                # +-service_provider_name_length: 0x0 (0)
                # +-service_provider_name: 
                # +-service_name_encoding: default (ISO 6937, latin)
                # +-service_name_length: 0x3 (3)
                # +-service_name: STV
             # +-Descriptor: default_authority_descriptor: 0x73 (115)
               # +-descriptor_tag: 0x73 (115) => default_authority_descriptor
               # +-descriptor_length: 0xA (10)
               # +-descriptor_data: 0x7777772E7374762E7476 "www.stv.tv"
               # +-default_authority_byte: 0x7777772E7374762E7476 "www.stv.tv"
        
        service_loop_item(
            service_ID                      = 8273,
            EIT_schedule_flag               = 0x1,
            EIT_present_following_flag      = 0x1, 
            running_status                  = 4, 
            free_CA_mode                    = 0, 
            service_descriptor_loop = [
                service_descriptor(
                    service_type            = 0x1, 
                    service_provider_name   = "DUK",
                    service_name            = "STV",
                ),    
            ],
        ),	
    
        # +-service (STV+1)
           # +-service_id: 0x20B5 (8373)
           # +-reserved_future_use: 0x3F (63)
           # +-EIT_schedule_flag: 0x1 (1) => EIT schedule information present in TS
           # +-EIT_present_following_flag: 0x1 (1) => EIT_present_following information present in TS
           # +-running_status: 0x4 (4) => running
           # +-free_CA_mode: 0x0 (0) => clear
           # +-service_descriptors_length: 0x16 (22)
           # +-service_descriptors: 2 entries
             # +-Descriptor: service_descriptor: 0x48 (72)
                # +-descriptor_tag: 0x48 (72) => service_descriptor
                # +-descriptor_length: 0x8 (8)
                # +-descriptor_data: 0x0100055354562B31 "...STV+1"
                # +-service_type: 0x1 (1) => digital television service
                # +-service_provider_name_encoding: -
                # +-service_provider_name_length: 0x0 (0)
                # +-service_provider_name: 
                # +-service_name_encoding: default (ISO 6937, latin)
                # +-service_name_length: 0x5 (5)
                # +-service_name: STV+1
             # +-Descriptor: default_authority_descriptor: 0x73 (115)
               # +-descriptor_tag: 0x73 (115) => default_authority_descriptor
               # +-descriptor_length: 0xA (10)
               # +-descriptor_data: 0x7777772E7374762E7476 "www.stv.tv"
               # +-default_authority_byte: 0x7777772E7374762E7476 "www.stv.tv"
    
        service_loop_item(
            service_ID                      = 8373,
            EIT_schedule_flag               = 0x1,
            EIT_present_following_flag      = 0x1, 
            running_status                  = 4, 
            free_CA_mode                    = 0, 
            service_descriptor_loop = [
                service_descriptor(
                    service_type            = 0x1, 
                    service_provider_name   = "DUK",
                    service_name            = "STV+1",
                ),    
            ],
        ),	
            
    ],
    
    version_number = 1, # you need to change the table number every time you edit, so the decoder will compare its version with the new one and update the table
    section_number = 0,
    last_section_number = 0,
)
        

out = open("./tmp/sdt.sec", "wb")
out.write(sdt.pack())
out.close

out = open("./tmp/sdt.sec", "wb") # python flush bug
out.close

os.system('/usr/bin/sec2ts 17 < ./tmp/sdt.sec > ./tmp/sdt.ts')

#os.system('rm ./tmp/sdt.sec')

