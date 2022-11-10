"""
Создать и вывести с помощью print() список который будет хранить данные о пользователе которые хранятся в словаре base:
login, avatar, email, phone, gdpr_data, loss_limit_amount.
ответ в формате: ['Test_login', 'banana', 1000]

Создать и вывести с помощью print() словарь который будет хранить ключи со значениями.
ключи: login, avatar, email, phone, gdpr_data, loss_limit_amount.
ответ в формате: {'login': 'Test_login', 'loss_limit_amount': 1000}
только перечисленные ключи должны быть в словаре
Выполняем задание теми средствами которые вчера прошли.
если у кого то есть опыт работы с циклами, можно сделать и прислать мне как альтернативное решение
"""

base = {
    "login": "Test_login",
    "password": "Yurec1989",
    "retype": "Yurec1989",
    "accept": True,
    "avatar": "banana",
    "address": "asqdrrrr",
    "birthday": "1989-01-10",
    "city": "sdaddqddd",
    "country": "FI",
    "currency": "EUR",
    "email": "WERTYrU@ASDFffqaffrfff",
    "gdpr_data": True,
    "gdpr_marketing": True,
    "gender": "M",
    "name": "sdfghffaffrff",
    "phone": 380529876025,
    "postcode": 12345643245,
    "product": "test",
    "surname": "uoieccccccccac",
    "trigger_codes": "casino-welcome-bonus",
    "qa": {},
    "birth_country": "DE",
    "nationality": "DE",
    "birth_name": "dasdasda",
    "birth_place": "Bavaria",
    "loss_limit": {"amount": 1000, "period": "week"},
}

a = ["login", "avatar", "email", "phone", "gdpr_data", "amount"]
user_data = list()
user_base_new = {}

for x, y in base.items():
    if x in a:
        user_data.append(y)
        user_base_new.update({x: y})
    if isinstance(y, dict):
        k = base.get(x)
        for i, b in k.items():
            if i in a:
                user_data.append(b)
                user_base_new.update({i: b})
print(user_data)
print(user_base_new)


