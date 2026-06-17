import csv
from datetime import datetime
import os

def log_moderator_action(admin_email, action_type, target_user_email, content_id, filename="moderator_actions.csv"):
    """
    Logs moderator actions (like spam deletion) into a shared CSV ledger.
    """
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")
    
    # Expanded headers to cover social media moderation requirements
    header = ["Date", "Time", "Moderator", "Action", "Target User", "Content ID"]
    row = [current_date, current_time, admin_email, action_type, target_user_email, content_id]
    
    file_exists = os.path.isfile(filename)
    
    try:
        with open(filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            print("I am here -----------------------------------------------------------------------------------------------------------------------------")
            if not file_exists:
                writer.writerow(header)
            writer.writerow(row)
    except Exception as e:
        # Prevents a server crash if the text file is locked or unwriteable
        print(f"File logging failed: {e}")
