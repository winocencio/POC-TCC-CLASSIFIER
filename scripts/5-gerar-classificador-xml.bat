cd openCV
copy opencv_traincascade.exe "../../negativas"
copy opencv_world346.dll "../../negativas"
cd ../../vetores
copy vetor_final.vec "../negativas"
cd ../negativas
mkdir classificador
opencv_traincascade -data classificador -vec vetor_final.vec -bg bg.txt -numPos 1600 -numNeg 800 -numStages 10 -w 18 -h 18 -precalcBufSize 1024 -precalcIdxBufSize 1024
del opencv_traincascade.exe
del opencv_world346.dll
del vetor_final.vec
cd classificador
mkdir "../../classificador"
copy "*" "../../classificador"
cd ..
rd /s classificador