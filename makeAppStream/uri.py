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
class uri_linkage_descriptor(Descriptor):

    descriptor_tag = 0x7F

    def bytes(self):

        descriptor_tag_extension = 0x13
        uri_linkage_type = 0x80
        uri_length = len(self.uri_char)

        fmt = "!BBB%ds" % uri_length
        return pack(fmt,
            descriptor_tag_extension,
            uri_linkage_type,
            uri_length,
            self.uri_char,
            )
