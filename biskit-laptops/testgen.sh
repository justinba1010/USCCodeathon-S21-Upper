# might only work on windows

#on windows, open this using run, then type Bash
# cd Documents/College\ Notes/ACM/CodeathonFall2020/SymbolSubstitution/

#or using cmd use bash testgen.sh

#first use dos2unix testgen.sh to get rid of windows characters
#in bash use ./testgen.sh

# SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd -P)"
# echo $SCRIPT_DIR

[[ -e input/ ]] && rm -r input/ 
[[ -e output/ ]] && rm -r output/ 
# rm -r -p output/
mkdir -p input
mkdir -p output


# [[ -e samples/input ]] && cp -r samples/input ./
# [[ -e samples/output ]] && cp -r samples/output ./

# [[ -e f.txt ]] && cp ../../perimGen23.java ./ 
# pushd $SCRIPT_DIR


#gen samples
# for i in {0..1}
# do
#   # echo "$(cd "$(dirname "$0")" && pwd -P)"
#   echo $i | python3 mkin.py > samples/input/input$i.txt
#   python3 solutions/sol.py < samples/input/input$i.txt > samples/output/output$i.txt

#   echo $i
# done

[[ -e samples/input ]] && cp -r samples/input ./
# [[ -e samples/output ]] && cp -r samples/output ./

# for i in {0..1}
# do
#   python3 solutions/sol.py < input/input$i.txt > output/output$i.txt
# done


for i in {2..30}
do
  echo $i | python3 ./mkin.py > input/input$i.txt
  python3 ./solutions/sol.py < input/input$i.txt > output/output$i.txt

  echo $i
done

rm -rf cases.zip
zip -r cases input output
