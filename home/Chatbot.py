import openai as ai

ai.api_key = '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'

def generate_gpt3_response(user_text, print_output=False):
    """
    Query OpenAI GPT-3 for the specific key and get back a response
    :type user_text: str the user's text to query for
    :type print_output: boolean whether or not to print the raw output JSON
    """
    completions = ai.Completion.create(
        engine='text-davinci-003',  # Determines the quality, speed, and cost.
        temperature=0.5,            # Level of creativity in the response
        prompt=user_text,           # What the user typed in
        max_tokens=100,             # Maximum tokens in the prompt AND response
        n=1,                        # The number of completions to generate
        stop=None,                  # An optional setting to control response generation
    )

    # Displaying the output can be helpful if things go wrong
    if print_output:
        print(completions)

    # Return the first choice's text
    return completions.choices[0].text

text = generate_gpt3_response('hellow', True)
#models = ai.Model.list()

#for model in models.data:
#    print(model.id)


'''
if __name__ == '__main__':
    prompt = input("")
    response = generate_gpt3_response(prompt)
    
    file2write=open(prompt.split()[:3] +".txt",'w')
    file2write.write(response)
    file2write.close()

'''