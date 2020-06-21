from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .forms import RegisterForm
from django.db.models import Q
from users.models import Roommates
from django.http import HttpResponse

def register(request):
	if request.user.is_authenticated:
		return redirect('home')
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			user = User.objects.get(username = username)
			genre = form.cleaned_data.get('genre')
			group = Group.objects.get(name = genre)
			group.user_set.add(user)
			user.save()
			annee = form.cleaned_data.get('annee')
			group = Group.objects.get(name = annee)
			group.user_set.add(user)
			user.save()
			return redirect('home')
	else:
		form = RegisterForm()
	return render(request, 'register.html', {'form': form})

@login_required
def roommate(request):
	if request.user.roommate1.all().count() != 0 or request.user.roommate2.all().count() != 0:
		return redirect('home')
	if request.GET.get('search'):
		roomate = request.GET.get('search')
		group = request.user.groups.all().first()
		results = User.objects.filter(groups__name=group)
		results = results.filter(Q(first_name__icontains=roomate) | Q(last_name__icontains=roomate))
		return render(request, 'roommate.html', {'results': results})
	return render(request, 'roommate.html')

@login_required
def add(request, pk):
	if request.user.roommate1.all().count() != 0 or request.user.roommate2.all().count() != 0:
		return HttpResponse("Nice Try :)")
	rmt = User.objects.get(id=pk)
	obj = Roommates(user1=request.user, user2=rmt)
	obj.save()
	return redirect('home')

@login_required
def delete(request):
	if request.user.roommate1.all().count() != 0:
		request.user.roommate1.all().first().delete()
	if request.user.roommate2.all().count() != 0:
		request.user.roommate2.all().first().delete()
	return redirect('roommate')

def fuck(request):
	if not request.user.is_superuser:
		raise PermissionDenied
	lst = Roommates.objects.all()
	arr = []
	for e in lst:
		f1 = Q(user1__first_name__icontains=e.first_name)
		f2 = Q(user1__last_name__icontains=e.last_name)
		f3 = Q(user2__first_name__icontains=e.first_name)
		f4 = Q(user2__last_name__icontains=e.last_name)
		f5 = Q(user1__first_name__icontains=e.last_name)
		f6 = Q(user1__last_name__icontains=e.first_name)
		f7 = Q(user2__first_name__icontains=e.last_name)
		f8 = Q(user2__last_name__icontains=e.first_name)
		f = Q(Q(f1, f2) | Q(f3, f4) | Q(f5, f6) | Q(f7, f8))
		obj = Roommates.objects.filter(f)
		arr.append(obj)
	return render(request, 'fuck.html', {'arr': arr})



