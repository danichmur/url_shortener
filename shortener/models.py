from django.db import models
from django import forms
import hashlib

# Create your models here.

class Shortener(models.Model):
	url = models.CharField(max_length=200)
	short_url = models.CharField(max_length=200)
	visits = models.PositiveIntegerField(default=1)

	@staticmethod
	def get_hash_url(url):
		hash_object = hashlib.md5(url.encode())
		cut_hash = hash_object.hexdigest()[:6]
		return cut_hash

	@classmethod
	def create(cls, url, prefix):
		hash_url = cls.get_hash_url(url)
		#short_url = '{}/{}'.format(prefix, hash_url)

		shortener = cls(url=url, short_url=hash_url)
		return shortener

	def __str__(self):
		return 'URL: {}; Hash: {}; visits: {}'.format(self.url, self.short_url, self.visits)
