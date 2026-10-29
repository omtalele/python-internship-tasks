
import shutil
from pathlib import Path

# File extensions and their categories
FILE_TYPES = {
    "Documents": [
        ".pdf", ".doc", ".docx", ".txt", ".ppt",
        ".pptx", ".xls", ".xlsx", ".csv"
    ],
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif",
        ".bmp", ".webp", ".svg"
    ],
    "Videos": [
        ".mp4", ".mkv", ".avi", ".mov", ".wmv"
    ],
    "Archives": [
        ".zip", ".rar", ".7z", ".tar", ".gz"
    ],
    "Code": [
        ".py", ".js", ".html", ".css", ".java",
        ".cpp", ".c", ".php", ".json"
    ]
}


def get_category(extension):
    for category, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return category
    return "Others"


def get_unique_path(destination):
    """Avoid overwriting a file with the same name."""
    if not destination.exists():
        return destination

    folder = destination.parent
    stem = destination.stem
    suffix = destination.suffix
    count = 1

    while True:
        new_path = folder / f"{stem}_{count}{suffix}"
        if not new_path.exists():
            return new_path
        count += 1


def organize_files(folder_path):
    folder = Path(folder_path).expanduser()

    if not folder.exists() or not folder.is_dir():
        print("Error: Folder does not exist.")
        return

    # Only inspect files directly inside the selected folder
    files = [item for item in folder.iterdir() if item.is_file()]

    if not files:
        print("No files found in this folder.")
        return

    print(f"\nFound {len(files)} files in: {folder}")
    print("\nPreview of file organization:")

    for file in files:
        category = get_category(file.suffix)
        print(f"{file.name}  ->  {category}/")

    confirm = input(
        "\nMove these files? Type YES to continue: "
    ).strip()

    if confirm != "YES":
        print("Cancelled. No files were moved.")
        return

    moved = 0
    skipped = 0

    for file in files:
        category = get_category(file.suffix)
        target_folder = folder / category

        try:
            target_folder.mkdir(exist_ok=True)
            destination = get_unique_path(target_folder / file.name)

            shutil.move(str(file), str(destination))
            print(f"Moved: {file.name} -> {category}/")
            moved += 1

        except PermissionError:
            print(f"Permission denied: {file.name}")
            skipped += 1

        except OSError as error:
            print(f"Could not move {file.name}: {error}")
            skipped += 1

    print("\n===== ORGANIZATION SUMMARY =====")
    print(f"Files moved: {moved}")
    print(f"Files skipped: {skipped}")


if __name__ == "__main__":
    print("===== AUTOMATIC FILE ORGANIZER =====")
    print("Tip: Test on a temporary folder first.")

    selected_folder = input(
        "Enter folder path to organize: "
    ).strip().strip('"')

    organize_files(selected_folder)
