for gender in male female
do

for type in sms gsm
do

for day in 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18

do

echo $type'_'$gender'_cleaned_2014-06-'$day'.txt'

python callvolume_per_hour_extractor.py $type'_'$gender'_cleaned_2014-06-'$day'.txt'


done


done


done

