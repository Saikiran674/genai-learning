from openai import OpenAI

# Hardcode your API key (⚠️ don't commit this to GitHub!)
client = OpenAI(api_key="YOUR_API_KEY_HERE")

conversation = [
    {"role": "system", "content": "You are a helpful assistant."}
]

print("🤖 AI Chatbot (type 'exit' to quit)")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    conversation.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",   # efficient model
            messages=conversation
        )
        answer = response.choices[0].message.content
        print("AI:", answer)

        # Add assistant reply to conversation (memory)
        conversation.append({"role": "assistant", "content": answer})

    except Exception as e:
        print("⚠️ Error:", e)
