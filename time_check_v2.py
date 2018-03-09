import os
import datetime
import calendar
import time
import xml_check_v2
import subprocess
import shlex


def make_xml(start, end):
    args = "/usr/local/rrdtool/bin/rrdtool xport --start " + str(start) + " --end " + str(end) + " DEF:test='/usr/local/cacti-0.8.8a/rra/10lan-testnw-01_traffic_in_82726.rrd':'traffic_in':AVERAGE CDEF:test2='test,8,*' XPORT:test2:'test is '"
    seperator = ','
    seperator.join(args)
    args = shlex.split(args)

    output = subprocess.Popen(args, stdout=subprocess.PIPE).communicate()[0]
    return output
    #return args #-> TEST

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

print("Make XML from CACTI. Input 'Game, Start, End' (24-hour-clock)")

#ip_name = input("Input Game Name to Extract XML from CACTI (L1, L2, AION, BS, LM ... ) : ")
#ip_name = raw_input("Input Game Name to Extract XML from CACTI (L1, L2, AION, BS, LM ... ) : ") # -> version2
start_date = raw_input("Input From Time(YYYY-MM-DD HH:MM:SS) : ") #version 2
end_date = raw_input("Input From Time(YYYY-MM-DD HH:MM:SS) : ")

# start_date = input("Input From Time(YYYY-MM-DD HH:MM:SS) : ") - version 3
# end_date = input("Input From Time(YYYY-MM-DD HH:MM:SS) : ")

#print(start_date.month)
#print(start_date.day)

#print ("UTC START TIME:", time_convert(start_date))
#print ("UTC END TIME:", time_convert(end_date))



def time_division(t_start, t_end='2018-03-31 13:00:00'):
    day_array = []
    print "TIME _ DIVISION - START : " + t_start
    print "TIME _ DIVISION - END : " + t_end

    time_format = "%Y-%m-%d %H:%M:%S"

    if(time_convert(t_start) >= time_convert(t_end)):
        print ("Start time should be earlier than End time")
        return -1


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

        print a, ": ", start, " | ", start_finish
        xml_result = make_xml(time_convert(start), time_convert(start_finish))
        t_value, d_value = xml_check_v2.find_TV(xml_result)
        print "Maximum in one day is :", xml_check_v2.day_max(d_value)
        day_array.append(d_value) #For getting day's average.

    avg_result = xml_check_v2.get_average(day_array)
    print "Average is : ", avg_result

    return 0


time_division(start_date, end_date)

# __array_file = 'rrdtool_xport.txt'
# a, b = xml_check.find_TV(__array_file)
#
# print("Maximum in one day is : ", xml_check.day_max(b))
