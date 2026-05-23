from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from djangoapp.views import login_user, logout_request, registration

app_name = 'djangoapp'
urlpatterns = [
    path('register', registration, name='registration'),
    path('login', login_user, name='login'),
    path('logout/', logout_request, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)