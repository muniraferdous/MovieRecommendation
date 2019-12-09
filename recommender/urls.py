from django.urls import path
from recommender import views as v

urlpatterns = [
    path('', v.home_view, name="home"),
    path('result/', v.result_view, name="result"),

]
