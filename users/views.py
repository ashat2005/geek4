from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from users.forms import UserRegistrationForm

class RegisterView(FormView):
    form_class = UserRegistrationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("register_done")

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data.get("password2"))
        new_user.save()
        return super().form_valid(form)