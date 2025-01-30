from langchain.prompts import PromptTemplate, load_prompt

template = "Question: {user_question} \n\n Response: Review step by step"
prompt = PromptTemplate.from_template(template)

file_name = "prompt_example.json"
prompt.save(file_name)


prompt_from_json = load_prompt(file_name)
print(prompt_from_json)