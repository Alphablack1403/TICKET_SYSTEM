from django.test import TestCase
from django.urls import reverse
from ..models import Ticket, Comentario
from django.contrib.auth.models import User


class TicketTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="12345"
        )

    def test_crear_ticket(self):
        ticket = Ticket.objects.create(
            titulo="Test Ticket",
            descripcion="Descripción de prueba",
            categoria="General",
            prioridad="ALTA",
            estado="ABIERTO",
            usuario=self.user
        )

        self.assertEqual(ticket.titulo, "Test Ticket")
        self.assertEqual(ticket.estado, "ABIERTO")

    def test_agregar_comentario(self):
        ticket = Ticket.objects.create(
            titulo="Test Ticket",
            descripcion="Descripción",
            categoria="General",
            prioridad="MEDIA",
            estado="ABIERTO",
            usuario=self.user
        )

        comentario = Comentario.objects.create(
            descripcion="Comentario prueba",
            ticket=ticket,
            usuario=self.user
        )

        self.assertEqual(ticket.comentario_set.count(), 1)

    def test_cambiar_estado(self):
        ticket = Ticket.objects.create(
            titulo="Estado Test",
            descripcion="Desc",
            categoria="General",
            prioridad="BAJA",
            estado="ABIERTO",
            usuario=self.user
        )

        ticket.estado = "CERRADO"
        ticket.save()

        self.assertEqual(ticket.estado, "CERRADO")

    def test_filtro_por_estado(self):
        Ticket.objects.create(
            titulo="Abierto",
            descripcion="",
            categoria="General",
            prioridad="BAJA",
            estado="ABIERTO",
            usuario=self.user
        )

        Ticket.objects.create(
            titulo="Cerrado",
            descripcion="",
            categoria="General",
            prioridad="ALTA",
            estado="CERRADO",
            usuario=self.user
        )

        abiertos = Ticket.objects.filter(estado="ABIERTO")

        self.assertEqual(abiertos.count(), 1)
