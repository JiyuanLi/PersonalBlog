from django.urls import path
from . import views


app_name = "PhotoGallery"
urlpatterns = [
    path("", views.IndexView.as_view(), name="PhotoGalleryIndex"),
    path("<int:pk>/", views.DetailView.as_view(), name="PhotoGalleryDetail"),
    path("<int:image_id>/vote/", views.vote, name="PhotoGalleryVote")
]
