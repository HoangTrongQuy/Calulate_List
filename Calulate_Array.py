
def averge(lst):
    ''''
    computes the average
    '''
    return sum(lst) / len(lst)

def MeanDeviation(lst):
    '''
    computes mean deviation'''
    averge_ = averge(lst)
    meanDeviation = 0
    for i in lst:
        meanDeviation += abs(averge_ - i)
    return meanDeviation / len(lst)

def count_elenment(lst):
    '''show the occurtence of all value in list'''
    lst_occurtence = []
    for i in lst:
        lst_occurtence.append(lst.count(i))
    return lst_occurtence

def variance(lst):
    '''compute variance'''
    averge_ = averge(lst)
    variance_lst = 0
    for v in lst:
        variance_lst += ((averge_ - v)**2)
    return variance_lst / len(lst)

def standardDeviation(lst):
    '''computes the standard deviation'''
    return variance(lst)**0.5

def median(lst):
    '''computes the median'''
    lst = sorted(lst)
    mid = int(len(lst) / 2)

    if len(lst) % 2 == 0:
        return (lst[mid] + lst[mid-1]) / 2
    return lst[mid]

if __name__=='__main__':
    lst = [3, 2, 4, 3, 10, 14, 7, 6, 16, 1]
    print("Average:\t", averge(lst))
    print("Mean Deviation:\t", MeanDeviation(lst))
    print("Count:\t", count_elenment(lst))
    print("Length:\t", len(lst))
    print("Max:\t", max(lst))
    print("Min:\t", min(lst))
    print("Range:\t", max(lst)-min(lst))
    print("Sum:\t", sum(lst))
    print("Sort:\t", sorted(lst))
    print("Variance:\t", variance(lst))
    print("Standard Deviation:\t", standardDeviation(lst))
    print("Median:\t", median(lst))

