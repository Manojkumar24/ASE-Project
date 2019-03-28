from django.urls import path
from Homepage import views
from django.views.generic import TemplateView

app_name = "Homepage"
urlpatterns = [
    path("<str:category>/", views.default, name="home"),
    path("searchdb", views.search, name='search'),
    path("itemdetail/<int:pk>/<str:username>", views.itemdetailview, name='specificitem'),
    path('review/<int:pk>/<str:username>', views.reviewtext, name='item_review'),
]
