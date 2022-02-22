def gen1():
    yield "oh"
    yield "hello"
    yield "there"

for i in gen1():
    print(i)