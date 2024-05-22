from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
import re #Para validar el RUT ya que manipula cadenas basandose en patrones espcificos


    
def validate_not_all_numeric(value):
    if value.isdigit():
        raise ValidationError(
            'La contraseña no puede ser completamente numérica.',
            params={'value': value},
        )




#Modelo del formulario
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=20,
        label='Nombre de usuario',
        error_messages={
            'required': 'Este campo es requerido.',
            'max_length': 'El nombre de usuario debe tener un máximo de 20 caracteres.',
        },
        widget=forms.TextInput(attrs={'placeholder': 'ej: amantedeperros1234'})
    )
    first_name = forms.CharField(
        max_length=50,
        label='Nombre/s',
        error_messages={
            'required': 'Este campo es requerido.',
            'max_length': 'El nombre debe tener un máximo de 50 caracteres.',
        },
        widget=forms.TextInput(attrs={'placeholder': 'ej: Juan'})
    )
    last_name = forms.CharField(
        max_length=50,
        label='Apellido/s',
        error_messages={
            'required': 'Este campo es requerido.',
            'max_length': 'Los apellidos deben tener un máximo de 50 caracteres.',
        },
        widget=forms.TextInput(attrs={'placeholder': 'ej: Perez Garcia'})
    )
    email = forms.EmailField(
        max_length=80,
        label='Correo electrónico',
        validators=[EmailValidator(message="Debe ser una dirección de correo electrónico válida.")],
        widget=forms.EmailInput(attrs={'placeholder': 'ej: correo@gmail.com'})
    )
    rut = forms.CharField(
        max_length=12,
        error_messages={
            'required': 'Este campo es requerido.',
            'max_length': 'El RUT debe tener un máximo de 9 caracteres.',
        },
    )
    password1 = forms.CharField(
        label='Contraseña',
        validators=[validate_not_all_numeric],
        widget=forms.PasswordInput,

    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        validators=[validate_not_all_numeric],
        widget=forms.PasswordInput,

    )
    
    
    # Se define o se especifica el formulario el modelo de datos que se utilizara y los campos, formulario django
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email','rut','phone_number', 'password1', 'password2']

    # Este método se ejecuta cuando se crea una instancia del formulario
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].label = "Número de celular"
        self.fields['phone_number'].widget.attrs.update({'placeholder': 'ej: +56912345678'})

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if CustomUser.objects.filter(rut=rut).exists():
            raise ValidationError("Este RUT ya está en uso.")
        return rut
    #Valida campo rut
    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        pattern = r'^\d{1,2}\.\d{3}\.\d{3}-[\dkK]$'        
        if not re.match(pattern, rut):
            raise ValidationError("El RUT debe estar en el formato correcto (XX.XXX.XXX-X).")
        if CustomUser.objects.filter(rut=rut).exists():
            raise ValidationError("Este RUT ya está en uso.")
        return rut
    
    #Validar campo first_name
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        # Transforma la primera letra de cada palabra a mayúscula
        first_name = ' '.join(word.capitalize() for word in first_name.split())
        return first_name

    #Lo mismo
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        # Transforma la primera letra de cada palabra a mayúscula
        last_name = ' '.join(word.capitalize() for word in last_name.split())
        return last_name
    
    #email = forms.EmailField()
    #Lo mismin
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Este correo electrónico ya está en uso.")
        return email
    





