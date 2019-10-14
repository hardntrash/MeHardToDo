from django.contrib import admin

from .models import Task, ToDoList, Importance, Category


# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    pass


@admin.register(Importance)
class ImportanceAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
