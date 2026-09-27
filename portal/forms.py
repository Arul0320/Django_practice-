from django import forms
from .models import Student, ContactMessage
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "email", "age", "course"]
        
    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        existing = Student.objects.filter(email__iexact=email)
        
        if self.instance.pk:
            existing = existing.exclude(pk=self.instance.pk)
            
        if existing.exists():
            raise forms.ValidationError("This email is already registered.")
        
        return email
    
    def clean_age(self):
        age = self.cleaned_data["age"]
        
        if age < 16:
            raise forms.ValidationError("Student age must be 16 or above.")
        
        return age
    
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]
        
    def clean_subject(self):
        subject = self.cleaned_data["subject"].strip()
        
        if len(subject) < 3:
            raise forms.ValidationError("Subject must contain at least 3 characters.")
        
        return subject
