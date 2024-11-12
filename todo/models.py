from django.db import models

class Todo(models.Model):
    CHECK_CHOICES = (
        ("✅", "✅"),
        ("❌", "❌")
    )
    title_todo = models.CharField(max_length=100,verbose_name='Укажите задачу')
    time_start = models.TimeField(verbose_name='укажите время начала')
    time_end = models.TimeField(verbose_name='укажите время конца задачи')
    check_yes_no = models.CharField(max_length=100, verbose_name='укажите выполнено задача или нет',
                             choices=CHECK_CHOICES)

    def __str__(self):
        return f'{self.title_todo} - {self.check_yes_no}'
