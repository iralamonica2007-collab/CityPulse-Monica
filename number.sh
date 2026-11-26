#!/bin/bash
# if / elif / else and a while loop

read -p "Enter a number: " num
if [ "$num" -gt 0 ]; then
  echo "$num is positive"
elif [ "$num" -lt 0 ]; then
  echo "$num is negative"
else
  echo "$num is zero"
fi

count=1
while [ $count -le 5 ]; do
  echo "Count: $count"
  ((count++))
done
