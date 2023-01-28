# Date: 28 Jan 2023 (leetcode)

# nums: List[int] = [2,3,5,6]

# target: int = 11
from typing import List
from datetime import datetime
from random import randint, sample
import matplotlib.pyplot as pylt

def findSum(numbers: List[int], target: int):
    """Runtime: 5600ms"""
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            if target == numbers[i] + numbers[j]:
                return list([i, j])
            else:
                continue

def findSumHashMap(numbers: List[int], target: int):
    hashmap = {}
    for i in range(len(numbers)):
        complement = target - numbers[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[numbers[i]] = i

def generate_random_array(ARR_LIMIT, numbers):
    arr_length, findSumHashMap_data, findSum_data= [], [], []
    for elem_list in range(0, ARR_LIMIT):
        for elem in range(2, ARR_LIMIT):
            numbers.append(randint(2, ARR_LIMIT))
            target = arr_summation(sample(numbers, 2))

            # data for y-axis
            start = datetime.now()
            findSumHashMap(numbers, target)
            end = datetime.now()
            result = (end - start)
            findSumHashMap_data.append(result.total_seconds() * 1000)


            start = datetime.now()
            findSum(numbers, target)
            end = datetime.now()
            result = (end - start)
            findSum_data.append(result.total_seconds() * 1000)

            # data for x-axis
            arr_length.append(len(numbers))

    return [findSum_data, findSumHashMap_data, arr_length]

def arr_summation(arr: List[int]) -> int:
    result = 0
    for e in arr:
        result = result + e
    return result



if __name__=="__main__":
    LIMIT = 10
    nums = [randint(0, LIMIT)]
    output = generate_random_array(LIMIT, nums)
    print(output)
    pylt.plot(output[2], output[1], label="Hashmap Technique")
    pylt.plot(output[2], output[0], label="iteration Technique")
    pylt.xlabel('array length')
    pylt.ylabel('execution time')
    pylt.legend()
    pylt.show()
