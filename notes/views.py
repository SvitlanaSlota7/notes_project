from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Note


@login_required
def notes_list(request):
    # Отримуємо тип нотаток з GET-запиту (за замовчуванням 'personal')
    view_type = request.GET.get('view', 'personal')

    if view_type == 'group':
        # Нотатки груп, у яких перебуває поточний користувач
        user_groups = request.user.groups.all()
        notes = Note.objects.filter(group__in=user_groups)
    else:
        # Тільки власні нотатки користувача
        notes = Note.objects.filter(author=request.user)

    return render(request, 'notes/index.html', {
        'notes': notes,
        'view_type': view_type
    })


@login_required
def note_delete(request, pk):
    # Захист: користувач може видалити тільки СВОЮ нотатку
    note = get_object_or_404(Note, pk=pk, author=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('notes_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})