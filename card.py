cards = ['ace','jack','king','joker']

points = 0

for x in range(6):
    import random
    random.shuffle(cards)
    print("current card is", cards[0])
    random.shuffle(cards)
    answer = str(input("can you guess next card:"))
    if answer == cards[0]:
        print("its wrong! card was", cards[0])
        print("game over you scored",points)