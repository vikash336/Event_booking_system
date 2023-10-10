from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class EventOrganizersManager(BaseUserManager):
    def create_user(self, email, name, tc, password=None, password2=None):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            tc=tc,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, tc, password=None):
        """
        Creates and saves a superuser with the given email, name, tc and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            tc=tc,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class EventOrganizers(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    groups = models.ManyToManyField(Group, related_name='event_organizers_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='event_organizers_user_permissions', blank=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = EventOrganizersManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if self._state.adding:  # Check if it's a new user
            self.set_password(self.password)
        super().save(*args, **kwargs)

class Customers(AbstractUser):
    email = models.EmailField(unique=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    date_joined = models.DateTimeField(default=timezone.now)
    groups = models.ManyToManyField(Group, related_name='customers_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='customers_user_permissions')
    def __str__(self):
        return self.email

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    venue = models.CharField(max_length=100)
    organizer = models.ForeignKey(EventOrganizers, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class TicketType(models.Model):
    name = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ticket_types = models.ManyToManyField(TicketType)

    def __str__(self):
        return f"Booking for {self.event.name} by {self.customer.name}"
