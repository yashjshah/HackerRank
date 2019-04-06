def count_substring(string, sub_string):
    count = 0
    i = 0
    while True:
        if string.find(sub_string,i) == -1:
            return count
        else:
            count += 1
            i = string.find(sub_string,i) + 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)