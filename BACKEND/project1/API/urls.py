from django.urls import path
from project import views
#import rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns =[
    path('chairpersons/', views.get_and_post),
]