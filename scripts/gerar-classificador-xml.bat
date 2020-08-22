
set destino=%1
set numPos=%2
set numNeg=%3
set wh=%4
set numStages=%5
set featureType=%6
set mode=%7
set boostType=%8
set memoriaUsada=%9


cd openCV
copy opencv_traincascade.exe "../../negativas"
copy opencv_world346.dll "../../negativas"
cd ../../vetores
copy vetor_final.vec "../negativas"
cd ../negativas
mkdir classificador
opencv_traincascade -data classificador -vec vetor_final.vec -bg bg.txt -numPos %numPos% -numNeg %numNeg% -numStages %numStages% -w %wh% -h %wh% -precalcBufSize %memoriaUsada% -precalcIdxBufSize %memoriaUsada% -featureType %featureType% -mode %mode% -bt %boostType%
del opencv_traincascade.exe
del opencv_world346.dll
del vetor_final.vec
cd classificador
mkdir "../../classificador/%destino%"
copy "*" "../../classificador/%destino%"
cd ..
rd /s /q classificador