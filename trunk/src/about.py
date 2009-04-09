#!/usr/bin/python
# -*- coding: utf-8 -*-

# smoltkde4gui - KDE4 user interface for Smolt
#
# Copyright (C) 2009,  Fethican Coşkuner
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Please read the COPYING file.

# PyKDE4 Stuff
from PyKDE4.kdecore import *

# Application Data
appName     = "Smolt"
catalog     = ""
programName = ki18n("")
version     = ""
description = ki18n("")
license     = KAboutData.License_GPL
copyright   = ki18n("")
text        = ki18n(None)
homePage    = "http://code.google.com/p/smoltkde4gui/"
bugEmail    = ""
aboutData   = KAboutData(appName, catalog, programName, version, description, license, copyright, text, homePage, bugEmail)

# Authors
aboutData.addAuthor (ki18n("Fethican Coşkuner"), ki18n("Maintainer"))
