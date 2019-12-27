from django.urls import path
from system.accounts import views
from django.contrib.auth.views import LoginView, LogoutView

app_name="accounts"

urlpatterns = [
	path('entrar/', LoginView.as_view(template_name='accounts/login.html', redirect_authenticated_user=True), name='login'),
	path('sair/', LogoutView.as_view(next_page='/conta/entrar/'), name='logout'),
	path('editar/', views.edit, name='edit'),
	path('cadastro/', views.register, name='register'),

]