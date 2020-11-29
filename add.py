from functools import reduce
import numpy as np

def mean(mylist):
    score = reduce(lambda x,y: x + y, mylist)/ len(mylist)
    return score

def median(mylist):
    newlist = (sorted(mylist))
    list_len = len(mylist) % 2
    i = round(len(mylist)/2)
    x = len(mylist)//2

    if list_len == 0:
        median = (newlist[x] + newlist[x+1]) / 2  
    else:
        median = newlist[i]
    return median

def mode(mylist):
    unique = set(mylist)
    unique = list(unique)
    collector = [mylist.count(key) for key in unique]
    maxi = max(collector)
    loc = collector.index(maxi)
    return unique[loc]


def main():
    scores = input( 'Enter list of numbers: ').split(",")

    scores = [int(score) for score in scores]
    
    operation = input('Enter operation: ')
    operator = ['mean', 'median', 'mode']
    
    for x in iter(list, 0):
        if operation in operator:
            break
        print("Invalid operation: ")
        operation = input('Enter operation')
    
    index_loc = operator.index(operation)
    
    if index_loc == 0:
        return mean(scores)

    elif index_loc == 1:
        return median(scores)
        #return np.median(scores)

    elif index_loc == 2:
        #return stats.mode(scores)[0]
        return mode(scores)


if __name__ == "__main__":
    print(main())