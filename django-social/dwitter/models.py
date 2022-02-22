from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    trust = models.ManyToManyField(
        "self",
        related_name="trusts",
        symmetrical=False,
        blank=True
    )

    def __str__(self):
        return self.user.username


class Item(models.Model):

    user = models.ForeignKey(User, related_name="items", on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=30)
    trading_time = (models.DateTimeField(), models.DateTimeField())
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user} "
            f"({self.created_at:%Y-%m-%d %H:%M}): "
            f"{self.body[:30]}..."
            f"{self.description} "
        )


class File(models.Model):

    item = models.ForeignKey(Item, related_name="files", on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.trust.set([instance.profile.id])
        user_profile.save()

#@receiver(post_save, sender=User)
#def create_item(sencer, instance,created, **kwargs):
#    if created:
#        item = Item