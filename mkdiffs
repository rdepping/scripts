#!/bin/sh
#if [ $# -ne 1 ]
#then
#	echo "mkdiffs: Find the differences ibetween the current directory and another directory."
#	echo "Usage: mkdiffs <dir>"
#	echo " <dir> must be a relative path"
#	exit 1
#fi
#if [ ! -d $1 ]
#then
#        echo "Error: please supply a directory for differencing."
#        exit 1
#fi
rm -rf ./tmp
mkdir tmp
basename `pwd` >./tmp/basename
diff -x CVS -x tmp -qr . ../`cat ./tmp/basename`-new > ./tmp/rawdiffs.diff
#diff -x CVS -x tmp -qr . $1 > ./tmp/rawdiffs.diff
#
# Find the deletions.
#
grep 'Only in ./' ./tmp/rawdiffs.diff > ./tmp/dels.diff
grep 'Only in .:' ./tmp/rawdiffs.diff >> ./tmp/dels.diff
awk '{printf("%s%s\n", $3, $4)}' ./tmp/dels.diff > ./tmp/dels1.diff
awk -F: '{printf("%s/%s\n", $1, $2)}' ./tmp/dels1.diff > ./tmp/dels2.diff
rm -f ./tmp/del_dirs1 ./tmp/del_files
for x in `cat ./tmp/dels2.diff`
do
	if [ -d $x ]
	then
		echo $x >> ./tmp/del_dirs
	else
		echo $x >> ./tmp/del_files
	fi
done
rm -f ./tmp/dels.diff ./tmp/dels1.diff ./tmp/dels2.diff 
for x in `cat ./tmp/del_dirs`
do
	find $x \( -type f -a ! -path '*CVS*' \) -exec echo {} \; > ./tmp/del_dirs1
done
awk '{printf("rm -f %s\ncvs rm %s\n", $1, $1);}' < ./tmp/del_dirs1 > ./tmp/del_dirs2
mv ./tmp/del_dirs2 ./tmp/del_dirs_files
rm -f ./tmp/del_dirs1 ./tmp/del_dirs2 ./tmp/del_dirs3
#
# Find the additions.
#
grep 'Only in ../' ./tmp/rawdiffs.diff > ./tmp/adds.diff
awk '{printf("%s%s\n", $3, $4)}' ./tmp/adds.diff > ./tmp/adds1.diff
awk -F: '{printf("%s/%s\n", $1, $2)}' ./tmp/adds1.diff > ./tmp/adds2.diff
rm -f ./tmp/add_dirs1 ./tmp/add_files1
for x in `cat ./tmp/adds2.diff`
do
	if [ -d $x ]
	then
		echo $x >> ./tmp/add_dirs1
	else
		echo $x >> ./tmp/add_files1
	fi
done
awk '{printf("%s %s\n", $1, $1)}' ./tmp/add_dirs1 > ./tmp/add_dirs2
sed '1,$s:\.\./'`cat ./tmp/basename`'-new:\.:' ./tmp/add_dirs2 > ./tmp/add_dirs3
awk '{printf("cp -r %s %s\n", $2, $1)}' ./tmp/add_dirs3 > ./tmp/add_dirs4
echo "#!/bin/sh" > ./tmp/add_dirs
cat ./tmp/add_dirs4 >> ./tmp/add_dirs
awk '{printf("%s %s\n", $1, $1)}' ./tmp/add_files1 > ./tmp/add_files2
sed '1,$s:\.\./'`cat ./tmp/basename`'-new:\.:' ./tmp/add_files2 > ./tmp/add_files3
awk '{printf("cp %s %s\n", $2, $1)}' ./tmp/add_files3 > ./tmp/add_files4
echo "#!/bin/sh" > ./tmp/add_files
cat ./tmp/add_files4 >> ./tmp/add_files
rm -f ./tmp/adds.diff ./tmp/adds1.diff ./tmp/adds2.diff ./tmp/add_files1 ./tmp/add_files2 ./tmp/add_files3 ./tmp/add_files4 ./tmp/add_dirs1 ./tmp/add_dirs2 ./tmp/add_dirs3 ./tmp/add_dirs4
#
# Find the changed files.
#
grep '^Files' ./tmp/rawdiffs.diff > ./tmp/diffs.diff
awk '{printf("cp %s %s\n", $4, $2)}' ./tmp/diffs.diff > ./tmp/diffs1.diff
rm -f ./tmp/diff_files
echo "#!/bin/sh" > ./tmp/diff_files
cat ./tmp/diffs1.diff >> ./tmp/diff_files
rm -f ./tmp/rawdiffs.diff ./tmp/diffs.diff ./tmp/diffs1.diff 
rm -f ./tmp/basename
