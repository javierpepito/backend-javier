from django import forms
from .models import Producto

class ProductoForm(forms.Modelform):
    class Meta:
        model = Producto
        fields = ["nombre", "descripcion", "precio", "stock"]