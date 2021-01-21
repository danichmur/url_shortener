from django.test import TestCase
from .forms import ShortenerForm
from .models import Shortener
# Create your tests here.

class UnitTestCase(TestCase):

	def test_home_page(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'shortener/home.html')

	def test_form(self):
		form = ShortenerForm(data={'url':'hello'})
		self.assertTrue(form.is_valid)


	def test_hash_works(self):
		hash_ = Shortener.get_hash_url('hello')
		self.assertEqual(hash_, '5d4140')

	def test_shortener_object(self):
		shortener = Shortener.create('hello')
		shortener.save()
		pulled_shortener = Shortener.objects.get(short_url=shortener.short_url)
		self.assertEqual(shortener.url, pulled_shortener.url)
