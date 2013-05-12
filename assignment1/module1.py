#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sadavoya
#
# Created:     10/05/2013
# Copyright:   (c) sadavoya 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    length = 1000
    f = open("E:\Output.txt")
    g = open("tweets_{0}.txt".format(length), 'w')
    for i in range(length):
        line = f.readline()
        g.write(line)
    g.close()
    f.close()


if __name__ == '__main__':
    main()
