def calculate_average(scores):
    count = 0
    scores_sum = 0
    for score in scores:
        count = count + 1
        scores_sum = scores_sum + score
    return scores_sum / count
def get_best_score(scores):
    maximum_score = 0
    for score in scores:
        if score > maximum_score:
            maximum_score = score
    return maximum_score

if __name__ == "__main__":
    print("Файл запущен")