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
        service_loop_item(
            service_ID                      = 2580,
            EIT_schedule_flag               = 0x0,
            EIT_present_following_flag      = 0x0,
            running_status                  = 4,
            free_CA_mode                    = 0,
            service_descriptor_loop = [
                service_descriptor(
                    service_type            = 0xC,
                    service_provider_name   = "DUK",
                    service_name            = "Accessible TV Guide",
                ),
            ],
        ),
        service_loop_item(
            service_ID                      = 2510,
            EIT_schedule_flag               = 0x0,
            EIT_present_following_flag      = 0x0,
            running_status                  = 4,
            free_CA_mode                    = 0,
            service_descriptor_loop = [
                service_descriptor(
                    service_type            = 0x1,
                    service_provider_name   = "DUK",
                    service_name            = "Xmas roaring fire",
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

os.system('rm ./tmp/sdt.sec')
