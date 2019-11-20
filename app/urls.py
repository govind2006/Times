from django.urls import path
from . import views

urlpatterns = [
path('',views.index,name='index'),
path('state',views.bstate,name='state'),
path('national',views.bnational,name='national'),
path('buisness',views.buisness,name='buisness'),
path('opinion',views.opinion,name='opinion'),
path('sport',views.sport,name='sport'),
path('international',views.international,name='international'),
path('sunday_magazine',views.sunday_magazine,name='sunday_magazine'),
path('Gallery',views.gallery,name="Gallery"),
path('sitemap/',views.sitemap,name="sitemap"),
]