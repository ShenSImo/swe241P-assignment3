#Task1
#takes in 
#func1 Mergesort
def sortString(s, algorithm="merge"):
    #str is immutable, list is 
    word = []
    for i in s:
        word.append(i.lower())
    new_word = ""
    if algorithm == "merge":
        for i in mergeSort(word):
            new_word += i
    else:
        for i in quickSort(word):
            new_word += i
    return new_word
    # two different ways
def mergeSort(word):
    if len(word) > 1:
        mid = len(word) // 2
        lefthalf = word[:mid]
        righthalf = word[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        #continue when recursie call reaches the end
        i = 0 #left index
        j = 0 #right index
        k = 0 #index for word

        while i < len(lefthalf) and j < len(righthalf):
            if ord(lefthalf[i]) <= ord(righthalf[j]):
                word[k] = lefthalf[i]
                i += 1
            else:
                word[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            word[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            word[k] = righthalf[j]
            j += 1
            k += 1
    return word

# def quickSort(word): #word is a character list of single str
import random
def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)
    return alist

def quickSortHelper(alist, first, last):#start sorting a list/sublist that has at least two elements
    if first < last:
        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint-1)
        quickSortHelper(alist, splitpoint+1, last)

def partition(alist, first, last):#two pointers tracking left greater than pivot, and right less than pivot
    random_index = random.randint(first, last)#use random
    alist[first], alist[random_index] = alist[random_index], alist[first] #switch the randomized num to the first
    pivotvalue = alist[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:#find the first item that is larger than pivot, right viceversa
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1
        while leftmark <= rightmark and alist[rightmark] >= pivotvalue:
            rightmark -= 1
        if leftmark > rightmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = (alist[rightmark], alist[leftmark])
    alist[first], alist[rightmark] = alist[rightmark], alist[first]
    return rightmark#decide where the rest sublist should be sorted






                
def groupAnagram(alist):
    count = {

    }
    for i in alist:
        sorted = sortString(i)
        if sorted not in count:
            count[sorted] = [i]
        else:
            count[sorted].append(i)
    result = []
    for i in count.values():
        result.append(i)
    return result





        


print(groupAnagram(["bucket","rat","mango","tango","ogtan","tar"]))

print(quickSort(list("dcba")))      # ['a', 'b', 'c', 'd']
print(quickSort(list("aaaa")))      # ['a', 'a', 'a', 'a']
print(quickSort([]))                # []

# 和 mergeSort 对比
for s in ["rat", "mango", "Happy", "zyxwvu", "aAbB", "banana"]:
    assert quickSort(list(s)) == mergeSort(list(s)), s

# 压力测试：10 万个随机小写字母（改之前会崩溃）
big = [random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(100000)]
assert quickSort(big[:]) == mergeSort(big[:])
print("全部通过 ✅")