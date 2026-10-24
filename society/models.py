from django.db import models

class SocietyRecord(models.Model):
    """Flexible storage for records added while migrating legacy JSP screens."""
    category = models.CharField(max_length=80, db_index=True)
    title = models.CharField(max_length=200, blank=True)
    details = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.category}: {self.title}"
