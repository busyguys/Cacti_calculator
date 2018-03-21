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
        l1_1 = " DEF:a='/usr/local/cacti-0.8.8a/rra/public-n7k-1-game-new_traffic_in_20122.rrd':'traffic_in':AVERAGE"
        l1_2 = " DEF:b='/usr/local/cacti-0.8.8a/rra/public-n7k-2-game-new_traffic_in_20502.rrd':'traffic_in':AVERAGE"
        l1_3 = " CDEF:c='a,b,+'"
        l1_4 = " CDEF:result='c,8,*'"
        l1_5 = " XPORT:result:'Result is '"
        print start_point + l1_1 + l1_2 + l1_3 + l1_4 + l1_5
        args = start_point + l1_1 + l1_2 + l1_3 + l1_4 + l1_5
    elif(ip_name=="l2"):
        print "L2!!!!"
        l2_1 = " DEF:a='/usr/local/cacti-0.8.8a/rra/public-n7k-1-game-new_traffic_in_20124.rrd':'traffic_in':AVERAGE"
        l2_2 = " DEF:b='/usr/local/cacti-0.8.8a/rra/public-n7k-2-game-new_traffic_in_20504.rrd':'traffic_in':AVERAGE"
        l2_3 = " CDEF:c='a,b,+'"
        l2_4 = " CDEF:result='c,8,*'"
        l2_5 = " XPORT:result:'Result is '"
        print start_point + l2_1 + l2_2 + l2_3 + l2_4 + l2_5
        args = start_point + l2_1 + l2_2 + l2_3 + l2_4 + l2_5
    elif(ip_name=="aion"):
        print "AION!!!"
        aion_1 = " DEF:a='/usr/local/cacti-0.8.8a/rra/public-n7k-1-game-new_traffic_in_20114.rrd':'traffic_in':AVERAGE"
        aion_2 = " DEF:b='/usr/local/cacti-0.8.8a/rra/public-n7k-1-game-new_traffic_in_20117.rrd':'traffic_in':AVERAGE"
        aion_3 = " DEF:c='/usr/local/cacti-0.8.8a/rra/public-n7k-2-game-new_traffic_in_20494.rrd':'traffic_in':AVERAGE"
        aion_4 = " DEF:d='/usr/local/cacti-0.8.8a/rra/public-n7k-2-game-new_traffic_in_20497.rrd':'traffic_in':AVERAGE"
        aion_5 = " CDEF:e='a,b,+,c,d,+,+'"
        aion_6 = " CDEF:result='e,8,*'"
        aion_7 = " XPORT:result:'Result is '"
        print start_point + aion_1 + aion_2 + aion_3 + aion_4 + aion_5 + aion_6 + aion_7
        args = start_point + aion_1 + aion_2 + aion_3 + aion_4 + aion_5 + aion_6 + aion_7
    elif(ip_name=="bs"):
        print "B&S!!!"
        bs_1 = " DEF:a='/usr/local/cacti-0.8.8a/rra/public-n7k-1-game-new_traffic_in_20107.rrd':'traffic_in':AVERAGE"
        bs_2 = " DEF:b='/usr/local/cacti-0.8.8a/rra/public-n7k-1-game-new_traffic_in_20110.rrd':'traffic_in':AVERAGE"
        bs_3 = " DEF:c='/usr/local/cacti-0.8.8a/rra/public-n7k-2-game-new_traffic_in_20487.rrd':'traffic_in':AVERAGE"
        bs_4 = " DEF:d='/usr/local/cacti-0.8.8a/rra/public-n7k-2-game-new_traffic_in_20490.rrd':'traffic_in':AVERAGE"
        bs_5 = " CDEF:e='a,b,+,c,d,+,+'"
        bs_6 = " CDEF:result='e,8,*'"
        bs_7 = " XPORT:result:'Result is '"
        print start_point+bs_1+bs_2+bs_3+bs_4+bs_5+bs_6+bs_7
        args = start_point+bs_1+bs_2+bs_3+bs_4+bs_5+bs_6+bs_7
    elif(ip_name=="lm"):
        print "LM!!!!"
        lm_1 = " DEF:a='/usr/local/cacti-0.8.8a/rra/public-n7k-1-game_201511_traffic_in_62895.rrd':'traffic_in':AVERAGE"
        lm_2 = " DEF:b='/usr/local/cacti-0.8.8a/rra/public-n7k-2-game_201511_traffic_in_62513.rrd':'traffic_in':AVERAGE"
        lm_3 = " CDEF:c='a,b,+'"
        lm_4 = " CDEF:result='c,8,*'"
        lm_5 = " XPORT:result:'Result is '"
        print start_point+lm_1+lm_2+lm_3+lm_4+lm_5
        args = start_point+lm_1+lm_2+lm_3+lm_4+lm_5
    elif(ip_name=="mobile"):
        print "Mobile!!!!!"
        #args =
    elif(ip_name=="web"):
        print "WEB!!!!!!!"
        #args =
    else:
        print "Input should be L1, L2, AION, BS, LM, MOBILE, WEB"

    # args = start_point + " DEF:test='/usr/local/cacti-0.8.8a/rra/10lan-testnw-01_traffic_in_82726.rrd':'traffic_in':AVERAGE CDEF:test2='test,8,*' XPORT:test2:'test is '"
    seperator = ','
    seperator.join(args)
    args = shlex.split(args)
    #
    output = subprocess.Popen(args, stdout=subprocess.PIPE).communicate()[0]

    return output
    #return args #-> TEST

print "Make XML from CACTI. Input 'Game, Start, End' (24-hour-clock)"

#ip_name = input("Input Game Name to Extract XML from CACTI (L1, L2, AION, BS, LM ... ) : ")
ip_name = raw_input("Input Game Name to Extract XML from CACTI (L1, L2, AION, BS, LM ... ) : ") # -> version2
ip_name = ip_name.lower()

make_xml(ip_name)
