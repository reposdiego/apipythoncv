from django import forms


class formulario_laboral(forms.Form):
      
    nombre=forms.CharField(label='Nombre del proyecto', required=True)

    link = forms.URLField(label='link  del proyecto' , required= True) 

    Tecnologia = forms.CharField(label='Tecnologia utilizada' , required= True)

    descripcion = forms.CharField(label=' descripcion proyecto', widget=forms.Textarea)