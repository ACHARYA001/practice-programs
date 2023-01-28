if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    scores = list(arr)
    scores = [i for i in scores if i != max(scores)]
    print(max(scores))