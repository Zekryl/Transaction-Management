from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Transaction
from .models import Category
# from .models import Type
from app_User import models
from rest_framework import status
from django.conf import settings


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_transaction(request):
    user = request.user
    category_name = request.data['category']
    type_name = request.data['type']
    amount = request.data['amount']
    comment = request.data['comment']

    if type_name == "plus":
        user.balance = user.balance + amount
        user.save()
    elif type_name == "minus":
        user.balance = user.balance - amount
        user.save()
    else:
        return Response({'answer': 'failed', 'your_message:': f'Wrong transaction type'})

    transaction = Transaction(user=user,category=Category.objects.get(name=category_name),type=type_name,amount=amount,comment=comment)
    transaction.save()
    return Response({'answer': 'success', 'your_message:': f'Transaction with id: {transaction.id} is added'})

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def remove_transaction(request):
#     user = request.user
#     id = request.data['id']
#     transaction = Transaction.objects.filter(user=user).get(id=id)
#     transaction.delete()

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_transactions_list(request):
    user = request.user
    transactions = Transaction.objects.filter(user=user).values()
    return Response({'transactions': transactions})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_balance(request):
    user = request.user
    balance = user.balance
    return Response({'your_balance': f'Your balance: {balance}'})