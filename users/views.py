from django.shortcuts import render
from django.views import View
from users.forms import UserRegistrationForm


class RegisterView(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, "registration/register.html", {"form": form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password2'])
            new_user.save()
            return render(request, "registration/register_done.html", {"user": new_user})
        return render(request, "registration/register.html", {"form": form})


