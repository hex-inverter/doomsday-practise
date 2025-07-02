import random
import time

NUM_OF_LOOPS = 20

month_keys = {
    "January": 4,
    "February": 0,
    "March": 0,
    "April": 3,
    "May": 5,
    "June": 1,
    "July": 3,
    "August": 6,
    "September": 2,
    "October": 4,
    "November": 0,
    "December": 2,
}

def main():
    print("Enter key for specified month!")
    wrong = 0
    start_time = time.time()
    for _ in range(NUM_OF_LOOPS):
        month = random.choice(list(month_keys.keys()))
        # print contains end value to prevent a new line
        print(f"{month}:", end=" ")
        entered_value = input()
        if(int(entered_value) != month_keys[month]):
            print(f"Wrong! Correct value for {month} is {month_keys[month]}.")
            wrong += 1

    print(f"Score: {NUM_OF_LOOPS-wrong}/{NUM_OF_LOOPS}\nTime: {round(time.time()-start_time, 2)}s.")

if __name__ == "__main__":
    main()