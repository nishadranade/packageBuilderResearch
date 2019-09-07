declare a=10000
declare b=1

for i in {0..12}
do
    b=$((b*2));
    python run.py $a $b
done    