from django.contrib import admin

from .models import Relationship
from .models import Tweet

# Register your models here.

admin.site.register(Relationship)
admin.site.register(Tweet)