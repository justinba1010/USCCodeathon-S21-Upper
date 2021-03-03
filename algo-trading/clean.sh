# /bin/zsh
find . -iname '*.cpp' -type f -exec sed -i.orig 's/	/    /g' {} +
find . -iname '*.*.orig' -type f -exec rm {} +
find . -iname '*.*' -type f -exec zsh -c 'tail -n1 {} | read -r _ || echo >> {};' \;

for x in $(find . -iname '*.cpp' -type f); do  
head -5 $x | diff copyright.txt - || ( ( cat copyright.txt; echo; cat $x) > /tmp/file;  
mv /tmp/file $x )  
done 
