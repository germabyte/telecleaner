# telecleaner

**telecleaner** is a simple, user-friendly program designed to help you filter and clean data from Telegram exports. Whether you're organizing your chat history, focusing on specific contributors, or decluttering your records, **telecleaner** streamlines the process by allowing you to selectively filter messages based on user input.

## Features

- **Interactive User Selection:** Easily choose which users' messages to keep using a graphical interface.
- **Batch Processing:** Process multiple Telegram JSON export files in one go.
- **Cleaned Outputs:** Save filtered messages into clean text files for easier reading and storage.

---

## Getting Started

Follow these steps to download, set up, and run **telecleaner** on your computer:

### Step 1: Download the Repository

1. Click the green "Code" button at the top of this GitHub page.
2. Select **Download ZIP**.
3. Save the ZIP file to a location of your choice.

### Step 2: Extract the Files

1. Locate the downloaded ZIP file on your computer.
2. Right-click the file and select **Extract All** (Windows) or **Expand** (macOS).
3. Choose a destination folder for the extracted files.

### Step 3: Run the Program

1. Open the extracted folder.
2. Double-click the file named `telecleaner.py` to start the program. (Ensure Python is installed on your system.)
3. Follow the on-screen instructions to select and clean your Telegram export files.

---

## Use Cases and Examples

### Scenario 1: Organizing Chat Data

You have exported a large group chat and want to focus only on messages from specific people. With **telecleaner**, you can:
- Load the exported JSON file.
- Select the contributors whose messages you want to keep.
- Save their messages in a cleaned text file for easy review.

### Scenario 2: Research or Analysis

You're analyzing conversations for a project and need messages from select individuals. Use **telecleaner** to filter messages quickly and accurately.

---

## Editing and Customizing the Code

Want to tweak **telecleaner** to better suit your needs? Here are some simple ways to modify the program:

- **Adjust the Number of Users per Page:**
  Open the `telecleaner.py` file in a text editor and look for this line in the `UserSelector` class:
  ```python
  self.users_per_page = 20
  ```
  Change `20` to a different number to display more or fewer users per page in the selection window.

- **Change the Output Format:**
  If you prefer a different output format, edit the `clean_json` function. Customize the line:
  ```python
  cleaned_message = f"{message['from']}: {message['text']}"
  ```
  to suit your needs.

- **Add New Filters:**
  Enhance the filtering logic in the `clean_json` function to include or exclude messages based on additional criteria, such as message content or date.

---

## Disclaimers and Updates

- **Updates:** This repository may be updated at any time to improve features or fix bugs. If you encounter issues, consider downloading the latest version.
- **Compatibility:** The program is designed for use with Telegram JSON exports. Ensure your exports are in the correct format.

---

## Feedback and Contributions

We welcome feedback and contributions! If you have suggestions for improvement or encounter any issues, feel free to open an issue or submit a pull request.

Enjoy using **telecleaner** to make your Telegram data easier to manage!

