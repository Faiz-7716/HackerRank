if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    sorted = list(set(arr))
    print(sorted[1])


