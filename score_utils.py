def calculate_average(scores):
    count = 0
    scores_sum = 0
    try:    
        for score in scores:
            count += 1
            scores_sum += score
        return scores_sum / count
    except ZeroDivisionError:
        print("Список пуст")
def get_best_score(scores):
    maximum_score = scores[0]
    for score in scores:
        if score > maximum_score:
            maximum_score = score
    return maximum_score

if __name__ == "__main__":
    print(f'Средний балл: {calculate_average([1, 2, 3, 4, 5])}\nЛучший результат: {get_best_score([1, 2, 3, 4, 5])}')
    print("Файл запущен")