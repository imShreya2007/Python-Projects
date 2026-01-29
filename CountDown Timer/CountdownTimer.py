import time
import winsound

print("CountDowm Timer....")
# Frequency and duration for the beep sound
f= 4000
d = 4000

while True:
    try:
        seconds= int(input("Enter the time in seconds: "))
        if seconds < 1:
            print("Please Enter a number Greater than one.")
            continue
        break
    except ValueError:
        print("Invalid input, Please enter a whole number.")

print("\n Timer Started....")
for remaining in range(seconds, 0, -1):
    mins, secs = divmod(remaining, 60)
    time_format = f"{mins:02}:{secs:02}"
    print(f"Time left: {time_format}", end="\r")
    time.sleep(1)

print("Time's Up!")
winsound.Beep(f, d)
