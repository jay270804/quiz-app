from rest_framework import serializers
from .models import Questions

VALID_KEYS={"A", "B", "C", "D", "E"}

class QuestionsSerializer(serializers.ModelSerializer):
    """Serializer to validate Questions model"""

    class Meta:
        model = Questions
        fields = ['question_text', 'options', 'correct_option']

    def validate_options(self, value):
        """method to validate the keys in options are Capital alphabets"""
        valid_keys = VALID_KEYS
        if not isinstance(value, dict):
            raise serializers.ValidationError("Options must be passed as dictionary: {'A':'option_a', 'B':'option_b'}, etc.")
        if not all(keys in valid_keys for keys in value):
            raise serializers.ValidationError("Option keys must be capital alphabets: 'A', 'B', 'C', 'D', etc.")
        return value

    def validate(self, data):
        """custom method to validate if correct options present in options"""
        options = data.get('options', {})
        correct_option = data.get('correct_option')

        if correct_option not in options:
            raise serializers.ValidationError("Correct option must be present in options.")

        return data