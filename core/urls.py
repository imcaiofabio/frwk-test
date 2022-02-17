#from django.contrib import admin
from django.urls import path
from app.views import UsersView

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('results', UsersView.as_view()),
]
