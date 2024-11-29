from celery import shared_task
from django.utils.timezone import now, timedelta
from .models import Request
from apps.users.models import UserProfile

@shared_task
def deduct_balance():
    # 1 kun oldin yaratilgan so'rovlarni toping
    time_threshold = now() - timedelta(days=1)
    requests = Request.objects.filter(created__lte=time_threshold, is_active=True)

    for req in requests:
        user = req.user
        if user.balance >= 5000:  # Faqat balans yetarli bo'lsa
            user.balance -= 5000
            user.save()
