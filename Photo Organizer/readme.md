# Photo Organizer 

A **Python console-based Photo Organizer** that allows users to **batch rename photos safely** with a built-in **UNDO feature**.  
The project previews changes before renaming, stores rename history in a JSON log, and lets users revert the last rename operation easily.

---

## Table of Contents
- [Features](#features)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Undo Functionality](#undo-functionality)
- [Data Storage](#data-storage)
- [Concepts Covered](#concepts-covered)

---

## Features

- Batch rename files in a selected folder
- Supports custom:
  - Base filename
  - File extension (jpg, png, etc.)
- Automatic numbering of files
- Preview before renaming
- **Undo last rename operation**
- Stores rename history safely using JSON
- Works on current directory or custom folder path
- Prevents accidental renames with confirmations
- Simple and clean console interface

---

## Usage

1. Run the program:
```bash
python photo_organizer.py
```
2. Choose an option:
    1. Rename Photos
    2. Undo Last Rename
3. Follow the prompts:
    * Enter folder path (or leave blank for current directory)
    * Provide base name and file extension
    * Confirm preview to proceed

---

## How It Works

The program:
1. Reads files matching the selected extension
2. Sorts files alphabetically
3. Generates new filenames using:
```bash
    BaseName_1.ext
    BaseName_2.ext
``` 
4. Shows a preview of old → new filenames
5. Renames files only after user confirmation
6. Saves rename mappings in a JSON log file

## Undo Functionality

1.The rename mapping is stored in rename_log.json
2. Undo option:
    * Displays reverse preview
    * Restores original filenames
    * Deletes the log file after successful undo
3.Prevents undo if no previous rename data exists

---

## Data Storage
* File used: rename_log.json
* Format:
```json
{
  "Photo_1.jpg": "IMG_2031.jpg",
  "Photo_2.jpg": "IMG_2032.jpg"
}
```
* The file is automatically removed after undo

---

## Concepts Covered

* File and directory handling (os)
* Batch file operations
* JSON file read/write
* Safe undo implementation
* Input validation
* Preview-based user confirmation
* Dictionary-based mapping
* Modular function structure