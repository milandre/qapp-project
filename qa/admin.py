"""QAPP Admin

This file has the qa database models register
for django admin module.
"""

from django.contrib import admin

from models import *

# Register your models here.

admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Comment)
