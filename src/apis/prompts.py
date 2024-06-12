from langchain_core.prompts import ChatPromptTemplate

TEMPLATES = [
    {
        'id': 'SUCCESS',
        'template': '''You are responsible for writing creative notification messages for script executions.\
Write a creative message stating that an script ran successfully. \
As the message will be sent via Telegram, avoid characters that will not be interpreted correctly. \
Use emojis as much as you like. Keep an average of approximately 400 characters in your response. \
The script took {execution_time} to execute.\
The message must be written entirely in Brazilian Portuguese''',
    },
    {
        'id': 'error',
        'template': '''You are responsible for writing creative notification messages for script executions. \
Write a creative message stating that an error occurred while running the script. \
As the message will be sent via Telegram, avoid characters that will not be interpreted correctly. Use emojis as much as you want. \
Keep your response to an average of approximately 400 characters. \
The script took {execution_time} to execute.\
The error that occurred was: {error}. \
The message must be written entirely in Brazilian Portuguese.''',
    },
]


for template in TEMPLATES:
    template['prompt'] = ChatPromptTemplate.from_template(template['template'])


def get_prompt(template_id: str) -> ChatPromptTemplate:
    template = next((t for t in TEMPLATES if t['id'] == template_id), None)
    if template is None:
        raise ValueError(f'Invalid template id: {template_id}')
