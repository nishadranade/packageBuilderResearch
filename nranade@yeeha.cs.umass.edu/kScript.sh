declare a=100
declare b=5

for i in {0..2}
do
    b=$((b*2));
    python run.py $a $b
done    