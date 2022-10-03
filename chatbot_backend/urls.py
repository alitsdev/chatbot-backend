
from django.contrib import admin
from django.urls import path
from chatbot_backend import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('chatUser/', views.chatUser_list),
    path('assistance/', views.assistance_request),

]
