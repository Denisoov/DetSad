from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    title = models.CharField(max_length=150, help_text='Введите название организации доп. образования', verbose_name='Организация', null=False)
    director = models.CharField(max_length=150, help_text='Введите директора организации', verbose_name='Директор', null = True, blank=True)

    def __str__(self):
        return self.title


class Section(models.Model):
    title = models.CharField(max_length=150, help_text='Введите название секции', verbose_name='Секция', null=False)
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, help_text='Выберите организацию', verbose_name='Организация', null=False)
    date = models.DateField(help_text='Введите дату начала', verbose_name='Дата', auto_now_add=True)
    coach = models.CharField(max_length=150, help_text='Введите главного тренера секции', verbose_name='Тренер', null=True, blank=True)
    load = models.FloatField(default=10, help_text='Введите нагруженность секции', verbose_name="Нагруженность секции")

    def __str__(self):
        return self.title


class Garten(models.Model):
    number = models.IntegerField(default=1, help_text='Введите номер детского сада', verbose_name='Номер дет. сада')
    title = models.CharField(max_length=150, help_text='Введите название дет. сада', verbose_name='Название', null=False)
    director = models.CharField(max_length=150, help_text='Введите директора дет. сада', verbose_name='Директор', null=False)

    def __str__(self):
        return self.title


class Group(models.Model):
    title = models.CharField(max_length=50, help_text='Введите имя ребенка', verbose_name='Имя', null=False)
    garten = models.ForeignKey('Garten', on_delete=models.CASCADE, help_text='Выберите дет. сад', verbose_name='Дет. сад', null=False)

    def __str__(self):
        return '%s: %s' % (self.garten.title, self.title)


class Child(models.Model):
    Firstname = models.CharField(max_length=50, help_text='Введите имя ребенка', verbose_name='Имя', null=False)
    Lastname = models.CharField(max_length=50, help_text='Введите фамилию ребенка', verbose_name='Фамилия', null=False)
    Secondname = models.CharField(max_length=50, help_text='Введите отчество ребенка', verbose_name='Отчество', null=True, blank=True)
    date = models.DateField(help_text='Введите дату рождения', verbose_name='Дата рождения')
    group = models.ForeignKey('Group', on_delete=models.CASCADE, help_text='Введите номер группы', verbose_name='Группа')
    load = models.FloatField(default=0, help_text='Введите нагруженность ребенка', verbose_name="Нагруженность ребенка")
    sections = models.ManyToManyField('Section', help_text='Выберите секции ребенка', verbose_name='Секции', blank=True)
    parents = models.ManyToManyField('Parent', help_text='Выберите родителей ребенка', verbose_name='Родители', blank=True)

    def __str__(self):
        return self.Lastname


class Parent(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Родитель', null=False)

    def __str__(self):
        if self.person.last_name:
            return self.person.last_name
        else:
            return self.person.username


class Admin_Garten(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Работник садика', null=False)
    garten = models.ForeignKey(Garten, on_delete=models.CASCADE, verbose_name='Cадик', null=False)

    def __str__(self):
        if self.person.last_name:
            return self.person.last_name
        else:
            return self.person.username


class Admin_Organization(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Работник организации', null=False)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name='Организация', null=False)

    def __str__(self):
        if self.person.last_name:
            return self.person.last_name
        else:
            return self.person.username

