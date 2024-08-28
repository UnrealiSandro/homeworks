#1
def check_odd_or_even():
    
    number = int(input("gtoxvt sheiyvanet ricxvi: "))
    
    if number % 2 == 0:
        print(f"ricxvi {number} aris luwi.")
    else:
        print(f"ricxvi {number} aris kenti.")

check_odd_or_even()


#2
def check_positive_or_negative():
    number = float(input("gtxovt sheiyvanet ricxvi: "))
    
    if number > 0:
        print(f"ricxvi {number} aris positiuri.")
    elif number < 0:
        print(f"ricxvi {number} aris negatirui.")
    else:
        print(f"ricxvi {number} aris 0.")

check_positive_or_negative()


#3
def check_multiple_of_five():
    number = int(input("gtoxvt sheiyvanet ricxvi: "))
    
    if number % 5 == 0:
        print(f"ricxvi {number} aris xutis namravli.")
    else:
        print(f"ricxvi {number} araris xutis namravli.")

check_multiple_of_five()



#4 
def check_legal_age():
    age = int(input("gtxovt sheiyvanet sheni asaki: "))
    
    if age >= 18:
        print("shen xar legaluri asakis.")
    else:
        print("ar xar legaluri asakis.")

check_legal_age()


#5
def print_square():
    number = int(input("gtxovt sheiyvanet ricxvi: "))
    print(number ** 2)

print_square()


#6
def check_password():
    while True:
        password = input("gtxov sheiyvanet paroli: ")
        if len(password) == 8:
            print("registracia warmatebulia.")
            break
        else:
            print("paroli unda iyos 8 asoiani, sheecade axlidan.")

check_password()



#7
def collect_and_square_numbers():
    numbers = []
    
    for _ in range(10):
        number = int(input("sheitane ricxvi: "))
        numbers.append(number)
    
    for number in numbers:
        print(number ** 2)

collect_and_square_numbers()
