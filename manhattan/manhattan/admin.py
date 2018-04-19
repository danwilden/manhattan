from django.contrib import admin

from .models import Business
from .models import Books
from .models import item_types

admin.site.register(Business)
admin.site.register(Books)
admin.site.register(item_types)
