docker images |grep "kolla" |awk '{print $1}' > kolla.txt
for i in `cat kolla.txt`
do
    docker tag $i:4.0.0 192.168.8.73:5000/$i:4.0.0 
    docker push 192.168.8.73:5000/$i
done