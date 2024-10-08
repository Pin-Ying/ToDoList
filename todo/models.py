from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(blank=True, null=True)
    important = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    ### 外部鍵連結使用者
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        # 排序功能
        ordering = ["completed", "-created"]
        # ordering = ["-created", "important"]

    def __str__(self):
        return f"{self.id}-{self.title}-{self.created}"
