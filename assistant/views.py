
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from clientes.models import Cliente

# esta app será la que registrará a a los leads en el CRM y los clasificará. 
#Import Model of deals - 
#Create a function that receives the clients or  prospects from the chatbot - whatsapp 

@csrf_exempt  # Permite solicitudes sin token CSRF (útil para API)
def create_cliente(request):
    if request.method == 'POST':
        try:
                # Intentamos cargar los datos JSON enviados en la solicitud
            data = json.loads(request.body)
            print("1")
                # Creamos el nuevo cliente con los datos del JSON
            cliente = Cliente(
                        nombre=data.get('nombre'),
                        mail=data.get('mail'),
                        telefono=data.get('telefono'), 
                        empresa=data.get('empresa'),  # Campo de empresa como texto
                        posicion=data.get('posicion', 'Desconocido'),
                        etapa=data.get('etapa', 'inicial'),
                    )

                    # Guardamos el cliente
            cliente.save()
            print(cliente)
            print("2")

                    # Devolvemos una respuesta exitosa
            return JsonResponse({'message': 'Cliente created successfully!', 'id': cliente.id}, status=201)
                
        except json.JSONDecodeError:
                    # Si no se pudo parsear el JSON, devolvemos un error
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    else:
                # Si el método no es POST, devolvemos un error
        return JsonResponse({'error': 'Invalid request method'}, status=405)
