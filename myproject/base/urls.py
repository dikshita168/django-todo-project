from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about',views.about, name='about'),
    path('add',views.add, name='add'),

    path('details/<int:pk>', views.details , name='details'),
    path('update/<int:pk>',views.update, name='update'),

    path('delete_task/<int:pk>',views.delete_task, name='delete_task'),
    path('confirm_del/<int:pk>', views.confirm_del, name='confirm_del'),

    path('mark_as_completed/<int:pk>', views.mark_as_completed, name='mark_as_completed'),
    path('completed' , views.completed, name='completed'),
    path('restore_complete/<int:pk>' , views.restore_complete, name='restore_complete'),
    path('remove_complete/<int:pk>' , views.remove_complete, name='remove_complete'),
    path('restore_all_complete/<int:pk>' , views.restore_all_complete, name='restore_all_complete'),
    path('remove_all_completed' , views.remove_all_completed, name='remove_all_completed'),


    path('history',views.history, name='history'),
    path('restore_task/<int:pk>',views.restore_task, name='restore_task'),
    path('permenant_delete/<int:pk>',views.permenant_delete, name='permenant_delete'),
    path('restore_all',views.restore_all, name='restore_all'),
    path('delete_all',views.delete_all, name='delete_all'),
]