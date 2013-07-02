__author__ = 'Julie'

import re, sys
from conf import configure
counts={} #dictionary to hold counts of items
posPATTS={'N':re.compile('.*/N'),'V':re.compile('.*/V'),'J':re.compile('.*/J'),'R':re.compile('.*/R')}


def inccount(item):
    current=counts.get(item,0)
    counts[item]=current+1

def count(filename,posPATT):
    with open(filename,'r') as instream:
        for line in instream:
            initial = line.split('\t')[0]
            if posPATT.match(initial):
                inccount(initial)



def myfilter(filename,pos,excl_list):
    return

if __name__=="__main__":
    parameters=configure(sys.argv)
    count(parameters['filename'],posPATTS[parameters['pos']]) #make count dictionary
    myfilter(parameters['filename'],parameters['pos'],parameters['exclude-feat'])

    print counts
