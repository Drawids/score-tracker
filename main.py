from score_utils import calculate_average, get_best_score

scores = [74, 91, 83, 67, 95]

print(f'Средний балл: {calculate_average(scores)}\nЛучший результат: {get_best_score(scores)}')