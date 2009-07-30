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
appName     = "smoltGui"
catalog     = appName
programName = ki18n("SmoltGui")
version     = "0.1"
description = ki18n("Graphical user interface for Smolt")
license     = KAboutData.License_GPL
copyright   = ki18n("(c) 2009 Fethican Coşkuner")
text        = ki18n(None)
homePage    = "http://code.google.com/p/smoltkde4gui/"
bugEmail    = ""
aboutData   = KAboutData(appName, catalog, programName, version, description, license, copyright, text, homePage, bugEmail)

# Authors
aboutData.addAuthor (ki18n("Fethican Coşkuner"), ki18n("Maintainer"))
