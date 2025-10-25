if __name__ == '__main__':
    list1 = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list1.append([name,score])
    scores = sorted(set([x[1] for x in  list1]))
    second_lowest = scores[1]
    names = [x[0] for x in list1 if x[1] == second_lowest]
    names.sort()
    for n in names:
        print(n)