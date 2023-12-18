from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="Movie Description")

    def __str__(self):
        return self.title


# in postman how to di register User
# get toekn and refresh toekn?