from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model()


class News(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    text = models.CharField(max_length=1024, null=False, blank=False)
    author = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='author',
        db_index=True,
        null=False,
        blank=False,
    )
    created_at = models.DateTimeField(default=timezone.now)
