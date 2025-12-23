import google.generativeai as genai

Api_KEY = "AIzaSyDqmD8mNMP4yvSmSvNLbQ5E3ogUiO-eg9k"
genai.configure(api_key=Api_KEY)


model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

print("Chat with CASPHER! Type 'exit' to end the convo.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Ending the chat. Goodbye!")
        break

    response = chat.send_message(user_input)
    print("CASPHER: " + response.text)
