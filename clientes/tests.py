from django.test import TestCase
from django.contrib.auth.models import User
from empresas.models import Empresa  # Asegúrate de que el modelo Empresa esté bien importado
from .models import Cliente  # Importamos el modelo Cliente

class ClienteModelTest(TestCase):

    def setUp(self):
        """Crea los objetos necesarios para las pruebas."""
        # Crear un usuario para la relación ManyToManyField
        self.user1 = User.objects.create_user(username='usuario1', password='12345')
        self.user2 = User.objects.create_user(username='usuario2', password='12345')

        # Crear una empresa para la ForeignKey
        self.empresa = Empresa.objects.create(nombre='Empresa Test')

        # Crear un cliente de prueba
        self.cliente = Cliente.objects.create(
            nombre="Cliente Test",
            mail="cliente@test.com",
            telefono="1234567890",
            empresa=self.empresa,
            posicion="Gerente",
            etapa="inicial"
        )
        self.cliente.encargado_cuenta.add(self.user1, self.user2)

    def test_cliente_str(self):
        """Prueba la representación en cadena (__str__) del modelo Cliente."""
        self.assertEqual(str(self.cliente), "Cliente Test - inicial")

    def test_cliente_etapas(self):
        """Prueba las diferentes etapas del cliente."""
        etapas = dict(Cliente.ETAPAS)
        self.assertIn(self.cliente.etapa, etapas)

    def test_cliente_email_valido(self):
        """Prueba que el campo email sea válido."""
        self.assertEqual(self.cliente.mail, "cliente@test.com")

    def test_relacion_empresa(self):
        """Prueba que la relación ForeignKey con Empresa funcione correctamente."""
        self.assertEqual(self.cliente.empresa, self.empresa)

    def test_relacion_encargado_cuenta(self):
        """Prueba la relación ManyToManyField con User."""
        self.assertEqual(self.cliente.encargado_cuenta.count(), 2)
        self.assertIn(self.user1, self.cliente.encargado_cuenta.all())
        self.assertIn(self.user2, self.cliente.encargado_cuenta.all())

    def test_actualizar_etapa(self):
        """Prueba que se pueda actualizar la etapa de un cliente."""
        self.cliente.etapa = 'seguimiento'
        self.cliente.save()
        self.assertEqual(self.cliente.etapa, 'seguimiento')
