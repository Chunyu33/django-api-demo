def ak(f):
    def wrapper(*args, **kwargs):
        print('获取位置参数内容', *args)
        print('获取位置参数元祖', args)
        print('获取关键字参数的key', *kwargs)
        print('获取关键字参数的dict', kwargs)
        return f(*args, **kwargs)

    return wrapper


@ak
def fun1(a=0, b=0, c=8):
    print("===全是关键字参数")


@ak
def fun2(a, b, c):
    print("===全是位置参数")


@ak
def fun3(data):
    print("===data===")


if __name__ == '__main__':
    # fun1(a=3, b=4)
    # fun2(1, 2, 3)
    fun3({"header": 'application/json'})
