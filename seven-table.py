import random
import time

NUM_OF_LOOPS = 20

def main():
    print("Solve given equation!")
    wrong = 0
    start_time = time.time()
    for _ in range(NUM_OF_LOOPS):
        factor = random.randint(0, 14)
        # print contains end value to prevent a new line
        print(f"{factor} * 7 =", end=" ")
        entered_value = input()
        if(int(entered_value) != (factor * 7)):
            print(f"Wrong! {factor} * 7 = {factor*7}.")
            wrong += 1
    
    print(f"Score: {NUM_OF_LOOPS-wrong}/{NUM_OF_LOOPS}\nTime: {round(time.time()-start_time, 2)}s.")

if __name__ == "__main__":
    main()