from collections import Counter 
import numpy as np 

def l1_norm(v):
    return np.linalg.norm(v, 1)

def similarity(v0, v1): 
    freq_table = Counter(v1)
    return sum(x * freq_table.get(x, 0) for x in v0) 

if __name__ == '__main__':

    src = './input01.txt'

    v0, v1 = [], [] 
    with open(src, 'r') as f: 
        for line in f.readlines():
            x0, x1 = line.split()
            v0.append(int(x0)); v1.append(int(x1))
    
    sorted_vector = lambda v: np.sort(np.array(v))

    v0, v1 = sorted_vector(v0), sorted_vector(v1) 

    print(l1_norm(v0 - v1))
    print(similarity(v0, v1))