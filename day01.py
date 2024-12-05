from collections import Counter 

def day01_part01(l1, l2):
    # Basically calculate L1 norm of difference (of sorted) vector 
    return sum(abs(x - y) for x, y in zip(l1, l2))


def day01_part02(l1, l2): 
    freq_table = Counter(l2)
    return sum(x * Counter(l2).get(x, 0) for x in l1) 

if __name__ == '__main__':

    src = './input01.txt'

    l1, l2 = [], [] 
    with open(src, 'r') as f: 
        for line in f.readlines():
            n, m = line.split()
            l1.append(int(n)); l2.append(int(m))
            l1 = sorted(l1); l2 = sorted(l2)

    print(day01_part01(l1, l2))
    print(day01_part02(l1, l2))