from django.contrib import admin

from .data.user import User
from .data.task import Task
from .data.category import Category
from .data.restore_codes import Password_Restoration_Codes



admin.site.register(User)
admin.site.register(Task)
admin.site.register(Category)
admin.site.register(Password_Restoration_Codes)