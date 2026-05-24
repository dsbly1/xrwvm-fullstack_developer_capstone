from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from djangoapp import views
from djangoapp.views import login_user, logout_request, registration

app_name = 'djangoapp'
urlpatterns = [
    path('register', registration, name='registration'),
    path('login', login_user, name='login'),
    path('logout/', logout_request, name='logout'),
    path('get_cars', views.get_cars, name='getcars'),
    path('get_dealers', views.get_dealerships, name='get_dealers'),
    path('get_dealers/<str:state>', views.get_dealerships, name='get_dealers_by_state'),
    path('dealer/<int:dealer_id>', views.get_dealer_details, name='dealer_details'),
    path('reviews/dealer/<int:dealer_id>', views.get_dealer_reviews, name='dealer_reviews'),
    path('add_review', views.add_review, name='add_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)