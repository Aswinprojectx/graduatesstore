# from django.db import models
#
#
# class Cou(models.Model):
#     name = models.CharField(max_length=40)
#
#     def __str__(self):
#         return self.name
#
#
# class SP(models.Model):
#     course = models.ForeignKey(Cou, on_delete=models.CASCADE)
#     name = models.CharField(max_length=40)
#
#     def __str__(self):
#         return self.name
#
#
# class Person(models.Model):
#     name = models.CharField(max_length=124)
#     course = models.ForeignKey(Cou, on_delete=models.SET_NULL, blank=True, null=True)
#     specialization = models.ForeignKey(SP, on_delete=models.SET_NULL, blank=True, null=True)
#
#     def __str__(self):
#         return self.name