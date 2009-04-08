#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from urlparse import urljoin
from PyKDE4.kdecore import *

sys.path.append('/usr/share/smolt/client')

import smolt




class Host:
    def __init__(self):
        self.profile = smolt.Hardware()

    def host_info(self):
        self.sendable_host_data = [ self.profile.host.UUID,
                                    self.profile.host.os,
                                    self.profile.host.defaultRunlevel,
                                    self.profile.host.language,
                                    self.profile.host.platform,
                                    self.profile.host.bogomips,
                                    self.profile.host.cpuVendor,
                                    self.profile.host.cpuModel,
                                    self.profile.host.numCpus,
                                    self.profile.host.cpuSpeed,
                                    self.profile.host.systemMemory,
                                    self.profile.host.systemSwap,
                                    self.profile.host.systemVendor,
                                    self.profile.host.systemModel,
                                    self.profile.host.kernelVersion,
                                    self.profile.host.formfactor,
                                    self.profile.host.selinux_enabled,
                                    self.profile.host.selinux_policy,
                                    self.profile.host.selinux_enforce ]

        return self.sendable_host_data

    def send_profile(self):
        retvalue, pub_uuid, admin = self.profile.send(smoonURL=smolt.smoonURL)
        url = urljoin(smolt.smoonURL, '/show?uuid=%s' % pub_uuid)

    def getLabels(self):
        self.sendable_host_labels = [ i18n("UUID"),
                                      i18n("OS"),
                                      i18n("Default run level"),
                                      i18n("Language"),
                                      i18n("Platform"),
                                      i18n("BogoMIPS"),
                                      i18n("CPU Vendor"),
                                      i18n("CPU Model"),
                                      i18n("Number of CPUs"),
                                      i18n("CPU Speed"),
                                      i18n("System Memory"),
                                      i18n("System Swap"),
                                      i18n("Vendor"),
                                      i18n("System"),
                                      i18n("Form Factor"),
                                      i18n("Kernel"),
                                      i18n("SELinux Enabled"),
                                      i18n("SELinux Policy"),
                                      i18n("SELinux Enforce") ]

        return self.sendable_host_labels

