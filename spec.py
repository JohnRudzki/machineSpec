# machineSpec; figure out a machine's specification, what hardware is here?
# This might grow to include some diagnostics, like exercise the HDD, ...
__author__ = 'dalem'

# Many current machine specifications can be found with psutil from here https://github.com/giampaolo/psutil
#TODO; how much memory
#TODO; what kind of processor
#TODO; performance whetstones counter

import os
import psutil
print "cpu times: " + str(psutil.cpu_times())
print "memory: " + str(psutil.TOTAL_PHYMEM)
print "disk: " + str(psutil.disk_usage(os.getcwd()))