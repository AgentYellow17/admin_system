from django.db import models
from django.urls import reverse

class Role(models.Model):
  category = models.CharField(max_length = 200)

  def __str__(self):
    return self.category

class Link(models.Model):
  name = models.CharField(max_length = 200)
  role = models.ManyToManyField(Role)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('link-detail', args = [str(self.id)])

  def display_role(self):
    return ', '.join(role.category for role in self.role.all()[:3])