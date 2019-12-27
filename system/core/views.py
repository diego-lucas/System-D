from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def initial_menu(request):
	return render(request, 'initial-menu.html')