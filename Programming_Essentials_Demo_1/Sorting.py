Goalscorers=[["Arthur",18,29],["Braithwaite",15,45],["Andres",19,73],["Chillwell",17,79],["Mount",16,90]]
def sortlist(Goal):
    for i in range(len(Goal)-1):
        for j in range(0, len(Goal)-i-1):
            if Goal[j][1] > Goal[j + 1][1]:
                Goal[j], Goal[j + 1] = Goal[j + 1], Goal[j]
    return(Goal)            
print(sortlist(Goalscorers))




