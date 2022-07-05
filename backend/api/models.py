from django.db import models
from django.utils.translation import gettext_lazy as _


class Client(models.Model):
    name = models.CharField(
        verbose_name=_("Название клиента"),
        unique=True,
        max_length=200,
    )

    class Meta:
        ordering = ['name']
        verbose_name = _('Клиент')
        verbose_name_plural = _('Клиенты')

    def __str__(self):
        return self.name


class ClientOrganization(models.Model):
    client_name = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="client_organizations",
        verbose_name=_("Название клиента"),
    )
    name = models.CharField(
        verbose_name=_("Организация клиента"),
        max_length=200,
    )
    address = models.CharField(
        verbose_name=_("Адрес"),
        max_length=200,
    )
    fraud_weight = models.PositiveIntegerField(
        verbose_name=_("Мошенничество"),
        default=0
    )

    class Meta:
        ordering = ['client_name']
        verbose_name = _('Организация клиента')
        verbose_name_plural = _('Организации клиента')
        constraints = [
            models.UniqueConstraint(
                fields=["client_name", "name"],
                name="unique_client_organizations",
            )
        ]

    def __str__(self):
        return self.name


class Bill(models.Model):
    client_name = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="bills",
        verbose_name=_("Имя клиента"),
    )
    client_org = models.ForeignKey(
        ClientOrganization,
        on_delete=models.CASCADE,
        related_name="bills",
        verbose_name=_("Имя организации клиента"),
    )
    order_number = models.PositiveIntegerField(
        verbose_name=_("№"),
    )
    sum = models.FloatField(
        verbose_name=_("Сумма"),
    )
    date = models.DateField(
        verbose_name=_("Дата"),
    )
    service = models.CharField(
        verbose_name=_("Услуга"),
        max_length=200,
    )
    fraud_score = models.FloatField(
        verbose_name=_("Случайное значение"),
    )
    service_class = models.PositiveIntegerField(
        verbose_name=_("Класс сервиса"),
    )
    service_name = models.CharField(
        verbose_name=_("Название сервиса"),
        max_length=200,
    )

    class Meta:
        ordering = ['client_name']
        verbose_name = _('Счет')
        verbose_name_plural = _('Счета')
        constraints = [
            models.UniqueConstraint(
                fields=["client_org", "order_number"],
                name="unique_bill_client_org",
            )
        ]

    def __str__(self):
        return f"{self.client_org} - {self.order_number}"
