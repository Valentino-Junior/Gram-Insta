from django.test import TestCase
from .models import Images, Comments, Profile
from django.contrib.auth.models import User

class ProfileTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(
            username='test_user',
            first_name='ian',
            last_name='seme'
        )
        Profile.objects.create(
            bio='test bio',
            prof_photo='https://unsplash.com/photos/Pp6efQ_ghiA',
            user_id=user.id
        )

    def test_bio(self):
        profile = Profile.objects.get(bio='test bio')
        self.assertEqual(profile.bio, 'test bio')

class ImageTestCase(TestCase):
    def setUp(self):
        # create a user
        user = User.objects.create(
            username='test_user',
        )
        Images.objects.create(
            photo_name='test_image',
            image='https://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Kenya.svg',
            photo_caption='test image',
            user_id=user.id
        )
    def test_image_name(self):
        image = Images.objects.get(photo_name='test_image')
        self.assertEqual(image.photo_name, 'test_image')
    def test_image_id(self):
        user = User.objects.create(
            username='newuser',
        )
        photo = Images.objects.create(
            photo_caption='test post',
            image='https://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Kenya.svg',
            user_id=user.id
        )
    def test_image_posted_at(self):
        user = User.objects.create(
            username='newuser',
        )
        photo = Images.objects.create(
            photo_caption='test post',
            image='https://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Kenya.svg',
            user_id=user.id
        )
    def test_image_user(self):
        user = User.objects.create(
            username='newuser',
        )
        photo = Images.objects.create(
            photo_caption='test post',
            image='https://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Kenya.svg',
            user_id=user.id
        )
    def test_image_photo_caption(self):
        user = User.objects.create(
            username='newuser',
        )
        photo = Images.objects.create(
            photo_caption='test post',
            image='https://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Kenya.svg',
            user_id=user.id
        )
    def test_image_liked(self):
        user = User.objects.create(
            username='newuser',
        )
        photo = Images.objects.create(
            photo_caption='test post',
            image='https://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Kenya.svg',
            user_id=user.id
        )

