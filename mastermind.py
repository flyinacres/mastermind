i# Master Mind

__colors = set([c for c in "RGBY"])
solution = "RRRR"

guess = "none"
found = False
while guess != "end" and not found:
    guess = input("Enter your guess: ")
    h = 0
    ph = 0
    for c in guess:
        if c in __colors:
            ph = ph + 1
    for i,c in enumerate(guess):
        if solution[i] == c:
            h = h + 1
            ph = ph - 1
    
    print("Hits: ", h)
    print("Psuedo Hits", ph)
