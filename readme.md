### 安装依赖
```shell
pip install -r requirements.txt -i https://pypi.douban.com/simple
```

### django脚本创建项目(这一步可以省略，因为代码都已经准备好了)
```shell
django-admin startproject xxx 
```

### 创建应用
```shell
django-admin startapp xxx
```


### 创建表结构
```shell
python manage.py migrate 
```

### 表结构变化更新(执行完这个要再次执行上一步)
```shell
python manage.py makemigrations app_name

```

### 创建超级用户
```shell
python manage.py createsuperuser
```
