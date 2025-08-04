# "PERSONALITY QUIZ GAME🎊"
Name = input("Enter your name : ")     
print("☺️WELCOME TO THE PERSONALITY QUIZ GAME",Name)
print("🤩Let's start our game",Name)
print("Answers the following questions")
score = 0
#QUESTION NO 1
print("1.what do you prefer in weekends?")
print("(a):Exploring the world✈️")
print("(b):Reading books📚")
print("(c):Painting🎨")
print("(d):Sleeping😴")
ans1 = input("Enter your ans (a/b/c/d):")
if ans1 == 'a':
    score += 4
elif(ans1=='b'):
    score += 3
elif(ans1=='c'):
    score += 2
else:
    score += 1
#QUESTION NO 2
print("What is your favourite colour?")
print("(a):Blue💙")
print("(b):Green💚")
print("(c):orange🧡")
print("(d):White🤍")
ans2 = input("Enter your ans (a/b/c/d) :")
if ans2 == 'a':
    score+=4
elif ans2 == 'b':
    score+=3
elif(ans1=='c'):
    score += 2
else:
    score += 1
#QUESTION NO 3
print("3.How do you handle stress?")
print("(a):Go for a walk 🚶‍♀️‍➡️")
print("(b):Cry in a corner😭")
print("(c):Talk to your friend🫂")
print("(d):Eat or sleep🍴")
ans3 = input("Enter your ans (a/b/c/d):")
if ans3=='a':
    score+=3
elif ans3=='b':
    score+=1
elif ans3=='c':
    score+=4
else:
    score+=2
if score >=10:
    print("KIND HEARTED💝")
elif score >=8:
    print("THINKER🤔")
elif score>=6:
    print("CREATIVE PERSON🧠")
else:
    print("JUST CHILL BRO,YOU'RE RELAXED AND GO WITH THE FLOW😉")
print("THANK YOU",Name,"😍")