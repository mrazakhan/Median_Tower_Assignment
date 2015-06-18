#A,Tower,Hour,Count
#1046909783724,KKX630,11,1
#1046880554439,KSKR04,08,1
#1046935211462,LHFR06,11,1

import sys
from collections import defaultdict
import operator

def assign_median_location(fin_name,sep=',', evening="0"):

	fin=open(fin_name,'r')

	all_tower_dict=defaultdict(lambda: defaultdict(int))

	for each in fin:
	  if 'Hour' not in each:
		A,Tower,Hour,Count=each.split(sep)
		Hour=int(Hour)
		if evening =="1":
			if Hour<9 or Hour>18:
				all_tower_dict[A][Tower]+=1
		else:

			all_tower_dict[A][Tower]+=1

	#1046881870459 defaultdict(<type 'int'>, {'ACR006': 1})
	#1046909783724 defaultdict(<type 'int'>, {'KKX630': 4, 'KKX601': 1, 'KKX621': 1})

	
	median_tower_dict=defaultdict()

	for each in all_tower_dict.keys():
		median_tower_dict[each]=max(all_tower_dict[each].iteritems(), key=operator.itemgetter(1))[0]
	'''
	for each in median_tower_dict.keys():
		print each,median_tower_dict[each]
		
		#temp='1046909783724'
		#print temp, median_tower_dict[temp]
		#break
		#Expected output
		#1046925726019 KDSR01
		#1046909783724 KKX630
	'''
	fout=open('median_'+fin_name,'w')

	fout.write('A,Tower\n')
	for each in median_tower_dict.keys():
		fout.write(each+','+median_tower_dict[each]+'\n')

	fout.close()


if __name__=='__main__':
	if len(sys.argv)!=3:
		print 'Wrong number of args'
		print 'Args: InputFilename, evening=1 or overall=0'
		sys.exit(-1)
	fin_name=sys.argv[1]
	mode=sys.argv[2]
	
	assign_median_location(fin_name,evening=mode)
		
