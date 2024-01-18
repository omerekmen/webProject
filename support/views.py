from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_POST
from .models import *
from members.models import Member
from django.http import JsonResponse 

@login_required
def create_support_ticket(request):
    if request.method == 'POST':
        category = request.POST['category']
        subject = request.POST['subject']
        title = request.POST['title']
        description = request.POST['description']
        uploaded_file = request.FILES.get('fileUpload')
        member = Member.objects.get(member_id=request.user.member_id)

        support_ticket = SupportTicket.objects.create(
            member=member,
            title=title,
            category=category,
            subject=subject,
        )

        support_ticket_message = SupportMessage.objects.create(
            ticket=support_ticket,
            sender=member,
            message=description,
            file=uploaded_file
        )

        return redirect('/account/#support') 

    return render(request, 'chat-box.html')

@permission_required('support.view_supportticket')
def support_response_view(request, ticket_id):
    ticket = SupportTicket.objects.get(ticket_id=ticket_id)
    messages = SupportMessage.objects.filter(ticket=ticket)
    context = {
        'ticket': ticket,
        'messages': messages,
    }
    return render(request, 'admin/support/support_response.html', context)


@permission_required('support.change_supportticket')
def admin_message_response(request, ticket_id):
    ticket = get_object_or_404(SupportTicket, ticket_id=ticket_id)
    message = SupportMessage.objects.filter(ticket=ticket)

    if request.method == 'POST':
        response_text = request.POST.get('response')
        response_file = request.FILES.get('validatedCustomFile')
        response_checkbox = request.POST.get('close_ticket')
        
        new_message = SupportMessage.objects.create(
            ticket=ticket,
            sender=request.user,
            message=response_text,
            file=response_file,
        )

        if response_checkbox == 'close':
            ticket.status = 'CLOSED'
            ticket.save()

        messages.success(request, 'Yanıtınız başarıyla oluşturuldu.')

        return redirect(reverse('admin:support_supportticket_changelist'))

    context = {
        'ticket': ticket,
        'messages': message,
    }
    return render(request, 'admin/support/support_response.html', context)

@login_required
def post_chat_message(request):
    if request.method == 'POST':
        ticket_id = request.POST.get('ticket_id')
        message_text = request.POST.get('message')
        uploaded_file = request.FILES.get('file')

        # Fetch the SupportTicket instance
        try:
            ticket = SupportTicket.objects.get(ticket_id=ticket_id)
        except SupportTicket.DoesNotExist:
            # Handle the case where the ticket does not exist
            return JsonResponse({'status': 'error', 'message': 'Ticket not found'}, status=404)

        member = Member.objects.get(member_id=request.user.member_id)

        support_message = SupportMessage.objects.create(
            ticket=ticket,  # Assign the SupportTicket instance here
            sender=member,
            message=message_text,
            file=uploaded_file
        )

        # Return a success response
        return JsonResponse({'status': 'success'})

