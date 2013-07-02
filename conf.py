__author__ = 'Julie'

def configure(args):
    #first 2 args must be filename and frequency threshold

    posspos=['N','V','J','R'] #possible parts of speech for filtering
    parameters={}
    if len(args)<3:
        print "pbfilter.py has 2 compulsory arguments: filename and frequency threshold"
        exit(1)
    parameters['filename']=args[1]
    parameters['fthresh']=int(args[2])
    parameters['pos']=[]
    parameters['exclude-feat']=[]

    if len(args)> 3:
        for arg in args[3:]:
            if arg in posspos:
                parameters['pos'].append(arg)
            else:
                #probably a parameter for setting features
                parameters['exclude-feat'].append(arg)

    if len(parameters['pos'])==0: parameters['pos']=['N'] #default to noun option

    return parameters

