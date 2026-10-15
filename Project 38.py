import GROQ
import HF

def prompt_engineering_activity():
    print("Welcome to the AI Prompt Engineering Tutorial!")
    
    print("\nChoose your AI Provider:")
    print("1) Groq")
    print("2) Hugging Face")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "2":
        generate_fn = HF.generate_response
        print("\n--> Selected: Hugging Face\n")
    else:
        generate_fn = GROQ.generate_response
        print("\n--> Selected: Groq\n")

    vague = input("Enter a vague prompt: ")
    print("\nAI's response to the vague prompt:")
    print(generate_fn(vague))

    specific = input(f"\nNow, enter a more specific prompt based on the vague prompt '{vague}': ")
    print("\nAI's response to the specific prompt:")
    print(generate_fn(specific))

    context = input(f"\nFinally, enter a prompt with additional context based on the specific prompt '{specific}': ")
    print("\nAI's response to the context-rich prompt:")
    print(generate_fn(context))

    print("\n--- Reflection ---")
    print("1. How did the AI's responses change when the prompt was made more specific?")
    print("2. How did the AI's responses change when additional context was provided?")
    print("3. Which prompt yielded the most useful or relevant response from the AI? Why?")

if __name__ == "__main__":
    prompt_engineering_activity()
