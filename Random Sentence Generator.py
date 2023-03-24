import openai

# Set your OpenAI API key
openai.api_key = "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"

# Receive input as a string separated by commas
input_str = input("Enter words separated by commas: ")

# Split the input string into a list of words
words = input_str.split(",")

# Generate completions for each word and store the results in separate variables
for i, word in enumerate(words):
    prompt = f"Make a long sentence with the word {word.strip()}"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.7,
    )
    completion = response.choices[0].text.strip()
    
    # Store the completion in a separate variable based on the index of the current word
    globals()[f"sentence{i+1}"] = completion

# Print the resulting sentences
for i, word in enumerate(words):
    print(f"Sentence {i+1}: {globals()[f'sentence{i+1}']}")