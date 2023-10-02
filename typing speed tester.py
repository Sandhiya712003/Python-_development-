import time

def typing_speed_test():
    prompt_text = "The quick brown fox jumps over the lazy dog"
    print("Type the following:")
    print(prompt_text)
    input("Press Enter when you're ready...")

    start_time = time.time()
    user_input = input("Start typing: ")
    end_time = time.time()

    elapsed_time = end_time - start_time

    correct_chars = 0
    for i in range(min(len(user_input), len(prompt_text))):
        if user_input[i] == prompt_text[i]:
            correct_chars += 1

    accuracy = (correct_chars / len(prompt_text)) * 100
    speed = (len(prompt_text) / elapsed_time) * 60

    print(f"\nTime taken: {round(elapsed_time, 2)} seconds")
    print(f"Accuracy: {round(accuracy, 2)}%")
    print(f"Typing speed: {round(speed, 2)} words per minute")


typing_speed_test()

