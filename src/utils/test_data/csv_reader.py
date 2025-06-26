import csv
import os
import random
import requests
from io import StringIO
from dotenv import load_dotenv

# Explicitly load the .env file from the config folder
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../../config/.env'))

def get_random_credentials_from_google_sheet(role):
    # Load environment variables
    
    
    # Fetch CSV data from the URL
    csv_url = os.getenv("CSV_FILE_URL")
    if not csv_url:
        raise ValueError("CSV_FILE_URL is not set in the environment")
    
    response = requests.get(csv_url)
    response.raise_for_status()  
    lines=response.text.splitlines()

    header_row_index = None
    for i, line in enumerate(lines):
        if "Learner Email" in line and "TP Email" in line and "Admin Email" in line:
            header_row_index = i
            break
    if header_row_index is None:
      raise Exception("Could not find header row with required columns")  
    
    csvfile = StringIO("\n".join(lines[header_row_index:]))
    reader = csv.DictReader(csvfile)
    
    cleaned_fieldnames = []

    for name in reader.fieldnames:
        if name:
            cleaned_fieldnames.append(name.strip())
        else:
            cleaned_fieldnames.append('')

    reader.fieldnames = cleaned_fieldnames
    
    users = []
    for row in reader:
        if role == "learner" and row.get("Learner Email") and row.get("Learner Password"):
            users.append({
                "email": row["Learner Email"].strip(),
                "password": row["Learner Password"].strip(),
                "url": "https://beta.findyourcourses.org/signin"
            })
        elif role == "trainer" and row.get("TP Email") and row.get("TP Password"):
            users.append({
                "email": row["TP Email"].strip(),
                "password": row["TP Password"].strip(),
                "url": "https://beta-tp.findyourcourses.org/login"
            })
        elif role == "admin" and row.get("Admin Email") and row.get("Admin Password") :
            users.append({
                "email": row["Admin Email"].strip(),
                "password": row["Admin Password"].strip(),
                "url": "https://beta-admin.findyourcourses.org/"
            })

    if not users:
     print(f"No users found for role {role} in CSV.")
     raise Exception(f"No credentials found for role: {role}")

    return random.choice(users)

def get_untried_trainer(tried_emails,max_attempts=5):
    attempts=0
    used=set()

    while attempts <max_attempts:
        trainer=get_random_credentials_from_google_sheet("trainer")
        email=trainer["email"]

        if email not in tried_emails:
            return trainer
        
        attempts+=1
    raise Exception ("No untrained found after max tries")