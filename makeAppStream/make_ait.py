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


aitPID      = sys.argv[1]   # 3105  3305
appID       = sys.argv[2]   # 2     3
urlBase     = sys.argv[3]   # "http://discoveryapp-staging.cloud.digitaluk.co.uk/"
appName     = sys.argv[4]   # "Freeview Explore"
appLoc      = sys.argv[5]   # "?nids%5B%5D=65535&lloc=lcn"
fName       = sys.argv[6]   # "ait1"


ait = application_information_section(

    # AIT (Application Information Table) PID=3105
    # +-AIT: 0x10 (16) => HBBTV
      # +-TableType: MHP-application information section (AIT) (0/0)
        # +-table_id: 0x74 (116) => MHP-application information section (AIT)
        # +-section_syntax_indicator: 0x1 (1)
        # +-private_indicator: 0x1 (1)
        # +-section_length: 0x8C (140)
        # +-table_id_extension: 0x10 (16)
        # +-version: 0x1C (28)
        # +-current_next_indicator: 0x1 (1) => current
        # +-section_number: 0x0 (0)
        # +-last_section_number: 0x0 (0)
        # +-private_data: 0xF000F07F00000370000101F076023700030032687474703A2F2F646973636F766572796170702D73746167696E672E636C6F75642E6469676974616C756B2E636F2E756B2F000009050000010301FF01000114656E67104672656576696577204578706C ".......p....v.7...2http://discoveryapp-staging.cloud.digitaluk.co.uk/..............eng.Freeview Expl"
        # +-test_application_flag: 0x0 (0)
        # +-application_type: 0x10 (16) => HBBTV
        
        application_type = 0x0010,

        # +-common_descriptors_length: 0x0 (0)
        common_descriptor_loop = [
            # external_application_authorisation_descriptor(
            #     application_identifiers = 0x370,
            #     application_priority = [5]
            # ) 
        ],

        # +-applications: 1 entries
        application_loop = [
            application_loop_item(
              # +-application (Freeview Explore)

                # +-organisation_id: 0x370 (880) => unknown
                organisation_id = 0x370,
                 
                # +-application_id: 0x1 (1) => Application_ids for unsigned applications
                application_id = int(appID),  
                
                # +-application_control_code: 0x1 (1) => AUTOSTART
                application_control_code = 1, 
  
                # +-application_descriptors_loop_length: 0x76 (118)
                # +-application_descriptors: 4 entries
                application_descriptors_loop = [
                
                    # +-Descriptor: transport_protocol_descriptor: 0x2 (2)
                    # | +-descriptor_tag: 0x2 (2) => transport_protocol_descriptor
                    # | +-descriptor_length: 0x37 (55)
                    # | +-descriptor_data: 0x00030032687474703A2F2F646973636F766572796170702D73746167696E672E636C6F75642E6469676974616C756B2E636F2E756B2F00 "...2http://discoveryapp-staging.cloud.digitaluk.co.uk/."
                    # | +-protocol_id: 0x3 (3) => HTTP over back channel (i.e. broadband connection).
                    # | +-transport_protocol_label: 0x0 (0)
                    # | +-selector_bytes: 0x32687474703A2F2F646973636F766572796170702D73746167696E672E636C6F75642E6469676974616C756B2E636F2E756B2F00 "2http://discoveryapp-staging.cloud.digitaluk.co.uk/."
                    # | +-url_base_length: 0x32 (50)
                    # | +-url_base_byte: 0x687474703A2F2F646973636F766572796170702D73746167696E672E636C6F75642E6469676974616C756B2E636F2E756B2F "http://discoveryapp-staging.cloud.digitaluk.co.uk/"
                    # | +-url_extension_count: 0x0 (0)
                      
                    transport_protocol_descriptor(
                        protocol_id = 0x0003, # HTTP transport protocol
                        URL_base = urlBase,
                        URL_extensions = [],
                        transport_protocol_label = 3, # Or 0????
                    ),  

                    # +-Descriptor: application_descriptor: 0x0 (0)
                    # | +-descriptor_tag: 0x0 (0) => application_descriptor
                    # | +-descriptor_length: 0x9 (9)
                    # | +-descriptor_data: 0x050000010301FF0100 "........."
                    # | +-application_profiles_length: 0x5 (5)
                    # | +-application_profiles: 1 entries
                    # | +-application_profile (1.3.1)
                    # +-application_profile: 0x0 (0)
                    # +-version_major: 0x1 (1)
                    # +-version_minor: 0x3 (3)
                    # +-version_micro: 0x1 (1)
                    # | +-service_bound_flag: 0x1 (1) => the application is only associated with the current service
                    # | +-visibility: 0x3 (3) => VISIBLE_ALL (This application can be visible to users and shall be visible to applications via an application listing API)
                    # | +-application_priority: 0x1 (1)
                    # | +-transport_protocol_labels: 1 entries
                    # +-transport_protocol_label: 0x0 (0)

                    application_descriptor(
                        application_profile = 0x0000,
                        version_major = 1, 
                        version_minor = 3,
                        version_micro = 1,
                        service_bound_flag = 1, 
                        visibility = 3, 
                        application_priority = 1,
                        transport_protocol_labels = [3], # 0?
                    ),

                    # +-Descriptor: application_name_descriptor: 0x1 (1)
                      # | +-descriptor_tag: 0x1 (1) => application_name_descriptor
                      # | +-descriptor_length: 0x14 (20)
                      # | +-descriptor_data: 0x656E67104672656576696577204578706C6F7265 "eng.Freeview Explore"
                      # | +-application_names: 1 entries
                      #    +-application_name: Freeview Explore
                      #      +-ISO_639_language_code: eng
                      #      +-application_name_length: 0x10 (16)
                      #      +-application_name_encoding: default (ISO 6937, latin)
                      #      +-application_name: Freeview Explore
                        
                    application_name_descriptor(
                        application_name = appName,
                        ISO_639_language_code = "eng"
                    ),

                    # +-Descriptor: simple_application_location_descriptor: 0x15 (21)
                        # +-descriptor_tag: 0x15 (21) => simple_application_location_descriptor
                        # +-descriptor_length: 0x1A (26)
                        # +-descriptor_data: 0x3F6E6964732535422535443D3635353335266C6C6F633D6C636E "?nids%5B%5D=65535&lloc=lcn"
                        # +-initial_path_bytes: 0x3F6E6964732535422535443D3635353335266C6C6F633D6C636E "?nids%5B%5D=65535&lloc=lcn"

                    simple_application_location_descriptor(
                        initial_path_bytes = appLoc
                    ),      
                ]
            ),
        ],
        
        version_number = 1,
        section_number = 0,
        last_section_number = 0,
    )



out = open("./tmp/ait.sec", "wb")
out.write(ait.pack())
out.close

out = open("./tmp/ait.sec", "wb") # python flush bug
out.close

os.system('/usr/bin/sec2ts ' + str(aitPID) + ' < ./tmp/ait.sec > ./tmp/' + fName + '.ts')

#os.system('rm ./tmp/ait.sec')

