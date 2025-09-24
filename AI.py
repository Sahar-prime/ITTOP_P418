from mistralai import Mistral
API_KEY = "R0KfhkjCVoa8Y5fFjd2yn8s4zoASkbd5"

model = "mistral-large-latest"

messages = [
    {
        "role": "system",
        "content": ""
    }
]


def get_chat_response(message: str, model: str, client: Mistral) -> str:
    user_question = {
        "role": "user",
        "content": message,
    }
    messages.append(user_question)

    chat_response = client.chat.complete(
        model=model,
        messages=messages
    )

    messages.append(
        {
            "role": "assistant",
            "content": chat_response.choices[0].message.content
            }
        )

    return chat_response.choices[0].message.content


def main() -> None:
    client = Mistral(api_key=API_KEY)

    while True:
        user_message = input("Введите сообщение:\n")
        if user_message == "exit":
            input("Для выхода нажмите Enter")
            break

        messages.append(
            {
                "role": "user",
                "content": user_message
            }
        )

        response = get_chat_response(user_message, model, client)
        messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )
        print(response)


main()
