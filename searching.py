from pathlib import Path
import json

from pkg_resources import non_empty_lines


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


def main():

    return linear_search(read_data("sequential.json", "unordered_numbers"), 0)

sequential_data = main()
print(sequential_data)

if __name__ == "__main__":
    main()