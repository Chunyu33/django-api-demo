from django.http import JsonResponse

from utils.token import auth_token


# 认证动作
def _auth(request):
    """
    :request 请求体信息
    header key必须增加前缀HTTP，同时大写，中划先会转成下划线，
    例如你的key为X-Token，那么应该写成request.META.get(“HTTP_X_TOKEN”)
    """
    token = request.META.get("HTTP_X_TOKEN", b'')
    if token:
        res = auth_token(token)
        if res['status'] == 'success':
            return True
    else:
        return False


def token_auth(func):
    """
    token验证 装饰器
    :func 被验证的函数
    """
    def wrapper(*args, **kwargs):
        # 验证成功
        if _auth(*args):
            return func(*args, **kwargs)
        else:
            # 验证失败
            return JsonResponse({"status": "401", "msg": "验证失败"})
    return wrapper
