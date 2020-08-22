#!/bin/bash
export destino=$1
export numPos=$2
export numNeg=$3
export wh=$4
export numStages=$5
export featureType=$6
export mode=$7
export boostType=$8
export memoriaUsada=$9

cd ../vetores
cp vetor_final.vec "../negativas"
cd ../negativas
mkdir classificador
opencv_traincascade -data classificador -vec vetor_final.vec -bg bg.txt -numPos $numPos -numNeg $numNeg -numStages $numStages -w $wh -h $wh -precalcBufSize $memoriaUsada -precalcIdxBufSize $memoriaUsada -featureType $featureType -mode $mode -bt $boostType
del vetor_final.vec
cd classificador
mkdir "../../classificador/$destino"
cp "*" "../../classificador/$destino"
cd ..
rm -rf classificador