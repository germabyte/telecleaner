import json
import tkinter as tk
from tkinter import filedialog, messagebox
import os

class UserSelector:
    def __init__(self, users):
        self.users = users
        self.selected_users = set()
        self.current_page = 0
        self.users_per_page = 20

        self.root = tk.Tk()
        self.root.title("Select Users")
        self.root.geometry("300x400")

        self.listbox = tk.Listbox(self.root, selectmode=tk.MULTIPLE, width=40, height=20)
        self.listbox.pack(pady=10)

        self.prev_button = tk.Button(self.root, text="Previous", command=self.prev_page)
        self.prev_button.pack(side=tk.LEFT, padx=10)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_page)
        self.next_button.pack(side=tk.RIGHT, padx=10)

        self.done_button = tk.Button(self.root, text="Done", command=self.done)
        self.done_button.pack(side=tk.BOTTOM, pady=10)

        self.update_page()

    def update_page(self):
        self.listbox.delete(0, tk.END)
        start = self.current_page * self.users_per_page
        end = start + self.users_per_page
        page_users = self.users[start:end]
        
        for user in page_users:
            self.listbox.insert(tk.END, user)
            if user in self.selected_users:
                self.listbox.selection_set(tk.END)

        self.prev_button.config(state=tk.NORMAL if self.current_page > 0 else tk.DISABLED)
        self.next_button.config(state=tk.NORMAL if end < len(self.users) else tk.DISABLED)

    def prev_page(self):
        self.update_selected_users()
        self.current_page -= 1
        self.update_page()

    def next_page(self):
        self.update_selected_users()
        self.current_page += 1
        self.update_page()

    def update_selected_users(self):
        start = self.current_page * self.users_per_page
        selected_indices = self.listbox.curselection()
        for i in selected_indices:
            self.selected_users.add(self.users[start + i])
        
        for i in range(self.listbox.size()):
            if i not in selected_indices:
                user = self.users[start + i]
                if user in self.selected_users:
                    self.selected_users.remove(user)

    def done(self):
        self.update_selected_users()
        self.root.quit()
        self.root.destroy()

    def get_selected_users(self):
        self.root.mainloop()
        return list(self.selected_users)

def clean_json(input_file, output_file, selected_users):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    cleaned_messages = []
    for message in data['messages']:
        if (message['type'] == 'message' and 
            'from' in message and 
            message['from'] is not None and 
            message['from'] in selected_users):
            cleaned_message = f"{message['from']}: {message['text']}"
            cleaned_messages.append(cleaned_message)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(cleaned_messages))

def select_files():
    root = tk.Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames(filetypes=[("JSON files", "*.json")])
    return file_paths

def get_all_users(input_files):
    all_users = set()
    for input_file in input_files:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for message in data['messages']:
            if message['type'] == 'message' and 'from' in message and message['from'] is not None:
                all_users.add(message['from'])
    return sorted(list(all_users))

def process_files():
    input_files = select_files()
    if not input_files:
        print("No files selected. Exiting.")
        return

    all_users = get_all_users(input_files)
    user_selector = UserSelector(all_users)
    selected_users = user_selector.get_selected_users()

    if not selected_users:
        messagebox.showwarning("Warning", "No users selected. Exiting.")
        return

    for input_file in input_files:
        output_file = os.path.splitext(input_file)[0] + "_cleaned.txt"
        clean_json(input_file, output_file, selected_users)
        print(f"Processed {input_file} -> {output_file}")

    print("All files processed successfully.")

if __name__ == "__main__":
    process_files()