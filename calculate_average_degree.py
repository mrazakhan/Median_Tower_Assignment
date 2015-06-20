from __future__ import division
import sys
from collections import defaultdict
def averagedegree(filenames, outfilename,sep=','):

	sum_dict=defaultdict(int)

	for each2 in filenames:
		fin=open(each2,'r')
		for each in fin:
		  if 'Degree' not in each:
			A,degree=each.split(sep)
			degree=int(degree.rstrip())
			sum_dict[A]+=degree

	for key in sum_dict.keys():
		sum_dict[key]=sum_dict[key]/len(filenames)
	
	fout =open(outfilename,'w')
	fout.write('A,AvgDegree\n')
	for each in sum_dict.keys():
		fout.write(each+','+str(sum_dict[each])+'\n')

	fout.close()		


if __name__=='__main__':
	
	cmdargs=sys.argv[2:]
	outfilename=sys.argv[1]

	averagedegree(cmdargs,outfilename)
