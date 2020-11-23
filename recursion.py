"""

"""

#  对不确定长度的列表求和
def list_sum(lis):
    sum = 0
    for i in lis:
        sum += i
    return sum
# print(list_sum([1,2,4,5,6]))

#  不用循环解决对不确定长度的列表求和问题
def recursion_sum(lis):
    if not lis:
        sum = 0
    else:
        sum = lis[0] + recursion_sum(lis[1:])

    return sum

# print(recursion_sum([1,2,4,5,6]))

#  十进制转换问题
def recursion(data):
    if data < 10:
        return [data]

    else:
        yushu = data // 10
        remainer = data % 10
        return recursion(yushu) + [remainer]
print(recursion(768))

#  任意进制转换问题
def recursion_any(data, base):
    convert_string = '0123456789ABCDEF'
    if data < base:
        return [convert_string[data]]
    else:
        yushu = data // base
        remainer = data % base
        return recursion_any(yushu, base) + [convert_string[remainer]]

print(recursion_any(1453, 16))

