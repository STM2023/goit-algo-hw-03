from random import randint # Імпортуємо функцію, для генерування числа

def get_numbers_ticket(min, max, quantity) :
    numbers=[]
    k=0
    while k< quantity :
        k +=1
        goal = randint(min, max) # генеруємо число від min до max
        numbers.append(goal)  
    #print(f"список до сортування та перевірки на унікальність {numbers}")
   
    len_numbers=len(numbers) # длина списка
    m_numbers=set(numbers)  # перетворэмо список у множину  
    m_len=len(m_numbers)    # длина множини
    numbers=list(m_numbers) # перетвор знову множину  у список 
    numbers.sort()     
    #print(f"список після сортування  {numbers}")
    if len_numbers!=m_len : 
        numbers=[]          # не уникальные элементы-формируем пустой список
    return numbers


while True :
    min=int(input('Введіть min- мінімальне можливе число у наборі (не менше 1 але менше 1000) : '))
    if 1<=min<1000:
        break 
    else:
        print(f"------Ви помилились та ввели min= {min}")
while True :
    max=int(input(f"Введіть max- максимальне можливе число у наборі (не більше 1000) але більше за min= {min} : " ))
    if min< max <=1000:
        break 
    else:
        print(f"------Ви помилились та ввели max= {max}")    

while True :       
    quantity=int(input(f'Введіть  кількість чисел, які потрібно вибрати (значення між {min} і {max}) : '))
    if min< quantity< max:
        break 
    else:
        print(f"------Ви помилились та ввели quantity= {quantity}")  

lottery_numbers = get_numbers_ticket(min, max, quantity)
print("Ваші унікальні лотерейні числа:", lottery_numbers)