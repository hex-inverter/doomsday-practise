import random
import time

NUM_OF_LOOPS = 20

def main():
    print("Enter integer division by 4!")
    wrong = 0
    start_time = time.time()
    for _ in range(NUM_OF_LOOPS):
        multiplicator = random.randint(0, 99)
        # print contains end value to prevent a new line
        print(f"{multiplicator} / 4 =", end=" ")
        entered_value = input()
        if(int(entered_value) != int(multiplicator/4)):
            print(f"Wrong! {multiplicator} = 4 * {int(multiplicator/4)} + {multiplicator%4} = {4*int(multiplicator/4)} + {multiplicator%4}.")
            wrong += 1

    print(f"Score: {NUM_OF_LOOPS-wrong}/{NUM_OF_LOOPS}\nTime: {round(time.time()-start_time, 2)}s.")


if __name__ == "__main__":
    main()