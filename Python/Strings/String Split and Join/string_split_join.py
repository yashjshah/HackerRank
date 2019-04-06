def split_and_join(line):
    linesplit = line.split(" ")
    return '-'.join(linesplit) 


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)