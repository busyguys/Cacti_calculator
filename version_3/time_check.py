import os
import datetime
import calendar
import time
import xml_check

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
start_date = raw_input("Input From Time(YYYY-MM-DD HH:MM:SS) : ") #version 2
end_date = raw_input("Input From Time(YYYY-MM-DD HH:MM:SS) : ")

# start_date = input("Input From Time(YYYY-MM-DD HH:MM:SS) : ") - version 3
# end_date = input("Input From Time(YYYY-MM-DD HH:MM:SS) : ")

#print(start_date.month)
#print(start_date.day)

#print ("UTC START TIME:", time_convert(start_date))
#print ("UTC END TIME:", time_convert(end_date))



def time_division(t_start, t_end='2018-03-31 13:00:00'):
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
        print time_convert(start), " | " , time_convert(start_finish)
        #make_xml(time_convert(start), time_convert(start_finish)) -> Make XML files.

    return 0


time_division(start_date, end_date)




def make_xml(start, end):
    return 0

__array_file = 'rrdtool_xport.txt'
a, b = xml_check.find_TV(__array_file)

print("Maximum in one day is : ", xml_check.day_max(b))
