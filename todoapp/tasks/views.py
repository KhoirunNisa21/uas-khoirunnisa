from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Tugas
from .import TugasForm

class TugasListView(View):
    def get(self, request):
        tugas = Tugas.objects.all()
        return render(request, 'tugas/tugas_list.html', {'tugas': Tugas})

class AddTugaskView(View):
    def get(self, request):
        form = TugasForm()
        return render(request, 'tugas/add_tugas.html', {'tugas': TugasForm})

    def post(self, request):
        form = TugasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tugas_list')
        return render(request, 'tugas/add_tugas.html', {'tugas': TugasForm})

class CompleteTaskView(View):
    def post(self, request, tugas_id):
        task = get_object_or_404(Tugas, pk=tugas_id)
        task.completed = True
        task.save()
        return redirect('tugas_list')

class DeleteTugasView(View):
    def post(self, request, tugas_id):
        tugas = get_object_or_404(Tugas, pk=tugas_id)
        tugas.delete()
        return redirect('task_list')



