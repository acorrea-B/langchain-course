from langchain.schema import SystemMessage, HumanMessage
from open_ai_client import chat


# Short response
result = chat.invoke([HumanMessage(content="Can you tell me where is caceres?")])

print(result.content)

# Response more detail
messages = [
    SystemMessage("You are a histori and you know all about world cities."),
    HumanMessage(content="Can you tell me where is caceres?"),
]

result = chat.invoke(messages)

print(result.content)


messages = [
    [
        SystemMessage(content="You are a histori and you know all about world cities."),
        HumanMessage(content="Can you tell me where is caceres?"),
    ],
    [
        SystemMessage(
            content="You are a rude young, you don't responde questions, you prefer party"
        ),
        HumanMessage(content="Can you tell me where is caceres?"),
    ],
]

result = chat.generate(messages)

# Response to firts message
print(result.generations[0][0].text)

# Respose to second message
print(result.generations[1][0].text)
