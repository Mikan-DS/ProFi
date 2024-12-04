from django.urls import path

from surveys import views

urlpatterns = [
    path('get/<int:survey_id>/', views.get_survey, name='get_survey'),
    path('list/', views.surveys_list, name='surveys_list'),
]
