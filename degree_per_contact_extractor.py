import pandas as pd
import numpy as np
import os
import sys

from collections import defaultdict

DEBUG =1

def process_input_file(filename, sep='|'):
	fin=open(filename,'r')

	degree_dict=defaultdict(lambda: defaultdict(int))
	
	first=0
	for each in fin:
		lst=each.split(sep)
		hour=lst[0].split(' ')[-1].split(':')[0]
		A_party=lst[1]
		B_party=lst[2]
		A_tower=lst[4]
		B_tower=lst[5]

		A_string=A_party
		if first==0:
			print 'DEBUG '+A_string
			first=first+1
		degree_dict[A_string][B_party]+=1
		degree_dict[B_party][A_party]+=1		

	fout=open('degree_'+filename,'w')
	fout.write('A,Degree\n')

	for each in degree_dict.keys():
		fout.write(each+','+str(len(degree_dict[each].keys()))+'\n')
	fout.close()

	
		
if __name__=='__main__':
	if len(sys.argv)!=2:
		print 'Wrong number of arguments'
		print 'Input file name required'

		sys.exit(-1)

	process_input_file(sys.argv[1])
