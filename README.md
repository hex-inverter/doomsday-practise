# Doomsday practice

[Doomsday algorithm](https://en.wikipedia.org/wiki/Doomsday_rule) is used to calculate day of the week for any given day. This simple project is intended for practising variant of doomsday algorithm that used Zeller's Congruence. This specific doomsday algorithm can be found [here](https://worldmentalcalculation.com/how-to-calculate-calendar-dates/). The advantage of this algorithm is that it is much faster to calculate, but you have to memorize more data. For average human this can decrease time to calulate day of the week from 15 seconds to 7 seconds[citation needed].

The main parts this project focuses on is division by 4 (without reminder), finding a reminder
when dividing by 7 and remembering key values for each month.

## Requirements

- Python 3.x

## Practice runs
### 7 multiplication table 

Your goal is to solve the equation, where given number is multiplied by 7. This helps you memorize 7 multiplication table for higher numbers than 10, and helps you find remainder in next step.
To run this practice, run command:
``` cmd
python3 seven-table.py
 ```

### Remainder of 7

Your goal is to find the remainder given number when dividing by 7.
To run this practice, run command:
``` cmd
python3 seven-remainder.py
 ```

### Division by 4
To run this practice, run command:
``` cmd
python3 division-by-four.py
 ```
Your goal is to find the solution of given number when dividing by 4 (without remainder).

### Month keys
Each month has a specific value associated with it that has to be memorized. Your goal is to type key value of given month. Flashcards can be used to memorize this table of month keys.
To run this practice, run command:
``` cmd
python3 month-keys.py
 ```





