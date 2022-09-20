def hello_name(user_name):
   print(f"hello_{user_name}")


def first_odds():
    for number in range(1, 101):
        if number % 2 > 0:
           print(number)


def max_num_in_list(a_list):
    max_number = 0
    for number in a_list:
        if number > max_number:
           max_number = number

    return max_number


def is_leap_year(a_year):
    is_leap = False

    if a_year % 4 == 0:
        if a_year % 100 != 0:
           is_leap = True
        elif a_year % 400 == 0:
           is_leap = True
        else:
           is_leap = False

    return is_leap


def is_consecutive_list(a_list):
    a_list = sorted(a_list)
    is_consecutive = False
    current_number = None
    for number in a_list:
        if not current_number:
           current_number = number
        else:
            if current_number + 1 == number:
               is_consecutive = True
            else:
               is_consecutive = False
               break
            current_number = number

    return is_consecutive

