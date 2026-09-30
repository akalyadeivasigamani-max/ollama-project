import streamlit as st
import requests

st.set_page_config(
    page_title="Python AI Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Python AI Assistant")
st.write("Ask anything about Python")

prompt = st.text_input(
    "Enter your question:",
    placeholder="Explain Python in simple terms"
)

if st.button("Generate Answer"):
    if prompt:
        url = "http://localhost:11434/api/generate"

        data = {
            "model": "llama3.2:1b",
            "prompt": prompt,
            "stream": False
        }

        try:
            response = requests.post(url, json=data)

            if response.status_code == 200:
                result = response.json()

                st.subheader("💡 AI Response")
                st.write(result["response"])

            else:
                st.error("Error connecting to Ollama")

        except requests.exceptions.ConnectionError:
            st.error(
                "Ollama is not running. "
                "Please start Ollama and try again."
            )
    else:
        st.warning("Please enter a question.")