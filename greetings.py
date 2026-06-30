def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    print("Testing greet() directly:")
    greet("Test")   # only fires when you run greetings.py directly
                    # silent when use_greetings.py imports it