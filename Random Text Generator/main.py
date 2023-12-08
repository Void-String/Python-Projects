import random
import string
import time

def get_random_string(length):
    letters = "YOURNAMES" # Origin | Credit!
    result_str = ''.join(
        random.choice(letters.lower()) 
            for i in range(length)
        )
    return(result_str)

for x in range(20):                     # Repeat 20x times
    time.sleep(.25)                     # Pause for .25 second
    up = get_random_string(1).upper();  # Get 1 random capital letter
    # "6" for my first name & "5" for my last name
    # "-1" for each names for 1 random capital letter above
    print(up + get_random_string(5), up + get_random_string(4))

# I made this for myself | Silly/Randomized/Unique | I don't care!
# Now this is your own code | Come back here If you satisfied, or else... 




