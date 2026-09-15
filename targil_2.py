import timeit
from functools import reduce
from datetime import datetime, timedelta
import math

#1

linear_function = lambda x: (x / 2) + 2

#1.1
L = list(map(linear_function, range(10001)))

#1.2
def functional_approach():
    return sum(L)

#1.3
def imperative_approach():
    mapped_list = []
    for x in range(10001):
        mapped_list.append((x / 2) + 2)
        
    total_sum = 0
    for val in mapped_list:
        total_sum += val
        
    return total_sum

def compare_times():
    return (
        timeit.timeit(lambda: sum(map(linear_function, range(10001))), number=100),
        timeit.timeit(imperative_approach, number=100)
    )

#1.4
def one_liner_functional():
    return reduce(lambda acc, x: acc + linear_function(x), range(10001), 0)


#2
numbers = range(1, 1001)
evens = list(filter(lambda x: x % 2 == 0, numbers))
odds = list(filter(lambda x: x % 2 != 0, numbers))

#2.1 
even_lambda = lambda acc, x: acc * x
odd_lambda = lambda acc, x: ((acc + x) / 2) + 2

#2.2
def apply_lambdas_to_lists(evens_list, odds_list):
    evens_result = reduce(even_lambda, evens_list)
    odds_result = reduce(odd_lambda, odds_list)
    
    return evens_result, odds_result

#2.3
def sum_list_results(evens_res, odds_res):
    return sum(map(int, [evens_res, odds_res]))


#3.1

def is_armstrong(n):

    if not isinstance(n, int) or n <= 0:
        return False
        
    str_n = str(n)
    num_digits = len(str_n)
    
    armstrong_sum = sum(int(digit) ** num_digits for digit in str_n)
    
    return armstrong_sum == n

#3.2
def armstrong_range(n1, n2):

    return list(filter(is_armstrong, range(n1, n2)))

#4

def generate_dates(start_date_str, num_dates, skip_days):

    base_date = datetime.strptime(start_date_str, "%d/%m/%Y")
    dates_list = list(map(
        lambda i: (base_date + timedelta(days=i * skip_days)).strftime("%d/%m/%Y"),
        range(num_dates)
    ))
    
    return dates_list

#5.1
def power_function(exp):
    return lambda base: base ** exp

#5.2
def generate_power_funcs(n):
    return map(power_function, range(n))

#5.3
def taylor_e_x(x, n):
    funcs_map = generate_power_funcs(n)
    return sum(
        map(lambda item: item[1](x) / math.factorial(item[0]), enumerate(funcs_map))
    )

#6

def task_manager():
    tasks = {}

    def add_task(task, status="incomplete"):
        tasks[task] = status

    def get_tasks():
        return tasks

    def complete_task(task):
        if task in tasks:
            tasks[task] = "complete"

    return {
        'add_task': add_task,
        'get_tasks': get_tasks,
        'complete_task': complete_task
    }

# 7.1.1
def clean_spaces(text):
    return text.strip()

# 7.1.2
def capitalize_text(text):
    return text.title()

# 7.1.3
def add_stars(text):
    return f"***{text}***"



# 7.2.1
def create_pipeline():
    return lambda x: x

# 7.2.2
def add_to_pipeline(pipeline_fn, new_fn):
    return lambda x: new_fn(pipeline_fn(x))

if __name__ == "__main__":
    while True:
        print("\n--- תפריט תרגיל 2 ---")
        print("1: הרצת שאלה 1")
        print("2: הרצת שאלה 2")
        print("3: הרצת שאלה 3")
        print("5: הרצת שאלה 5")
        print("7: הרצת שאלה 7")
        print("0: יציאה")
        
        choice = input("בחר סעיף להרצה: ")
        
        if choice == '0':
            print("יציאה...")
            break
            
        elif choice == '1':
            # --- שאלה 1 ---
            print("סכימה בעזרת פונקציית על:", functional_approach())
            print("סכימה בשיטה אימפרטיבית:", imperative_approach())
            print("סכימה בעזרת פונקציית על אחת:", one_liner_functional())

            functional_time, imperative_time = compare_times()
            print("זמן ריצה פונקציונלי:", functional_time)
            print("זמן ריצה אימפרטיבי:", imperative_time)

        elif choice == '2':
            # --- שאלה 2 ---
            evens_result, odds_result = apply_lambdas_to_lists(evens, odds)
            print("תוצאת הרשימה הזוגית:", evens_result)
            print("תוצאת הרשימה האי זוגית:", odds_result)
            print("סכום התוצאות:", sum_list_results(evens_result, odds_result))

        elif choice == '3':
            # --- שאלה 3 ---
            num_input = input("Enter number:\n")
            
            if not num_input.isdigit() or int(num_input) <= 0:
                print("invalid input")
            else:
                print(armstrong_range(1, int(num_input)))
                
        elif choice == '5':
            # --- שאלה 5 ---
            n = int(input("Enter number of powers:\n"))
            
            result = generate_power_funcs(n)
            print(type(result))
            
            base = int(input("Enter base:\n"))
            
            powers_tuple = tuple(func(base) for func in result)
            print(powers_tuple)
            
        elif choice == '7':
            # --- שאלה 7 ---
            pipeline = create_pipeline()
            pipeline = add_to_pipeline(pipeline, clean_spaces)
            pipeline = add_to_pipeline(pipeline, capitalize_text)
            pipeline = add_to_pipeline(pipeline, add_stars)
            
            text_input = input("enter text:\n")
            
            if not text_input.strip():
                print("invalid input")
            else:
                print(pipeline(text_input))
                
        else:
            print("בחירה לא תקינה, נסה שוב.")