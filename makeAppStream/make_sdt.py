import os

from dvbobjects.PSI.PAT import *
from dvbobjects.PSI.NIT import *
from dvbobjects.PSI.SDT import *
from dvbobjects.PSI.PMT import *
from dvbobjects.DVB.Descriptors import *
from dvbobjects.MPEG.Descriptors import *
from dvbobjects.MHP.AIT import *
from dvbobjects.HBBTV.Descriptors import *


# transport stream: 0x1000
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
	transport_stream_id = 0x1000,
	original_network_id = 9018,

    # +-services_loop: 6 entries
    service_loop = [
        # +-service (FVX Test)
           # +-service_id: 0xE00 (3584)
           # +-reserved_future_use: 0x3F (63)
           # +-EIT_schedule_flag: 0x0 (0) => No EIT schedule information
           # +-EIT_present_following_flag: 0x0 (0) => No EIT_present_following information
           # +-running_status: 0x4 (4) => running
           # +-free_CA_mode: 0x0 (0) => clear
           # +-service_descriptors_length: 0xD (13)
           # +-service_descriptors: 1 entries
             # +-Descriptor: service_descriptor: 0x48 (72)
               # +-descriptor_tag: 0x48 (72) => service_descriptor
               # +-descriptor_length: 0xB (11)
               # +-descriptor_data: 0x0C00084656582054657374 "...FVX Test"
               # +-service_type: 0xC (12) => data broadcast service
               # +-service_provider_name_encoding: -
               # +-service_provider_name_length: 0x0 (0)
               # +-service_provider_name: 
               # +-service_name_encoding: default (ISO 6937, latin)
               # +-service_name_length: 0x8 (8)
               # +-service_name: FVX Test            

        service_loop_item(
            service_ID                      = 3584,
            EIT_schedule_flag               = 0x0,
            EIT_present_following_flag      = 0x0, 
            running_status                  = 4, 
            free_CA_mode                    = 0, 
            service_descriptor_loop = [
                service_descriptor(
                    service_type            = 0xC, 
                    service_provider_name   = "DUK",
                    service_name            = "FVX Test",
                ),    
            ],
        ),	

        
        # +-service (FVX Staging)
           # +-service_id: 0xE01 (3585)
           # +-reserved_future_use: 0x3F (63)
           # +-EIT_schedule_flag: 0x0 (0) => No EIT schedule information
           # +-EIT_present_following_flag: 0x0 (0) => No EIT_present_following information
           # +-running_status: 0x4 (4) => running
           # +-free_CA_mode: 0x0 (0) => clear
           # +-service_descriptors_length: 0x10 (16)
           # +-service_descriptors: 1 entries
             # +-Descriptor: service_descriptor: 0x48 (72)
               # +-descriptor_tag: 0x48 (72) => service_descriptor
               # +-descriptor_length: 0xE (14)
               # +-descriptor_data: 0x0C000B4656582053746167696E67 "...FVX Staging"
               # +-service_type: 0xC (12) => data broadcast service
               # +-service_provider_name_encoding: -
               # +-service_provider_name_length: 0x0 (0)
               # +-service_provider_name: 
               # +-service_name_encoding: default (ISO 6937, latin)
               # +-service_name_length: 0xB (11)
               # +-service_name: FVX Staging
        
        service_loop_item(
            service_ID                      = 3585,
            EIT_schedule_flag               = 0x0,
            EIT_present_following_flag      = 0x0, 
            running_status                  = 4, 
            free_CA_mode                    = 0, 
            service_descriptor_loop = [
                service_descriptor(
                    service_type            = 0xC, 
                    service_provider_name   = "DUK",
                    service_name            = "FVX Staging",
                ),    
            ],
        ),	

        # New service: FVX Pre-Production
        service_loop_item(
            service_ID                      = 3586,
            EIT_schedule_flag               = 0x0,
            EIT_present_following_flag      = 0x0, 
            running_status                  = 4, 
            free_CA_mode                    = 0, 
            service_descriptor_loop = [
                service_descriptor(
                    service_type            = 0xC, 
                    service_provider_name   = "DUK",
                    service_name            = "FVX Pre-Production",
                ),    
            ],
        ),	
        
        # New services: User App
        service_loop_item(
            service_ID                      = 4000,
            EIT_schedule_flag               = 0x0,
            EIT_present_following_flag      = 0x0, 
            running_status                  = 4, 
            free_CA_mode                    = 0, 
            service_descriptor_loop = [
                service_descriptor(
                    service_type            = 0xC, 
                    service_provider_name   = "DUK",
                    service_name            = "User App 1",
                ),    
            ],
        ),	
        
        service_loop_item(
            service_ID                      = 4001,
            EIT_schedule_flag               = 0x0,
            EIT_present_following_flag      = 0x0, 
            running_status                  = 4, 
            free_CA_mode                    = 0, 
            service_descriptor_loop = [
                service_descriptor(
                    service_type            = 0xC, 
                    service_provider_name   = "DUK",
                    service_name            = "User App 2",
                ),    
            ],
        ),	
        
        service_loop_item(
            service_ID                      = 4002,
            EIT_schedule_flag               = 0x0,
            EIT_present_following_flag      = 0x0, 
            running_status                  = 4, 
            free_CA_mode                    = 0, 
            service_descriptor_loop = [
                service_descriptor(
                    service_type            = 0xC, 
                    service_provider_name   = "DUK",
                    service_name            = "User App 3",
                ),    
            ],
        ),	
        
        service_loop_item(
            service_ID                      = 4003,
            EIT_schedule_flag               = 0x0,
            EIT_present_following_flag      = 0x0, 
            running_status                  = 4, 
            free_CA_mode                    = 0, 
            service_descriptor_loop = [
                service_descriptor(
                    service_type            = 0xC, 
                    service_provider_name   = "DUK",
                    service_name            = "User App 4",
                ),    
            ],
        ),	
        
        service_loop_item(
            service_ID                      = 4004,
            EIT_schedule_flag               = 0x0,
            EIT_present_following_flag      = 0x0, 
            running_status                  = 4, 
            free_CA_mode                    = 0, 
            service_descriptor_loop = [
                service_descriptor(
                    service_type            = 0xC, 
                    service_provider_name   = "DUK",
                    service_name            = "User App 5",
                ),    
            ],
        ),	
        
        service_loop_item(
            service_ID                      = 4005,
            EIT_schedule_flag               = 0x0,
            EIT_present_following_flag      = 0x0, 
            running_status                  = 4, 
            free_CA_mode                    = 0, 
            service_descriptor_loop = [
                service_descriptor(
                    service_type            = 0xC, 
                    service_provider_name   = "DUK",
                    service_name            = "User App 6",
                ),    
            ],
        ),	
        
        service_loop_item(
            service_ID                      = 4006,
            EIT_schedule_flag               = 0x0,
            EIT_present_following_flag      = 0x0, 
            running_status                  = 4, 
            free_CA_mode                    = 0, 
            service_descriptor_loop = [
                service_descriptor(
                    service_type            = 0xC, 
                    service_provider_name   = "DUK",
                    service_name            = "User App 7",
                ),    
            ],
        ),	
        
        service_loop_item(
            service_ID                      = 4007,
            EIT_schedule_flag               = 0x0,
            EIT_present_following_flag      = 0x0, 
            running_status                  = 4, 
            free_CA_mode                    = 0, 
            service_descriptor_loop = [
                service_descriptor(
                    service_type            = 0xC, 
                    service_provider_name   = "DUK",
                    service_name            = "User App 8",
                ),    
            ],
        ),	
        
        service_loop_item(
            service_ID                      = 4008,
            EIT_schedule_flag               = 0x0,
            EIT_present_following_flag      = 0x0, 
            running_status                  = 4, 
            free_CA_mode                    = 0, 
            service_descriptor_loop = [
                service_descriptor(
                    service_type            = 0xC, 
                    service_provider_name   = "DUK",
                    service_name            = "User App 9",
                ),    
            ],
        ),	
        
        service_loop_item(
            service_ID                      = 4009,
            EIT_schedule_flag               = 0x0,
            EIT_present_following_flag      = 0x0, 
            running_status                  = 4, 
            free_CA_mode                    = 0, 
            service_descriptor_loop = [
                service_descriptor(
                    service_type            = 0xC, 
                    service_provider_name   = "DUK",
                    service_name            = "User App 10",
                ),    
            ],
        ),	
        
        service_loop_item(
            service_ID                      = 4010,
            EIT_schedule_flag               = 0x0,
            EIT_present_following_flag      = 0x0, 
            running_status                  = 4, 
            free_CA_mode                    = 0, 
            service_descriptor_loop = [
                service_descriptor(
                    service_type            = 0xC, 
                    service_provider_name   = "DUK",
                    service_name            = "User App 11",
                ),    
            ],
        ),	
        
        service_loop_item(
            service_ID                      = 4011,
            EIT_schedule_flag               = 0x0,
            EIT_present_following_flag      = 0x0, 
            running_status                  = 4, 
            free_CA_mode                    = 0, 
            service_descriptor_loop = [
                service_descriptor(
                    service_type            = 0xC, 
                    service_provider_name   = "DUK",
                    service_name            = "User App 12",
                ),    
            ],
        ),	
        
        service_loop_item(
            service_ID                      = 4012,
            EIT_schedule_flag               = 0x0,
            EIT_present_following_flag      = 0x0, 
            running_status                  = 4, 
            free_CA_mode                    = 0, 
            service_descriptor_loop = [
                service_descriptor(
                    service_type            = 0xC, 
                    service_provider_name   = "DUK",
                    service_name            = "User App 13",
                ),    
            ],
        ),	
        
        service_loop_item(
            service_ID                      = 4013,
            EIT_schedule_flag               = 0x0,
            EIT_present_following_flag      = 0x0, 
            running_status                  = 4, 
            free_CA_mode                    = 0, 
            service_descriptor_loop = [
                service_descriptor(
                    service_type            = 0xC, 
                    service_provider_name   = "DUK",
                    service_name            = "User App 14",
                ),    
            ],
        ),	
        
        service_loop_item(
            service_ID                      = 4014,
            EIT_schedule_flag               = 0x0,
            EIT_present_following_flag      = 0x0, 
            running_status                  = 4, 
            free_CA_mode                    = 0, 
            service_descriptor_loop = [
                service_descriptor(
                    service_type            = 0xC, 
                    service_provider_name   = "DUK",
                    service_name            = "User App 15",
                ),    
            ],
        ),	
        
        service_loop_item(
            service_ID                      = 4015,
            EIT_schedule_flag               = 0x0,
            EIT_present_following_flag      = 0x0, 
            running_status                  = 4, 
            free_CA_mode                    = 0, 
            service_descriptor_loop = [
                service_descriptor(
                    service_type            = 0xC, 
                    service_provider_name   = "DUK",
                    service_name            = "User App 16",
                ),    
            ],
        ),	
        
        # +-service (the.suite.st)
           # +-service_id: 0x1 (1)
           # +-reserved_future_use: 0x3F (63)
           # +-EIT_schedule_flag: 0x0 (0) => No EIT schedule information
           # +-EIT_present_following_flag: 0x0 (0) => No EIT_present_following information
           # +-running_status: 0x4 (4) => running
           # +-free_CA_mode: 0x0 (0) => clear
           # +-service_descriptors_length: 0x11 (17)
           # +-service_descriptors: 1 entries
             # +-Descriptor: service_descriptor: 0x48 (72)
               # +-descriptor_tag: 0x48 (72) => service_descriptor
               # +-descriptor_length: 0xF (15)
               # +-descriptor_data: 0x01000C7468652E73756974652E7374 "...the.suite.st"
               # +-service_type: 0x1 (1) => digital television service
               # +-service_provider_name_encoding: -
               # +-service_provider_name_length: 0x0 (0)
               # +-service_provider_name: 
               # +-service_name_encoding: default (ISO 6937, latin)
               # +-service_name_length: 0xC (12)
               # +-service_name: the.suite.st

        service_loop_item(
            service_ID                      = 1,
            EIT_schedule_flag               = 0x0,
            EIT_present_following_flag      = 0x0, 
            running_status                  = 4, 
            free_CA_mode                    = 0, 
            service_descriptor_loop = [
                service_descriptor(
                    service_type            = 1, 
                    service_provider_name   = "DUK",
                    service_name            = "the.suite.st",
                ),    
            ],
        ),	
        
        
        # +-service (staging.suite.st)
          # +-service_id: 0x2 (2)
          # +-reserved_future_use: 0x3F (63)
          # +-EIT_schedule_flag: 0x0 (0) => No EIT schedule information
          # +-EIT_present_following_flag: 0x0 (0) => No EIT_present_following information
          # +-running_status: 0x4 (4) => running
          # +-free_CA_mode: 0x0 (0) => clear
          # +-service_descriptors_length: 0x15 (21)
          # +-service_descriptors: 1 entries
            # +-Descriptor: service_descriptor: 0x48 (72)
              # +-descriptor_tag: 0x48 (72) => service_descriptor
              # +-descriptor_length: 0x13 (19)
              # +-descriptor_data: 0x01001073746167696E672E73756974652E7374 "...staging.suite.st"
              # +-service_type: 0x1 (1) => digital television service
              # +-service_provider_name_encoding: -
              # +-service_provider_name_length: 0x0 (0)
              # +-service_provider_name: 
              # +-service_name_encoding: default (ISO 6937, latin)
              # +-service_name_length: 0x10 (16)
              # +-service_name: staging.suite.st

        service_loop_item(
            service_ID                      = 2,
            EIT_schedule_flag               = 0x0,
            EIT_present_following_flag      = 0x0, 
            running_status                  = 4, 
            free_CA_mode                    = 0, 
            service_descriptor_loop = [
                service_descriptor(
                    service_type            = 1, 
                    service_provider_name   = "DUK",
                    service_name            = "staging.suite.st",
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

