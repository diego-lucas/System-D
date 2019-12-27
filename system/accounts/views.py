from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, get_user_model


from .forms import EditAccountForm, RegisterForm

@login_required
def edit(request):
	template_name = 'accounts/edit.html'
	context = {}
	if request.method == 'POST':
		form = EditAccountForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			form = EditAccountForm(instance=request.user)
			context['success'] = True
	else:
		form = EditAccountForm(instance=request.user)
	context['form'] = form
	return render(request, template_name, context)


def register(request):
	if not request.user.is_authenticated:
		template_name = 'accounts/register.html'
		if request.method == 'POST':
			form = RegisterForm(request.POST)
			if form.is_valid():
				user = form.save()
				user = authenticate(
					username=user.username, password=form.cleaned_data['password1']
				)
				login(request, user)
				return redirect('core:home')
		else:
			form = RegisterForm()
		context = {
			'form': form
		}
		return render(request, template_name, context)
	else:
		return redirect('core:home')