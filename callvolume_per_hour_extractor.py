import pandas as pd
import numpy as np
import os
import sys

from collections import defaultdict

DEBUG =1

def process_input_file(filename, sep='|'):
	fin=open(filename,'r')

	counts_dict=defaultdict(int)
	
	first=0
	for each in fin:
		lst=each.split(sep)
		hour=lst[0].split(' ')[-1].split(':')[0]
		A_party=lst[1]
		B_party=lst[2]
		A_tower=lst[4]
		B_tower=lst[5]

		if A_tower!="":
			A_string=A_party+","+A_tower+","+hour
			if first==0:
				print 'DEBUG '+A_string
				first+=1
			counts_dict[A_string]+=1
		
		if B_tower!="":
			B_string=B_party+","+B_tower+","+hour
			counts_dict[B_string]+=1

	fout=open('celltowercounts_'+filename,'w')
	fout.write('A,Tower,Hour,Count\n')

	for each in counts_dict.keys():
		fout.write(each+','+str(counts_dict[each])+'\n')
	fout.close()

	
		
if __name__=='__main__':
	if len(sys.argv)!=2:
		print 'Wrong number of arguments'
		print 'Input file name required'

		sys.exit(-1)

	process_input_file(sys.argv[1])
