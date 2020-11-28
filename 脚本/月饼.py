
def zhaoling(bills):
    five = 0
    ten = 0
    for i in range(len(bills)):

        if bills[i] == 5:
            five += 1
        elif bills[i] == 10:
            if five >= 1:
                five -= 1
                ten += 1
            else:
                return False
        elif bills[i] == 20:
            if five >= 1 and ten >= 1:
                five -= 1
                ten -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    return True




bills = [10, 10]
print(zhaoling(bills))

#
# def dieluohan(array1, array2, array3):
#     result = []
#     for i in range(3):
#         result.append(array1[i])
#         result.append(array2[i])
#         result.append(array3[i])
#     return result