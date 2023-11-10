from django.db import models


class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    comment = models.TextField()
    deadline = models.DateField()
    status = models.BooleanField()
    hide = models.BooleanField()

    class Meta:
        db_table = 'task'