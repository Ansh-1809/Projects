import time

def countdown(seconds):
    print(f"⏳ Countdown started for {seconds} seconds...\n")
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")  # overwrite the same line
        time.sleep(1)
        seconds -= 1

    print("⏰ Time's up!              ")

# Input time in seconds
try:
    secs = int(input("Enter countdown time in seconds: "))
    countdown(secs)
except ValueError:
    print("Please enter a valid number.")
