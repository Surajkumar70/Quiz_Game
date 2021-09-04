print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("Q1. Who programmed the first computer game 'Spacewar!' in 1962 ?"'\n')
if answer.lower() == "steave russell":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Q2. Who developed Java Programming Language ?"'\n')
if answer.lower() == "james gosling":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Q3. Which one is volatile memory in a computer system ?" '\n')
if answer.lower() == "ram":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Q4. One Terabyte (1 TB) is equal to ?" '\n')
if answer.lower() == "1024 gb":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Q5. Linus Torvalds develop which operating system" '\n')
if answer.lower() == "linux":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")

