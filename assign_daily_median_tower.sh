
for file in `ls celltowercounts_*`
do
	echo 'Processing'$file
	python assign_daily_median_tower.py $file 1
done
