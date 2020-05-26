import json

def sample_operation():
    return {"result":"sampleout"}


def json_read(db_path):
    with open(db_path, encoding='utf-8') as f:
        original_data = json.load(f)

    with open(db_path, 'w') as f:
        json.dump(original_data, f)


def sum_of_nums(num1, num2):
    return num1+num2


def fib(num1):
    return num1