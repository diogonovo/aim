import os
import json
from datetime import datetime

PROFILE_DIR = "data"

def get_profile_path(profile_name: str) -> str:
    """
    Returns the full path to the user's profile file.
    Automatically adds the .json extension if not present.
    """
    if not profile_name.endswith(".json"):
        profile_name += ".json"
    return os.path.join(PROFILE_DIR, profile_name)

def load_profile(profile_name: str) -> dict:
    """
    Loads the user profile from a JSON file.
    If the profile does not exist, a new one is created.
    """
    path = get_profile_path(profile_name)

    if not os.path.exists(PROFILE_DIR):
        os.makedirs(PROFILE_DIR)

    if not os.path.isfile(path):
        print(f"No profile found for '{profile_name}'. Creating a new profile...")
        return create_new_profile(profile_name)

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def create_new_profile(profile_name: str) -> dict:
    """
    Creates a new user profile with default values and saves it.
    """
    profile = {
        "name": profile_name.replace(".json", ""),
        "created_at": datetime.now().isoformat(),
        "history": []
    }
    save_profile(profile, profile_name)
    return profile

def save_profile(profile: dict, profile_name: str) -> None:
    """
    Saves the user profile to a JSON file.
    """
    path = get_profile_path(profile_name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=4, ensure_ascii=False)

def add_topic_to_history(profile: dict, topic: str, profile_name: str) -> None:
    """
    Adds a new topic to the user's learning history and saves the profile.
    """
    profile["history"].append({
        "topic": topic,
        "timestamp": datetime.now().isoformat()
    })
    save_profile(profile, profile_name)

def clear_history(profile: dict, profile_name: str) -> None:
    """
    Clears the user's learning history.
    """
    profile["history"] = []
    save_profile(profile, profile_name)

def show_history(profile: dict) -> None:
    """
    Displays the user's learning history in the terminal.
    """
    if not profile["history"]:
        print("No topics studied yet.")
        return

    print("\n--- Your Learning History ---")
    for entry in profile["history"]:
        print(f"- {entry['topic']} ({entry['timestamp']})")
