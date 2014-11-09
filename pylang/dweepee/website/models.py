from django.db import models


class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    ip = models.CharField(max_length=27, default="")
    join_data = models.DateTimeField(auto_now=True)

    followers = models.ManyToManyField("self", through="Rela", symmetrical=False, related_name="followers_")
    following = models.ManyToManyField("self", through="Rela", symmetrical=False, related_name="following_")

    def __str__(self):
        return username


class Message(models.Model):
    created_by = models.ForeignKey(User)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return content


class Rela(models.Model):
    to_user = models.ForeignKey(User, related_name="related_to")
    from_user = models.ForeignKey(User, related_name="relationships")
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "from_user: %s, to_user: %s" % (from_user, to_user)


