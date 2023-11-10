from django.db import models

class Password_Restoration_Codes(models.Model):
    user_id = models.IntegerField()
    code = models.CharField(max_length=6)
    code_deadline = models.DateField()

    class Meta:
        db_table = 'password_restoration_codes'