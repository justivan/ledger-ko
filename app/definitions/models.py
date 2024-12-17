from django.db import models
from django.core.exceptions import ValidationError


class Currency(models.Model):
    code = models.CharField(max_length=3, primary_key=True, verbose_name="Currency Code")
    name = models.CharField(max_length=120, unique=True, verbose_name="Currency Name")

    class Meta:
        ordering = ("code",)
        verbose_name_plural = "Currencies"

    def __str__(self) -> str:
        return f"{self.code} - {self.name}"


class ExchangeRate(models.Model):
    source_currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        related_name="source_rates",
        verbose_name="Source Currency",
    )
    target_currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        related_name="target_rates",
        verbose_name="Target Currency",
    )
    rate = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        verbose_name="Exchange Rate",
    )
    date = models.DateField()

    class Meta:
        unique_together = ("source_currency", "target_currency", "date")
        verbose_name = "Exchange Rate"
        verbose_name_plural = "Exchange Rates"

    def __str__(self):
        return f"{self.source_currency.code} to {self.target_currency.code}"

    def clean(self):
        if self.source_currency == self.target_currency:
            raise ValidationError("Source and target currencies must be different.")
