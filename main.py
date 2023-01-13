score = 0
# q1
print("What is the most IMPORTANT piece in chess?")
q1 = str(input("Q1 Answer: ")).lower()
if q1 == "the king" or q1 == "king":
    score += 1
    print("Correct")
else:
    print("Incorrect")

# q2
print("What is the most POWERFUL piece in chess?")
q2 = str(input("Q2 Answer: ")).lower()
if q2 == "the queen" or q2 == "queen":
    score += 1
    print("Correct")
else:
    print("Incorrect")

# q3
print("How many small squares are on a chess board?")
q3 = int(input("Q3 Answer: "))
if q3 == 64:
    score += 1
    print("Correct")
else:
    print("Incorrect")

# q4
print("What is the only chess piece that can jump over other pieces?")
q4 = str(input("Q4 Answer: ")).lower()
if q4 == "the horse" or q4 == "horse" or q4 == "knight" or q4 == "the knight":
    score += 1
    print("Correct")
else:
    print("Incorrect")

# results
print("YOUR RESULTS:")
percent = str(score / 4 * 100)
print(str(score) + " / 4 (" + percent + "%)")
# feedback
if score == 4:
    print("Excellent")
elif score == 3:
    print("Good job")
elif score <= 2:
    print("Try again")
