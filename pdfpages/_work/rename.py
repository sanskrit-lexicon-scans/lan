"""
"""
import sys,re,codecs
from os import listdir
from os.path import isfile, join
mypath = "../"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
if __name__ == "__main__":
 fileout = sys.argv[1]
 #print(onlyfiles)
 print(len(onlyfiles))
 # generate a script
 outarr = []
 outarr.append('cd ../')
 for filename in onlyfiles:
  m = re.search(r'^sanskritreaderw00lanm_bw ([0-9]+)[.]pdf$',filename)
  if not m:
   print('unparsed',filename)
   continue
  fnum = int(m.group(1))
  newname = "lan_%03d.pdf" %fnum
  outarr.append("mv '%s' %s" %(filename,newname))
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
