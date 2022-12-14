#!/bin/bash



if [ "$1" == "" ]
then
echo "yOu foRgot An IP addResS!"
echo "Syntax: ./pingsweeper.sh 192.168.0.1"


else
for ip in `seq 1 254` ; do

# $1 for giving an argument when launching the script

ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &

# & sign to multipe threAds at once
# without it it will iterate thhrough them 1 by 1


# or doing with a static way
#ping -c 1 192.168.0.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &

done
fi
