from django.contrib import admin
from user import models
from diary.models import UserProfile, Diary, DiaryImage

# DiaryImage 클래스를 inline으로 나타낸다.
class DiaryImageInline(admin.TabularInline):
    model = DiaryImage

# Diary 클래스는 해당하는 DiaryImage 객체를 리스트로 관리한다.
class DiaryAdmin(admin.ModelAdmin):
    inlines = [DiaryImageInline, ]

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Diary, DiaryAdmin)
