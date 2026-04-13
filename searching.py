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


def main():

    return read_data("sequential.json", "unordered_numbers")

sequential_data = main()
print(sequential_data)

if __name__ == "__main__":
    main()