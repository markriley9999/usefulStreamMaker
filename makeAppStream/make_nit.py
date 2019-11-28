import os

from dvbobjects.PSI.PAT import *
from dvbobjects.PSI.NIT import *
from dvbobjects.PSI.SDT import *
from dvbobjects.PSI.PMT import *
from dvbobjects.DVB.Descriptors import *
from dvbobjects.MPEG.Descriptors import *
from dvbobjects.MHP.AIT import *
from dvbobjects.HBBTV.Descriptors import *
from uri import *
from target_region_descriptor import *

nit = network_information_section(
	network_id = 12339,
    network_descriptor_loop = [
	    network_descriptor(network_name = "DUK in-house testing",),
		target_region_name_descriptor(
			ISO_639_language_code = "eng",
			target_region_name_descriptor_loop = [
				target_region_name_descriptor_loop_item(
				region_depth = 0x01,
				region_name = "England",
				primary_region_code = 0x01,
				secondary_region_code = 0x00,
				tertiary_region_code = 0x0000,
				),
				target_region_name_descriptor_loop_item(
				region_depth = 0x02,
				region_name = "London",
				primary_region_code = 0x01,
				secondary_region_code = 0x12,
				tertiary_region_code = 0x0000,
				),
				target_region_name_descriptor_loop_item(
				region_depth = 0x03,
				region_name = "Greater London",
				primary_region_code = 0x01,
				secondary_region_code = 0x12,
				tertiary_region_code = 0x0001,
				),
			],
			country_code = "GBR",
		),
		target_region_descriptor(
			target_region_descriptor_loop = [
				target_region_descriptor_loop_item(
				reserved = 0x1F,
				country_code_flag = 0x0,
				region_depth = 0x02,
				primary_region_code = 0x01,
				secondary_region_code = 0x12,
				),
			],
			country_code = "GBR",
		),
		private_data_specifier_descriptor(private_data_specifier = 0x0000233a,),
		uri_linkage_descriptor(uri_char = "https://auth.freeviewplay.net",),
    ],
	transport_stream_loop = [
	    transport_stream_loop_item(
            transport_stream_id = 0x1000,
            original_network_id = 0x233A,
            transport_descriptor_loop = [
                service_list_descriptor(
                    dvb_service_descriptor_loop = [
                        service_descriptor_loop_item(
                            service_ID      = 0xE00,
                            service_type    = 0xC,
                        ),
                        service_descriptor_loop_item(
                            service_ID      = 0xE01,
                            service_type    = 0xC,
                        ),
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
                        service_descriptor_loop_item(
                            service_ID      = 0x1, # Suitest channel
                            service_type    = 0x1,
                        ),
                        service_descriptor_loop_item(
                            service_ID      = 0x2, # Suitest staging channel
                            service_type    = 0x1,
                        ),
                        service_descriptor_loop_item(
                            service_ID      = 0xA14, # Accessible TV Guide
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
                            service_ID              = 0xE00,
                            visible_service_flag    = 1,
                            logical_channel_number  = 300,
                        ),
                        lcn_service_descriptor_loop_item(
                            service_ID              = 0xE01,
                            visible_service_flag    = 1,
                            logical_channel_number  = 301,
                        ),
                        lcn_service_descriptor_loop_item(
                            service_ID              = 0xE02,
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
                        lcn_service_descriptor_loop_item(
                            service_ID              = 0x1,
                            visible_service_flag    = 1,
                            logical_channel_number  = 781,
                        ),
                        lcn_service_descriptor_loop_item(
                            service_ID              = 0x2,
                            visible_service_flag    = 1,
                            logical_channel_number  = 782,
                        ),
                        lcn_service_descriptor_loop_item(
                            service_ID              = 0xA14,
                            visible_service_flag    = 1,
                            logical_channel_number  = 555,
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

os.system('rm ./tmp/nit.sec')
