from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 100)
    scores = models.JSONField(default = list)

    def get_average_score(self):
        if not self.scores:
            return 0 
        return sum(self.scores)/len(self.scores)
    
    def get_top_score(self):
        return max(self.scores) if self.scores else 0
    
    def __str__(self):
        return self.name
    
