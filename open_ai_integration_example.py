from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from os import environ


open_ai_key = environ.get("OPEN_API_KEY")

chat = ChatOpenAI(api_key=open_ai_key)
# Short response
resultado = chat.invoke([HumanMessage(content="Can you tell me where is caceres?")])

print(resultado.content)

# Response more detail
messages = [
    SystemMessage("You are a histori and you know all about world cities."),
    HumanMessage(content="Can you tell me where is caceres?"),
]

resultado = chat.invoke(messages)

print(resultado.content)


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

resultado = chat.generate(messages)

# Response to firts message
print(resultado.generations[0][0].text)

# Respose to second message
print(resultado.generations[1][0].text)
