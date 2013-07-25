__author__ = 'Julie'

import re, sys
from conf import configure
counts={} #dictionary to hold counts of items
posPATTS={'N':re.compile('.*/N'),'V':re.compile('.*/V'),'J':re.compile('.*/J'),'R':re.compile('.*/R')}
filtPATTS={'deps':re.compile('T:.*'),'wins':re.compile('.*-.*:')}
total=0

def inccount(item):
    current=counts.get(item,0)
    counts[item]=current+1

def count(filename,posPATTS):
    with open(filename,'r') as instream:
        print "Reading "+filename
        linesread=0
        for line in instream:
            initial = line.split('\t')[0]
            for posPATT in posPATTS:
                if posPATT.match(initial):
                    inccount(initial)
            linesread+=1
            if linesread%10000==0:
                print "Read "+str(linesread)+" lines"
    global total
    total=linesread

def filterline(fields,excl_list):
    #filter out features in exclusion_list

    for filtPATT in excl_list:
        newline=[]
        while len(fields)>0:
            feat=fields.pop()
            if not filtPATT.match(feat):
                newline.append(feat)
                #print "Keeping "+feat
            #else:
                #print "Discarding "+feat
        fields=newline

    newline=""
    if len(fields)>0:
        for field in fields:
            newline=newline+"\t"+field
        newline=newline+"\n"

        return newline
    else:
        return ""

def myfilter(filename,fthresh,posPATTS,excl_list):

    outfile = filename+".pbfiltered"

    with open(filename,'r') as instream:
        print "Rereading "+filename
        with open(outfile,'w') as outstream:
            print "Writing "+outfile
            linesprocessed=0
            for line in instream:
                line=line.rstrip()
                fields = line.split('\t')
                initial=fields.pop(0)
                for posPATT in posPATTS:
                    if posPATT.match(initial):
                        if counts.get(initial,0)>fthresh:
                            fields=filterline(fields,excl_list)
                            if len(fields)>0:
                                outstream.write(initial+fields)
                linesprocessed+=1
                if linesprocessed%10000==0:
                    percent = float(linesprocessed)*100/float(total)
                    print "Processed "+str(linesprocessed)+" lines ("+str(percent)+"%)"


    return

if __name__=="__main__":
    parameters=configure(sys.argv)
    in_pos=[]
    for pos in parameters['pos']:
        patt = posPATTS.get(pos,"none")
        if patt != "none":
            in_pos.append(patt)
    print in_pos
    count(parameters['filename'],in_pos) #make count dictionary
    #print counts
    print "Number of counted words is "+str(len(counts))
    excl_list=[]
    for exclude in parameters['exclude-feat']:
        patt = filtPATTS.get(exclude,"none")
        if patt != "none":
            excl_list.append(patt)

    myfilter(parameters['filename'],parameters['fthresh']-1,in_pos,excl_list)


