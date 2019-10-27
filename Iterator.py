import json

class MyIter():
    def __init__(self, start, end):
        self.start, self.end = start - 1, end

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        return self.start


def main():
    pass


url = 'https://ru.wikipedia.org/wiki/'
main()
