import os

from dvbobjects.PSI.PAT import *
from dvbobjects.PSI.NIT import *
from dvbobjects.PSI.SDT import *
from dvbobjects.PSI.PMT import *
from dvbobjects.DVB.Descriptors import *
from dvbobjects.MPEG.Descriptors import *
from dvbobjects.MHP.AIT import *
from dvbobjects.HBBTV.Descriptors import *


  
nit = network_information_section(

	network_id = 12339,

    network_descriptor_loop = [
        network_descriptor(network_name = "London"), 
    ],
                     
	transport_stream_loop = [
	    transport_stream_loop_item(

            transport_stream_id = 0x1000,
            original_network_id = 0x233A,

            transport_descriptor_loop = [

                service_list_descriptor( 

                    dvb_service_descriptor_loop = [
                      
                         service_descriptor_loop_item(
                            service_ID      = 4000, 
                            service_type    = 0xC, 
                        ),
                                           
                    ],
                ),

                private_data_specifier_descriptor(
                
                    private_data_specifier = 0x0000233A
                    
                ),

                logical_channel_descriptor(
                
                    lcn_service_descriptor_loop = [

                        lcn_service_descriptor_loop_item(
                            service_ID              = 4000,
                            visible_service_flag    = 1,
                            logical_channel_number  = 1,
                        ),
                        
                    ],
                ),
            ],
            
        ),
          
    ],
        
    version_number = 1, 
    section_number = 0,
    last_section_number = 0,
)


  
  
out = open("./tmp/nit.sec", "wb")
out.write(nit.pack())
out.close

out = open("./tmp/nit.sec", "wb") # python flush bug
out.close

os.system('/usr/bin/sec2ts 16 < ./tmp/nit.sec > ./tmp/nit.ts')

#os.system('rm ./tmp/nit.sec')


  
  
