from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class NewsCategory(models.Model):
    category_name = models.CharField(max_length=255)
    category_summary = models.CharField(max_length=255)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "News Categories"

    def __str__(self):
        return self.category_name

class Article(models.Model):
    news_category = models.ForeignKey(NewsCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    article_title = models.CharField(max_length=255)
    published = models.DateTimeField('date published')
    summary = models.TextField(default="Short Abstract")
    author = models.CharField(max_length=127)
    text = models.TextField()

    def __str__(self):
        return self.article_title

class Blog(models.Model):
    category = models.ForeignKey(NewsCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    author = models.CharField(max_length=127, default="author")
    published = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)
    abstract = models.TextField(default='Abstract')
    content = models.TextField()

    def __str__(self):
        return self.title

class Project(models.Model):
    owner = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)
    category = models.ForeignKey(NewsCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    title = models.CharField(max_length=255)
    published = models.DateField(auto_now_add=True)
    abstract = models.TextField()
    description = models.TextField()
    target_funds = models.BigIntegerField()
    current_funds = models.BigIntegerField(default=0)
    attachment = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True)    

    def __str__(self):
        return f"{self.title}"

class Message(models.Model):
    SUBJECTS = (
        ('more', 'More information'),
        ('collaboration', 'Collaboration offer'),
        ('join', 'Join Project'),
        ('invest', 'Make investment'),
        ('advertise', 'Advertisement'),
        ('other', 'Other business offer'),
    )
    project_reference = models.ForeignKey(Project, default=1, verbose_name="Project", on_delete=models.SET_DEFAULT)
    sender = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)
    sent = models.DateTimeField('date sent', default=datetime.now())
    subject = models.CharField(max_length=64, choices=SUBJECTS)
    message_text = models.TextField()
    read = models.BooleanField(default=False)

class Fund(models.Model):
    project_reference = models.ForeignKey(Project, default=1, verbose_name="Project", on_delete=models.SET_DEFAULT)
    donated = models.DateTimeField('date sent', default=datetime.now())
    contributor = models.ForeignKey(User, default=1, on_delete=models.SET_DEFAULT)
    amount = models.BigIntegerField()

    def __str__(self):
        return f"${self.amount} from {self.contributor} for {self.project_reference}"