from django.urls import path
from . import views

urlpatterns = [
    path('post', views.post_contributions ,name='post-contribution'),
    path('home', views.home ,name='home'),
    path('detail/<int:pk>', views.detail_contribution ,name='detail-contribution'),
    path('select/<int:id>', views.select_contribution ,name='select-contribution'),
    path('edit/<int:pk>', views.edit_contribution ,name='edit-contribution'),
    path('delete/<int:pk>', views.delete_contribution ,name='delete-contribution'),
    path('deselect/<int:id>', views.deselect_contribution ,name='deselect-contribution'),
    path('editcom/<int:pk>', views.edit_comment ,name='edit-comment'),
    path('comment/<int:pk>', views.write_comment ,name='write-comment'),
    path('deletecom/<int:pk>', views.delete_comment ,name='delete-comment'),
    path('selected', views.selected ,name='selected'),
    path('notselected', views.not_selected ,name='not-selected'),
    path('sendmail/<int:pk>', views.send_mail ,name='send-mail'),
    path('search', views.search ,name='search'),
]



