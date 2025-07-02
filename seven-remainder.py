import random
import time

NUM_OF_LOOPS = 20

def main():
    print("Enter remainder of division by seven!")
    wrong = 0
    start_time = time.time()
    for _ in range(NUM_OF_LOOPS):
        quotient = random.randint(0, 99)
        # print contains end value to prevent a new line
        print(f"{quotient} % 7 =", end=" ")
        entered_value = input()
        if(int(entered_value) != (quotient%7)):
            print(f"Wrong! {quotient} = 7 * {int(quotient/7)} + {quotient%7} = {7*int(quotient/7)} + {quotient%7}.")
            wrong += 1

    print(f"Score: {NUM_OF_LOOPS-wrong}/{NUM_OF_LOOPS}\nTime: {round(time.time()-start_time, 2)}s.")

if __name__ == "__main__":
    main()