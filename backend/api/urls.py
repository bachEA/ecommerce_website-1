from django.urls import path, include
from rest_framework.authtoken import views
from .views import home


urlpatterns = [

    path('', home, name = 'api.home'),
    # home is a function which is declared in the views.py file
    path('category/', include('api.category.urls')),
    path('product/', include('api.product.urls')),
    path('user/', include('api.user.urls'))
]