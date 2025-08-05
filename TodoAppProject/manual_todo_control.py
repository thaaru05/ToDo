import os
import webbrowser

browser = None
html_path = os.path.abspath("todo_app.html")
file_url = "file://" + html_path

def open_browser():
    global browser
    print("Opening TODO app...")
    browser = webbrowser.open(file_url)

def manual_test():
    while True:
        cmd = input("Enter command (open / exit): ").strip().lower()
        if cmd == "open":
            open_browser()
        elif cmd == "exit":
            print("Exiting.")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    manual_test()
