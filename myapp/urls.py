from django.urls import path
from .views import CourierDetail,CourierDetail_pages #,CourierDetail_page

urlpatterns = [
    path('GetAllCourierRegister/', CourierDetail.as_view(), name='courier-detail'),
    path('CourierDividePages/<int:no>/', CourierDetail_pages.as_view(), name='CourierDetail_pages'),
    #path('CourierDetail_page/<int:no>/PageOfNo/<int:no_of_page>/', CourierDetail_page.as_view(), name='CourierDetail_page'),
]
