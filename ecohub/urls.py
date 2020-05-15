from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("register", views.register, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("messages", views.messages_view, name="messages"),
    path("messages/message/<int:message_id>", views.message_view, name="message_view"),
    path("home", views.home, name="home"),
    path("news", views.news_view, name="news"),
    path("news/<int:article_id>/article", views.article_view, name="article"),
    path("news/category/<int:category_id>", views.news_category, name="news_category"),
    path("blogs", views.blogs_view, name="blogs"),
    path("blogs/<int:blog_id>/blog", views.blog_view, name="blog"),
    path("blogs/category/<int:category_id>", views.blog_category, name="blog_category"),
    path("blogs/myblogs", views.myblogs_view, name="myblogs"),
    path("blogs/blogwriting", views.blogwriting, name="blogwriting"),
    path("projects", views.projects, name="projects"),
    path("projects/category/<int:category_id>", views.project_category, name="project_category"),
    path("projects/myprojects", views.myprojects_view, name="myprojects"),
    path("projects/start_project", views.start_project, name="start_project"),
    path("projects/<int:project_id>/project", views.project_view, name="project"),
    path("projects/<int:project_id>/support_project", views.fund_project, name="support_project"),
    path("projects/<int:project_id>/contact_owner", views.contacting, name="contact_owner")
]