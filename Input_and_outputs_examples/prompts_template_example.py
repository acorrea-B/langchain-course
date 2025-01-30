from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from open_ai_client import chat

# Define template to system
system_template = "You are an AI especilized in type car {type_car} and generate articles to read in {time_read}"
system_message_promt = SystemMessagePromptTemplate.from_template(system_template)

# Print variables required to use in system template
print(system_message_promt.input_variables)

# Create template to user
human_template = "I need an article to car with motor {required_motor}"
human_message_template = HumanMessagePromptTemplate.from_template(human_template)

# Print variables required to use in human template
print(human_message_template.input_variables)

# Concatenate templates
chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_promt, human_message_template]
)

messages = chat_prompt.format_prompt(
    required_motor="Hibryd", time_read="10 minnutes", type_car="japaneses"
).to_messages()


response = chat.invoke(messages)

print(response.content)