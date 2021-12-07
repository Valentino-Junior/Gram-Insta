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

#     def test_save_image_method(self):
#         images = Images.objects.all()
#         self.assertTrue(len(images)> 0)

#     def test_delete_image(self):
#         images1 = Images.objects.all()
#         self.assertEqual(len(images1),1)
#         self.food.delete_image()
#         images2 = Images.objects.all()
#         self.assertEqual(len(images2),0)

#     def test_update_caption(self):
#         self.food.update_caption('Bolognese')
#         self.assertEqual(self.food.caption, 'Bolognese')

#     def test_get_profile_images(self):
#         self.maua.save_image()
#         images = Images.get_profile_images(self.profile)
#         self.assertEqual(len(images),2)

# class ProfileTestClass(TestCase):
#     def setUp(self):
#         self.lorna = User(username = "lorna", email = "lorna@gmail.com",password = "1234")
#         self.profile = Profile(bio='bio', user= self.lorna)
#         self.lorna.save()

#     def tearDown(self):
#         Profile.objects.all().delete()
#         User.objects.all().delete()

#     def test_instance(self):
#         self.assertTrue(isinstance(self.lorna, User))
#         self.assertTrue(isinstance(self.profile, Profile))

#     def test_search_user(self):
#         user = Profile.search_user(self.lorna)
#         self.assertEqual(len(user), 1)

# class CommentTestClass(TestCase):
#     def setUp(self):
#         self.lorna = User(username = "lorna", email = "lorna@gmail.com",password = "1234")
#         self.profile = Profile(bio='bio', user= self.lorna)
#         self.food = Images(image = 'imageurl', name ='food', caption = 'Chicken Taco', profile = self.profile)
#         self.comment = Comments(image=self.food, content= 'Looks delicious', user = self.lorna)

#         self.lorna.save()
#         self.profile.save()
#         self.food.save_image()
#         self.comment.save_comment()

#     def tearDown(self):
#         Images.objects.all().delete()
#         Comments.objects.all().delete()

#     def test_instance(self):
#         self.assertTrue(isinstance(self.comment, Comments))

#     def test_save_comment(self):
#         comments = Comments.objects.all()
#         self.assertTrue(len(comments)> 0)

#     def test_delete_comment(self):
#         comments1 = Comments.objects.all()
#         self.assertEqual(len(comments1),1)
#         self.comment.delete_comment()
#         comments2 = Comments.objects.all()
#         self.assertEqual(len(comments2),0)

#     def test_get_image_comments(self):
#         comments = Comments.get_image_comments(self.food)
#         self.assertEqual(comments[0].content, 'Looks delicious')
#         self.assertTrue(len(comments) > 0)
