players = [
    {"name": "Alex", "score": 120},
    {"name": "Max", "score": 80},
    {"name": "John", "score": 150},
    {"name": "Kate", "score": 95}
]
print("Список игроков с кол-во очков 10 и больше:")
for player in players:
    if player["score"] >= 10:
        print(f'Name: {player["name"]}, Score: {player["score"]}')