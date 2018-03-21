import re
import os


def find_TV(array_file):
    #new_file = open(array_file,'r')
    new_file = array_file.split()

    t_array=[]
    v_array=[]
    t_v_pattern = '<t>\d*</t><v>.*</v>'
    t_pattern = '<t>\d*</t>' # Time RE Pattern
    v_pattern = '<v>.*</v>' # Value RE Pattern
    re_pattern = '(\d*\.*\d*e(\+|\-)\d*)|\d+' # Get numbers in T | V Pattern

    for line in new_file:
        t_result = re.search(t_pattern, line)
        v_result = re.search(v_pattern, line)

        if(t_result or v_result):
		try:
	            t_array.append(re.search(re_pattern, t_result.group()).group())
        	    v_array.append(float(re.search(re_pattern, v_result.group()).group()))
		except:
		    t_array.append(0)
		    v_array.append(0)
             #print(a, ': ' + line + "Correct!")
#    print t_array
#    print v_array


    return (t_array, v_array)

#print(3.4002473993e+03)
# print(t_array)
# print("==========================================")
# print(v_array)

__array_file = '''
<xport>
  <meta>
    <start>1519703100</start>
    <step>300</step>
    <end>1519789500</end>
    <rows>289</rows>
    <columns>1</columns>
    <legend>
      <entry>TEST is </entry>
    </legend>
  </meta>
  <data>
    <row><t>1519703100</t><v>3.4002473993e+03</v></row>
    <row><t>1519703400</t><v>3.5028342007e+03</v></row>
    <row><t>1519703700</t><v>3.8037973333e+03</v></row>
    <row><t>1519704000</t><v>3.4045698667e+03</v></row>
    <row><t>1519704300</t><v>3.5838546667e+03</v></row>
    <row><t>1519704600</t><v>3.7969330667e+03</v></row>
    <row><t>1519704900</t><v>3.3344794667e+03</v></row>
    <row><t>1519705200</t><v>3.5613410667e+03</v></row>
    <row><t>1519705500</t><v>3.7216948602e+03</v></row>
    <row><t>1519705800</t><v>3.4848956497e+03</v></row>
    <row><t>1519706100</t><v>4.0045011842e+03</v></row>
    <row><t>1519706400</t><v>3.9857558257e+03</v></row>
  </data>
</xport>
'''

def day_max(arrayfile):
    #print(arrayfile)
    day_ = max(arrayfile)
    return day_

def get_average(arrayfile):
#   print sum(arrayfile)
#    print len(arrayfile)
    avg_result = sum(arrayfile) / float(len(arrayfile))
    return avg_result
    #return 0

# __array_file = 'rrdtool_xport.txt'
# a, b = find_TV(__array_file)
# print day_max(b)
# testing = [1,2,3,4,5,6,7,8,9,10]
# print get_average(testing)
