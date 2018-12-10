from django.contrib import admin
from .models import user_review,item_review,Review
admin.site.register(user_review)
admin.site.register(item_review)
admin.site.register(Review)
