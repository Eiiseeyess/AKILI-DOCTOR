from .models import Account
from rest_framework import serializers
from datetime import date

class AccountSerializer(serializers.ModelSerializer):
    '''The Account model serializer with validation'''
    profile_picture = serializers.ImageField(required=False) 

    class Meta:
        model = Account
        fields = [
            'id', 'first_name', 'last_name', 'username', 'email', 'phone',
            'password', 'date_of_birth', 'profile_picture', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']
        extra_kwargs = {'password': {'write_only': True}}  

    def validate_first_name(self, value):
        '''Validate the first name'''
        if not value.isalpha():
            raise serializers.ValidationError("First name must contain only alphabetic characters.")
        return value

    def validate_last_name(self, value):
        '''Validate the last name'''
        if not value.isalpha():
            raise serializers.ValidationError("Last name must contain only alphabetic characters.")
        return value

    def validate_email(self, value):
        '''Validate the email format'''
        if not "@" in value or not "." in value:
            raise serializers.ValidationError("Enter a valid email address.")
        if Account.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def validate_phone(self, value):
        '''Validate the phone number'''
        if not value.isdigit() or len(value) < 10:
            raise serializers.ValidationError("Enter a valid phone number with at least 10 digits.")
        return value

    def validate_date_of_birth(self, value):
        '''Validate the date of birth'''
        today = date.today()
        if value >= today:
            raise serializers.ValidationError("Date of birth must be in the past.")
        if (today.year - value.year) < 14:
            raise serializers.ValidationError("Users must be at least 14 years old.")
        return value

    def validate_profile_picture(self, value):
        '''Validate the profile picture size and type'''
        if value.size > 2 * 1024 * 1024: 
            raise serializers.ValidationError("Profile picture size must not exceed 2MB.")
            
        file_type = getattr(value, 'content_type', None) or getattr(value.file, 'content_type', None)
        if file_type and not file_type.startswith('image/'):
            raise serializers.ValidationError("Invalid file type. Please upload an image.")
    # Cross-field validation
    def validate(self, attrs):
        ''' cross-field validation '''
        username = attrs.get('username')
        email = attrs.get('email')
        if username and Account.objects.filter(username=username).exists():
            raise serializers.ValidationError("A user with this username already exists.")
        return attrs

    def create(self, validated_data):
        '''Create user securely using the Account manager'''
        user = Account.objects.create_user(**validated_data)
        return user
