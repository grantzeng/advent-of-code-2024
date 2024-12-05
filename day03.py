import re

def evaluate(str, pattern=r"mul\((\d+),(\d+)\)"): 
    # This solution only works if there's no nesting of muls... which there doesn't seem to be
    ops = re.findall(pattern, str)
    print(ops)
    return sum(int(x) * int(y) for x, y in ops)


if __name__ == '__main__':
    src = './input03a.txt'
    corrupted_data = "".join(line.strip() for line in open(src, 'r').readlines()) 


    print(evaluate(corrupted_data))

    # ".*?" supposedly results in a non-greedy match
    # - but this doesn't quite work because of the default of being turned on at start
    conditional_pattern = r"do\(\).*?mul\((\d+),(\d+)\)"
    
    print(evaluate(corrupted_data, pattern=conditional_pattern))
    
