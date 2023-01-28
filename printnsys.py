def print_formatted(number):
    binVal =  bin(number).replace("0b", "")
    for i in range(1, number+1):
        print(str(i).rjust(len(binVal)), oct(i).replace("0o", "").rjust(len(binVal)), hex(i).upper().replace("0X", "").rjust(len(binVal)), bin(i).replace("0b", "").rjust(len(binVal)))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)