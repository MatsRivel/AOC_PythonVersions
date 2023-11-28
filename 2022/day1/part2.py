
def line_to_num_else_none(line:str)->int:
    if line == "\n" or line == "":
        return None
    return int(line)
    
def line_yielder(file_name:str)->int:
    for line in open(file_name,'r'):
        yield line_to_num_else_none(line)
            
def main(file_name:str):
    best = [0,1,2]
    total = 0
    for line in line_yielder(file_name):
        if line is None:
            if best[0] < total:
                best.append(total)
                best.sort()
                best = best[1:]
            total = 0
        else:
            total += line
    if best[0] < total:
        best.append(total)
        best.sort()
        best = best[1:]
    return sum(best)
    
if __name__ == '__main__':
    file_name, answer = "dummy.txt",45000
    output = main(file_name)
    assert output == answer, f"Wrong dummy answer! {output} != {answer}"
    print(f"{output} was the correct answer for the dummy!")
    file_name, answer = "puzzle.txt",198041
    output = main(file_name)
    assert output == answer, f"Wrong dummy answer! {output} != {answer}"
    print(f"{output} was the correct answer for the puzzle!")
    
    
        