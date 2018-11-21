
job = [[0, 0, 0], [10, 50, 10], [10, 38, 5], [13, 49, 1], [4, 12, 5],
       [9, 20, 10], [4, 105, 1], [8, 73, 5], [15, 45, 10], [7, 6, 5],
       [1, 64, 1], [9, 15, 5], [3, 6, 10], [15, 92, 10], [9, 43, 5],
       [11, 78, 1], [6, 21, 10], [5, 15, 5], [14, 50, 5], [18, 150, 1],
       [3, 99, 5]
       ]
# job  [Processing Time, Due Time, Weights]
choose = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
tabulist= [[1, 4], [4, 1]]
#tabulist_len = input('input tabulist len')

def count_t(inputarray):
    processtime = 0
    t = 0
    for i in range(0, 20):
        processtime += job[inputarray[i]][0]
        t += job[inputarray[i]][2]*max(processtime - job[inputarray[i]][1], 0)
    return  t

def Tabu():
    bestchoose = choose[:]
    bestnum = count_t()
    for n in range(0, 50):
        t = 999999
        for i in range(0, 19):
            swap = choose[:]
            swap[i], swap[i+1] = swap[i+1], swap[i]
            temp = count_t(swap)
            if t > temp and tabulist.count([swap[i], swap[i+1]]) == 0 and tabulist.count([swap[i+1], swap[i]]):
                t = temp
                tabulist.append()   ////////////////////////
        if bestnum > t:
            bestnum = t






print(tabulist.count([1, 4]))
print(len(tabulist))

print(tabulist)


# print(count_t())
