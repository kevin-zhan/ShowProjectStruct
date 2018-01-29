#coding=utf8
import sys
import os
from prettytable import *

level = 3
detect_dir = "."
if len(sys.argv) > 1:
    detect_dir = str(sys.argv[1])
    
if len(sys.argv) > 2:
    level = int(sys.argv[2])

root_dirs = []
contained_dirs = []

for root, dirs, files in os.walk(detect_dir):
    root_dirs.append(root)
    contained_dirs.append(dirs)

table = PrettyTable()
rows = []
for i in range(0,len(contained_dirs)):
    if len(contained_dirs[i]) == 0:
        row = root_dirs[i].split("/")[len(detect_dir.split("/"))-1:]
        rows.append(row)

max_len = 0
for row in rows:
    if max_len < len(row):
        max_len = len(row)
max_len = min(max_len,level)

field_names = []
for i in range(0,max_len):
    field_names.append(str(i+1)+"级目录")
table.field_names = field_names

temp_row = []
for row in rows:
    if len(temp_row) == 0:
        temp_row = list(row)
        continue
    min_len = min(len(temp_row),len(row))
    for i in range(0,min_len):
        if temp_row[i] == row[i]:
            row[i] = ""
        else:
            temp_row[i:] = list(row[i:])
            break

for row in rows:
    to_add_row = []
    for i in range(0,max_len):
        to_add_row.append("")
    if len(row) > max_len:
        to_add_row = row[0:max_len]
    else:
        to_add_row[0:len(row)] = row
    for i in range(0,len(to_add_row)):
        if to_add_row[i] != "":
            table.add_row(to_add_row)
            break

print table
    





