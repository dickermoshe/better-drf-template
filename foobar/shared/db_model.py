from django.db import models


class BaseDjangoModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs) -> None:
        for field in self._meta.fields:
            if isinstance(field, models.Field):
                value = getattr(self, field.name)
                if value == "":
                    setattr(self, field.name, None)
        return super().save(*args, **kwargs)
