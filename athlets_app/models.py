from django.db import models

# Created Athletics models here.

#Type of Gender.

gender_choice = [
    (1, "Male"),
    (2, "Female"),
    (3, "Transgender")
]
#Choose Participate or not

participate_choice = [
    ("participate", "Participate"),
    ("not participate", "Not Participate")
]

#AthleticsCategories ( AthleticsCategory model)
class AthleticsCategories(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

#Athletics ( Athletics model)
class Athletics(models.Model):
    name = models.CharField(max_length=50)
    athletics_category = models.ForeignKey(AthleticsCategories, on_delete=models.CASCADE)
    join_date = models.DateField()
    is_participated = models.CharField(choices=participate_choice, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

#Players ( Players model)

class Players(models.Model):
    name = models.CharField(max_length=50)
    gender = models.IntegerField(choices=gender_choice)
    number_race = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

#Competitions ( Competition model)
class Competitions(models.Model):
    athletics = models.ForeignKey(Athletics, on_delete=models.CASCADE)
    players = models.ForeignKey(Players, on_delete=models.CASCADE)
    distance = models.IntegerField(blank=False, default=0)
    date = models.DateTimeField()

