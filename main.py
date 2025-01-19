from datetime import datetime

def get_discord_registration_date(user_id):
    try:
        user_id = int(user_id.strip())  # Удаляем лишние пробелы и конвертируем в число
        timestamp_ms = (user_id >> 22) + 1420070400000
        timestamp_s = timestamp_ms / 1000
        date = datetime.fromtimestamp(timestamp_s)
        return date
    except:
        return None

# Читаем ID из файла
try:
    with open('id.txt', 'r') as file:
        ids = file.readlines()
except FileNotFoundError:
    print("Ошибка: Файл id.txt не найден!")
    exit()

# Открываем файл для записи результатов
with open('results.txt', 'w', encoding='utf-8') as results_file:
    print("\nДаты регистрации аккаунтов:")
    
    for discord_id in ids:
        if discord_id.strip():  # Проверяем, что строка не пустая
            date = get_discord_registration_date(discord_id)
            
            if date:
                # Вывод в консоль
                print(f"{discord_id.strip()} : {date}")
                
                # Запись в файл только даты в нужном формате
                results_file.write(f"{date.strftime('%d.%m.%Y')}\n")

print("\nРезультаты сохранены в файл results.txt")