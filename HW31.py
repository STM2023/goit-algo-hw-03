from datetime import datetime # Імпортуємо функцію, для роботи з датой
import re

def get_days_from_today(date):
     
     today = datetime.today().date()  #поточна дата
     try:
         date_n=datetime.strptime(date,"%Y-%m-%d").date() # введена дата
     except ValueError:
         print("Error!!! Введено невірні дані!")
     return  (today-date_n).days 




while True:
    date_string = input("Введіть дату у форматі 'РРРР-ММ-ДД' : ")
    match = re.search(r"(\d{4})-(\d{2})-(\d{2})", date_string)
    if match:
        date_year = int(match.group(1))
        date_month = int(match.group(2))
        date_day=int(match.group(3))
        print(" Рік = ", date_year)
        print(" Місяць= ", date_month)
        print(" День= ", date_day)
        if   0< date_month <=12 and 0<date_day<=31 : 
            if date_month in (1,3,5,7,8,10,12) and date_day<=31 or date_month in (4,6,9,11) and date_day<=30 or date_month ==2 and date_day<=29 and date_year%4==0 or  date_month ==2 and date_day<=28 and date_year%4!=0 :
                break

    print("----- Ви помилились та ввели :", date_string)
      
diff_date = get_days_from_today(date_string)
print(f"Різниця між поточною датою та заданою датою = {diff_date}")

