# if __name__ == '__main__':
#     n = int(input())
#     def st(n,result):
#         for i in range(n):
#             i+=1
#             i=str(i)
#             result.append(i)
#     store = []
#     st(n,store)
# print("".join(store))
#
if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1):
        print(i, sep='', end='')