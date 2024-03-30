import jwt
import datetime


def generate_token(data, expire=3, secret='SECRET'):
    """
    生成token
    :data 自定义用户信息
    :expire 过期时间(天)
    :secret 密钥
    :return: str
    """
    dic = {
        'exp': datetime.datetime.now() + datetime.timedelta(days=expire),  # 过期时间
        'iat': int(datetime.datetime.now().timestamp() - 120),  # 签发时间
        'iss': 'LIU_CY0309',  # 签名
        'data': data,
    }
    return jwt.encode(dic, secret, algorithm='HS256')


def auth_token(token, secret='SECRET'):
    """
    验证token
    :token token
    :secret 密钥
    :return: dict
    """
    try:
        result = jwt.decode(token, secret, iss='LIU_CY0309', algorithms=['HS256'])
        if result['iss']:
            return {"status": "success", "result": result}
    except jwt.exceptions.DecodeError as err:
        return {"status": "fail", "result": str(err)}
