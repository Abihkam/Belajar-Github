# def fizzbuzz (num) :
#     for x in range (1,num+1):
#         if(x % 15 == 0):
#             print('FizzBuzz')
#         elif (x % 3 == 0):
#             print('Fizz')
#         elif (x % 5 == 0):
#             print('Buzz')
#         else:
#             print(x)
# fizzbuzz(20)

# def fibonacci(urutkan):
#     listData = [1,1]
#     for x in range (2,urutkan):
#         listData.append(listData[x-2] + listData[x-1])
#     return listData[-1]

# print(fibonacci(8))

# a = [1,2,3,4,5,6,7,8,9]
# a.reverse()
# print(a)

# import math 

# def reverseList(theList):
#     for i in range(math.floor(len(theList)/2)):
#         tempList = theList[i]
#         theList[i] = theList[len(theList) - 1 - i]
#         theList[len(theList) - 1 - i] = tempList
#     return theList

# listNya = [1,2,3,4,5,6,7,8,9]
# print(reverseList(listNya))

# import statistics
# x = [1,2,3,2,5,2,7,2]
# print(statistics.mean(x))
# print(statistics.median(x))
# print(statistics.mode(x))

# Mean
def mean(theList):
    return sum(theList)/ len(theList)

x = mean([1,2,3,2,5,2,7,2])
print (x)

# Median
import math
x = [ 1,2,3,2,5,2,7,2 ]
def getMedian(list) :
    list.sort();
    median = 0;
    if (len(list) % 2 != 0) :
        median = list[math.floor(len(list) / 2)]; 
    else :
       mid1 = list[(int(len(list) / 2)) - 1];
       mid2 = list[int(len(list) / 2)];
       median = (mid1 + mid2) / 2;
    return median; 
print(getMedian(x));

# Modes

x = [ 1,2,3,2,5,2,7,2 ]
def getMode(list) :
    countList = [];
    # create countList
    for num in list :
        check = False;
        for list1 in countList :
            if(list1[0] == num) :
                list1[1] += 1;
                check = True;
                break
        if(check == False) :
            countList.append([num, 0]);
    # create list of mode/s
    maxFrequency = 0;
    modes = [];
    for list1 in countList :
        if (list1[1] > maxFrequency) :
            modes = [list1[0]];
            maxFrequency = list1[1];
        elif (list1[1] == maxFrequency) :
            modes.append(list1[0]);
    # if every value appears same amount of times
    if (len(modes) == len(countList)) :
        modes = [];
    return modes;
print(getMode(x));

