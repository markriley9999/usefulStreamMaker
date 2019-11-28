#! /usr/bin/env python

#
# Copyright (C) 2004-2013  Lorenzo Pallara, l.pallara@avalpa.com
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

import string
import pdb
from dvbobjects.utils import *
from dvbobjects.utils.MJD import *
from dvbobjects.MPEG.Descriptor import Descriptor

######################################################################
class target_region_name_descriptor_loop_item(DVBobject):

    def pack(self):

        region_name_length = len(self.region_name)

        fmt = "!BB%dsBBB" % region_name_length
        return pack(fmt,
            self.region_depth,
            region_name_length,
            self.region_name,
            self.primary_region_code,
            self.secondary_region_code,
            self.tertiary_region_code,
	    )

####################################################################
class target_region_name_descriptor(Descriptor):

    descriptor_tag = 0x7F

    def bytes(self):

        descriptor_tag_extension = 0x0A
        target_region_name_bytes = string.join(
            map(lambda x: x.pack(),
                self.target_region_name_descriptor_loop
            ),
        "")

        fmt = "!B%ds%ds%ds" % (len(self.country_code), len(self.ISO_639_language_code), len(target_region_name_bytes))
        return pack(fmt,
            descriptor_tag_extension,
            self.country_code,
            self.ISO_639_language_code,
            target_region_name_bytes,
        )

######################################################################
class target_region_descriptor_loop_item(DVBobject):

    def pack(self):

        fmt = "!BBBBB"
        return pack(fmt,
            self.reserved,
            self.country_code_flag,
            self.region_depth,
            self.primary_region_code,
            self.secondary_region_code
	    )

####################################################################
class target_region_descriptor(Descriptor):

    descriptor_tag = 0x7F

    def bytes(self):

        descriptor_tag_extension = 0x09
        target_region_bytes = string.join(
            map(lambda x: x.pack(),
                self.target_region_descriptor_loop
            ),
        "")

        fmt = "!B%ds%ds" % (len(self.country_code), len(target_region_bytes))
        return pack(fmt,
            descriptor_tag_extension,
            self.country_code,
            target_region_bytes,
        )


######################################################################
