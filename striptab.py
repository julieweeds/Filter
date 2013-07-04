__author__ = 'juliewe'

#file="wikipedia_t100.pbfiltered"
file="testdata.pbfiltered"
outfile="wikipedia_nounsdeps_t100.pbfiltered"

with open(file,'r') as instream:
    with open(outfile,'w') as outstream:
        processed=0
        for line in instream:
            line=line.rstrip()
            outstream.write(line+"\n")
            processed+=1
            if processed%1000==0: print"Processed "+str(processed)+"lines"
