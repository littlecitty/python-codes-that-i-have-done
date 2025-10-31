#!/bin/bash
for i in {21..30}; do
  echo "🔹 File: $i.py 🔹"
  echo "------------------------"
  cat "$i.py"
  echo                         # blank line between files
done


# ##[shivam@archlinux 1_to_100_journey]$ echo {11..23}.py
# 11.py 12.py 13.py 14.py 15.py 16.py 17.py 18.py 19.py 20.py 21.py 22.py 23.py
# [shivam@archlinux 1_to_100_journey]$ cat {11..23}.py
