from math import floor
from pathlib import Path
import json
import time
from pkg_resources import non_empty_lines
from generators import unordered_sequence
from generators import ordered_sequence

length = [10,100,1000]
unordered_sequences = [unordered_sequence(length[0]),unordered_sequence(length[1]),unordered_sequence(length[2])]
ordered_sequences = [ordered_sequence(length[0]),ordered_sequence(length[1]),ordered_sequence(length[2])]


def read_data(file_name, field):
    with open(file_name, "r") as file_obj:
        data = json.load(file_obj)
    if field not in data:
        return None
    return data[field]
    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name
def linear_search(searched_seq, num):
    empty = {}
    indexes = []
    count = 0
    for i,j in enumerate(searched_seq):
        if j == num:
            indexes.append(i)
            count += 1
    empty["Indexy:"] = indexes
    empty["Pocet:"] = count
    return empty
def binary_search(numbers, number):
    start = 0
    end = len(numbers)-1

    while start <= end:
        stred = (start + end) / 2
        if numbers[round(stred)] == number:
            return round(stred), number
        elif numbers[round(stred)] < number:
            start = stred +1
        elif numbers[round(stred)] > number:
            end = stred - 1
    return None


def main():
    ordered_sequences_times = []
    unordered_sequences_times = []
    result1 = []
    result2 = []
    for i in unordered_sequences:
        start = time.perf_counter()
        l = linear_search(i,5)
        result1.append(l)
        end = time.perf_counter()

        duration = end - start
        unordered_sequences_times.append(duration)
    for i in ordered_sequences:
        print(i)
        start = time.perf_counter()
        l = binary_search(i, 5)
        result2.append(l)
        end = time.perf_counter()

        duration = end - start
        ordered_sequences_times.append(duration)
    return unordered_sequences_times, ordered_sequences_times , result1, result2

sequential_data = main()
print(sequential_data)

# if __name__ == "__main__":
