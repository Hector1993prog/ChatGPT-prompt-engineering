import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())


def get_completion(prompt, model="gpt-3.5-turbo"):

    '''
    This functions calls the openai.ChatCompletion class and 
    uses to complete the response of the model with your prompts.
    '''
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_temp(prompt, model="gpt-3.5-turbo",temperature=0): 
    '''
    This functions calls the openai.ChatCompletion class and 
     uses it to complete the response of the model with your prompts.
    It also allows to change the temp value, which will provide
    a more complete answer from the LLM.
    '''
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    '''
    This functions calls the openai.ChatCompletion class and 
    uses it to complete the messages of the model with your prompts as a user.
    It also allows to change the temp value, which will provide
    a more complete answer from the LLM. It is a chatbot prompt system.
    '''
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]

def collect_messages(_):
    prompt = inp.value_input
    inp.value = ''
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context) 
    context.append({'role':'assistant', 'content':f"{response}"})
    panels.append(
        pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(response, width=600, style={'background-color': '#F6F6F6'})))
 
    return pn.Column(*panels)



