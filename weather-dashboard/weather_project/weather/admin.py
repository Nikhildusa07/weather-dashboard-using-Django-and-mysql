from django.contrib import admin
from .models import User, Weather

admin.site.register(User)
admin.site.register(Weather)