import numpy as np 

def red_nosed_standard(v): 
    diff = np.diff(v)

    monotonic = np.all(diff < 0) or np.all(diff > 0)
    bounded  = np.all(np.abs(diff) >= 1) and np.all(np.abs(diff) <= 3)

    return monotonic and bounded

def leave_out_one_standard(v): 
    return any(
            list(
                map(
                    red_nosed_standard, 
                    [
                        np.delete(v, i) for i in range(len(v))
                    ]
                )
            )
        )

def count_safe_strict(lines):
    return sum(1 for row in lines if red_nosed_standard(row))

def count_safe_one_fault_allowed(lines): 
    return sum(1 for row in lines if red_nosed_standard(row) or leave_out_one_standard(row))
     
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

    print(count_safe_strict(lines))
    print(count_safe_one_fault_allowed(lines))