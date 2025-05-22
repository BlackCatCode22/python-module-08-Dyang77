import openai
import datetime

openai.api_key = "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"  #

def chat_with_gpt():
    print("Master AI : Hi! Type 'exit' to quit.")

    messages = [{"role": "system", "content": "You are a helpful assistant."}]

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Master AI : Goodbye!")
            break

        #  Time check
        if "time" in user_input.lower():
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            print("Master AI:", f"The current time is {current_time}")
            continue

        messages.append({"role": "user", "content": user_input})

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        reply = response.choices[0].message.content
        print("Master AI:", reply)

        messages.append({"role": "assistant", "content": reply})


# Start the chatbot
chat_with_gpt()


