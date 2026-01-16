<div align="center">

# Fakify - The place where fake news starts to sweat
Fakify is a modern fake news detector powered by the Mistral and Exa API's
</div>

### Discalimer: AI can sometimes produce wrong results or hallucinate. Please check critical information manually.

## How it works 🔎
1. Paste in the URL of the article you want to check
2. The Exa API will firstly get the websites content
3. Mistral medium API will then generate a search query for Exa search
4. Exa search will then get similar articles related to the topic
5. Mistral large will then generate a comprehensive review of the article based on content and similar results on the internet
6. The result is then displayed to you (the user) throughout the sleek and clean Streamlit UI -> It sould then contain the different aspects such as 'Claim', 'Source Credibility', 'Language Used', 'Inconsistencies', and 'Overall Assessment'

## Tech Stack 📚
- Frontend: [Streamlit](https://streamlit.io/) (Python)
- Website Context: [Exa Context API](https://exa.ai/docs/reference/get-contents)
- Search query generation: [Mistral API (Model: Mistral Medium)](https://mistral.ai/news/mistral-medium-3)
- AI Search: [Exa Search API](https://exa.ai/docs/reference/search)
- Brief AI Summary (Model: Mistral Large latest) -> [Mistral-large-latest](https://mistral.ai/news/mistral-3)

## Fakify RAG architecture 
<img width="988" height="573" alt="Fakify activity flowchart (2026-01-11 15 36 25) excalidraw" src="https://github.com/user-attachments/assets/aa943451-a3a8-4c31-91e6-34f08f0e151f" />

[Get the flowchart as a PDF](https://github.com/user-attachments/files/24555013/Fakify.activity.flowchart.2026-01-11.15.36.25.excalidraw.pdf)

## Definition RAG (Retrieval-augmented generation) 

> \[!NOTE]
> Retrieval-augmented generation (RAG) is a technique that enables large language models (LLMs) to retrieve and incorporate new information from external data sources. With RAG, LLMs do not respond to user queries until they refer to a specified set of documents. These documents supplement information from the LLM's pre-existing training data.

## Screenshots

<img width="765" height="1218" alt="Bildschirmfoto 2026-01-11 um 18 51 05" src="https://github.com/user-attachments/assets/a0f95589-27ac-4efb-bf40-b10e153e2770" />

### Please mind your usage. Thank you! (My API credit balance is not infinite --> 1 query ≈ 0.50$)

## Project information ℹ️
- Duration of the Project (Beginnging - End): 10. Janurary 2026 - 12. Janurary 2026
- Sticky notes used: ≈ 0
- Hours I spend building this Project: ≈ 10h
