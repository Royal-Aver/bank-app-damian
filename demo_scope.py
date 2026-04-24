# demo_scope.py — демонстрация областей видимости

bank_name = "🏦 Банк 'Ученик'"  # глобальная

def show_bank_name():
    print(f"Внутри функции: {bank_name}")  # читаем глобальную

def try_to_change():
    bank_name = "Новый банк"  # создаётся ЛОКАЛЬНАЯ!
    print(f"Локальная внутри: {bank_name}")

def really_change():
    global bank_name
    bank_name = "Обновлённый банк"  # меняем глобальную
    print(f"Глобальная изменена на: {bank_name}")

# Проверяем
print(f"Глобальная в начале: {bank_name}")
show_bank_name()
try_to_change()
print(f"Глобальная после try_to_change: {bank_name}")
really_change()
print(f"Глобальная после really_change: {bank_name}")