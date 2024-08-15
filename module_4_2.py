def test_function(): # 1
    def inner_function(): # 2
        print("Я в области видимости функции test_function")

    inner_function() # 3 здесь не возвращает

inner_function() # ошибка
# Вызов inner_function() вне test_function приводит к появлению ошбики -
# NameError: name 'inner_function' is not defined
# вследствие различия пространства имён, т.к. мы не можем доставать значения внутри функции

test_function() # Здесь - работает :-)