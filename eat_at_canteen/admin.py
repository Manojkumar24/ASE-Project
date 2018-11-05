from django.contrib import admin
from eat_at_canteen.models import UserProfileInfo,FoodItems,CustomerFoodItems,Tables,Post,Comment
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(FoodItems)
admin.site.register(CustomerFoodItems)
admin.site.register(Tables)
admin.site.register(Post)
admin.site.register(Comment)
