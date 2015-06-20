#A,Tower
#1046912098846,IRP625
#1046928914229,INS110
#1046916434433,IHG001


import sys
from collections import defaultdict
import operator

def assign_location(filenames,outfilename,sep=','):
	
	location_dict=defaultdict(lambda: defaultdict(int))
	for each in filenames:
		fin=open(each,'r')
		for each in fin:
			A, Tower=each.split(sep)
			Tower=Tower.rstrip()
			location_dict[A][Tower]+=1

	
        median_tower_dict=defaultdict()

        for each in location_dict.keys():
                median_tower_dict[each]=max(location_dict[each].iteritems(), key=operator.itemgetter(1))[0]

	fout=open('median_'+outfilename,'w')

        fout.write('A,Tower\n')
        for each in median_tower_dict.keys():
                fout.write(each+','+median_tower_dict[each]+'\n')

        fout.close()




if __name__=='__main__':
	total=len(sys.argv)
	outfilename=sys.argv[1]
	cmdargs=sys.argv[2:]
	

	assign_location( cmdargs,outfilename)	
