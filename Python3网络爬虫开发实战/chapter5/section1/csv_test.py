import csv


def test1():
    with open('data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id', 'name', 'age'])
        writer.writerow(['10001', 'Mike', 20])
        writer.writerow(['10002', 'Bob', 22])
        writer.writerow(['10003', 'Jordan', 21])


def test2():
    with open('data.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=' ')
        writer.writerow(['id', 'name', 'age'])
        writer.writerow(['10001', 'Mike', 20])
        writer.writerow(['10002', 'Bob', 22])
        writer.writerow(['10003', 'Jordan', 21])


def test3():
    with open('data.csv', 'w', newline='') as f:
        fieldnames = ['id', 'name', 'age']
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='-')
        writer.writeheader()
        writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
        writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
        writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})


def test4():
    with open('data.csv', 'a', newline='') as f:
        fieldnames = ['id', 'name', 'age']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({'id': '10004', 'name': 'Durant', 'age': 22})


def test5():
    with open('data.csv', 'a', encoding='utf-8') as f:
        fieldnames = ['id', 'name', 'age']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({'id': '10005', 'name': '王伟', 'age': 22})


def test6():
    with open('data.csv', 'r', encoding='utf8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


def test7():
    with open('data.csv', 'r', encoding='utf-8') as f:
        fieldnames = ['id', 'name', 'age']
        reader = csv.DictReader(f, fieldnames=fieldnames)
        for row in reader:
            print(row)


if __name__ == '__main__':
    test7()
