import sys
import timeit
import math
from itertools import count, islice, accumulate

sys.setrecursionlimit(5000)

#1 - רקורסיה רגילה
def build_numbers(n):
    return () if n < 1 else build_numbers(n - 1) + (n,)

#1 - רקורסיה זנבית
def build_numbers_tail(n, acc=()):
    return acc if n < 1 else build_numbers_tail(n - 1, (n,) + acc)

#2 - רקורסיה רגילה
def sum_values(values):
    return 0 if not values else values[0] + sum_values(values[1:])

#2 - רקורסיה זנבית
def sum_values_tail(values, acc=0):
    return acc if not values else sum_values_tail(values[1:], acc + values[0])

#3 - רקורסיה רגילה
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

#3 - רקורסיה זנבית
def lcm_tail(a, b, acc=0):
    return acc if acc > 0 and acc % min(a, b) == 0 else lcm_tail(a, b, acc + max(a, b))

#4 - רקורסיה רגילה
def count_digits(n):
    return 1 if n < 10 else 1 + count_digits(n // 10)

def reverse_number(n):
    return n if n < 10 else (n % 10) * 10 ** (count_digits(n) - 1) + reverse_number(n // 10)

def is_palindrome_number(n):
    return n == reverse_number(n)

#4 - רקורסיה זנבית
def reverse_number_tail(n, acc=0):
    return acc if n == 0 else reverse_number_tail(n // 10, acc * 10 + n % 10)

def is_palindrome_number_tail(n):
    return n == reverse_number_tail(n)

#5
FINAL_LETTERS = {'ך': 'כ', 'ם': 'מ', 'ן': 'נ', 'ף': 'פ', 'ץ': 'צ'}

def normalize_char(char):
    return FINAL_LETTERS.get(char.lower(), char.lower())

#5 - רקורסיה רגילה
def clean_text(text):
    return "" if not text else (normalize_char(text[0]) if text[0].isalnum() else "") + clean_text(text[1:])

def is_clean_palindrome(text):
    return True if len(text) < 2 else text[0] == text[-1] and is_clean_palindrome(text[1:-1])

def is_palindrome_alphanumeric(text):
    return is_clean_palindrome(clean_text(text))

#5 - רקורסיה זנבית
def clean_text_tail(text, acc=""):
    return acc if not text else clean_text_tail(
        text[1:],
        acc + (normalize_char(text[0]) if text[0].isalnum() else "")
    )

def is_clean_palindrome_tail(text, index=0):
    return True if index >= len(text) // 2 else (
        text[index] == text[-1 - index] and is_clean_palindrome_tail(text, index + 1)
    )

def is_palindrome_alphanumeric_tail(text):
    return is_clean_palindrome_tail(clean_text_tail(text))

#6 - רקורסיה רגילה
def insert_sorted(value, values):
    return (value,) if not values else (
        (value,) + tuple(values) if value <= values[0]
        else (values[0],) + insert_sorted(value, values[1:])
    )

def sort_values(values):
    return () if not values else insert_sorted(values[0], sort_values(values[1:]))

def sortedzip(lists):
    return zip(*map(sort_values, lists))

#6 - רקורסיה זנבית
def insert_sorted_tail(value, values, acc=()):
    return acc + (value,) + tuple(values) if not values or value <= values[0] else (
        insert_sorted_tail(value, values[1:], acc + (values[0],))
    )

def sort_values_tail(values, acc=()):
    return acc if not values else sort_values_tail(values[1:], insert_sorted_tail(values[0], acc))

def sortedzip_tail(lists):
    return zip(*map(sort_values_tail, lists))

#7 - רקורסיה רגילה
def count_repeats(text, char):
    return 0 if not text or text[0] != char else 1 + count_repeats(text[1:], char)

def encode_rle(text):
    return "" if not text else (
        text[0] + str(count_repeats(text, text[0])) + encode_rle(text[count_repeats(text, text[0]):])
    )

#7 - רקורסיה זנבית
def count_repeats_tail(text, char, acc=0):
    return acc if not text or text[0] != char else count_repeats_tail(text[1:], char, acc + 1)

def encode_rle_tail(text, acc=""):
    return acc if not text else encode_rle_tail(
        text[count_repeats_tail(text, text[0]):],
        acc + text[0] + str(count_repeats_tail(text, text[0]))
    )


# Lazy Evaluation, Generators

#1א - ללא lazy evaluation
def create_numbers():
    return list(range(10001))

#1א - עם lazy evaluation
def create_numbers_lazy():
    return (number for number in range(10001))

#1ב - ללא lazy evaluation
def take_first_half(numbers):
    return numbers[:5000]

#1ב - עם lazy evaluation
def take_first_half_lazy(numbers):
    return (number for number in islice(numbers, 5000))

def measure(func, *args):
    return timeit.timeit(lambda: func(*args), number=1), sys.getsizeof(func(*args))

def format_measure(func, *args):
    return "זמן: {:.6f} שניות, גודל: {} בתים".format(*measure(func, *args))

#2
def is_prime(n):
    return n > 1 and all(n % divisor for divisor in range(2, int(n ** 0.5) + 1))

def primes_generator():
    return (number for number in count(2) if is_prime(number))

#3
def power_function(exp):
    return lambda base: base ** exp

def taylor_generator(x):
    return (
        value for value in accumulate(
            map(lambda n: power_function(n)(x) / math.factorial(n), count(0))
        )
    )


if __name__ == "__main__":
    while True:
        print("\n--- תפריט תרגיל 3 ---")
        print("1: שאלות 1-2 - יצירת tuple וסכימת איבריו")
        print("3: שאלה 3 - LCM")
        print("4: שאלה 4 - פלינדרום של מספר")
        print("5: שאלה 5 - פלינדרום אלפאנומרי")
        print("6: שאלה 6 - sortedzip")
        print("7: שאלה 7 - דחיסת RLE")
        print("8: גנרטורים שאלה 1 - Lazy Evaluation")
        print("9: גנרטורים שאלה 2 - גנרטור ראשוניים")
        print("10: גנרטורים שאלה 3 - גנרטור טור טיילור")
        print("0: יציאה")

        choice = input("בחר סעיף להרצה: ")

        if choice == '0':
            print("יציאה...")
            break

        elif choice == '1':
            print("רקורסיה רגילה:", build_numbers(1000)[:5], "...", build_numbers(1000)[-5:])
            print("סכום:", sum_values(build_numbers(1000)))
            print("רקורסיה זנבית:", build_numbers_tail(1000)[:5], "...", build_numbers_tail(1000)[-5:])
            print("סכום:", sum_values_tail(build_numbers_tail(1000)))

        elif choice == '3':
            a = int(input("enter first number:\n"))
            b = int(input("enter second number:\n"))
            print("רקורסיה רגילה:", lcm(a, b))
            print("רקורסיה זנבית:", lcm_tail(a, b))

        elif choice == '4':
            num_input = input("enter number:\n")

            if not num_input.isdigit():
                print("invalid input")
            else:
                print("רקורסיה רגילה:", is_palindrome_number(int(num_input)))
                print("רקורסיה זנבית:", is_palindrome_number_tail(int(num_input)))

        elif choice == '5':
            text_input = input("enter text:\n")

            if not text_input.strip():
                print("invalid input")
            else:
                print(is_palindrome_alphanumeric(text_input))

        elif choice == '6':
            print(list(sortedzip([[3, 1, 2], [5, 6, 4], ['a', 'b', 'c']])))
            print(list(sortedzip_tail([[3, 1, 2], [5, 6, 4], ['a', 'b', 'c']])))

        elif choice == '7':
            text_input = input("enter text:\n")

            if not text_input.strip():
                print("invalid input")
            else:
                print(encode_rle(text_input))

        elif choice == '8':
            print("ללא lazy evaluation:")
            print("יצירת המערך -", format_measure(create_numbers))
            print("5000 האיברים הראשונים -", format_measure(take_first_half, create_numbers()))
            print("type המערך המלא:", type(create_numbers()))
            print("type המערך החדש:", type(take_first_half(create_numbers())))
            print("אותו type:", type(create_numbers()) is type(take_first_half(create_numbers())))

            print("\nעם lazy evaluation:")
            print("יצירת המערך -", format_measure(create_numbers_lazy))
            print("5000 האיברים הראשונים -", format_measure(take_first_half_lazy, create_numbers_lazy()))
            print("type המערך המלא:", type(create_numbers_lazy()))
            print("type המערך החדש:", type(take_first_half_lazy(create_numbers_lazy())))
            print("אותו type:", type(create_numbers_lazy()) is type(take_first_half_lazy(create_numbers_lazy())))

        elif choice == '9':
            amount = int(input("enter amount of primes:\n"))
            print(*islice(primes_generator(), amount), sep="\n")

        elif choice == '10':
            x = float(input("enter number:\n"))
            amount = int(input("enter amount of elements:\n"))
            print(*islice(taylor_generator(x), amount), sep="\n")

        else:
            print("בחירה לא תקינה, נסה שוב.")
