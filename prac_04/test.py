
#DO THIS NOW LEcture vid 2
from operator import itemgetter


score_pairs = [['Derek', 7], ['Carrie', 8], ['Bob', 6], ['Aaron', 9]]
name_score = input("Enter your Name and Score: ").split()
score_pairs.append([name_score])
score_pairs.sort(key=itemgetter(1))
try:
    print(score_pairs)
except IndexError:
    print("Invalid")
except TypeError:
    print("Invalid")

#Do this Now Vid 4





