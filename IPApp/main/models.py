from django.db import models


class Departments(models.Model):
    title = models.CharField('Название отдела', max_length=60)
    description = models.TextField(' Описание отдела')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = 'Отделы'


class Positions(models.Model):
    department_id = models.ForeignKey(Departments, verbose_name='Название отдела', related_name='post',
                                      on_delete=models.CASCADE)
    title = models.CharField('Название должности', max_length=60)
    description = models.TextField(' Описание должности')

    def __str__(self):
        return self.title + ' (' + self.department_id.title + ' отдел)'

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = 'Должности'


class Workers(models.Model):
    position_id = models.ForeignKey(Positions, verbose_name='Название должности', related_name='employee',
                                    on_delete=models.CASCADE)
    surname = models.CharField('Фамилия', max_length=100)
    name = models.CharField('Имя', max_length=60)
    middle_name = models.CharField('Отчество', max_length=100)

    def __str__(self):
        return self.surname + ' ' + self.name + ' ' + self.middle_name

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = 'Сотрудники'


class PersonInfo(models.Model):
    worker_id = models.ForeignKey(Workers, verbose_name='Работник', related_name='information',
                                  on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    passport = models.CharField('Паспорт', max_length=20)
    phone = models.CharField('Телефон', max_length=30)

    def __str__(self):
        return self.passport

    class Meta:
        verbose_name = "Личная информация"
        verbose_name_plural = "Личная информация"


class Experience(models.Model):
    worker_id = models.ForeignKey(Workers, verbose_name='Работник', related_name='exp',
                                  on_delete=models.CASCADE)
    company = models.CharField('Работодатель', max_length=100)
    post = models.CharField('Должность', max_length=30)
    duration = models.CharField('Длительность', max_length=30)

    def __str__(self):
        return self.company

    class Meta:
        verbose_name = "Опыт работы"
        verbose_name_plural = "Опыт работы"


class Tasks(models.Model):
    worker_id = models.ForeignKey(Workers, verbose_name='Работник', related_name='job',
                                  on_delete=models.CASCADE)
    title = models.CharField('Название задачи', max_length=100)
    description = models.TextField('Описание задачи')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
