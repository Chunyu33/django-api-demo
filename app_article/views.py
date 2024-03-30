from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app_article.models import Article
import json

from utils.auth import token_auth


# 查询/新增
@csrf_exempt
@token_auth
def add_article(request):
    if request.method == "POST":
        req = json.loads(request.body)
        key_flag = req.get("title") and req.get("content") and len(req) == 2
        # 判断请求体是否正确
        if key_flag:
            title = req["title"]
            content = req["content"]
            # title返回的是一个list
            title_exist = Article.objects.filter(title=title)
            # 判断是否存在同名title
            if len(title_exist) != 0:
                return JsonResponse({"code": "400", "msg": "失败！该标题已经存在"})

            '''插入数据'''
            add_art = Article(title=title, content=content, status="1")
            add_art.save()
            return JsonResponse({"code": "200", "msg": "创建成功"})
        else:
            return JsonResponse({"code": "400", "msg": "请检查参数"})
    if request.method == 'GET':
        article_list = Article.objects.all()
        data = []
        for item in article_list:
            data.append({
                "id": item.id,
                "title": item.title,
                "content": item.content
            })
        return JsonResponse({"code": "200", "data": data, "msg": "查询成功"})


# 修改/删除
@csrf_exempt
@token_auth
def modify_article(request, art_id):
    if request.method == "POST":
        req = json.loads(request.body)
        try:
            key_flag = req.get("title") and req.get("content") and len(req) == 2
            if key_flag:
                title = req["title"]
                content = req["content"]
                old_art = Article.objects.get(id=art_id)
                old_art.title = title
                old_art.content = content
                old_art.save()
                return JsonResponse({"code": "200", "msg": "修改成功"})
        except Exception as err:
            return JsonResponse({"code": "500", "msg": str(err)})
    # 删除
    if request.method == "DELETE":
        try:
            art = Article.objects.get(id=art_id)
            art.delete()
            return JsonResponse({"code": "200", "msg": "删除成功"})
        except Exception as err:
            return JsonResponse({"code": "500", "msg": str(err)})
