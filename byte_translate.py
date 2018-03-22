import re


sample1=11443771980.2
sample2=318042091.235
sample3=10063991671.3

samples=[sample1,sample2,sample3]

giga=1000000000
mega=1049000
kilo=1000

if __name__=="__main__":
    print "Hello!"
    #print samples
    for a in samples:
        if(a>giga):
            print a/giga, "GB"
        elif(a>mega):
            print a/mega, "MB"

            dlxo
        elif(a>kilo):
            print a/kilo, "KB"
        else:
            print a, "B"
