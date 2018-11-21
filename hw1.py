job = [[0, 0, 0], [10, 50, 10], [10, 38, 5], [13, 49, 1], [4, 12, 5],
       [9, 20, 10], [4, 105, 1], [8, 73, 5], [15, 45, 10], [7, 6, 5],
       [1, 64, 1], [9, 15, 5], [3, 6, 10], [15, 92, 10], [9, 43, 5],
       [11, 78, 1], [6, 21, 10], [5, 15, 5], [14, 50, 5], [18, 150, 1],
       [3, 99, 5]
       ]
# job  [Processing Time, Due Time, Weights]
choose = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
tabulist= []
#tabulist_len = input('input tabulist len')

def count_t(inputarray):
    processtime = 0
    t = 0
    for i in range(0, 20):
        processtime += job[inputarray[i]][0]
        t += job[inputarray[i]][2]*max(processtime - job[inputarray[i]][1], 0)
    return t

def Tabu():
    historyBestchoose = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    histroyBestnum = count_t(historyBestchoose)
    localBestChoose = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    for n in range(0, 100):
        localbest = 999999
        swapNum = []
        for i in range(0, 19):
            tempChoose = localBestChoose[:]
            tempChoose[i], tempChoose[i+1] = tempChoose[i+1], tempChoose[i]
            localcount = count_t(tempChoose)
            if localbest > localcount and tabulist.count([tempChoose[i], tempChoose[i+1]]) == 0 and tabulist.count([tempChoose[i+1], tempChoose[i]]) == 0:
                localbest = localcount
                swapNum = [i, i+1]
        localBestChoose[swapNum[0]], localBestChoose[swapNum[1]] = localBestChoose[swapNum[1]], localBestChoose[swapNum[0]]
        tabulist.insert(0, swapNum)
        if len(tabulist) > 5:
            tabulist.pop()
        if histroyBestnum > localbest:
            histroyBestnum = localbest
            historyBestchoose = localBestChoose[:]
        print( "time = ", n, " best: ", histroyBestnum, "\nbestchoose: ", historyBestchoose)
    print('\nTabu list size is:', 5)
    print("Min total weighted tardiness is:", histroyBestnum)
    print('Best choose is:', historyBestchoose)
    return 0




Tabu()
#print(count_t([12, 4, 5, 1, 2, 8, 16, 9, 7, 10, 17, 3, 6, 20, 13, 11, 14, 18, 15, 19]))
# print(count_t())