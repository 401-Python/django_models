from django.test import TestCase
from .models import Comment
from django.contrib.auth import get_user_model
# Create your tests here.
class CommentTests(TestCase):
  def setUp(self):
    self.user = get_user_model().objects.create_user(username='testuser', email='test@test.com', password='secret')

    self.comment = Comment.objects.create(title='please work', body='it worked', author=self.user)


  def test_string_repr(self):
    comment = Comment.objects.get(id=1)

    self.assertEqual(str(comment), 'please work')