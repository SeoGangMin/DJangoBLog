from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
        author = models.ForeignKey('auth.User')
        title = models.CharField(max_length=200)
        text = models.TextField()
        created_date = models.DateTimeField(
                default=timezone.now)
        published_date = models.DateTimeField(
                blank=True, null=True)

        def as_json(self):
            return dict(
                author=self.author
                ,title=self.title
                ,text=self.text
                ,created_date=self.created_date
                ,published_date=self.published_date
                )
        # def publish(self):
        #     self.published_date = timezone.now()
        #     self.save()
        #
        # def __str__(self):
        #     return self.title
