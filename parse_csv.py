import json


# it's func parsing .csv
def parse_csv():
    # open file "BelFactory.csv" and read line by line
    with open("BelFactory.csv", "r") as f:
        keys = f.readline().strip().split(",")  # strip() delet \n in the end str
        res = [
            dict(zip(keys, line.strip().split(","))) for line in f
        ]  # split() separation string sep=","
    return res


# it's func to print result
def show(parse=None):
    print(f"{parse}")


# it's func to save result as file .json
def save_json(save=None):
    with open("BelFactory.json", "w") as file:
        json.dump(save, file, indent=4)


def main():
    parse_csv_ = parse_csv()
    show(parse=parse_csv_)
    save_json(save=parse_csv_)


if __name__ == "__main__":
    main()
