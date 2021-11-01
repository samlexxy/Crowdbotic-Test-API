from django.db import models
from django.contrib.auth.models import User
# from django.db.models.fields import CharField
# from django.db.models.fields.related import OneToOneField

# Create your models here.

class Plan(models.Model):
    SUBSCRIPTIONS = (
        ('Free', 'Free ($0.00)'),
        ('Standard', 'Standard ($10.00)'),
        ('Pro', 'Pro ($25.00)')
    )
    """
    FREE = $0.00
    STANDARD = $10.00
    PRO = $25.00 
    """

    name = models.CharField(max_length=20, choices=SUBSCRIPTIONS)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    # type = models.CharField(max_length=8, choices=SUBSCRIPTIONS)
    # app = models.OneToOneField(App, on_delete=models.CASCADE)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        types = {
            "Free": 0,
            "Standard": 10.00,
            "Pro": 25.00
        }
        self.price = types[self.name]
        super(Plan, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class App(models.Model):
    TYPES = (
        ('Web', 'Web'),
        ('Mobile', 'Mobile')
    )

    FRAMEWORKS = (
        ('Django', 'Django'),
        ('React Native', 'React Native')
    )

    name = models.CharField(max_length=50)
    description = models.TextField()
    type = models.CharField(max_length=7, choices=TYPES)
    framework = models.CharField(max_length=15, choices=FRAMEWORKS)
    domain_name = models.CharField(max_length=50)
    screenshot = models.URLField(blank=True, null=True)
    # subscription = models.OneToOneField(Subscription, models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='app')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='subscription')
    plan = models.OneToOneField(Plan, on_delete=models.PROTECT, related_name='subscription')
    app = models.OneToOneField(App, on_delete=models.PROTECT, related_name='subscription')
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


