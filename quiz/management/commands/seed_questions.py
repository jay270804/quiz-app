from django.core.management.base import BaseCommand
from django.db import IntegrityError
from quiz.models import Questions
from quiz.config import SeedConfig
from quiz.serializers import QuestionsSerializer

class Command(BaseCommand):
    """Custom command to seed the database"""

    help = "Seed database with questions"

    def handle(self, *args, **kwargs):
        """method to start seeding."""
        seed_data = SeedConfig.SEED_DATA

        for data in seed_data:
            serializer = QuestionsSerializer(data=data)

            if serializer.is_valid():
                try:
                    serializer.save()
                    self.stdout.write(f"Created Question: {data['question_text']}")
                except Exception as e:
                    self.stderr.write(f"Failed to save question - {data['question_text']} - Error: {str(e)}")
            else:
                self.stderr.write(f"Validation error: {serializer.errors}")