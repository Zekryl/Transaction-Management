# Transaction-Management

API URLS:

http://127.0.0.1:8000/user/register/
http://127.0.0.1:8000/user/token/
http://127.0.0.1:8000/user/token-refresh/

http://127.0.0.1:8000/transactions/add
POST
{
    "category" : "food" (добавлять новые категории через админ панель),
    "type" : "plus/minus",
    "amount" : "1000",
    "comment": "Comment example"
}
http://127.0.0.1:8000/transactions/balance
GET
http://127.0.0.1:8000/transactions/list
GET
