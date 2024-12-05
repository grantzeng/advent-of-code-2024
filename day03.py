import re


def evaluate(str): 
    # This solution only works if there's no nesting of muls... which there doesn't seem to be
    pattern = r"mul\((\d+),(\d+)\)"

    ops = re.findall(pattern, str)
    print(ops)
    
    return sum(int(x) * int(y) for x, y, in ops)

if __name__ == '__main__':
    src = './input03.txt'
    corrupted_data = "".join(line.strip() for line in open(src, 'r').readlines()) 
    print(evaluate(corrupted_data))

    
