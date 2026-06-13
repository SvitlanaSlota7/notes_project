from django.db import models
from django.contrib.auth.models import User, Group


class Note(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст нотатки")
    created_at = models.DateTimeField(auto_now_add=True)

    # Зв'язок з користувачем. Якщо користувача видалено, його нотатки теж видаляються (CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')

    # Зв'язок з групою. Нотатка може не належати групі (null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, related_name='group_notes')

    def __str__(self):
        return self.title
