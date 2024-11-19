from django.shortcuts import render
from .models import Table, Booking
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

def home(request):
    return render(request, 'reservations/home.html')

def booking(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        table_id = request.POST['table']
        date = request.POST['date']
        time = request.POST['time']
        
        table = Table.objects.get(id=table_id)
        booking = Booking(name=name, email=email, phone=phone, table=table, date=date, time=time)
        booking.save()

        messages.success(request, "Your booking was successful!")
        return redirect('home')

def booking(request):
    tables = Table.objects.all()  # Ensure tables are fetched
    return render(request, 'reservations/booking.html', {'tables': tables})

def user_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'reservations/user_bookings.html', {'bookings': bookings})

def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.delete()
    messages.success(request, "Booking canceled successfully.")
    return redirect('user_bookings')


def logout_view(request):
    logout(request)  # Logs out the user
    messages.success(request, "You have successfully logged out.")  # Optional feedback
    return redirect('login')  # Redirect to the login page

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect('home')  # Redirect to homepage or another page
        else:
            messages.error(request, "Invalid credentials. Please try again.")
    return render(request, 'reservations/login.html')




