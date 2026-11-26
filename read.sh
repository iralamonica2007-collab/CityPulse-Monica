#!/bin/bash
# Read input from the user and save it to a file

read -p "Your name: " name
read -p "Your roll number: " roll
read -p "Comment: " comment

mkdir -p output
echo "Name: $name" > output/output.txt
echo "Roll Number: $roll" >> output/output.txt
echo "Comment: $comment" >> output/output.txt
cat output/output.txt
