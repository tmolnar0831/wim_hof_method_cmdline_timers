#!/bin/bash

#
# Tom's Health Cafe Wim Hof Method breathing timer
# URL: https://tomsitcafe.com
#

# Define the number of rounds
rounds=3

# Define the number of breaths per round
breaths=30

# Define breath lenght in seconds
breath_length=3

# Define the retention times
retention1=30
retention2=60
retention3=90

# Define the recovery time
recovery=15

# Loop through each round
for ((i=1; i<=$rounds; i++))
do
    echo "Round $i"
    echo "Breathing in $breaths breaths:"
    for ((j=1; j<=$breaths; j++))
    do
        echo "Breath $j"
        sleep $breath_length
    done

    echo "Retention 1 for $retention1 seconds"
    sleep $retention1

    echo "Recovery for $recovery seconds"
    sleep $recovery

    echo "Retention 2 for $retention2 seconds"
    sleep $retention2

    echo "Recovery for $recovery seconds"
    sleep $recovery

    echo "Retention 3 for $retention3 seconds"
    sleep $retention3

    echo "Recovery for $recovery seconds"
    sleep $recovery
done