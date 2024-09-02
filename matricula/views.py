from django.shortcuts import render, redirect
from .forms import AlunoForm

def aluno_preenche(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('preenche')
    else:
        form = AlunoForm()

    return render(request, 'form_aluno.html',{'form': form})       