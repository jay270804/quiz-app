from django.db import models

# Create your models here.
class Questions(models.Model):
    """Model for quiz questions"""
    question_text = models.CharField(max_length=255)
    options = models.JSONField()
    correct_option = models.CharField(max_length=5)

    def __str__(self):
        return self.question_text

    def save(self, *args, **kwargs):
        """overriding method to validate if correct option is present in options"""
        if isinstance(self.options, dict) and self.correct_option not in self.options:
            raise ValueError("Correct option must be a key in options.")
        super().save(*args, **kwargs)

class QuizSession(models.Model):
    """Model to store user progress in quiz"""
    total_questions = models.IntegerField(default=0)
    correct_questions = models.IntegerField(default=0)
    incorrect_questions = models.IntegerField(default=0)

    def __str__(self):
        return f"Session: {self.id}"