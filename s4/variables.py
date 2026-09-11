# def = variables locales à "add" ou "sub", dans cette disposition


def add():
    x1=10
    y1=20
    return x1 + y1 + c

def sub():
    x2=10
    y2=20
    return x2-y2-c

if __name__ == "__main__":
    c =100
    print(add())
    print(sub())

# if __name__ = variables globales