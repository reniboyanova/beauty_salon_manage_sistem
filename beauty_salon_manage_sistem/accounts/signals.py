from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

# from beauty_salon_manage_sistem.accounts.models import AppStaffProfile
#
# UserModel = get_user_model()
#
#
# @receiver(post_save, sender=UserModel)
# def crete_profile(sender, instance, created, **kwargs):
#     if created:
#         AppStaffProfile.objects.create(user=instance)

#
# @receiver(post_save, sender=UserModel)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()