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
        '14,15,10240' 
)

pushd solutions
clang++ -std=c++11 solution.cpp -o solutioncpp
popd

  for datarow in "${values[@]}"; do
    while IFS=',' read -r i n k;  do
      echo $i $n $k
      echo $n $k | python3 ./mkin.py > input/input$i.txt;
      ./solutions/solutioncpp < input/input$i.txt > output/output$i.txt
    done <<< "$datarow"
  done

  for i in {0..1}
  do
    ./solutions/solutioncpp < input/input$i.txt > output/output$i.txt
  done

rm -rf cases.zip
zip -r cases input output
popd
