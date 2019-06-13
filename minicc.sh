if [ $# -eq 0 ];then
python3 compiler.py
elif [ $# -eq 1 ];then
python3 compiler.py $1 >> .tmp
rm .tmp
else
python3 compiler.py $1 $2 >> .tmp
rm .tmp
fi
