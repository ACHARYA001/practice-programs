def inquireAge(age):
    if (age[0] <= age[2] and age[2] < age[1]):
        return "YES"
    else:
        return "NO"

if (__name__=="__main__"):
    T = int(input())
    hashmap = {}
    for i in range(0, T):
        hashmap[i] = list(map(int, input().split()))
    
    for j in range(0, T):
        print(hashmap[j])
        print(inquireAge(hashmap[j]))

