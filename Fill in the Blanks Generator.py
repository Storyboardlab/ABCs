import openai
import re

# Set your OpenAI API key
openai.api_key = "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"

# Receive input as a string separated by commas
input_str = input("Enter words separated by commas: ")

# Receive length of blank line as an integer
blank_length = int(input("Enter the length of the blank line: "))

# Split the input string into a list of words
words = input_str.split(",")

# Generate completions for each word and store the results in separate variables
sentences = []
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

    # Store the completion in a separate variable
    sentences.append(completion)

    # Replace all occurrences of the input word with the blank line in the sentence
    pattern = re.compile(r"\b" + re.escape(word.strip()) + r"(\w*)\b", re.IGNORECASE)
    blank_line = "_" * blank_length
    sentences[i] = pattern.sub(blank_line, sentences[i])

# Print the resulting sentences
for i, sentence in enumerate(sentences):
    print(f"Sentence {i+1}: {sentence}")
