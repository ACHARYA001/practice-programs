def checkLight(data):
    if data[1] == 0:
        if ((data[0] % 4) == 0):
            return "OFF"
        else:
            return "ON"
    else:
        if ((data[0] % 4) == 0):
            return "ON"
        else:
            return "Ambiguous"


if (__name__=="__main__"):
    T = int(input())
    torch_data = {}
    for i in range(0, T):
        torch_data[i] = list(map(int, input().split()))

    for k in range(0, T):
        print(checkLight(torch_data[k]))


