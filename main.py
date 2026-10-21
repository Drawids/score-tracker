from score_utils import calculate_average, get_best_score

players = [
    {"name": "Alex", "score": 120},
    {"name": "Max", "score": 80},
    {"name": "John", "score": 150},
    {"name": "Kate", "score": 95}
]

scores = [74, 91, 83, 67, 95]

#print("Список игроков с кол-во очков 100 и больше:")
#for player in players:
    #if player["score"] >= 100:
        #print(f'Name: {player["name"]}, Score: {player["score"]}')

print(f'Средний балл: {calculate_average(scores)}\nЛучший результат: {get_best_score(scores)}')