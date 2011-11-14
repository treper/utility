import os
import sys
import string
fileList = []
rootdir = os.getcwd()
for root, subFolders, files in os.walk(rootdir):
    for file in files:
        fn=os.path.join(root,file)
        #print fn
        filename,filext=os.path.splitext(file)
        #print filename,filext
        if filext=='.cpp' or filext=='.h' or filext=='.c':
            print fn
            f=open(fn)
            ft=fn+'.bak'
            fb=open(ft,'w')
            for fl in f.readlines():
                if fl.find("#include")!=-1:
                    fl=fl.replace('\\','/')
                    #print fl
                fb.write(fl)
                     
            f.close()
            os.remove(fn)
            fb.close()
            os.rename(os.path.join(root,ft),fn)
            
            

