import os
import datetime
import calendar
import time
import xml_check_v2
import subprocess
import shlex


def make_xml_2(start, end):
    args = "/usr/local/rrdtool/bin/rrdtool xport --start " + str(start) + " --end " + str(end) + " DEF:test='/usr/local/cacti-0.8.8a/rra/10lan-testnw-01_traffic_in_82726.rrd':'traffic_in':AVERAGE CDEF:test2='test,8,*' XPORT:test2:'test is '"
    seperator = ','
    seperator.join(args)
    args = shlex.split(args)

    output = subprocess.Popen(args, stdout=subprocess.PIPE).communicate()[0]
    return output
    #return args #-> TEST

def make_xml(ip_name, start=0, end=0):
    start_point = "/usr/local/rrdtool/bin/rrdtool xport --start " + str(start) + " --end " + str(end)
    
    if(ip_name=="l1"):
#        print "L1!!!!"
        l1_1 = " DEF:a='/usr/local/cacti-0.8.8a/rra/public-n7k-1-game-new_traffic_in_20122.rrd':'traffic_in':AVERAGE"
        l1_2 = " DEF:b='/usr/local/cacti-0.8.8a/rra/public-n7k-2-game-new_traffic_in_20502.rrd':'traffic_in':AVERAGE"
        l1_3 = " CDEF:c='a,b,+'"
        l1_4 = " CDEF:result='c,8,*'"
        l1_5 = " XPORT:result:'Result is '"
#        print start_point + l1_1 + l1_2 + l1_3 + l1_4 + l1_5
        args = start_point + l1_1 + l1_2 + l1_3 + l1_4 + l1_5
        
    elif(ip_name=="l2"):
#        print "L2!!!!"
        l2_1 = " DEF:a='/usr/local/cacti-0.8.8a/rra/public-n7k-1-game-new_traffic_in_20124.rrd':'traffic_in':AVERAGE"
        l2_2 = " DEF:b='/usr/local/cacti-0.8.8a/rra/public-n7k-2-game-new_traffic_in_20504.rrd':'traffic_in':AVERAGE"
        l2_3 = " CDEF:c='a,b,+'"
        l2_4 = " CDEF:result='c,8,*'"
        l2_5 = " XPORT:result:'Result is '"
#        print start_point + l2_1 + l2_2 + l2_3 + l2_4 + l2_5
        args = start_point + l2_1 + l2_2 + l2_3 + l2_4 + l2_5
        
    elif(ip_name=="aion"):
#        print "AION!!!"
        aion_1 = " DEF:a='/usr/local/cacti-0.8.8a/rra/public-n7k-1-game-new_traffic_in_20114.rrd':'traffic_in':AVERAGE"
        aion_2 = " DEF:b='/usr/local/cacti-0.8.8a/rra/public-n7k-1-game-new_traffic_in_20117.rrd':'traffic_in':AVERAGE"
        aion_3 = " DEF:c='/usr/local/cacti-0.8.8a/rra/public-n7k-2-game-new_traffic_in_20494.rrd':'traffic_in':AVERAGE"
        aion_4 = " DEF:d='/usr/local/cacti-0.8.8a/rra/public-n7k-2-game-new_traffic_in_20497.rrd':'traffic_in':AVERAGE"
        aion_5 = " CDEF:e='a,b,+,c,d,+,+'"
        aion_6 = " CDEF:result='e,8,*'"
        aion_7 = " XPORT:result:'Result is '"
#        print start_point + aion_1 + aion_2 + aion_3 + aion_4 + aion_5 + aion_6 + aion_7
        args = start_point + aion_1 + aion_2 + aion_3 + aion_4 + aion_5 + aion_6 + aion_7
        
    elif(ip_name=="bs"):
#        print "B&S!!!"
        bs_1 = " DEF:a='/usr/local/cacti-0.8.8a/rra/public-n7k-1-game-new_traffic_in_20107.rrd':'traffic_in':AVERAGE"
        bs_2 = " DEF:b='/usr/local/cacti-0.8.8a/rra/public-n7k-1-game-new_traffic_in_20110.rrd':'traffic_in':AVERAGE"
        bs_3 = " DEF:c='/usr/local/cacti-0.8.8a/rra/public-n7k-2-game-new_traffic_in_20487.rrd':'traffic_in':AVERAGE"
        bs_4 = " DEF:d='/usr/local/cacti-0.8.8a/rra/public-n7k-2-game-new_traffic_in_20490.rrd':'traffic_in':AVERAGE"
        bs_5 = " CDEF:e='a,b,+,c,d,+,+'"
        bs_6 = " CDEF:result='e,8,*'"
        bs_7 = " XPORT:result:'Result is '"
#        print start_point+bs_1+bs_2+bs_3+bs_4+bs_5+bs_6+bs_7
        args = start_point+bs_1+bs_2+bs_3+bs_4+bs_5+bs_6+bs_7
        
    elif(ip_name=="lm"):
#        print "LM!!!!"
        lm_1 = " DEF:a='/usr/local/cacti-0.8.8a/rra/public-n7k-1-game_201511_traffic_in_62895.rrd':'traffic_in':AVERAGE"
        lm_2 = " DEF:b='/usr/local/cacti-0.8.8a/rra/public-n7k-2-game_201511_traffic_in_62513.rrd':'traffic_in':AVERAGE"
        lm_3 = " CDEF:c='a,b,+'"
        lm_4 = " CDEF:result='c,8,*'"
        lm_5 = " XPORT:result:'Result is '"
#       print start_point+lm_1+lm_2+lm_3+lm_4+lm_5
        args = start_point+lm_1+lm_2+lm_3+lm_4+lm_5
        
    elif(ip_name=="plaync"):
        #print "ETC!!!!!!"
        nc_1 = " DEF:a='/usr/local/cacti-0.8.8a/rra/public-gpgame-new_traffic_in_41846.rrd':'traffic_in':AVERAGE"
        nc_2 = " DEF:b='/usr/local/cacti-0.8.8a/rra/public-gpgame-new_traffic_in_41847.rrd':'traffic_in':AVERAGE"
        nc_3 = " CDEF:c='a,b,+'"
        nc_4 = " CDEF:result='c,8,*'"
        nc_5 = " XPORT:result:'Result is '"
#       print start_point+lm_1+lm_2+lm_3+lm_4+lm_5
        args = start_point+nc_1+nc_2+nc_3+nc_4+nc_5
        #args =
        
    elif(ip_name=="web"):
        #print "WEB!!!!!!!"
        web_1 = " DEF:a='/usr/local/cacti-0.8.8a/rra/public-n7k-1-web-new_traffic_in_22360.rrd':'traffic_in':AVERAGE"
        web_2 = " DEF:b='/usr/local/cacti-0.8.8a/rra/public-n7k-2-web-new_traffic_in_22210.rrd':'traffic_in':AVERAGE"
        web_3 = " CDEF:c='a,b,+'"
        web_4 = " CDEF:result='c,8,*'"
        web_5 = " XPORT:result:'Result is '"
#       print start_point+lm_1+lm_2+lm_3+lm_4+lm_5
        args = start_point+web_1+web_2+web_3+web_4+web_5

    elif(ip_name=="talk"):
        #print "TALK!!!!!"
        talk_1 = " DEF:a='/usr/local/cacti-0.8.8a/rra/public-nctalk-new_traffic_in_22071.rrd':'traffic_out':AVERAGE"
        talk_2 = " DEF:b='/usr/local/cacti-0.8.8a/rra/public-nctalk-new_traffic_in_22072.rrd':'traffic_out':AVERAGE"
        talk_3 = " DEF:c='/usr/local/cacti-0.8.8a/rra/public-nctalk-new_traffic_in_22073.rrd':'traffic_out':AVERAGE"
        talk_4 = " DEF:d='/usr/local/cacti-0.8.8a/rra/public-nctalk-new_traffic_in_22074.rrd':'traffic_out':AVERAGE"
        talk_5 = " DEF:e='/usr/local/cacti-0.8.8a/rra/public-nctalk-new_traffic_in_22075.rrd':'traffic_out':AVERAGE"
        talk_6 = " DEF:f='/usr/local/cacti-0.8.8a/rra/public-nctalk-new_traffic_in_22076.rrd':'traffic_out':AVERAGE"
        talk_7 = " CDEF:g='a,b,+,c,d,+,+,e,f,+,+'"
        talk_8 = " CDEF:result='g,8,*'"
        talk_9 = " XPORT:result:'Result is '"
        args = start_point + talk_1 + talk_2 + talk_3 + talk_4 + talk_5 + talk_6 + talk_7 + talk_8 + talk_9

        #args =

    elif(ip_name=="rk"):
        rk_1 = " DEF:a='/usr/local/cacti-0.8.8a/rra/public-lm-01_traffic_in_82648.rrd':'traffic_in':AVERAGE"
        rk_2 = " DEF:b='/usr/local/cacti-0.8.8a/rra/public-lm-02_traffic_in_82684.rrd':'traffic_in':AVERAGE"
        rk_3 = " DEF:c='/usr/local/cacti-0.8.8a/rra/public-lm-01_traffic_in_82649.rrd':'traffic_in':AVERAGE"
        rk_4 = " DEF:d='/usr/local/cacti-0.8.8a/rra/public-lm-02_traffic_in_82685.rrd':'traffic_in':AVERAGE"
        rk_5 = " DEF:e='/usr/local/cacti-0.8.8a/rra/public-lm-01_traffic_in_82650.rrd':'traffic_in':AVERAGE"
        rk_6 = " DEF:f='/usr/local/cacti-0.8.8a/rra/public-lm-02_traffic_in_82686.rrd':'traffic_in':AVERAGE"
        rk_7 = " DEF:g='/usr/local/cacti-0.8.8a/rra/public-lm-01_traffic_in_82651.rrd':'traffic_in':AVERAGE"
        rk_8 = " DEF:h='/usr/local/cacti-0.8.8a/rra/public-lm-02_traffic_in_82687.rrd':'traffic_in':AVERAGE"
        rk_9 = " DEF:i='/usr/local/cacti-0.8.8a/rra/public-lm-01_traffic_in_82652.rrd':'traffic_in':AVERAGE"
        rk_10 = " DEF:j='/usr/local/cacti-0.8.8a/rra/public-lm-02_traffic_in_82688.rrd':'traffic_in':AVERAGE"
        rk_11 = " DEF:k='/usr/local/cacti-0.8.8a/rra/public-lm-01_traffic_in_82653.rrd':'traffic_in':AVERAGE"
        rk_12 = " DEF:l='/usr/local/cacti-0.8.8a/rra/public-lm-02_traffic_in_82689.rrd':'traffic_in':AVERAGE"
        rk_13 = " CDEF:m='a,b,+,c,+,d,+,e,+,f,+,g,+,h,+,i,+,j,+,k,+,l,+'"
        rk_14 = " CDEF:result='m,8,*'"
        rk_15 = " XPORT:result:'Result is '"
        args = start_point + rk_1 + rk_2 + rk_3 + rk_4 + rk_5 + rk_6 + rk_7 + rk_8 + rk_9 + rk_10 + rk_11 + rk_12 + rk_13 + rk_14 + rk_15

    else:
        print "Input should be L1, L2, AION, BS, LM, MOBILE, WEB, RK"

    # args = start_point + " DEF:test='/usr/local/cacti-0.8.8a/rra/10lan-testnw-01_traffic_in_82726.rrd':'traffic_in':AVERAGE CDEF:test2='test,8,*' XPORT:test2:'test is '"
    seperator = ','
    seperator.join(args)
    args = shlex.split(args)
    # #
    output = subprocess.Popen(args, stdout=subprocess.PIPE).communicate()[0]

    return output
#    return 0

def time_convert(time_str):

    # if(n_month=='10' or n_month=='11' or n_month=='12'):
    #     n_month = n_month
    # else:

    time_format = "%Y-%m-%d %H:%M:%S"
    #time_str = n_year+"-"+n_month+"-"+n_day+" 00:00:00"
    #print(time_str)

    if(type(time_str) == datetime.datetime):
        n_time = time_str
    else:
        n_time = datetime.datetime(*time.strptime(time_str, time_format)[:6])
        #n_time = datetime.datetime.strptime(time_str, time_format) - version 3

    time_tuple = n_time.timetuple()
    utc_time = time.mktime(time_tuple)
    utc_time = int(utc_time)
    #print (utc_time)
    #print "UTC TIME IS : " , utc_time

    return utc_time

def time_division(ip_name, t_start, t_end):
    day_array = []
#    print "TIME _ DIVISION - START : " + t_start
#    print "TIME _ DIVISION - END : " + t_end

    time_format = "%Y-%m-%d %H:%M:%S"

    if(time_convert(t_start) >= time_convert(t_end)):
        print ("Start time should be earlier than End time")
        return -1

    print "=====================" + ip_name + "============================="
    #start = datetime.strptime(t_start, time_format) - version3
    start = datetime.datetime(*time.strptime(t_start, time_format)[:6]) #version2
    start_day = start.day
    #end = datetime.strptime(t_end, time_format) - version3
    end = datetime.datetime(*time.strptime(t_end, time_format)[:6])
    end_day = end.day

    for a in range(start_day, end_day+1):
        start = start.replace(day=a)
        start_finish = start.replace(day=a)

        if(a != start_day):
            start = start.replace(hour=00, minute=00, second=00)

        if(a == end_day):
            start_finish = start.replace(hour = end.time().hour, minute = end.time().minute, second = end.time().second)
        else:
            start_finish = start.replace(hour=23, minute=59, second=59)

#        print a, ": ", start, " | ", start_finish
        xml_result = make_xml(ip_name, time_convert(start), time_convert(start_finish))
        t_value, d_value = xml_check_v2.find_TV(xml_result)
	
	temp_max = xml_check_v2.day_max(d_value)
        
#	print "Maximum in one day is :", xml_check_v2.day_max(d_value)
        
	#day_array.append(d_value) #For getting day's average.
	day_array.append(temp_max)

#    print day_array

    avg_result = xml_check_v2.get_average(day_array)

#    print "Average is : ", avg_result

    return 0


if __name__=="__main__":
    print("Make XML from CACTI. Input 'Start, End' (24-hour-clock)")

    #ip_name = input("Input Game Name to Extract XML from CACTI (L1, L2, AION, BS, LM ... ) : ")
#    ip_name = raw_input("Input Game Name to Extract XML from CACTI (L1, L2, AION, BS, LM ... ) : ") # -> version2
#    ip_name = ip_name.lower()
    start_date = raw_input("Input START Time(YYYY-MM-DD HH:MM:SS) : ") #version 2
    end_date = raw_input("Input END Time(YYYY-MM-DD HH:MM:SS) : ")

    # start_date = input("Input From Time(YYYY-MM-DD HH:MM:SS) : ") - version 3
    # end_date = input("Input From Time(YYYY-MM-DD HH:MM:SS) : ")

    #print(start_date.month)
    #print(start_date.day)

    #print ("UTC START TIME:", time_convert(start_date))
    #print ("UTC END TIME:", time_convert(end_date))

    time_division("l1", start_date, end_date)
    time_division("l2", start_date, end_date)
    time_division("lm", start_date, end_date)
    time_division("aion", start_date, end_date)
    time_division("bs", start_date, end_date)
    time_division("talk", start_date, end_date)
    time_division("web", start_date, end_date)
    time_division("plaync", start_date, end_date)
    time_division("rk", start_date, end_date) # For Lineage RK


    print "\n\n\n\n"
    # __array_file = 'rrdtool_xport.txt'
    # a, b = xml_check.find_TV(__array_file)
    #
    # print("Maximum in one day is : ", xml_check.day_max(b))
