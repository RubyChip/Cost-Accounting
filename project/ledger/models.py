from django.db import models



class Budget(models.Model):
    budget_id = models.AutoField(verbose_name='Budget ID', primary_key=True)
    owner_phone = models.CharField(verbose_name='Owner phone', max_length=50)

    def __str__(self) -> str:
        return str(self.budget_id)


class Category(models.Model):
    CATEGORY_TYPES = (
        ('income', 'Income'),
        ('expenses', 'Expenses')
    )
    codename = models.CharField(verbose_name='Codename', max_length=255, primary_key=True)
    name = models.CharField(verbose_name='Category name', max_length=255)
    type = models.CharField(verbose_name='Category type', max_length=255, choices=CATEGORY_TYPES)

    def __str__(self) -> str:
        return f'{self.name} {self.type}'


class Ledger(models.Model):
    id = models.AutoField(verbose_name='Record ID', primary_key=True)
    budget_id = models.ForeignKey(Budget, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(verbose_name='Amount')
    description = models.TextField(verbose_name='Description', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Id: {self.budget_id} Category: {self.category_id} Amount: {self.amount}'
