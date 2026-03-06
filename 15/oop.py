import time


class AbstractClass:
    def get_data(self):
        ...

    def process_data(self):
        ...

    def print_data(self):
        ...


class Processor(AbstractClass):
    def get_data(self):
        ...

    def process_data(self):
        ...


class Memory(AbstractClass):
    def get_data(self):
        ...

    def print_data(self):
        ...


class Processes(AbstractClass):
    def get_data(self):
        ...

    def process_data(self):
        ...

    def print_data(self):
        ...


class Disk(AbstractClass):
    def get_data(self):
        ...

    def process_data(self):
        ...

    def print_data(self):
        ...


class Main:
    @staticmethod
    def run():
        processor = Processor()
        memory = Memory()
        processes = Processes()
        disk = Disk()

        data = [processor, memory, processes, disk]

        while True:
            for item in data:
                item.get_data()
                item.process_data()
                item.print_data()
            time.sleep(3)


Main.run()
