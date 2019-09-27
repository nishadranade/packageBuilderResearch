declare a=20
declare b=16

for i in {0..2}
do
    a=$((a*5));
    b=$((b*5));
    python run.py $a $b
done    