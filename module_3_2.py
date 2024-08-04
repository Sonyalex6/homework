def send_email(message,recipient,sender = "univerity.help@gmail.com"):
    if("@"and(".com"or".ru"or".net")) not in (recipient or sender) or("@" or(".com"or"ru"or".net")) not in (recipient or sender):
        print(f"Невозможно отправить письмо с адреса {sender}на адрес {recipient}")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса{sender} на адрес {recipient}.")
    elif sender !="university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
        send_email('messagje','university.help@mail.com','@.com')
        send_email('messagje','university.help@mail.com')
        send_email('messagje','universi@.com')
        send_email('messagje','universi@.co')
        send_email('messagje','universi@.com')