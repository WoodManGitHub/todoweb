from django.contrib import admin
from .models import Todo, HashTag, TodoAdmin

admin.site.register(Todo, TodoAdmin)
admin.site.register(HashTag)
