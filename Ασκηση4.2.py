'''
Python Mini Project Ασκηση 4.2
'''
import time
charPoints = { "Α" : 1, "Β" : 8, "Γ" : 4, "Δ" : 4, "Ε" : 1, "Ζ" : 10, "Η" : 1, "Θ" : 10, "Ι" : 1, "Κ" : 2, "Λ" : 3, "Μ" : 3, "Ν" : 1, "Ξ" : 10, "Ο" : 1, "Π" : 2, "Ρ" : 2, "Σ" : 1, "Τ" : 1, "Υ" : 2, "Φ" : 8, "Χ" : 8, "Ψ" : 10, "Ω" : 3}
dic = {}
points = 0
while True:
    text = input("Δώστε Λεξη (ή q για έξοδο) :")
    if text=="q":
        break
    else:
        for char in text:
            points += charPoints[char]
        dic[text] = points
        print(text,points, sep=" ")
        points = 0


for x in sorted(dic):
        print(x, dic[x])


time.sleep(10)
