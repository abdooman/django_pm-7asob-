from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from accounts.forms import UserRegisterForm, ProfileForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
# Create your views here.




class RegisterView(CreateView):
    form_class = UserRegisterForm
    #success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    def get_succss_url(self):
        login(self.request, self.object) # type: ignore
        return reverse_lazy('Project_list')
    
@login_required # type: ignore 

def edit_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:   
        form = ProfileForm(instance=request.user)
        return render(request, 'profile.html',{
             'form': form
        })