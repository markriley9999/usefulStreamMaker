import os

from dvbobjects.PSI.PAT import *
from dvbobjects.PSI.NIT import *
from dvbobjects.PSI.SDT import *
from dvbobjects.PSI.PMT import *
from dvbobjects.DVB.Descriptors import *
from dvbobjects.MPEG.Descriptors import *
from dvbobjects.MHP.AIT import *
from dvbobjects.HBBTV.Descriptors import *


sdt = service_description_section(
	transport_stream_id = 0x1000,
	original_network_id = 9018,

    service_loop = [

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

