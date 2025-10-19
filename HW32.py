from random import randint # Імпортуємо функцію, для генерування числа

def get_numbers_ticket(min, max, quantity) :

    numbers=[]
    if 1>min or min >1000:
        print(f"------Введено невірне значення min= {min}")
        return numbers
    if min>max or max >1000:
        print(f"------Введено невірне значення max= {max}")
        return numbers
    if 0>=quantity or quantity >max:
        print(f"------Введено невірне значення quantity= {quantity}")
        return numbers    
    k=0
    while k< quantity :
        k +=1
        goal = randint(min, max) # генеруємо число від min до max
        numbers.append(goal)  
    print(f"список до сортування та перевірки на унікальність {numbers}")
   
    len_numbers=len(numbers) # длина списка
    m_numbers=set(numbers)  # перетворэмо список у множину  
    m_len=len(m_numbers)    # длина множини
    numbers=list(m_numbers) # перетвор знову множину  у список 
    numbers.sort()     
    print(f"список після перетворення у множину та після сортування  {numbers}")
    if len_numbers!=m_len : 
        numbers=[]          # не уникальные элементы-формируем пустой список
    return numbers



min=int(input(' Введіть min- мінімальне можливе число у наборі (не менше 1 але менше 1000) : '))

max=int(input(f" Введіть max- максимальне можливе число у наборі (не більше 1000) але більше за min= {min} : " ))
 
quantity=int(input(f'Введіть  кількість чисел, які потрібно вибрати  : '))


lottery_numbers = get_numbers_ticket(min, max, quantity)
print("Ваші унікальні лотерейні числа:", lottery_numbers)