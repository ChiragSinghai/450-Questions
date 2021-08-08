from collections import Counter
def leastInterval(tasks, n) :
    taskscount=Counter(tasks)
    maxFreq = max(taskscount.values())
    maxFreq_occurence = list(taskscount.values()).count(maxFreq)
    answer = (maxFreq-1)*(n+1) + maxFreq_occurence
    return max(len(tasks),answer)

A=["A","A","A","B","B","B"]
n=2
print(leastInterval(A,n))
