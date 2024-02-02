from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="details"),
    path("<int:pk>/update/", views.UpdateView.as_view(), name="update"),
    path("create/", views.CreateView.as_view(), name="create"),
    path("<int:pk>/confirm_delete/", views.DeleteView.as_view(), name="confirm_delete"),
]
