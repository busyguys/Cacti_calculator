import os
import datetime
import calendar
import time
import xml_check_v2
import subprocess
import shlex


def make_xml(ip_name, start=0, end=0):

    if(ip_name=="l1"):
        print "L1!!!!"
        #args =
    elif(ip_name=="l2"):
        print "L2!!!!"
        #args =
    elif(ip_name=="aion"):
        print "AION!!!"
        #args =
    elif(ip_name=="bs"):
        print "B&S!!!"
        #args =
    elif(ip_name=="lm"):
        print "LM!!!!"
        #args =
    elif(ip_name=="mobile"):
        print "Mobile!!!!!"
        #args =
    elif(ip_name=="web"):
        print "WEB!!!!!!!"
        #args =
    else:
        print "Input should be L1, L2, AION, BS, LM, MOBILE, WEB"

    # args = "/usr/local/rrdtool/bin/rrdtool xport --start " + str(start) + " --end " + str(end) + " DEF:test='/usr/local/cacti-0.8.8a/rra/10lan-testnw-01_traffic_in_82726.rrd':'traffic_in':AVERAGE CDEF:test2='test,8,*' XPORT:test2:'test is '"
    # seperator = ','
    # seperator.join(args)
    # args = shlex.split(args)
    #
    # output = subprocess.Popen(args, stdout=subprocess.PIPE).communicate()[0]

    return 0
    #return args #-> TEST

print "Make XML from CACTI. Input 'Game, Start, End' (24-hour-clock)"

#ip_name = input("Input Game Name to Extract XML from CACTI (L1, L2, AION, BS, LM ... ) : ")
ip_name = raw_input("Input Game Name to Extract XML from CACTI (L1, L2, AION, BS, LM ... ) : ") # -> version2
ip_name = ip_name.lower()

make_xml(ip_name)
