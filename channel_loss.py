# -*- coding: utf-8 -*-
def weight(X):
    w = 0
    for i in X:
        if i == '1':
            w += 1
    return w

def W_Y_modk(Y, k):
    summ = 0
    for i in xrange(0, len(Y)):
        if Y[i] == '1':
            summ += i + 1
    return summ%k

def codeRepair(Y, a, counter):
    count = 0
    for i in xrange(len(Y)-1, 0, -1):
        if Y[i] == str(abs(1-int(a))):
            count += 1
        if count == counter:
            print 'исходный код:', Y[0:i]+a+Y[i:]
            break
    return Y[0:i]+a+Y[i:]


def repair(Y):
    print 'Y =', Y
    k = len(Y) + 2
    a = weight(Y)
    W_Y = W_Y_modk(Y, k)
    b = (k - W_Y)%k
    print '1) вес a =', a
    print '2) W(Y)modk =', W_Y
    print '3) b = (k-W(Y)) modk =', b
    if a < b:
        print '4) a < b => выпала 1'
        print 'нужно отсчитать n-b =', len(Y) + 1 - b, 'нуля с конца'
        codeRepair(Y, '1', counter=(len(Y) + 1 - b))
    elif a>= b:
        print '4) a >= b => выпал 0'
        print 'нужно отсчитать b =', b, 'единиц с конца'
        codeRepair(Y, '0', b)
    else:
        print 'какой-то бред'

if __name__ == '__main__':
    repair(raw_input())
