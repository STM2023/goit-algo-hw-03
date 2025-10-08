
import re # імпортуємо модуль для роботи з регулярними виразами 



def normalize_phone(raw_numbers) :
        
    formatted_phone= re.sub(r"[^\d+]", r"",raw_numbers)  # Видаляємо всі символи, крім цифр і "+"
    #print(formatted_phone)
        # перевіряемо що рядок починається з підрядка 
    if not formatted_phone.startswith("+"):      # Якщо номер не має знаку "+" 
        if formatted_phone.startswith("38"):          # Якщо номер маэ код "38"
            formatted_phone = "+" + formatted_phone    #— додаємо знак "+"
        else :
            formatted_phone = "+38" + formatted_phone    #иначе— додаємо український код "+38"
    #print(formatted_phone)
         
        
    return formatted_phone



raw_number = input("Введіть номер телефону : ")

sanitized_number = normalize_phone(raw_number) 
print("Нормалізований номер телефону для SMS-розсилки:", sanitized_number)

