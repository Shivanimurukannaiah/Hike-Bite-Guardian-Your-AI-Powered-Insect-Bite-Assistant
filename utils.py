import openai
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

def generate_bug_response(bug_info):
    """
    Formats the bug response in an ordered manner.
    """
    return f"""
    **🦟 Hike Bite Guardian**  
    Identify insect bites and get first-aid guidance.  

    **Identified Bug:** {bug_info["Identified Bug"]}  
    **Symptoms:** {bug_info["Symptoms"]}  
    **Severity:** {bug_info["Severity"]}  
    **Bug Information:** {bug_info["Bug Information"]}  
    **First Aid:** {bug_info["First Aid"]}  
    """

def generate_image(prompt, openai_api_key):
    """
    Uses OpenAI's DALL·E to generate an image based on the prompt.
    """
    client = openai.OpenAI(api_key=openai_api_key)
    
    response = client.images.generate(
        model="dall-e-3",
        prompt=f"A realistic image of a {prompt} bite with skin reaction",
        size="1024x1024"  # Updated size to 1024x1024
    )
    
    return response.data[0].url  # Return the image URL
