from django.db import models
from django.utils.timezone import now

class overall_status(models.Model):
    date = models.DateTimeField(default=now)
    akash = models.IntegerField(primary_key=True)
    ayush = models.IntegerField()
    ronak = models.IntegerField()
    raghav = models.IntegerField()
    house = models.IntegerField()

    def __str__(self):
        return str(self.akash) + '#' + str(self.ayush) + '#' + str(self.ronak) + '#' + str(self.raghav) +'#'+ str(self.house)


class match_status(models.Model):
    date = models.DateTimeField(default=now)
    match_number = models.IntegerField(primary_key=True)
    match_teams = models.TextField(default="")
    akash = models.TextField()
    ayush = models.TextField()
    ronak = models.TextField()
    raghav = models.TextField()
    isCalculated = models.BooleanField(default=False)

    def __str__(self):
        return str(self.match_number)+ '-'+ str(self.akash) + '-' + str(self.ayush) + '-' + str(self.ronak) + '-' + str(self.raghav) + '-' + str(self.isCalculated)
