from django.shortcuts import render
from .pass_generator import password_generator, create_password_str
from .forms import PasswordGenForm

# Create your views here.
def index(request):
    new_password = None
    if request.method == 'POST':
        form = PasswordGenForm(request.POST)
        if form.is_valid():
            temp = create_password_str(**form.cleaned_data)
            if temp:
                new_password = ''.join(password_generator(form.cleaned_data['password_length'], temp))
            form.fields['has_lower'].widget.attrs['checked'] = form.cleaned_data['has_lower'] or False
            form.fields['has_upper'].widget.attrs['checked'] = form.cleaned_data['has_upper'] or False
            form.fields['has_digit'].widget.attrs['checked'] = form.cleaned_data['has_digit'] or False
            form.fields['has_punctuation'].widget.attrs['checked'] = form.cleaned_data['has_punctuation'] or False
            context = {
                'new_password': new_password,
                'pass_form': form
            }
        return render(request, 'password_form.html', context)
    form = PasswordGenForm()
    context = {
        'new_password': new_password,
        'pass_form': form
    }
    return render(request, 'password_form.html', context)
