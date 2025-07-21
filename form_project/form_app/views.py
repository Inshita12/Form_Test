from django.shortcuts import render, redirect
from .forms import FormResponseForm

def submit_form(request):
    if request.method == 'POST':
        form = FormResponseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = FormResponseForm()
    return render(request, 'form_app/form.html', {'form': form})

def success_view(request):
    return render(request, 'form_app/success.html')
