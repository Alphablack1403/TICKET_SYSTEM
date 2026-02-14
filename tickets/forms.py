from django import forms
from .models import Ticket, Comentario

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ['usuario']
        fields = [
            'titulo',
            'descripcion',
            'categoria',
            'prioridad',
            'estado'
        ]
        
class TicketUpdateFormUsuario(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['titulo', 'descripcion', 'categoria', 'prioridad']

class TicketUpdateFormAdmin(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['estado']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['descripcion']

