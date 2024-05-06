from django.db import models


class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('Request Pending', 'Request Pending'),
        ('Request Resolved', 'Request Resolved'),
    ]

    TYPE_CHOICES = [
        ('New Connection', 'New Connection'),
        ('Installation', 'Installation'),
        ('Repair', 'Repair'),
        ('Inspection', 'Inspection'),
        ('Booking', 'Booking')
    ]
    requestdate_in_local=models.DateTimeField(null=True,blank=True)
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
    type = models.CharField(max_length=30, choices=TYPE_CHOICES, default='New Connection')
    description = models.TextField()
    status = models.CharField(max_length=30,choices=STATUS_CHOICES, default='Request Pending')
    attachment = models.FileField(upload_to='service_request_attachments/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.customer.username + ' - ' + self.type+ ' - ' + self.status 
    

