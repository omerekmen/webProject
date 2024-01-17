from django.shortcuts import render, redirect
from .models import *
from members.models import Member
from django.contrib.auth.decorators import login_required

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
