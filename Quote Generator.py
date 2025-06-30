import random

def random_quote():
    quotes = [
        "Life is what happens when you're busy making other plans. - John Lennon",
        "The way to get started is to quit talking and begin doing. - Walt Disney",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        "You learn more from failure than from success. - Unknown",
        "The purpose of our lives is to be happy. - Dalai Lama",
        "Life is really simple, but we insist on making it complicated. - Confucius",
        "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln"
    ]
    
    # Select and print a random quote from the list
    selected_quote = random.choice(quotes)
    print("\nHere's your quote:")
    print(selected_quote)

if __name__ == "__main__":
    random_quote()