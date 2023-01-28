def print_formatted(number:int):

    def getValue(divisor:int, num:int):
        remainder = []
        while (num != 0):
            remainder.append(int(num % divisor))
            num = int(num / divisor)
        
        return int((''.join(map(str, remainder[::-1]))))
    
    for i in range(1, number+1):
        print(i, getValue(8, i), getValue(2, i))



        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)