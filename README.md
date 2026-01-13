<div align="center">

# Fakify - The place where fake news starts to sweat
Fakify is a modern fake news detector powered by the Mistral and Exa API's
</div>

## Tech Stack 📚
- Frontend: Streamlit (Python)
- Website Context: Exa Context API
- Search query generation: Mistral API (Model: Mistral Medium) 
- AI Search: Exa Search API
- Brief AI Summary (Model: Mistral Large latest)

## Fakify RAG architecture 
<img width="988" height="573" alt="Fakify activity flowchart (2026-01-11 15 36 25) excalidraw" src="https://github.com/user-attachments/assets/aa943451-a3a8-4c31-91e6-34f08f0e151f" />

[Get the flowchart as a PDF](https://github.com/user-attachments/files/24555013/Fakify.activity.flowchart.2026-01-11.15.36.25.excalidraw.pdf)

## Definition RAG (Retrieval-augmented generation)

> [!TIP] What is the RAG architecture?
> Retrieval-augmented generation (RAG) is a technique that enables large language models (LLMs) to retrieve and incorporate new information from external data sources. With RAG, LLMs do not respond to user queries until they refer to a specified set of documents. These documents supplement information from the LLM's pre-existing training data.