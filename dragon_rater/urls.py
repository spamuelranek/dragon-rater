from django.urls import path
from .views import DragonAPIListView, DragonAPIDetailView

urlpatterns = [
  path("",DragonAPIListView.as_view(), name = 'dragon_list'),
  path("<int:pk>/", DragonAPIDetailView.as_view(), name = 'dragon_detail')
]