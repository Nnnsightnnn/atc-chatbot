"""This module contains the code to communicate with the language model (e.g., GPT-4)"""
import os
import openai
from dotenv import load_dotenv
from langchain.llms import OpenAI
from data_structure import get_best_matching_document_content

load_dotenv()

def embed_text(elements):
    """Your code to embed the text into a vector space"""
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    elements = openai.Embedding.create(
        input=elements,
        model="text-embedding-ada-002"
    )
    return elements


def generate_summary(document_content):
    """this function generates a summary from document content"""
    openapi_key = os.environ.get("OPENAI_API_KEY")
    llm = OpenAI(temperature=0.2, max_tokens=300, api_key=openapi_key)

    summary_prompt = (f"Please provide a brief summary of the"
                      f"following information:\n{document_content}")
    summary = llm(summary_prompt)
    return summary


def communicate_with_llm(user_message):
    """Your code to communicate with the language model (e.g., GPT-4)"""
#initialize llm
    api_key = os.environ.get("OPENAI_API_KEY")
    llm = OpenAI(temperature=0.9, max_tokens=200, api_key=api_key)
#create document content for llm
    document_content = get_best_matching_document_content(user_message)
#logic for document content
    if document_content:
        summary = generate_summary(document_content)
        new_prompt = (f"{user_message}\n\nBased on the summary of the relevant information:"
                      f"\n{summary}\n\nPlease provide an informed and natural response: ")
        response = llm(new_prompt)
#logic for no document content
    else:
        response = llm(user_message)

# Return the response string (replace 'response' with the actual response variable if different)
    return response
