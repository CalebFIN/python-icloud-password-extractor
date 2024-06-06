from pywinauto.application import Application
from pywinauto import keyboard
import pyperclip
import time
from dataclasses import dataclass
from typing import Optional, List
import json

@dataclass
class PassEntry:
    username: str
    password: str
    website: str
    
    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "website": self.website
        }
    
    # hash function to compare entries
    def __hash__(self):
        return hash((self.username, self.password, self.website))
    
    # equality function to compare entries
    def __eq__(self, other):
        return self.username == other.username and self.password == other.password and self.website == other.website

def find_window(app_name: str) -> Optional[Application]:
    """Attempt to connect to an application by name."""
    try:
        app = Application().connect(path=app_name)
        return app
    except Exception as e:
        print(f"Failed to find the application: {e}")
        return None

def get_entry_at_current_position() -> PassEntry:
    keyboard.send_keys('^u')
    time.sleep(0.001)
    current_username = pyperclip.paste()
    
    keyboard.send_keys('^p')
    time.sleep(0.001)
    current_password = pyperclip.paste()
    
    keyboard.send_keys('^w')
    time.sleep(0.001)
    current_website = pyperclip.paste()
    
    return PassEntry(current_username, current_password, current_website)

def click_and_extract_text(app: Application) -> List[PassEntry]:
    """Clicks at given positions and extracts text from the window."""
    entries: List[PassEntry] = []
    
    try:
        main_win: Application = app.top_window()
        main_win.set_focus()
        
        # click the position 100, 200 which is the start position within the window to ensure the window is in focus
        main_win.click_input(coords=(100, 200))
        
        # scroll to the top of the list
        keyboard.send_keys('{HOME}')
        
        # setup last entry and last entry hits
        last_entry = None
        last_entry_hits = 0
        
        while True:
            pass_entry = get_entry_at_current_position()
            
            # insert the entry into the list
            entries.append(pass_entry)
            
            # check equality with the last entry
            if last_entry:
                if last_entry == pass_entry:
                    last_entry_hits += 1
                else:
                    last_entry_hits = 0
            
            # set the last entry to the current entry
            last_entry = pass_entry
            
            # if the last entry has been the same for 3 times, we have reached the end of the list
            if last_entry_hits >= 3:
                break
            
            # hit the down arrow key to move to the next entry
            keyboard.send_keys('{DOWN}')
        
    except Exception as e:
        print(f"Error during operations: {e}")
    return entries

if __name__ == "__main__":
    app_path = 'iCloudPasswords.exe'
    app: Application = find_window(app_path)
    
    if app:
        pass_data: List[PassEntry] = click_and_extract_text(app)
        
        # remove any empty entries from the list
        pass_data = [entry for entry in pass_data if entry.username and entry.password and entry.website]
        
        # remove duplicates from the list
        pass_data = list(set(pass_data))
        
        # write the data to a file
        with open("./pass_data.json", "w") as f:
            json.dump([entry.to_dict() for entry in pass_data], f, indent=4)
    else:
        print("Application not found.")
