## ✅ README.md

---

# Telegram JSON Cleaner

## 1. Introduction and Purpose

### 🧩 Introduction  
**Telegram JSON Cleaner** is a simple, user-friendly program designed to extract and clean messages from Telegram chat export files (in JSON format). It allows users to visually select specific participants from a chat and filter the conversation based on those selections.

### 🎯 Purpose & Problem Statement  
Telegram's exported data includes all messages from all users in a group or private chat. Manually filtering messages from only specific users can be time-consuming and error-prone. This program simplifies that task by offering an interactive way to select users and automatically generate clean text files with only the relevant messages.

### 💡 Value Proposition  
- No coding required – intuitive interface for user selection  
- Supports multiple files at once  
- Fast and efficient extraction  
- Outputs clean, readable `.txt` files containing only the chosen users' messages

---

## 2. Dependencies (Required Software/Libraries)

This program uses Python’s built-in libraries and the standard GUI module `tkinter`.

### ✅ Required Software

| Dependency | Description | Installation |
|-----------|-------------|--------------|
| **Python 3.x** | The programming language used to run the program. | [Download Python](https://www.python.org/downloads/) |
| **tkinter** | Provides the graphical user interface (GUI) used to select users and files. | Comes pre-installed with Python on Windows and macOS. If using Linux and it’s missing, run: `sudo apt-get install python3-tk` |

> ⚠️ No additional external libraries or frameworks are required.

---

## 3. Getting Started (Installation & Execution)

### 📥 Step 1: Download the Project

1. Go to the repository page on GitHub.  
2. Click the green **"Code"** button.  
3. Select **"Download ZIP"**.  
4. Extract the ZIP file to any folder on your computer.

### 🧪 Step 2: Run the Program

1. Ensure Python is installed on your system.
2. Open your terminal or command prompt:
   - **Windows:** Press `Windows + R`, type `cmd`, press Enter  
   - **macOS:** Open **Terminal** from Applications  
   - **Linux:** Use your default terminal
3. Navigate to the extracted folder using the `cd` command.  
   Example:
   ```bash
   cd path/to/extracted/folder
   ```
4. Run the program:
   ```bash
   python telegram_cleaner.py
   ```

> Replace `telegram_cleaner.py` with the actual filename if different.

---

## 4. User Guide (How to Effectively Use the Program)

### 🗂️ Step-by-Step Usage

1. **File Selection:**  
   - A window will open allowing you to choose one or more `.json` files exported from Telegram.
   - Select the desired files and click **"Open"**.

2. **User Selection Interface:**  
   - A graphical window titled **"Select Users"** will appear.
   - Use checkboxes to select which users’ messages you want to include.
   - Navigate pages using **Previous** and **Next** buttons if there are many users.
   - Once done, click the **"Done"** button.

3. **Processing Output:**  
   - The program processes all selected `.json` files.
   - It creates a new cleaned `.txt` file for each, in the same folder as the original.
   - The new files will be named like: `originalfilename_cleaned.txt`

### 📥 Input Format

- One or more **Telegram-exported JSON files**
- The JSON structure must contain a `"messages"` array with message dictionaries including `"type"`, `"from"`, and `"text"` fields.

### 📤 Output Format

- For each selected file, a plain `.txt` file containing lines formatted as:
  ```
  Username: message text
  ```

> Messages from users not selected will be excluded entirely.

---

## 5. Use Cases and Real-World Examples

### ✅ Use Case 1: Extract Only Admin Messages  
**Scenario:** A group chat has many users, but you only want to save messages written by the group admin.  
**Steps:**  
- Select the JSON file.  
- Choose only the admin’s name in the selection window.  
- Output: A text file containing only the admin’s messages.

### ✅ Use Case 2: Create a Conversation Transcript Between Two Users  
**Scenario:** You want to extract a private back-and-forth between two specific participants in a group.  
**Steps:**  
- Select the group JSON file.  
- Choose both participants in the user selector.  
- Output: A readable conversation between only those two users.

### ✅ Use Case 3: Archive Personal Messages from Multiple Chats  
**Scenario:** You want to archive your own messages from several Telegram groups.  
**Steps:**  
- Select multiple exported JSON files at once.  
- Select only your name.  
- Output: One cleaned `.txt` file per chat, each containing only your messages.

---

## 6. Disclaimer & Important Notices

- This repository and its contents may be updated at any time without notice.  
- Such updates may render parts of this README obsolete.  
- The code is provided **"as-is"** with **no guarantees** regarding functionality, reliability, compatibility, or correctness.  
- Users are responsible for verifying output quality and ensuring compatibility with their systems.

---

## 7. Tone, Style, and Presentation Guidelines

- Clear and simple language throughout  
- GUI-based interaction for ease of use  
- Code-based execution kept minimal and user-friendly  
- Suggest screenshots or GIFs for visual aid if publishing the repository online
