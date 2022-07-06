from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ReviewList, ReviewDetail

urlpatterns = [
    path('api/review/', ReviewList.as_view()),
    path('api/review/<int:pk>', ReviewDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)