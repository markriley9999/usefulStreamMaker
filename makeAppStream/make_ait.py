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

        application_type = 0x0010,
        common_descriptor_loop = [
        ],
        application_loop = [
            application_loop_item(
                organisation_id = 0x370,
                application_id = int(appID),
                application_control_code = 1, # AUTOSTART
                application_descriptors_loop = [
                    transport_protocol_descriptor(
                        protocol_id = 0x0003, # HTTP transport protocol
                        URL_base = urlBase,
                        URL_extensions = [],
                        transport_protocol_label = 3, # Or 0????
                    ),
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
                    application_name_descriptor(
                        application_name = appName,
                        ISO_639_language_code = "eng"
                    ),
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

os.system('rm ./tmp/ait.sec')
