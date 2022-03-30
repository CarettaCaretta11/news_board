from huey import crontab
from huey.contrib.djhuey import db_periodic_task
from base.models import Post


@db_periodic_task(crontab(minute="0", hour="11", day="*", month="*", day_of_week="*"))
def update_upvotes():
    for obj in Post.objects.all():
        obj.upvotes = 0
        obj.save()
