from django.urls import path
from demo import settings
from . import views
app_name='books'

urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('books-details/<int:slug>/',views.bookdetails,name="bookdetails"),
    path('add-items/',views.additem,name="add_item"),
    path('delete-items/<int:slug>/',views.deleteitem,name="delete_item"),
    path('update-items/<int:item_id>/',views.updateitem,name="update_item"),
]

from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
