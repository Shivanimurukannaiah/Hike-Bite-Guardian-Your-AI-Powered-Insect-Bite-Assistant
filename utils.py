from bug_data import bug_bite_database

def identify_bug(description):
    """
    Identifies the most likely bug based on the user's symptom description.
    """
    description = description.lower()

    for bug, details in bug_bite_database.items():
        if any(keyword in description for keyword in [bug, "bite", "rash", "swelling", "pimples"]):
            return {
                "Identified Bug": bug.capitalize(),
                "Symptoms": details["symptoms"],
                "Severity": details["severity"],
                "Bug Information": details["info"],
                "First Aid": details["first_aid"]
            }

    return {
        "Identified Bug": "Unknown",
        "Symptoms": "N/A",
        "Severity": "N/A",
        "Bug Information": "No match found.",
        "First Aid": "Try applying ice and monitoring symptoms."
    }
