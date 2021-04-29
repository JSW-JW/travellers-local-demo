from django.db import models
from user.models import UserProfile

class Diary(models.Model):
    """
    Diary model. N:1 to UserProfile Model. It is possible to change the ForeignKey by writing on the N model.
    >>> new_article2.reporter.id
    1
    >>> r2.article_set.add(new_article2)
    >>> new_article2.reporter.id
    2
    """
    class Target(models.TextChoices):
        PUB = 'PUB', ('Public')
        SEC = 'SEC', ('Secret')
        FRI = 'FRI', ('Friends')

    target = models.CharField(
        max_length=3,
        choices=Target.choices,
        default=Target.PUB,
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class DiaryImage(models.Model):
    """DiaryImage"""
    image = models.ImageField(default='media/default_image.jpeg')
    thumbnail = models.ImageField(default='media/default_image.jpeg')
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)


# class Place(models.Model):
#     """Place model's informations which will be retrieved from GoogleMap"""