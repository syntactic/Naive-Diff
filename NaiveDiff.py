#!/usr/local/bin/python3

import sys

filename1 = sys.argv[1]
filename2 = sys.argv[2]

with open(filename1, 'r') as file1:
    content1 = file1.readlines()
content1 = [x.strip() for x in content1]

with open(filename2, 'r') as file2:
    content2 = file2.readlines()
content2 = [x.strip() for x in content2]

assert(len(content1) == len(content2))

alreadyNotMatching = False
beginNotMatch = 0
for i in range(len(content1)):
    file1linei = content1[i]
    file2linei = content2[i]
    if alreadyNotMatching and not file1linei == file2linei:
        continue
    elif alreadyNotMatching and file1linei == file2linei:
        if beginNotMatch+1 != i:
            print("%d,%dc%d,%d" % (beginNotMatch+1, i, beginNotMatch+1, i))
        else:
            print("%dc%d" % (beginNotMatch+1, i))
        print("\n".join(map(lambda x : "< " + x, content1[beginNotMatch:i])))
        print("---")
        print("\n".join(map(lambda x : "> " + x, content2[beginNotMatch:i])))
        alreadyNotMatching = False
    elif not alreadyNotMatching and not file1linei == file2linei:
        alreadyNotMatching = True
        beginNotMatch = i
    else:
        continue
total = len(content1)
if alreadyNotMatching:
    if beginNotMatch+1 != total:
        print("%d,%dc%d,%d" % (beginNotMatch+1, total, beginNotMatch+1, total))
    else:
        print("%dc%d" % (beginNotMatch+1, total))
    print("\n".join(map(lambda x : "< " + x, content1[beginNotMatch:total])))
    print("---")
    print("\n".join(map(lambda x : "> " + x, content2[beginNotMatch:total])))
