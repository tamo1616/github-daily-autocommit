import json
import datetime
import random

def update_activity():
    # Read existing data
    try:
        with open('data/activity.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"commits": []}
    
    # Add new entry
    current_time = datetime.datetime.now().isoformat()
    new_entry = {
        "timestamp": current_time,
        "day": datetime.datetime.now().strftime("%Y-%m-%d"),
        "message": random.choice([
            "Daily activity update",
            "Keeping the streak alive",
            "Another day, another commit",
            "Daily contribution",
            "Automated daily update"
        ])
    }
    
    data["commits"].append(new_entry)
    
    # Keep only last 30 entries to prevent file from growing too large
    if len(data["commits"]) > 30:
        data["commits"] = data["commits"][-30:]
    
    # Write updated data
    with open('data/activity.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Activity updated at {current_time}")

if __name__ == "__main__":
    update_activity()
