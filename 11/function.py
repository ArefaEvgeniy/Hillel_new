import time


def get_data():
    def get_processor(data):
        ...

    def get_memory(data):
        ...

    def get_disk(data):
        ...

    def get_processes(data):
        ...

    data = {}
    data = get_processor(data)
    data = get_memory(data)
    data = get_disk(data)
    data = get_processes(data)

    return data


def process_data(data):
    ...


def print_data(data):
    ...


def main():
    while True:
        data = get_data()
        new_data = process_data(data)
        print_data(new_data)
        time.sleep(3)


main()
