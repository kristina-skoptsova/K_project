from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    #path('main/register', RegisterUser.as_view(), name='register'),
    #path('main/login', LoginUser.as_view(), name="login"),
    path('', include('main.urls'))
]
