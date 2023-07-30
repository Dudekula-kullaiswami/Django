

from django.db import models
class Issue(models.Model):
    STATUS_CHOICES = (
        ('INQUEUE', 'In Queue'),
        ('ASSIGNED', 'Assigned'),
        ('DISPATCHED', 'Dispatched'),
    )

    issueID = models.AutoField(primary_key=True)
    userID = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    problem = models.TextField()
    time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Issue {self.issueID}: {self.problem}"
class Agents(models.Model):
    AgentID = models.AutoField(primary_key=True)
    Queue = models.IntegerField(default=0)

    def __str__(self):
        return f"Agent {self.AgentID} - Queue: {self.Queue}"
class Mechanic(models.Model):
    mechanicID = models.AutoField(primary_key=True)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"Mechanic {self.mechanicID} - Availability: {self.availability}"
