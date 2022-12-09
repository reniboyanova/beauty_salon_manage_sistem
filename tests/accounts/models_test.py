from django.test import TestCase

from beauty_salon_manage_sistem.accounts.models import AppStaffProfile, AppBaseUser


class AppUserProfileTest(TestCase):

    def test_profile_creation_with_user__one_to_one__relation(self):
        user = AppBaseUser(
            email='reni@info.bg',
            password='1234',
        )
        user.save()
        profile = AppStaffProfile(
            first_name='Reni',
            last_name='Boyanova',
            position='Owner',
            user=user
        )

        profile.full_clean()  # Call this for validation
        profile.save()

        # Assert
        self.assertIsNotNone(user)