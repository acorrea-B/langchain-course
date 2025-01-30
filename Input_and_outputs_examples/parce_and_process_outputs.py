from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.output_parsers import CommaSeparatedListOutputParser

from open_ai_client import chat

output_parser = CommaSeparatedListOutputParser()

# Get innstruccions to pass LLM
format_instructions = output_parser.get_format_instructions()

print(format_instructions)

human_template = "{request}\n {format_instructions}"
human_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([human_prompt])

message = chat_prompt.format_prompt(
    request="Tell me 5 caracteristics of American cars",
    format_instructions=format_instructions,
).to_messages()


response = chat.invoke(message)

print(response.content)