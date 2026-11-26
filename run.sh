#!/bin/bash
# Variables, echo, command output and simple file handling

name="Monica"
num=5
echo "Hello from $name"
echo "Number is $num"
echo "Today is $(date)"
echo "I am in $(pwd)"

mkdir -p atria
echo "hello" > atria/data.txt
cat atria/data.txt
ls -l
