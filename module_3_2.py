def send_email(message, recipient, *, sender="university.help@gmail.com"):
    a = False
    b = False
    c = False
    global sender_
    if sender_1 != '':
        sender = sender_1
    if '@' in sender and '@' in recipient:
        a = True
    if sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net'):
        b = True
    if recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net'):
        c = True
    if a == False or b == False or c == False:
        print(f'Невозможно отправить письмо с адреса: {sender} на адрес: {recipient}')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса: {sender} на адрес: {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса: {sender} на адрес: {recipient}')
recipient = input('Введите адрес получателя: ')
message = input('Введите адрес текст сообщения:')
sender_1 = input('Введите адрес отправителя или нажмите ENTER для адреса по умолчанию: ')
print('*************************************')
print()

send_email(message, recipient)
