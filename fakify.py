#IMPORTS
import streamlit as st
#from openai import OpenAI
#from groq import Groq
from mistralai import Mistral
from exa_py import Exa
import os
from dotenv import load_dotenv
import time

from streamlit import chat_message

#--------------------------------------------------------------------------
#Config
st.set_page_config(
    page_title="Fakify by Tim Seufert",
    page_icon="🔎",
    layout="centered", # Huh
    initial_sidebar_state="auto" #Huh
)


# Remove "Made with Streamlit" footer
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>    
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

#--------------------------------------------------------------------------
#FRONTEND (UI)
# content_generated = False
# generating_search = False
# doing_search = False
# creating_final_res = False

st.markdown("""
   ### Fakify - The fake news detector built by [Tim Seufert](https://timhongphuc.de)
""")

input_text = st.text_input( #VAR for input text below
        "AI can sometimes produce wrong results or hallucinate. Please check critical information manually.",
        placeholder="Enter the Articles URL here",
    )

if input_text:
    with st.status("Generating response...", expanded=True) as status:

#--------------------------------------------------------------------------
# EXA API (Content Endpoint)
        load_dotenv()

        st.write("Getting articles content...")

        if input_text:
            exa = Exa(api_key = os.environ.get("EXA_API_KEY"))

            response = exa.get_contents(
                urls=[input_text],
                text= True
            )

            article_content = response.results[0].text
            print(article_content)

#--------------------------------------------------------------------------
# #MISTRAL API (Endpoint No1) Search query for Exa API
        load_dotenv()

        st.write("Generating search query...")

        if input_text:
            client = Mistral(api_key=os.environ.get("MISTRAL_API_KEY"))

            inputs = [
                {"role": "user", "content": f"Generate ONE search query: {article_content}",}
            ]

            response = client.beta.conversations.start(
                agent_id= os.environ.get("AGENT_ID"), #System prompt is included in the Mistral API Dashboard
                inputs=inputs,
            )

            # Extract the clean markdown content from the response
            search = response.outputs[0].content

            print(search)
            #st.markdown(search)
            print("Received search query!")

#--------------------------------------------------------------------------
# EXA API (Search Endpoint)
            exa = Exa(api_key = os.environ.get("EXA_API_KEY"))

            st.write("Fetching results...")

            result = exa.search_and_contents(
              search,
              category = "news",
              livecrawl = "fallback",
              num_results=4,
              summary = {
                "query": "Your task is to create a brief AI summary of the Webpage. Max. 20 Words"
              },

              text = True,
              type = "auto"
            )

            search_results = result.results[3].text #Take the first 4 Search results (in index 3)
            print(search_results)
            print("Results fetched!")

#--------------------------------------------------------------------------
# Mistral API (API Endpoint No2) AI Summary of RAG analysis
            st.write("Analyzing insights...")
            time.sleep(3)
            st.write("Writing final response...")


            with Mistral(
                api_key=os.environ.get("MISTRAL_API_KEY"),
            ) as mistral:

                res = mistral.chat.complete(model="mistral-large-latest", messages=[
                    {
                       "content": f"Please provide me with an comprehensive analysis. These are the sources you can use to fulfill your task: The content of the News article you HAVE to check: {article_content}, similar search results to the topic (to verify credibility). Take a deep look into the sources: {search_results}. These sources are really important. If there are other Websites that provide the same information as given in the article, rate the article as real or likely real. If the topic in the article appears in other sources and the source is trustworthy change the rating accordingly.",
                       "role": "user"
                    },
                    {
                        "content": os.environ.get("SYSTEM_PROMPT"),
                        "role": "system"
                    },
                ], stream=False)

                # Handle response
                results_final = res.choices[0].message.content
                print(results_final)

                #with st.chat_message("user"):
                print("Finished analysis!")
        #else:
            #st.info("☝️ Please enter a valid URL to start the analysis.")

            status.update(
                label="Check complete!", state="complete", expanded=False
            )

    with st.expander("See similar articles"):
        st.markdown(""" ### Search is provided by Exa """)
        #st.markdown(f'''
         #   {search_results}
        #''')
        st.text("The feature 'See similar articles' got temporarily disabled for maintenance")

    with chat_message("assistant"):
        st.markdown(results_final)

#--------------------------------------------------------------------------
#GROQ API
# load_dotenv()
#
# client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
# chat_completion = client.chat.completions.create(
#     messages=[
#         # Set an optional system message. This sets the behavior of the
#         # assistant and can be used to provide specific instructions for
#         # how it should behave throughout the conversation.
#         {
#             "role": "system",
#             "content": os.environ.get("SYSTEM_PROMPT")
#         },
#         # Set a user message for the assistant to respond to.
#         {
#             "role": "user",
#             "content": input_text,
#         }
#     ],
#
#     # The language model which will generate the completion.
#     model="openai/gpt-oss-20b"
# )
#
# # Print the completion returned by the LLM.
# print(chat_completion.choices[0].message.content)
#
# st.markdown(f"{chat_completion.choices[0].message.content}") #Display result in the UI
