import numpy as np 

def red_nosed_standard(v): 
    diff = np.diff(v)
    abs = np.abs(diff)

    monotonic = np.all(diff < 0) or np.all(diff > 0)
    bounded  = np.all(abs >= 1) and np.all(abs <= 3)

    return monotonic and bounded

def leave_out_one_standard(v): 
    return any(
        red_nosed_standard(
            np.concatenate((v[:i], v[i + 1, :]))
            for i in range(v)
        )
    )

def count_safe(lines, predicate): 
    return sum(1 for _ in filter(predicate, lines))

if __name__ == '__main__': 
    src = './input02.txt' 
    
    lines =  [
        np.array([int(_) for _ in line.split()]) 
        for line 
        in open(src, 'r').readlines()
    ]

    print(count_safe(lines, red_nosed_standard))

    relaxed_standard = lambda v : red_nosed_standard(v) or leave_out_one_standard(v)
    print(count_safe(lines, relaxed_standard))