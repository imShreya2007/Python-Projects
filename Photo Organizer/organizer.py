import os
import json

LOG_FILE = "rename_log.json"

print("Photo Organizer with UNDO....")

def save_log(mapping):
    with open(LOG_FILE, "w", encoding="utf-8") as file:
        json.dump(mapping, file, indent=4)

def load_log():
    if not os.path.exists(LOG_FILE):
        return None
    with open(LOG_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def batch_rename(folder_path, base_name, extension):
    if not extension.startswith("."):
        extension = "." + extension

    files = [
        f for f in os.listdir(folder_path)
        if f.lower().endswith(extension.lower())
    ]
    files.sort()

    if not files:
        print("No files found.")
        return

    rename_map = {}

    print("\nPreview:")
    for i, file in enumerate(files, start=1):
        new_name = f"{base_name}_{i}{extension}"
        print(f"{file} -> {new_name}")
        rename_map[new_name] = file

    confirm = input("\nConfirm rename? (y/n): ").strip().lower()
    if confirm != "y":
        print("Cancelled.")
        return

    for new_name, old_name in rename_map.items():
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)

    save_log(rename_map)
    print("Renaming completed. Undo data saved.")

def undo_rename(folder_path):
    rename_map = load_log()
    if not rename_map:
        print("No undo data found.")
        return

    print("\nUndo Preview:")
    for new_name, old_name in rename_map.items():
        print(f"{new_name} -> {old_name}")

    confirm = input("\nUndo renaming? (y/n): ").strip().lower()
    if confirm != "y":
        print("Undo cancelled.")
        return

    for new_name, old_name in rename_map.items():
        new_path = os.path.join(folder_path, new_name)
        old_path = os.path.join(folder_path, old_name)

        if os.path.exists(new_path):
            os.rename(new_path, old_path)

    os.remove(LOG_FILE)
    print("Undo completed successfully.")

if __name__ == "__main__":
    folder = input("Enter folder path (blank = current): ").strip() or os.getcwd()

    print("\n1. Rename Photos")
    print("2. Undo Last Rename")

    choice = input("Choose option (1/2): ").strip()

    if choice == "1":
        base = input("Enter base name: ").strip() or "Photo"
        ext = input("Enter extension (jpg/png): ").strip() or "jpg"
        batch_rename(folder, base, ext)

    elif choice == "2":
        undo_rename(folder)

    else:
        print("Invalid choice.")
