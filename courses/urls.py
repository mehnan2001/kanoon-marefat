from django.urls import path

from . import views

urlpatterns = [
    path('', views.AllCoursesView.as_view(), name='all_courses'),
    path('course/<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('course/add', views.CourseAddView.as_view(), name='course_add'),
    path('course/<int:pk>/update', views.CourseUpdateView.as_view(), name='course_update'),
    path('course/<int:pk>/delete', views.CourseDeleteView.as_view(), name='course_delete'),
]