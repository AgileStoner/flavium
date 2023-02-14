# myapp/tasks.py

# datetime
from datetime import datetime
from .models import Booking

def update_booking():
    now = datetime.now()
    bookings = Booking.objects.filter(end_time__lt=now, status="Accepted")
    bookings.update(status="Completed")
