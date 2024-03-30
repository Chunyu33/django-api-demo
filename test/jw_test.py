if __name__ == '__main__':
    import jwt
    import datetime
    # print(int(datetime.datetime.now().timestamp() - 120))
    # print(datetime.datetime.now().timestamp())

    dic = {
        'exp': datetime.datetime.now() + datetime.timedelta(days=1),  # 过期时间
        'iat': int(datetime.datetime.now().timestamp() - 120),  # 签发时间
        'iss': 'liucy',  # 签名
        'data': {  # 内容，一般存放该用户id和开始时间
            'a': 1,
            'b': 2,
        },
    }
    str1 = """
        eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzY2NTE2MDUsImlhdCI6MTY3NjUzNjI4NSwiaXNzIjoibGl1Y3kiLCJkYXRhIjp7ImEiOjEsImIiOjJ9fQ.sZjzSs6rIcXgtn9XNjGxMzkIvBnyfc0iLJShEor5wzS
    """
    s = jwt.encode(dic, 'secret', algorithm='HS256')  # 加密生成字符串
    print('加密:', s)
    s2 = jwt.decode(s, 'secret', iss='liucy', algorithms=['HS256'])  # 解密，校验签名
    print('解密:', s2, s2['iss'])
    print(type(s2))
