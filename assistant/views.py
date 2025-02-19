from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from clientes.models import Cliente
from twilio.twiml.messaging_response import MessagingResponse

# esta app será la que registrará a a los leads en el CRM y los clasificará. 
#Import Model of deals - 
#Create a function that receives the clients or  prospects from the chatbot - whatsapp 

@csrf_exempt  # Permite solicitudes sin token CSRF (útil para API)
def chatbot(request):
    if request.method == "POST":
        from_number = request.POST.get('From')  # Número de WhatsApp del usuario
        user_response = request.POST.get('Body')  # Respuesta del usuario
        profile_name = request.POST.get("ProfileName", "").strip()  # Obtener nombre de perfil de Whats>
        to_number=request.POST.get('To')

        twilio_response = MessagingResponse() 

            
        

        # Enviar la respuesta a WhatsApp
        
        twilio_response.message("Bienvenido a Nuplee, puedes preguntarme acerca de chatbots o agendar una llamada con un agente humano")
        return HttpResponse(str(twilio_response), content_type='application/xml')

    return HttpResponse("Method Not Allowed", status=405)
