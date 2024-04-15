from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model, logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
User = get_user_model()


class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"

    def get_success_url(self):
        return reverse_lazy('home')

class EditView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = "registration/edit.html"

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        messages.success(self.request, "수정되었습니다.")
        return reverse_lazy("home")


class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = "registration/password_change.html"
    success_url = reverse_lazy("password_change_done")


@login_required
def delete_account(request):
    if request.method == "POST":
        user = request.user
        user.delete()
        logout(request)
        messages.success(request, "회원탈퇴가 완료되었습니다.")
        return redirect("home")
    else:
        return redirect("home")
