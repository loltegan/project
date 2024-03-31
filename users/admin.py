from django.contrib import admin
from users.models import Users
from products.admin import BasketAdmin


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    inlines = (BasketAdmin,)
    extra = 0

