def findPeople(student, n):
    count = [1 for _ in range(n)];
    # 从左往右遍历
    for i in range(n):
        for j in range(i):
            #如果i位置的数比j位置的数大
            #count[j] + 1>cont[i]是防止有重复的数字重复计算
            if student[i] > student[j] and count[i] < count[j] + 1:
                #如果大于并且是第一次出现那么就加一
                count[i] = count[j] + 1;
    return count;

while True:
    try:
        n = int(input());
        student = input().split(" ");
        for i in range(n):
            student[i] = int(student[i]);
        ltoR = findPeople(student, n);
        rtoL = findPeople(student[::-1],n);
        sumStore = [];
        for i in range(n):
            #表示此人是中间位置的人时，合唱队的人数
            sumStore.append(ltoR[i] + rtoL[n - i - 1] - 1);
        print(n - max(sumStore));
    except:
        break;

#最大上升子序列问题
#从左到右遍历一遍，然后从右到左遍历一遍
#然后相加就能求出。