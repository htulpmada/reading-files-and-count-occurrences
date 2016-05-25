#########################################
#adam pluth 				#
#project 1				#
#cs260					#
#reading a file	&			# 
#organizing data			#
#########################################


import sys

def numOfInts(nums):
  return len(nums)

def minInt(nums):
  if len(nums)==0:
    return None
  else:
    return int(nums[0])

def maxInt(nums):
  if len(nums)==0:
    return None
  else:
    return nums[-1]

def sums(nums):
  if len(nums)==0:
    return 0
  else:
    t=0
    for i in range(len(nums)):
      t+=int(nums[i])
    return t

def prod(nums):
  if len(nums)==0:
    return 1
  else:
    t=1
    for i in range(len(nums)):
      t = t * nums[i]
    return t

def average(nums):
  if len(nums)==0:
    return None
  else:
    return sums(nums)/len(nums)

def median(nums):
  if len(nums)==0:
    return None
  else:
    l=int(len(nums)/2)
    n=((nums[l]+nums[l-1])/2)
    if l%2==0:
      if(type(n)==float and n-int(n)!=0):
       return ((nums[l]+nums[l-1])/2)
      else:
       return int((nums[l]+nums[l-1])/2)
    else:
      return int(nums[int((len(nums)/2))])

def modes(nums):
    count={}
    temp=0
    modes=[]
    for i in range(len(nums)):
      count[nums[i]]=nums.count(nums[i])
    c = [v for k, v in count.items() if k in nums]
    c2 = list(zip(count.values(),count.keys()))
    c3 = []
    for i in range(len(c2)):
      c3.append(c2[i][1])
    for i in range(len(c)):
      if c[i]>=temp:
        temp=c[i]
    for i in range(len(c)):
      if c[i]==temp:
        modes.append(c3[i])
    modes.sort()
#    print(c,'\n',c2,'\n',c3,'\n',modes,'\n')
    return modes

def main(args):
  temp=[]
  nums=[]  
  if len(args)>=2:
    file = args[1]
    with open(file,'r')as f:
      for line in f:
        temp.append(line.split())
  else:
    infile=sys.stdin
    c=infile.read(1)
    s=''
    l=[]
    while c:
      if c not in " \t\n\r":
        s+=c
      elif len(s)>0:
        temp.append(int(s))
        s=''
      c=infile.read(1)
    if len(s)>0:
      temp.append(int(s))
  try:
    for i in range(len(temp)):
      for j in range(len(temp[i])):
        nums.append(int(temp[i][j]))
    nums.sort()
  except TypeError:
    nums=temp
    nums.sort()
  if len(args)>=3:
    with open(args[2],'w')as f:
      f.write('number = '+str(numOfInts(nums))+'\n')
      f.write('minimum = '+str(minInt(nums))+'\n')
      f.write('maximum = '+str(maxInt(nums))+'\n')
      f.write('sum = '+str(sums(nums))+'\n')
      f.write('product = '+str(prod(nums))+'\n')
      f.write('average = '+str(average(nums))+'\n')
      f.write('median = '+str(median(nums))+'\n')
      f.write('modes = '+str(modes(nums))+'\n')
  else:
    print('number = ',numOfInts(nums))
    print('minimum = ',minInt(nums))
    print('maximum = ',maxInt(nums))
    print('sum = ',sums(nums))
    print('product = ',prod(nums))
    print('average = ',average(nums))
    print('median = ',median(nums))
    print('modes = ',modes(nums))


if __name__=='__main__':
  sys.exit(main(sys.argv))


