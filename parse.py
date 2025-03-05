from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Define the template for the prompt that will be used to interact with the Llama model
template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

# Initialize the OllamaLLM model (Llama3) to interact with it
model = OllamaLLM(model="llama3.1")

# Define a function to parse the DOM content based on a provided description using the Llama model
def parse_with_ollama(dom_chunks, parse_description):
    # Create a prompt template from the defined template string, and bind dynamic values like dom_content and parse_description
    prompt = ChatPromptTemplate.from_template(template)

     # Chain the prompt with the model so that the prompt gets passed to the model for processing
    chain = prompt | model

     # Initialize an empty list to store the parsed results
    parsed_result = []

    # Loop through each chunk of DOM content and apply the model to extract the requested information
    for i, chunk in enumerate(dom_chunks, start=1):
         # Invoke the chain (the prompt and model) to get the response for the current chunk
        response = chain.invoke(
            {"dom_content": chunk, "parse_description": parse_description}
        )
         # Print progress to the console, showing which batch of chunks is currently being processed
        print(f"Parsed batch {i} of {len(dom_chunks)}")
         # Append the model's response for this chunk to the parsed_result list
        parsed_result.append(response)

     # Join the parsed results for all chunks into a single string and return it
    return "\n".join(parsed_result)