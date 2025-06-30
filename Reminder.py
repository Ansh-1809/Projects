import time

def reminder():
    reminder_msg = input("🔔 Enter your reminder message: ")
    delay = int(input("⏰ Enter time in seconds to wait: "))

    print(f"\nSetting reminder for {delay} seconds...")
    time.sleep(delay)

    print(f"\n🔔 Reminder: {reminder_msg}")

reminder()
