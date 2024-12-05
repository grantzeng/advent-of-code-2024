import numpy as np 

def red_nosed_standard(v): 
    diff = np.diff(v)

    monotonic = np.all(diff < 0) or np.all(diff > 0)
    bounded  = np.all(np.abs(diff) >= 1) and np.all(np.abs(diff) <= 3)

    return monotonic and bounded

def count_safe(lines):
    return sum(1 for row in lines if red_nosed_standard(row))
     
if __name__ == '__main__': 
    src = './input02.txt' 
    
    lines =  [
        np.array(
            list(
                map(int,line.split())
            )
        )
        for line 
        in open(src, 'r').readlines()
    ]

    print(count_safe(lines))