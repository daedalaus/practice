class MyIterable(object):
    def __init__(self):
        self.data = [2, 4, 8]
        self.step = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.step >= len(self.data):
            raise StopIteration()
        data = self.data[self.step]
        print("I'm in the idx: {0} call of next()".format(self.step))
        self.step += 1
        return data


def MyIterator():
    for i, data in enumerate([1, 3, 9]):
        print("I'm in the idx: {0} call of next()".format(i))
        yield data


if __name__ == '__main__':
    for p in MyIterable():
        print(p)

    for q in MyIterator():
        print(q)
