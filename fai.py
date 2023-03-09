import openai
import pyttsx3

# Replace with your OpenAI API key
openai.api_key = "sk-lFJVvhb8wPwDWBjRzhdUlFY"

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the voice rate
engine.setProperty("rate", 150)

# Function to get a response from OpenAI ChatGPT
def get_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Function to speak the response using the text-to-speech engine
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Ask for user input and get a response from OpenAI ChatGPT
while True:
    prompt = input("Ask FAI anything: ")
    if prompt.lower() == "exit":
        break
    response = get_response(prompt)

    # Print the response and speak it out
    print("Response:", response)
    speak(response)
