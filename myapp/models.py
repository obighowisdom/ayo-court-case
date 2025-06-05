from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import uuid



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

# accounts/models.py
class CustomUser(AbstractUser):
    username = None  # Remove username field
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    # Add this method for compatibility with allauth
    def get_username(self):
        return self.email


# Creating the unique access code
# models.py


# models.py
def client_photo_path(instance, filename):
    return f"cases/{instance.id}/client_photo/{filename}"


def case_document_path(instance, filename):
    return f"cases/{instance.case.id}/documents/{filename}"


class CourtCase(models.Model):
    # Unique Access Code
    access_code = models.CharField(max_length=12, unique=True, editable=False, default="")

    # Client Info
    client_name = models.CharField(max_length=100)
    client_tel = models.CharField(max_length=100)
    client_email = models.EmailField()
    client_address = models.TextField()
    client_dob = models.DateField(blank=True, null=True)
    next_of_kin = models.CharField(max_length=100, blank=True)
    client_photo = models.ImageField(upload_to=client_photo_path, blank=True, null=True)

    # Case Info
    case_title = models.CharField(max_length=200)
    case_number = models.CharField(max_length=100)
    case_description = models.TextField()
    court_name = models.CharField(max_length=100)
    trial_date = models.DateField()
    case_fee = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.access_code:
            self.access_code = uuid.uuid4().hex[:12].upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.case_title} - {self.client_name}"


class CaseDocument(models.Model):
    case = models.ForeignKey(CourtCase, on_delete=models.CASCADE, related_name='documents')
    file = models.FileField(upload_to=case_document_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class AccessCode(models.Model):
    code = models.CharField(max_length=12, unique=True, editable=False)
    case = models.ForeignKey(CourtCase, on_delete=models.CASCADE, related_name='access_codes')
    label = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = uuid.uuid4().hex[:12].upper()
        super().save(*args, **kwargs)

