from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket
from .forms import TicketForm, ComentarioForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .forms import TicketUpdateFormUsuario, TicketUpdateFormAdmin
from django.db.models import Q

@login_required
def ticket_list(request):

    if request.user.groups.filter(name='Administrador').exists():
        tickets = Ticket.objects.all()
    else:
        tickets = Ticket.objects.filter(usuario=request.user)

    # Obtener parámetros GET
    estado = request.GET.get('estado')
    prioridad = request.GET.get('prioridad')
    categoria = request.GET.get('categoria')

    # Aplicar filtros si existen
    if estado:
        tickets = tickets.filter(estado=estado)

    if prioridad:
        tickets = tickets.filter(prioridad=prioridad)

    if categoria:
        tickets = tickets.filter(categoria__icontains=categoria)

    # Orden recomendado (mejora profesional)
    tickets = tickets.order_by('-updated_at')

    return render(request, 'tickets/ticket_list.html', {
        'tickets': tickets,
        'estado_actual': estado,
        'prioridad_actual': prioridad,
        'categoria_actual': categoria,
        'estados': Ticket.Estado.choices,
        'prioridades': Ticket.Prioridad.choices
    })

@login_required
def ticket_detail(request, pk):

    ticket = get_object_or_404(Ticket, pk=pk)

    es_admin = request.user.groups.filter(name='Administrador').exists()

    if not es_admin and ticket.usuario != request.user:
        raise PermissionDenied

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.ticket = ticket
            comentario.usuario = request.user
            comentario.save()
            return redirect('ticket_detail', pk=pk)
    else:
        form = ComentarioForm()

    comentarios = ticket.comentarios.select_related('usuario').all().order_by('fecha_registro')

    return render(request, 'tickets/ticket_detail.html', {
        'ticket': ticket,
        'comentarios': comentarios,
        'form': form,
        'es_admin': es_admin
    })



@login_required
def ticket_create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.usuario = request.user
            ticket.save()
            return redirect('ticket_list')
    else:
        form = TicketForm()
    return render(request, 'tickets/ticket_form.html', {'form': form})


@login_required
def ticket_update(request, pk):

    ticket = get_object_or_404(Ticket, pk=pk)

    es_admin = request.user.groups.filter(name='Administrador').exists()

    # Usuario normal solo puede editar sus tickets
    if not es_admin and ticket.usuario != request.user:
        raise PermissionDenied

    FormClass = TicketUpdateFormAdmin if es_admin else TicketUpdateFormUsuario

    if request.method == 'POST':
        form = FormClass(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('ticket_list')
    else:
        form = FormClass(instance=ticket)

    return render(request, 'tickets/ticket_form.html', {'form': form})

@login_required
def ticket_delete(request, pk):

    ticket = get_object_or_404(Ticket, pk=pk)

    # Si no es administrador, solo puede eliminar sus propios tickets
    if not request.user.groups.filter(name='Administrador').exists():
        if ticket.usuario != request.user:
            raise PermissionDenied

    if request.method == 'POST':
        ticket.delete()
        return redirect('ticket_list')

    return render(request, 'tickets/ticket_confirm_delete.html', {'ticket': ticket})

@login_required
def ticket_reopen(request, pk):

    ticket = get_object_or_404(Ticket, pk=pk)

    # Solo el dueño o admin puede reabrir
    es_admin = request.user.groups.filter(name='Administrador').exists()

    if not es_admin and ticket.usuario != request.user:
        raise PermissionDenied

    if ticket.estado == Ticket.Estado.CERRADO:
        ticket.estado = Ticket.Estado.ABIERTO
        ticket.save(update_fields=['estado', 'updated_at'])

    return redirect('ticket_detail', pk=pk)

