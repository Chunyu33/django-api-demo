from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from app_user.models import User
import json

from utils.token import generate_token


@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            req = json.loads(request.body)
            username = req['username']
            password = req['password']
            code = req['code']
            key_flag = username and password and code
            if key_flag:
                user = User(username=username, password=password, status='1')
                user.save()
                return JsonResponse({"code": "200", "msg": "注册成功。"})
            else:
                return JsonResponse({"code": "400", "msg": "失败，参数错误。"})
        except Exception as err:
            return JsonResponse({"code": "500", "msg": "失败，参数错误。", "en_msg": str(err)})
    else:
        return JsonResponse({"code": "405", "msg": "请求方式不正确。"})


@csrf_exempt
def login(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        username = req['username']
        password = req['password']
        if username and password:
            try:
                user = User.objects.get(username=username)
                if user.id and user.password == password:
                    token = generate_token({
                        "uid": user.id,
                        "username": user.username
                    }, expire=1)
                    return JsonResponse({"code": "200", "msg": "登录成功", "token": token})
                else:
                    return JsonResponse({"code": "400", "msg": "用户名或密码错误"})
            except Exception as err:
                return JsonResponse({"code": "501", "msg": "用户名或密码错误", "en_msg": str(err)})
    else:
        return JsonResponse({"code": "500", "msg": "参数错误"})
