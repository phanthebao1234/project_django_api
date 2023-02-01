from django.contrib import admin
from .models import Todos
# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "body",
    )
    
admin.site.register(Todos, TodoAdmin)