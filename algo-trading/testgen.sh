SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd -P)"

mkdir -p input
mkdir -p output

pushd $SCRIPT_DIR
    values=(
        '2,3,5'
        '3,3,10'
        '4,3,15'
        '5,3,25'
        '6,5,32'
        '7,5,64'
        '8,7,128'
        '9,10,256'
        '10,10,512'
        '11,10,1024'
        '12,10,2048'
        '13,10,4096'
        '14,15,10000' 
        '15,50,10000'
        '16,75,10000'
        '17,100,10000'
        '18,10,10000'
        '19,5,10000'
        '20,3,10000'
        '21,15,20000'
        '22,15,100000'
        '23,5,100000'
        '24,5,150000'
        '25,5,250000'
        '26,5,300000'
        '27,2,300000'
        '28,2,450000'
)

pushd solutions
clang++ -std=c++11 solution.cpp -o solutioncpp
clang++ -std=c++11 solution2.cpp -o solutioncpp2
popd

  for datarow in "${values[@]}"; do
    while IFS=',' read -r i n k;  do
      echo $i $n $k
      echo $n $k | python3 ./mkin.py > input/input$i.txt;
      ./solutions/solutioncpp2 < input/input$i.txt > output/output$i.txt
      if [[ $i -gt "20" ]]
      then
        continue
      fi
      ./solutions/solutioncpp < input/input$i.txt > /tmp/output$i.txt
      S1=`wc -w output/output$i.txt | cut -f1 -d' '`
      S2=`wc -w /tmp/output$i.txt | cut -f1 -d' '`
      if [[ $S1 -ne $S2 ]]
      then
        diff output/output$i.txt /tmp/output$i.txt
      fi
    done <<< "$datarow"
  done

  for i in {0..0}
  do
    ./solutions/solutioncpp < input/input$i.txt > output/output$i.txt
  done

rm -rf cases.zip
zip -r cases input output
popd
