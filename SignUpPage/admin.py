from django.contrib import admin
from .models import Index
from .models import Profile
# Register your models here.
@admin.register(Index)
class IndexAdmin(admin.ModelAdmin):
    pass
admin.site.register(Profile)