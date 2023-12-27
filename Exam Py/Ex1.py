# ListA = (12,15,19,16,33,64,87,67,65)
# ListB = (43,32,45,21,12,32,12,34,34)
ListA = [12, 15, 19, 16, 33, 64, 87, 67, 65]
ListB = [43, 32, 45, 21, 12, 32, 12, 34, 34]

# for i in range (10):
for i in range(len(ListA)):
    print(ListA[i])

ListC = ListA
del ListA[2]
print(ListC)
# print(ListC.len())
print(len(ListC))

ListA.sort()
ListB.sort()

# if( ListA = ListB):
if (ListA == ListB):
    print('The Two Lists Are The Same !')

# else
else:
    print('The Two Lists Are Not The Same !')

ListA[1] = ListA[1] + 3
# ListA[6] =+ 3
ListA[6] += 3
# ListA[8] += 2
ListA[7] += 2

j = 0
ListD = []

while (j < 8):
    # ListD = []
    ListD.append(j)
    j = j + 1

# for k in range (8):
for k in range(len(ListD)):
    print(k)
    print(ListD[k])
