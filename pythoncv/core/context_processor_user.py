from datetime import datetime
#decorador
from curriculum.models import habilidades,tecnologias,proyectos_laborales,experiencia_laboral,Estudios,hobbies 
#modelos


#procesador de contexto para calcular edad:

def age_processor(request):
     if request.user.is_authenticated:
        usuario = request.user
        fecha_nacimiento = usuario.birthday
        try:
            if datetime.now().month <= fecha_nacimiento.month and datetime.now().day <= fecha_nacimiento.day:
                # Si el mes y el día actual es menor o igual al del nacimiento
                edad = (datetime.now().year-1) - fecha_nacimiento.year
            else:
                edad = datetime.now().year - fecha_nacimiento.year
        except:
            edad = 'No es posible calcular la edad'

        return {
                "edad": edad,
                "usuario" : usuario
                }
     else:
        return { 'mensaje': 'Usuario no conectado' }
     
# Procesador de contexto para las habilidades:

#@login_required()
def habilidad_procesor(request):
    # Query para traer todos los skills del usuario:
    user_habilidad = habilidades.objects.filter(user=request.user)
    return {
            "habilidad_user": user_habilidad
            }



