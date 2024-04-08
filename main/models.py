from django.db import models
from django.contrib.auth.models import User
from django.db.models import JSONField

class Hobby(models.Model):
    name = models.CharField('name of hobby', max_length=200)

    def __str__(self):
        return self.name

class Stories(models.Model):
    title = models.CharField('title of stories', max_length=200)
    content = models.TextField('text of stories')
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hobby = models.ForeignKey(Hobby, on_delete=models.CASCADE)
    likes = models.IntegerField('likes of stories')
    photo = models.ImageField(upload_to='images_stories/', default=None)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    content = models.CharField('text of comments', max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stories = models.ForeignKey(Stories, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='avatars/', default=None)
    hobby = models.ForeignKey(Hobby, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.user.username
    
class Statistics(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=1)
    second = models.IntegerField(default=0)
    numberofhappy = models.IntegerField()
    timeofhappy = models.DateTimeField(auto_now_add=True, blank=True)
    numberofanger = models.IntegerField()
    timeofanger = models.DateTimeField(auto_now_add=True, blank=True)
    numberofcontempt = models.IntegerField()
    timeofcontempt = models.DateTimeField(auto_now_add=True, blank=True)
    numberofdisgust = models.IntegerField()
    timeofdisgust = models.DateTimeField(auto_now_add=True, blank=True)
    numberoffear = models.IntegerField()
    timeofear = models.DateTimeField(auto_now_add=True, blank=True)
    numberofneutral = models.IntegerField()
    timeofneutral = models.DateTimeField(auto_now_add=True, blank=True)
    numberofsad = models.IntegerField()
    timeofsad = models.DateTimeField(auto_now_add=True, blank=True)
    numberofsurprise = models.IntegerField()
    timeofsurprise = models.DateTimeField(auto_now_add=True, blank=True)
