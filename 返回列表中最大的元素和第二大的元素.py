def max2(l):
    m1, m2 = (l[0], l[1]) if l[0] > l[1] else (l[1], l[0])

    for index in range(2, len(l)):
        if l[index] > m1 :
            m2 = m1
            m1 = l[index]
        elif l[index] > m2:
            m2 = l[index]
    return m1, m2

if __name__ == '__main__':
    a = [5,6,3,40,200,488,68379,58747,2954,67483]
    print(max2(a))