__author__ = 'juliewe'
#strip any tabs from end of lines and remove lines with no features

file="wikipedia_t100.pbfiltered"
#file="testdata.pbfiltered"
outfile="wikipedia_nounsdeps_t100.pbfiltered"

with open(file,'r') as instream:
    with open(outfile,'w') as outstream:
        processed=0
        for line in instream:
            line=line.rstrip()
            fields =line.split('\t')
            if len(fields)>1:
                outstream.write(line+"\n")
            processed+=1
            if processed%10000==0: print"Processed "+str(processed)+" lines"
