from django.shortcuts import render, redirect
from .models import Chambre
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from users.models import Roommates
from django.contrib import messages
from django.db.models import Q

# @login_required
# def home(request):
# 	u = request.user
# 	if u.roommate1.all().count() != 0 or u.roommate2.all().count() != 0:
# 		if u.roommate1.all().count() != 0:
# 			coch = u.roommate1.all().first().user2
# 		else:
# 			coch = u.roommate2.all().first().user1
# 		if u.groups.all().first().name == "boy":
# 			genre = 1
# 		else:
# 			genre = 2
# 		lst1 = Chambre.objects.filter(cite=1, genre=genre)
# 		lst2 = Chambre.objects.filter(cite=2, genre=genre)
# 		lst3 = Chambre.objects.filter(cite=3, genre=genre)

# 		rmt = Roommates.objects.get(Q(user1=u)|Q(user2=u))
# 		if len(rmt.choices) > 3:
# 			stored_choices = rmt.choices.split(",")
# 			for i in range(len(stored_choices)):
# 				num = stored_choices[i]
# 				ch = Chambre.objects.get(num=num)
# 				stored_choices[i] = ch.name + " " + ch.get_cite_display()
# 			updated_at = rmt.updated_at
# 			return render(request, 'home.html', {'lst1': lst1, 'lst2': lst2, 'lst3': lst3, 'coch': coch, 'stored_choices': stored_choices, 'updated_at': updated_at})
# 		else:
# 			return render(request, 'home.html', {'lst1': lst1, 'lst2': lst2, 'lst3': lst3, 'coch': coch})
# 	else:
# 		return redirect('roommate')

def home(request):
	return render(request, "gif.html")

@login_required
def results(request):
	if request.method == 'POST':
		if request.POST.get("choices_input"):
			choices = request.POST.get("choices_input")
			u = request.user
			rmt = Roommates.objects.get(Q(user1=u)|Q(user2=u))
			rmt.choices = choices
			rmt.save()
	return redirect('home')

def tirage(request):
	if not request.user.is_superuser:
		raise PermissionDenied
	lst = Roommates.objects.filter(valid=True, third=True, genre=1).order_by('?')
	for el in lst:
		ch_arr = el.choices.split(',')
		for i in ch_arr:
			ch = Chambre.objects.get(num=i)
			if not ch.is_taken:
				el.chambre = ch
				el.save()
				ch.is_taken = True
				ch.save()
				break
		if not el.chambre:
			void_ch_lst = Chambre.objects.filter(is_taken=False, genre=1).order_by('?')
			void_ch = void_ch_lst.first()
			el.chambre = void_ch
			el.save()
			void_ch.is_taken = True
			void_ch.save()

	lst = Roommates.objects.filter(valid=True, third=True, genre=2).order_by('?')
	for el in lst:
		ch_arr = el.choices.split(',')
		for i in ch_arr:
			ch = Chambre.objects.get(num=i)
			if not ch.is_taken:
				el.chambre = ch
				el.save()
				ch.is_taken = True
				ch.save()
				break
		if not el.chambre:
			void_ch_lst = Chambre.objects.filter(is_taken=False, genre=2).order_by('?')
			void_ch = void_ch_lst.first()
			el.chambre = void_ch
			el.save()
			void_ch.is_taken = True
			void_ch.save()

	lst = Roommates.objects.filter(valid=True, third=False, genre=1).order_by('?')
	for el in lst:
		ch_arr = el.choices.split(',')
		for i in ch_arr:
			ch = Chambre.objects.get(num=i)
			if not ch.is_taken:
				el.chambre = ch
				el.save()
				ch.is_taken = True
				ch.save()
				break
		if not el.chambre:
			void_ch_lst = Chambre.objects.filter(is_taken=False, genre=1).order_by('?')
			void_ch = void_ch_lst.first()
			el.chambre = void_ch
			el.save()
			void_ch.is_taken = True
			void_ch.save()

	lst = Roommates.objects.filter(valid=True, third=False, genre=2).order_by('?')
	for el in lst:
		ch_arr = el.choices.split(',')
		for i in ch_arr:
			ch = Chambre.objects.get(num=i)
			if not ch.is_taken:
				el.chambre = ch
				el.save()
				ch.is_taken = True
				ch.save()
				break
		if not el.chambre:
			void_ch_lst = Chambre.objects.filter(is_taken=False, genre=2).order_by('?')
			void_ch = void_ch_lst.first()
			el.chambre = void_ch
			el.save()
			void_ch.is_taken = True
			void_ch.save()

	return redirect('home')

def done(request):
	if not request.user.is_superuser:
		raise PermissionDenied
	u = request.user
	if u.roommate1.all().count() != 0 or u.roommate2.all().count() != 0:
		if u.roommate1.all().count() != 0:
			coch = u.roommate1.all().first().user2
			chambre = u.roommate1.all().first().chambre
			valid = u.roommate1.all().first().valid
		else:
			coch = u.roommate2.all().first().user1
			chambre = u.roommate2.all().first().chambre
			valid = u.roommate2.all().first().valid
	return render(request, 'done.html', {'coch': coch, 'chambre': chambre, 'valid': valid})






