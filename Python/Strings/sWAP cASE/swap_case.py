def swap_case(s):
    result = []
    result = [ch.lower() if ch.isupper() else ch.upper() for ch in s]
    return ''.join(result)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)