def remove_duplicates(arr):
    tempArr = []
    for i in arr:
        if i not in tempArr:
            tempArr.append(i)
    return tempArr
print(remove_duplicates([1, 1, 2, 2, 3, 3, 3]))