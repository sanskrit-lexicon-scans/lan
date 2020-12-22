"""
"""
import sys,re,codecs
class Name(object):
 def __init__(self,line):
  line = line.rstrip('\r\n')
  self.filename = line
  m = re.search(r'^lan_(.*)[.]pdf$',line)
  self.page3 = m.group(1)
  self.n = int(m.group(1))
  self.servename = None

def int_to_Roman(num):
 """ Ref: https://www.w3resource.com/python-exercises/class-exercises/python-class-exercise-1.php
 """
 val = [
  1000, 900, 500, 400,
  100, 90, 50, 40,
  10, 9, 5, 4,
  1
  ]
 syb = [
  "M", "CM", "D", "CD",
  "C", "XC", "L", "XL",
  "X", "IX", "V", "IV",
  "I"
  ]
 roman_num = ''
 i = 0
 while  num > 0:
  for _ in range(num // val[i]):
   roman_num += syb[i]
   num -= val[i]
  i += 1
 return roman_num

def find_servename(n):
 if n < 33:
  if n == 7:
   roman = int_to_Roman(1)
  elif n == 9:
   roman = int_to_Roman(2)
  else:
   # roman numerals with 11 <-> iii  (bw scans)
   n1 = (n-11)+3
   roman = int_to_Roman(n1)
  ans = roman
 else:
  # 33 <-> 1
  n1 = (n-33)+1
  ans = '%s' % n1
 return ans
if __name__ == "__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
 with codecs.open(filein,"r","utf-8") as f:
  recs = [Name(x) for x in f]
 print(len(recs))
 # generate pdffiles lines
 outarr = []
 for rec in recs:
  rec.servename = find_servename(rec.n)
  outarr.append("%s:%s:" %(rec.servename,rec.filename))
 with codecs.open(fileout,"w","utf-8") as f:
  for out in outarr:
   f.write(out+'\n')
