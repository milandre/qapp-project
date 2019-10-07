"""User Views.

This file has the views used
for user operations like
login and reistration.
"""

from django.views import generic
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages

from forms import RegisterForm

# Create your views here.


class RegisterView(generic.FormView):
    """RegisterView

    FormView for register user page.
    """

    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """If form is valid, save it and show
        a message.

        Args:
            form (obj): Form object

        Returns:
            A http response with a successful message
        """

        form.save()

        messages.add_message(self.request,
                             messages.SUCCESS,
                             'Successful sign in')

        return HttpResponseRedirect(self.get_success_url())
