import os

from dvbobjects.PSI.PAT import *
from dvbobjects.PSI.NIT import *
from dvbobjects.PSI.SDT import *
from dvbobjects.PSI.PMT import *
from dvbobjects.DVB.Descriptors import *
from dvbobjects.MPEG.Descriptors import *
from dvbobjects.MHP.AIT import *
from dvbobjects.HBBTV.Descriptors import *


# NIT
# +-network_id: 12336 => London
  # +-TableType: network_information_section - actual_network (0/1)
    # +-table_id: 0x40 (64) => network_information_section - actual_network
    # +-section_syntax_indicator: 0x1 (1)
    # +-private_indicator: 0x1 (1)
    # +-section_length: 0x35E (862)
    # +-table_id_extension: 0x3048 (12360)
    # +-version: 0x2 (2)
    # +-current_next_indicator: 0x1 (1) => current
    # +-section_number: 0x0 (0)
    # +-last_section_number: 0x1 (1)
    # +-private_data: 0xF0A6401043656E7472616C2053636F746C616E647F240A474252656E674853636F746C616E64029043656E7472616C2053636F746C616E6402047F0709474252FA02044A0C107C233A1140090400015A007F2A08FE656E67446174616261736520726967 "..@.Central Scotland.$.GBRengHScotland..Central Scotland.....GBR...J.. #:.@....Z..*..engDatabase rig"
    # +-network_descriptors_lengt: 0xA6 (166)
    # +-network_descriptors: 7 entries
      # +-Descriptor: network_name_descriptor: 0x40 (64)
        # +-descriptor_tag: 0x40 (64) => network_name_descriptor
        # +-descriptor_length: 0x10 (16)
        # +-descriptor_data: 0x43656E7472616C2053636F746C616E64 "Central Scotland"
        # +-network_name_encoding: default (ISO 6937, latin)
        # +-network_name_length: 0x10 (16)
        # +-network_name: Central Scotland
      # +-Descriptor: extension descriptor (target_region_name_descriptor): 0x7F (127)
        # +-descriptor_tag: 0x7F (127) => extension descriptor (target_region_name_descriptor)
        # +-descriptor_length: 0x24 (36)
        # +-descriptor_data: 0x0A474252656E674853636F746C616E64029043656E7472616C2053636F746C616E640204 ".GBRengHScotland..Central Scotland.."
        # +-descriptor_tag_extension: 0xA (10) => target_region_name_descriptor
        # +-selector_byte: 0x474252656E674853636F746C616E64029043656E7472616C2053636F746C616E640204 "GBRengHScotland..Central Scotland.."
        # +-country_code: GBR
        # +-ISO_639_language_code: eng
        # +-TargetRegionName
          # +-region_dept: 0x1 (1)
          # +-region_name_length: 0x8 (8)
          # +-region_name: Scotland
          # +-primary_region_code: 0x2 (2)
        # +-TargetRegionName
          # +-region_dept: 0x2 (2)
          # +-region_name_length: 0x10 (16)
          # +-region_name: Central Scotland
          # +-primary_region_code: 0x2 (2)
          # +-secondary_region_code: 0x4 (4)
      # +-Descriptor: extension descriptor (target_region_descriptor): 0x7F (127)
        # +-descriptor_tag: 0x7F (127) => extension descriptor (target_region_descriptor)
        # +-descriptor_length: 0x7 (7)
        # +-descriptor_data: 0x09474252FA0204 ".GBR..."
        # +-descriptor_tag_extension: 0x9 (9) => target_region_descriptor
        # +-selector_byte: 0x474252FA0204 "GBR..."
        # +-country_code: GBR
        # +-TargetRegion
          # +-reserved: 0x1F (31)
          # +-country_code_flag: 0x0 (0)
          # +-region_dept: 0x2 (2)
          # +-primary_region_code: 0x2 (2)
          # +-secondary_region_code: 0x4 (4)
      # +-Descriptor: linkage_descriptor: 0x4A (74)
        # +-descriptor_tag: 0x4A (74) => linkage_descriptor
        # +-descriptor_length: 0xC (12)
        # +-descriptor_data: 0x107C233A1140090400015A00 ". #:.@....Z."
        # +-transport_stream_id: 0x107C (4220)
        # +-original_network_id: 0x233A (9018) => UK Digital Terrestrial Television
        # +-service_id: 0x1140 (4416)
        # +-linkage_type: 0x9 (9) => System Software Update Service
        # +-Systems Software Update: 1 entries
          # +-OUI
            # +-oui: 0x15A (346) => Digital Video Broadcasting
            # +-selector_length: 0x0 (0)
            # +-selector_bytes: -
        # +-private_data_byte: -
      # +-Descriptor: extension descriptor (message_descriptor): 0x7F (127)
        # +-descriptor_tag: 0x7F (127) => extension descriptor (message_descriptor)
        # +-descriptor_length: 0x2A (42)
        # +-descriptor_data: 0x08FE656E674461746162617365207269676874206F66204469676974616C20554B204C74642032303137 "..engDatabase right of Digital UK Ltd 2017"
        # +-descriptor_tag_extension: 0x8 (8) => message_descriptor
        # +-selector_byte: 0xFE656E674461746162617365207269676874206F66204469676974616C20554B204C74642032303137 ".engDatabase right of Digital UK Ltd 2017"
        # +-message_id: 0xFE (254)
        # +-iso639LanguageCode: eng
        # +-message: Database right of Digital UK Ltd 2017
      # +-Descriptor: private_data_specifier_descriptor: 0x5F (95)
        # +-descriptor_tag: 0x5F (95) => private_data_specifier_descriptor
        # +-descriptor_length: 0x4 (4)
        # +-descriptor_data: 0x0000233A "..#:"
        # +-private_data_specifier: 0x233A (9018) => Independent Television Commission
      # +-Descriptor: extension descriptor (URI_linkage_descriptor): 0x7F (127)
        # +-descriptor_tag: 0x7F (127) => extension descriptor (URI_linkage_descriptor)
        # +-descriptor_length: 0x23 (35)
        # +-descriptor_data: 0x13802068747470733A2F2F617574682D6374762E6469676974616C756B2E636F2E756B ".. https://auth-ctv.digitaluk.co.uk"
        # +-descriptor_tag_extension: 0x13 (19) => URI_linkage_descriptor
        # +-selector_byte: 0x802068747470733A2F2F617574682D6374762E6469676974616C756B2E636F2E756B ". https://auth-ctv.digitaluk.co.uk"
        # +-uri_linkage_type: 0x80 (128) => User defined
        # +-uri_length: 0x20 (32)
        # +-uri_char: 0x68747470733A2F2F617574682D6374762E6469676974616C756B2E636F2E756B "https://auth-ctv.digitaluk.co.uk"
  
nit = network_information_section(

	network_id = 12339,

    network_descriptor_loop = [
        network_descriptor(network_name = "London"), 
    ],
            
         
    # +-transport_stream_loop_length: 0x2AB (683)
    # +-transport_stream_loop: 4 entries

	transport_stream_loop = [
	    transport_stream_loop_item(
  
          # +-transport_stream:: 0x2011 (8209)
            # +-transport_stream_id: 0x2011 (8209)
            # +-original_network_id: 0x233A (9018) => UK Digital Terrestrial Television
            # +-transport_descriptors_length: 0x41 (65)

            transport_stream_id = 0x1000,
            original_network_id = 0x233A,

            # +-transport_descriptors: 4 entries
              # +-Descriptor: service_list_descriptor: 0x41 (65)
                # +-descriptor_tag: 0x41 (65) => service_list_descriptor
                # +-descriptor_length: 0x12 (18)
                # +-descriptor_data: 0x20510120B5010E000C0E010C000101000201 " Q. .............."
                # +-service_list: 6 entries
            transport_descriptor_loop = [

                service_list_descriptor( 

                    dvb_service_descriptor_loop = [
                
                      # +-service (STV)
                        # +-service_id: 0x2051 (8273)
                        # +-service_type: 0x1 (1) => digital television service

                        service_descriptor_loop_item(
                            service_ID      = 0x2015, 
                            service_type    = 0x1, 
                        ),
                        
                      # +-service (STV+1)
                        # +-service_id: 0x20B5 (8373)
                        # +-service_type: 0x1 (1) => digital television service
                      
                        service_descriptor_loop_item(
                            service_ID      = 0x20B5, 
                            service_type    = 0x1, 
                        ),

                      # +-service (FVX Test)
                        # +-service_id: 0xE00 (3584)
                        # +-service_type: 0xC (12) => data broadcast service
                      
                        service_descriptor_loop_item(
                            service_ID      = 0xE00, 
                            service_type    = 0xC, 
                        ),
                      
                      # +-service (FVX Staging)
                        # +-service_id: 0xE01 (3585)
                        # +-service_type: 0xC (12) => data broadcast service
                      
                        service_descriptor_loop_item(
                            service_ID      = 0xE01, 
                            service_type    = 0xC, 
                        ),
                      
                      # +-service (the.suite.st)
                        # +-service_id: 0x1 (1)
                        # +-service_type: 0x1 (1) => digital television service
                      
                        service_descriptor_loop_item(
                            service_ID      = 0x1, 
                            service_type    = 0x1, 
                        ),
                      
                      # +-service (staging.suite.st)
                        # +-service_id: 0x2 (2)
                        # +-service_type: 0x1 (1) => digital television service
                      
                        service_descriptor_loop_item(
                            service_ID      = 0x2, 
                            service_type    = 0x1, 
                        ),

                      # New services
                                           
                        service_descriptor_loop_item(
                            service_ID      = 3586, 
                            service_type    = 0xC, 
                        ),
                                           
                        service_descriptor_loop_item(
                            service_ID      = 4000, 
                            service_type    = 0xC, 
                        ),
                                           
                        service_descriptor_loop_item(
                            service_ID      = 4001, 
                            service_type    = 0xC, 
                        ),
                                           
                        service_descriptor_loop_item(
                            service_ID      = 4002, 
                            service_type    = 0xC, 
                        ),
                                           
                        service_descriptor_loop_item(
                            service_ID      = 4003, 
                            service_type    = 0xC, 
                        ),
                                           
                        service_descriptor_loop_item(
                            service_ID      = 4004, 
                            service_type    = 0xC, 
                        ),
                                           
                        service_descriptor_loop_item(
                            service_ID      = 4005, 
                            service_type    = 0xC, 
                        ),
                                           
                        service_descriptor_loop_item(
                            service_ID      = 4006, 
                            service_type    = 0xC, 
                        ),
                                           
                        service_descriptor_loop_item(
                            service_ID      = 4007, 
                            service_type    = 0xC, 
                        ),
                                           
                        service_descriptor_loop_item(
                            service_ID      = 4008, 
                            service_type    = 0xC, 
                        ),
                                           
                        service_descriptor_loop_item(
                            service_ID      = 4009, 
                            service_type    = 0xC, 
                        ),
                                           
                        service_descriptor_loop_item(
                            service_ID      = 4010, 
                            service_type    = 0xC, 
                        ),
                                           
                        service_descriptor_loop_item(
                            service_ID      = 4011, 
                            service_type    = 0xC, 
                        ),
                                           
                        service_descriptor_loop_item(
                            service_ID      = 4012, 
                            service_type    = 0xC, 
                        ),
                                           
                        service_descriptor_loop_item(
                            service_ID      = 4013, 
                            service_type    = 0xC, 
                        ),
                                           
                        service_descriptor_loop_item(
                            service_ID      = 4014, 
                            service_type    = 0xC, 
                        ),
                                           
                        service_descriptor_loop_item(
                            service_ID      = 4015, 
                            service_type    = 0xC, 
                        ),

                    ],
                ),


              # +-Descriptor: Logical Channel Descriptor: 0x83 (131)
                # +-descriptor_tag: 0x83 (131) => Logical Channel Descriptor
                # +-descriptor_length: 0x18 (24)
                # +-descriptor_data: 0x0001FF0D0E01FD2D2051FD2F0002FF0E0E00FD2C20B5FD30 ".......- Q./......., ..0"

                private_data_specifier_descriptor(
                
                    private_data_specifier = 0x0000233A
                    
                ),

                # +-logical_channel_descriptor: 6 entries
                logical_channel_descriptor(
                
                    lcn_service_descriptor_loop = [

                      # +-logical_channel (the.suite.st): 781
                        # +-service_id: 0x1 (1)
                        # +-reserved: 0x3F (63)
                        # +-logical_channel_number: 0x30D (781)

                        lcn_service_descriptor_loop_item(
                            service_ID              = 0x1,
                            visible_service_flag    = 1, 
                            logical_channel_number  = 781, 
                        ),

                      # +-logical_channel (FVX Staging): 301
                        # +-service_id: 0xE01 (3585)
                        # +-reserved: 0x3F (63)
                        # +-logical_channel_number: 0x12D (301)

                        lcn_service_descriptor_loop_item(
                            service_ID              = 0xE01,
                            visible_service_flag    = 1,
                            logical_channel_number  = 301,
                        ),
                        
                      # +-logical_channel (STV): 303
                        # +-service_id: 0x2051 (8273)
                        # +-reserved: 0x3F (63)
                        # +-logical_channel_number: 0x12F (303)

                        lcn_service_descriptor_loop_item(
                            service_ID              = 0x2051,
                            visible_service_flag    = 1,
                            logical_channel_number  = 303,
                        ),
                        
                      # +-logical_channel (staging.suite.st): 782
                        # +-service_id: 0x2 (2)
                        # +-reserved: 0x3F (63)
                        # +-logical_channel_number: 0x30E (782)

                        lcn_service_descriptor_loop_item(
                            service_ID              = 0x2,
                            visible_service_flag    = 1,
                            logical_channel_number  = 782,
                        ),
                        
                      # +-logical_channel (FVX Test): 300
                        # +-service_id: 0xE00 (3584)
                        # +-reserved: 0x3F (63)
                        # +-logical_channel_number: 0x12C (300)

                        lcn_service_descriptor_loop_item(
                            service_ID              = 0xE00,
                            visible_service_flag    = 1,
                            logical_channel_number  = 300,
                        ),
                        
                      # +-logical_channel (STV+1): 304
                        # +-service_id: 0x20B5 (8373)
                        # +-reserved: 0x3F (63)
                        # +-logical_channel_number: 0x130 (304)

                        lcn_service_descriptor_loop_item(
                            service_ID              = 0x20B5,
                            visible_service_flag    = 1,
                            logical_channel_number  = 304,
                        ),
                        
                        
                      # New services

                        lcn_service_descriptor_loop_item(
                            service_ID              = 3586,
                            visible_service_flag    = 1,
                            logical_channel_number  = 305,
                        ),

                        lcn_service_descriptor_loop_item(
                            service_ID              = 4000,
                            visible_service_flag    = 1,
                            logical_channel_number  = 401,
                        ),
                        
                        lcn_service_descriptor_loop_item(
                            service_ID              = 4001,
                            visible_service_flag    = 1,
                            logical_channel_number  = 402,
                        ),
                        
                        lcn_service_descriptor_loop_item(
                            service_ID              = 4002,
                            visible_service_flag    = 1,
                            logical_channel_number  = 403,
                        ),
                        
                        lcn_service_descriptor_loop_item(
                            service_ID              = 4003,
                            visible_service_flag    = 1,
                            logical_channel_number  = 404,
                        ),
                        
                        lcn_service_descriptor_loop_item(
                            service_ID              = 4004,
                            visible_service_flag    = 1,
                            logical_channel_number  = 405,
                        ),
                        
                        lcn_service_descriptor_loop_item(
                            service_ID              = 4005,
                            visible_service_flag    = 1,
                            logical_channel_number  = 406,
                        ),
                        
                        lcn_service_descriptor_loop_item(
                            service_ID              = 4006,
                            visible_service_flag    = 1,
                            logical_channel_number  = 407,
                        ),
                        
                        lcn_service_descriptor_loop_item(
                            service_ID              = 4007,
                            visible_service_flag    = 1,
                            logical_channel_number  = 408,
                        ),

                        lcn_service_descriptor_loop_item(
                            service_ID              = 4008,
                            visible_service_flag    = 1,
                            logical_channel_number  = 409,
                        ),
                        
                        lcn_service_descriptor_loop_item(
                            service_ID              = 4009,
                            visible_service_flag    = 1,
                            logical_channel_number  = 410,
                        ),
                        
                        lcn_service_descriptor_loop_item(
                            service_ID              = 4010,
                            visible_service_flag    = 1,
                            logical_channel_number  = 411,
                        ),
                        
                        lcn_service_descriptor_loop_item(
                            service_ID              = 4011,
                            visible_service_flag    = 1,
                            logical_channel_number  = 412,
                        ),
                        
                        lcn_service_descriptor_loop_item(
                            service_ID              = 4012,
                            visible_service_flag    = 1,
                            logical_channel_number  = 413,
                        ),
                        
                        lcn_service_descriptor_loop_item(
                            service_ID              = 4013,
                            visible_service_flag    = 1,
                            logical_channel_number  = 414,
                        ),
                        
                        lcn_service_descriptor_loop_item(
                            service_ID              = 4014,
                            visible_service_flag    = 1,
                            logical_channel_number  = 415,
                        ),
                        
                        lcn_service_descriptor_loop_item(
                            service_ID              = 4015,
                            visible_service_flag    = 1,
                            logical_channel_number  = 416,
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


  
  
