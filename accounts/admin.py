from projects.models import Category, Project, Task
from django.contrib import admin
from django.db.models import Count
from . import models
admin.site.register(Category)


@admin.register(Project) # type: ignore
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'user', 'category', 'created_at', 'tasks_count']
    list_per_page = 20
    list_editable = ['status']
    list_select_related =  ['category', 'user']
    
    def tasks_count(self, obj):
        #return obj.task_set.count()
        return obj.tasks_count
    
    def get_queryset(self, request):
        query = super().get_queryset(request)
        query = query.annotate(tasks_count=Count('task'))
        return query 

@admin.register(Task) 
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'project', 'is_completed']
    list_editable = ['is_completed']
    list_per_page = 20
