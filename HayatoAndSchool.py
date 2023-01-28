def find_odd_sums():
    return

def get_data():
    test_cases = {}
    nums = int(input())
    for test_case in range(0, nums):
        test_cases[test_case] = list(map(int, input().split()))
    return test_cases

if (__name__=="__main__"):
    print(get_data())
