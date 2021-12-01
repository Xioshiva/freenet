#!/bin/bash
addresses=('34.136.85.136 ' '34.70.218.194' '34.132.71.50' '35.202.249.93' '34.135.18.32' '34.91.176.101')
file=('b.yaml wait' 'c.yaml wait' 'd.yaml wait' 'e.yaml wait' 'f.yaml wait' 'a.yaml init 50')
index=0

for address in "${addresses[@]}"; do
  ssh -o StrictHostKeyChecking=no -i key benjaminsitb@${address} 'bash -s' < sshLauncher.sh ${file[$index]} &
  index=$((index+1))
done
