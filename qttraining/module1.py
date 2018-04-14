#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Avinash.Gorde
#
# Created:     14-04-2018
# Copyright:   (c) Avinash.Gorde 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------




def main():
    pass

if __name__ == '__main__':

##
##    with open("C:\\prediction\\t1bcpointfile.txt","r") as ins:
##        array = []
##        tempList = []
##        allList = []
##        inline = ins.readlines()
##        counter = 0
##        for line in inline:
##            counter = counter + 1
##            tempList.append(line)
##            if counter%28 == 0:
##                array.append(tempList)
##                tempList = []
##
##        print(counter)
##        for lst in array:
##            #assert len(lst) == 28
##            print(lst)

    with open("C:\\prediction\\t1bcpointfile.txt","r") as fd:
        lines = fd.readlines()
        composite_list = [lines[x:x+28] for x in range(0, len(lines),28)]
##    print(composite_list)
    for lst in composite_list:
        print(lst)
