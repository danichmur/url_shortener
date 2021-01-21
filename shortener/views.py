from django.shortcuts import render, redirect
from .forms import ShortenerForm
from .models import Shortener
from django.http import HttpResponse, HttpResponseNotFound


def home(request):
	return render(request, 'shortener/home.html', {'shorteners': Shortener.objects.all})


def short(request):
	if request.method == 'POST':
		filled_form = ShortenerForm(request.POST)
		if filled_form.is_valid():
			url = filled_form.cleaned_data['url']
			shortener = Shortener.create(url)
			shortener.save()
			note = 'hash url {}/{}!'.format(request.build_absolute_uri(), shortener.short_url)
			new_form = ShortenerForm()
			return render(request, 'shortener/short.html', {'shortform': new_form, 'note': note})
	else:
		form = ShortenerForm()
		return render(request, 'shortener/short.html', {'shortform': form})


def short_redirect(request, short):
	shortener = Shortener.objects.filter(short_url=short).first()
	if shortener is None:
		return HttpResponseNotFound('<h1>Page not found</h1>')
	else:
		shortener.visits = shortener.visits + 1
		shortener.save()

		return redirect(shortener.url)
