import json
import os

from application import JobApplication

DATA_FILE = "data/applications.json"


def load_applications():
    """
    Load applications from the JSON file.
    Returns a list of JobApplication objects.
    """
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        applications_data = data.get("applications", [])
        return [
            JobApplication.from_dict(item)
            for item in applications_data
        ]

    except json.JSONDecodeError:
        return []


def save_applications(applications):
    """
    Save applications to the JSON file.
    """
    data = {
        "applications": [
            application.to_dict()
            for application in applications
        ]
    }

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
        