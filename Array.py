import array as arr

arrayNum = arr.array('i', [1,3,4,5,3,3,4,3,3,3])
print("Original array: ",arrayNum)


print(arrayNum.count(3))

arrayNum.reverse()
print(arrayNum)