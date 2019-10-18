from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=32)
    completed = models.BooleanField(default=False)
    todo_id = models.IntegerField(default=-1)

    def __str__(self):
        return self.title


# Create your models here.
