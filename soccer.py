#!/usr/bin/python
import sys
import os
import re
import os.path
from os import path

if len(sys.argv) < 2:
    name = input('ENTER DATA (FORMAT MUST BE CORRECT) OR TEXT FILE PATH\n')
    if (name.find(".txt") != -1):
        if path.exists(name):
            with open(name, "r") as text_file:
                name = text_file.read().replace('\n', ' ')
                name = re.split(r',\s|(?<=\d)\s|\s(?=\d)|(?<=,)\s', name)
        else:
            sys.exit("FAILED, INCORRECT INPUT")
    else:
        name = re.split(r',\s|(?<=\d)\s|\s(?=\d)|(?<=,)\s', name)
        if len(name) % 2 != 0:
            sys.exit("FAILED, INCORRECT INPUT")
else:
    if (sys.argv[1].find(".txt") != -1):
        if path.exists(sys.argv[1]):
            with open(sys.argv[1], "r") as text_file:
                name = text_file.read().replace('\n', ' ')
                name = re.split(r',\s|(?<=\d)\s|\s(?=\d)|(?<=,)\s', name)
        else:
            sys.exit("FAILED, INCORRECT INPUT")
    else:
        name = sys.argv[1]
        name = re.split(r',\s|(?<=\d)\s|\s(?=\d)|(?<=,)\s', name)
        if len(name) % 2 != 0:
            sys.exit("FAILED, INCORRECT INPUT")
n = len(name)
dup = 0
lines = []
f = open("output.txt", "w")
f.close()
for l in range(n//4):
    i = l * 4
    if int(name[i + 1]) > int(name[i + 3]):
        with open("output.txt", "a+") as text_file:
            dup = 0
            text_file.seek(0)
            lines = text_file.readlines()
            for j in range(len(lines)):
                if name[i] == lines[j].rstrip('\n\t'):
                    dup = 1
                    f = open("new_output.txt", "a+")
                    for k in range(len(lines)):
                        if (k == j + 1):
                            num = int(lines[j + 1].rstrip('\n\t')) + 3
                            print(f"{num}", file=f)
                        else:
                            str = lines[k].rstrip('\n\t')
                            print(f"{str}", file=f)
                    f.close()
        if (dup):
            os.remove('output.txt')
            os.rename('new_output.txt', 'output.txt')
        else:
            with open("output.txt", "a+") as text_file:
                print(f"{name[i]}", file=text_file)
                print(f"3", file=text_file)
        with open("output.txt", "a+") as text_file:
            dup = 0
            text_file.seek(0)
            lines = text_file.readlines()
            for j in range(len(lines)):
                if name[i + 2] == lines[j].rstrip('\n\t'):
                    dup = 1
                    f = open("new_output.txt", "a+")
                    for k in range(len(lines)):
                        if (k == j + 1):
                            num = int(lines[j + 1].rstrip('\n\t')) + 0
                            print(f"{num}", file=f)
                        else:
                            str = lines[k].rstrip('\n\t')
                            print(f"{str}", file=f)
                    f.close()
        if (dup):
            os.remove('output.txt')
            os.rename('new_output.txt', 'output.txt')
        else:
            with open("output.txt", "a+") as text_file:
                print(f"{name[i + 2]}", file=text_file)
                print("0", file=text_file)
    elif int(name[i + 1]) < int(name[i + 3]):
        with open("output.txt", "a+") as text_file:
            dup = 0
            text_file.seek(0)
            lines = text_file.readlines()
            for j in range(len(lines)):
                if name[i] == lines[j].rstrip('\n\t'):
                    dup = 1
                    f = open("new_output.txt", "a+")
                    for k in range(len(lines)):
                        if (k == j + 1):
                            num = int(lines[j + 1].rstrip('\n\t')) + 0
                            print(f"{num}", file=f)
                        else:
                            str = lines[k].rstrip('\n\t')
                            print(f"{str}", file=f)
                    f.close()
        if (dup):
            os.remove('output.txt')
            os.rename('new_output.txt', 'output.txt')
        else:
            with open("output.txt", "a+") as text_file:
                print(f"{name[i]}", file=text_file)
                print(f"0", file=text_file)
        with open("output.txt", "a+") as text_file:
            dup = 0
            text_file.seek(0)
            lines = text_file.readlines()
            for j in range(len(lines)):
                if name[i + 2] == lines[j].rstrip('\n\t'):
                    dup = 1
                    f = open("new_output.txt", "a+")
                    for k in range(len(lines)):
                        if (k == j + 1):
                            num = int(lines[j + 1].rstrip('\n\t')) + 3
                            print(f"{num}", file=f)
                        else:
                            str = lines[k].rstrip('\n\t')
                            print(f"{str}", file=f)
                    f.close()
        if (dup):
            os.remove('output.txt')
            os.rename('new_output.txt', 'output.txt')
        else:
            with open("output.txt", "a+") as text_file:
                print(f"{name[i + 2]}", file=text_file)
                print("3", file=text_file)
    elif int(name[i + 1]) == int(name[i + 3]):
        with open("output.txt", "a+") as text_file:
            dup = 0
            text_file.seek(0)
            lines = text_file.readlines()
            for j in range(len(lines)):
                if name[i] == lines[j].rstrip('\n\t'):
                    dup = 1
                    f = open("new_output.txt", "a+")
                    for k in range(len(lines)):
                        if (k == j + 1):
                            num = int(lines[j + 1].rstrip('\n\t')) + 1
                            print(f"{num}", file=f)
                        else:
                            str = lines[k].rstrip('\n\t')
                            print(f"{str}", file=f)
                    f.close()
        if (dup):
            os.remove('output.txt')
            os.rename('new_output.txt', 'output.txt')
        else:
            with open("output.txt", "a+") as text_file:
                print(f"{name[i]}", file=text_file)
                print(f"1", file=text_file)
        with open("output.txt", "a+") as text_file:
            dup = 0
            text_file.seek(0)
            lines = text_file.readlines()
            for j in range(len(lines)):
                if name[i + 2] == lines[j].rstrip('\n\t'):
                    dup = 1
                    f = open("new_output.txt", "a+")
                    for k in range(len(lines)):
                        if (k == j + 1):
                            num = int(lines[j + 1].rstrip('\n\t')) + 1
                            print(f"{num}", file=f)
                        else:
                            str = lines[k].rstrip('\n\t')
                            print(f"{str}", file=f)
                    f.close()
        if (dup):
            os.remove('output.txt')
            os.rename('new_output.txt', 'output.txt')
        else:
            with open("output.txt", "a+") as text_file:
                print(f"{name[i + 2]}", file=text_file)
                print("1", file=text_file)
with open("output.txt", "r") as text_file:
    lines = text_file.read().splitlines()
    i = 0
    loop = 0
    while i < len(lines)-3:
        if i % 2 & i > 0:
            i += 1
        if int(lines[i + 1]) < int(lines[i + 3]):
            tdup = lines[i]
            pdup = lines[i + 1]
            lines[i] = lines[i + 2]
            lines[i + 1] = lines[i + 3]
            lines[i + 2] = tdup
            lines[i + 3] = pdup
            loop = 1
            i = 0
        else:
            loop = 0
        if loop == 0:
            i += 1
    i = 0
    loop = 0
    while i < len(lines)-3:
        if i % 2 & i > 0:
            i += 1
        if (lines[i + 2] < lines[i]) & (int(lines[i + 1]) == int(lines[i + 3])):
            tdup = lines[i]
            pdup = lines[i + 1]
            lines[i] = lines[i + 2]
            lines[i + 1] = lines[i + 3]
            lines[i + 2] = tdup
            lines[i + 3] = pdup
            loop = 1
            i = 0
        else:
            loop = 0
        if loop == 0:
            i += 1
i = 0
a = 1
j = -1
while i < len(lines) - 2:
    if i % 2 & i > 0:
        i += 1
    if int(lines[i + 1]) != 1:
        if (j == int(lines[i + 1])):
            print(a - 1, ". ", sep='', end='')
        else:
            print(a, ". ", sep='', end='')
            a += 1
        print(lines[i], lines[i + 1], sep=", ", end=" pts\n")
    else:
        if (j == int(lines[i + 1])):
            print(a - 1, ". ", sep='', end='')
        else:
            print(a, ". ", sep='', end='')
            a += 1
        print(lines[i], lines[i + 1], sep=", ", end=" pt\n")
    j = int(lines[i + 1])
    i += 1
