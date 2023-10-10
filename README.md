# Transaction-Management
<br />
API URLS:<br />
<br />
http://127.0.0.1:8000/user/register/<br />
http://127.0.0.1:8000/user/token/<br />
http://127.0.0.1:8000/user/token-refresh/<br />
<br />
http://127.0.0.1:8000/transactions/add<br />
POST<br />
{<br />
    "category" : "food" (добавлять новые категории через админ панель),<br />
    "type" : "plus/minus",<br />
    "amount" : "1000",<br />
    "comment": "Comment example"<br />
}<br />
http://127.0.0.1:8000/transactions/balance<br />
GET<br />
http://127.0.0.1:8000/transactions/list<br />
GET<br />
