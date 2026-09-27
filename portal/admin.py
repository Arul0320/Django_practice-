from django.contrib import admin
from .models import Student, ContactMessage
# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ("name", "email", "age", "course", "created_at")
#     search_fields = ("name", "email")
#     list_filter = ("course",)
# @admin.register(ContactMessage)
# class ContactMessageAdmin(admin.ModelAdmin):
#     list_display = ("name", "email", "subject", "created_at")
#     search_fields = ("name", "email", "subject")
admin.site.register(Student)
admin.site.register(ContactMessage)