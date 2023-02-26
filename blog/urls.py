from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="blog-index"),
    path("about/", views.about, name="blog-about"),
    path("articles/", views.articles, name="blog-articles"),
    path("register/", views.register, name="blog-register"),
    path("login/", views.login_user, name="blog-login"),
    path("article-form/", views.article_form, name="blog-article-form"),
    path("authenticated/", views.authenticated, name="blog-authenticated"),
    path('articles/delete/<int:pk>/', views.delete_article, name='blog-article-delete'),
    path("logout/", views.logout_user, name="blog-logout"),
    path("article-form/<int:id>/", views.article_form, name="blog-article-edit"),
    path("profile/", views.user_profile, name="blog-profile"),
    path("profile/edit", views.edit_profile, name="blog-profile-edit"),
]
