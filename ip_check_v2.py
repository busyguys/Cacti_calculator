import os
import datetime
import calendar
import time
import xml_check_v2
import subprocess
import shlex


def make_xml(ip_name, start=0, end=0):
    start_point = "/usr/local/rrdtool/bin/rrdtool xport --start " + str(start) + " --end " + str(end)
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
        bs_1 = " DEF:a='/usr/local/cacti-0.8.8a/rra/public-n7k-1-game-new_traffic_in_20107.rrd':'traffic_in':AVERAGE"
        bs_2 = " DEF:b='/usr/local/cacti-0.8.8a/rra/public-n7k-1-game-new_traffic_in_20110.rrd':'traffic_in':AVERAGE"
        bs_3 = " DEF:c='/usr/local/cacti-0.8.8a/rra/public-n7k-2-game-new_traffic_in_20487.rrd':'traffic_in':AVERAGE"
        bs_4 = " DEF:d='/usr/local/cacti-0.8.8a/rra/public-n7k-2-game-new_traffic_in_20490.rrd':'traffic_in':AVERAGE"
        bs_5 = " CDEF:e='a,b,+,c,d,+,+'"
        bs_6 = " CDEF:result='e,8,*'"
        bs_7 = " XPORT:result:'Result is '"
        print start_point+bs_1+bs_2+bs_3+bs_4+bs_5+bs_6
        #args =
    elif(ip_name=="lm"):
        print "LM!!!!"
        lm_1 = " DEF:a='/usr/local/cacti-0.8.8a/rra/public-n7k-1-game_201511_traffic_in_62895.rrd':'traffic_in':AVERAGE"
        lm_2 = " DEF:b='/usr/local/cacti-0.8.8a/rra/public-n7k-2-game_201511_traffic_in_62513.rrd':'traffic_in':AVERAGE"
        lm_3 = " CDEF:c='a,8,*'"
        lm_4 = " CDEF:d='b,8,*'"
        lm_5 = " CDEF:result='c,d,+'"
        lm_6 = " XPORT:result:'Result is '"
        print start_point+lm_1+lm_2+lm_3+lm_4+lm_5+lm_6
        #args =
    elif(ip_name=="mobile"):
        print "Mobile!!!!!"
        #args =
    elif(ip_name=="web"):
        print "WEB!!!!!!!"
        #args =
    else:
        print "Input should be L1, L2, AION, BS, LM, MOBILE, WEB"

    # args = start_point + " DEF:test='/usr/local/cacti-0.8.8a/rra/10lan-testnw-01_traffic_in_82726.rrd':'traffic_in':AVERAGE CDEF:test2='test,8,*' XPORT:test2:'test is '"
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
