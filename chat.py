import openai

openai.api_key="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"
chat_history=[]



while True:
    prompt= input("Enter a prompt:")
    if prompt == "exit":
        break
    else:
        chat_history.append({
                    "role" : "user",
                    "content":prompt,
                })
        response=openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_history,
            stream=True,
            max_tokens=500
        )

        collected_messages=[]

        for chunk in response:
            chunk_message=chunk["choices"][0]["delta"]
            collected_messages.append(chunk_message)
            fully_repy_content=''.join([m.get('content','') for m in collected_messages])
            print("\033[H\033[J", end="")
            print(fully_repy_content)
        print("\033[H\033[J", end="")
        print(fully_repy_content)
        chat_history.append({"role":"assistant","content":fully_repy_content})
        