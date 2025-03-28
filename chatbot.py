import google.generativeai as genai
import time

def configure_gemini():
    API_KEY = ""  # Replace with your actual API key
    genai.configure(api_key=API_KEY)
    return genai.GenerativeModel("gemini-2.0-flash")
    
def get_motivational_response(model, mood, situation):
    if not mood or not situation:
        return "I’m here to help. Could you share a bit more about how you're feeling?"
    
    prompt = (
        f"I am feeling {mood} because {situation}. "
        "Give me a thoughtful, empathetic, and uplifting motivational response. "
        "If relevant, include practical advice or a calming affirmation."
    )
    
    response = model.generate_content(prompt)
    return response.text if response else "Sorry, I couldn't generate a response."

def ask_followup():
    followup = input("Would you like to share more about your situation? (yes/no): ").strip().lower()
    if followup == "yes":
        additional_info = input("Tell me more about what's on your mind: ").strip()
        return additional_info
    return ""

def main():
    print("\n💬 Welcome to Therorpist – Your AI Therapy Companion! 💬")
    model = configure_gemini()
    cached_mood, cached_situation = "", ""
    
    while True:
        print("\n📝 Let's talk...")
        if cached_mood and cached_situation:
            reuse = input("Would you like to continue our previous conversation? (yes/no): ").strip().lower()
            if reuse == "yes":
                mood, situation = cached_mood, cached_situation
            else:
                mood = input("How are you feeling? ").strip()
                situation = input("What’s happening? ").strip()
        else:
            mood = input("How are you feeling? ").strip()
            situation = input("What’s happening? ").strip()
        
        additional_info = ask_followup()
        if additional_info:
            situation += " " + additional_info
        
        print("\n⏳ Thinking...")
        time.sleep(1)  # Simulate processing time
        
        response = get_motivational_response(model, mood, situation)
        print("\n🤖 Therorpist:", response, "\n")
        
        cached_mood, cached_situation = mood, situation  # Cache conversation
        
        cont = input("Would you like more motivation or some calming exercises? (motivation/exercise/no): ").strip().lower()
        if cont == "exercise":
            print("\n🌿 Try this: Take a deep breath in... Hold for 4 seconds... Slowly exhale. Repeat 3 times. Feel better? 💖")
        elif cont != "motivation":
            print("\n💪 Stay strong, and take care! You got this! 💖")
            break

if __name__ == "__main__":
    main()
