import timeit
from boyer_moore_search import boyer_moore_search as bm_search
from knuth_morris_pratt_search import kmp_search
from rabin_karp_search import rabin_karp_search as rk_search


# Приклад використання timeit для вимірювання часу виконання:
#text = open("стаття1.txt", "r", encoding="CP1251").read()
text = open("стаття2.txt", "r", encoding="utf-8").read()

#pattern_exists = "Index"   # для файлу "стаття1.txt"
pattern_exists = "Крок"     # для файлу "стаття2.txt"
pattern_nonexistent = "nonexistent"

# Вимірювання часу для Боєра-Мура
time_boyer_moore_exists = timeit.timeit(lambda: bm_search(text, pattern_exists), number=100)
time_boyer_moore_nonexistent = timeit.timeit(lambda: bm_search(text, pattern_nonexistent), number=100)

# Вимірювання часу для Кнута-Морріса-Пратта
time_knuth_morris_pratt_exists = timeit.timeit(lambda: kmp_search(text, pattern_exists), number=100)
time_knuth_morris_pratt_nonexistent = timeit.timeit(lambda: kmp_search(text, pattern_nonexistent), number=100)

# Вимірювання часу для Рабіна-Карпа
time_rabin_karp_exists = timeit.timeit(lambda: rk_search(text, pattern_exists), number=100)
time_rabin_karp_nonexistent = timeit.timeit(lambda: rk_search(text, pattern_nonexistent), number=100)

# Виведення результатів
print(f"Боєра-Мура (існуючий): {time_boyer_moore_exists}")
print(f"Боєра-Мура (неіснуючий): {time_boyer_moore_nonexistent}")
print(f"Кнута-Морріса-Пратта (існуючий): {time_knuth_morris_pratt_exists}")
print(f"Кнута-Морріса-Пратта (неіснуючий): {time_knuth_morris_pratt_nonexistent}")
print(f"Рабіна-Карпа (існуючий): {time_rabin_karp_exists}")
print(f"Рабіна-Карпа (неіснуючий): {time_rabin_karp_nonexistent}")
