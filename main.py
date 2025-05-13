# main.py

from llm_engine import get_local_response
from user_profile import (
    load_profile,
    add_topic_to_history,
    clear_history,
    show_history
)

def print_menu():
    print("\n--- MENU ---")
    print("[1] Learn a new topic")
    print("[2] View my history")
    print("[3] Clear my history")
    print("[4] Exit")

def main():
    print("=== AIM - LLM Personal Trainer ===")

    # Ask user for profile
    profile_name = input("Enter your profile name: ").strip().lower()
    profile = load_profile(profile_name)

    print(f"Welcome back, {profile['name']}!")

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            topic = input("What topic do you want to learn about? ").strip()
            prompt = f"What is {topic}? Explain it in 2 sentences for a 12-year-old."

            response = get_local_response(prompt)
            print("\nAI Response:")
            print(response)
            add_topic_to_history(profile, topic, profile_name)

        elif choice == "2":
            show_history(profile)

        elif choice == "3":
            confirm = input("Are you sure you want to clear your history? (yes/no): ").strip().lower()
            if confirm == "yes":
                clear_history(profile, profile_name)
                print("History cleared.")
            else:
                print("Action canceled.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1–4.")

if __name__ == "__main__":
    main()
8231128