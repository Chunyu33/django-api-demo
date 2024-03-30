from django.db import models


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    # deleted alive
    status = models.CharField(max_length=10)

