import bcrypt
import io
from PIL import Image
from django.core.files.base import ContentFile
from django.db import models


class Complaint(models.Model):
    CATEGORY_CHOICES = [
        ('tiffin', 'Tiffin Theft'),
        ('bribe', 'Bribes'),
        ('syllabus', 'Syllabus Bloat'),
        ('other', 'Other'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    evidence_image = models.ImageField(upload_to='evidence/', blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_verified_strike = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.category} - {self.submitted_at.strftime('%d %b %Y')}"

    def save(self, *args, **kwargs):
        if self.evidence_image:
            self.evidence_image = self._strip_exif(self.evidence_image)
        super().save(*args, **kwargs)

    def _strip_exif(self, image_field):
        """
        Evidence Metadata Stripping: EXIF data (timestamp, GPS location,
        camera signature) remove kore, jate whistleblower er identity
        accidentally leak na hoy.
        """
        img = Image.open(image_field)
        img_format = img.format or 'JPEG'

        # Notun image toiri kori without EXIF (pixel data copy kore)
        data = list(img.getdata())
        clean_img = Image.new(img.mode, img.size)
        clean_img.putdata(data)

        buffer = io.BytesIO()
        clean_img.save(buffer, format=img_format)
        buffer.seek(0)

        return ContentFile(buffer.read(), name=image_field.name)


class RollNumberHash(models.Model):
    hashed_roll = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def hash_roll(roll_number: str, salt: bytes = None):
        if salt is None:
            salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(roll_number.encode(), salt)
        return hashed.decode()

    @staticmethod
    def verify_roll(roll_number: str, hashed: str) -> bool:
        return bcrypt.checkpw(roll_number.encode(), hashed.encode())