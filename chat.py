import streamlit as st
import ollama

def generate_llm_response(prompt,model="llama3.2"):

    messages=[
        {
            'role':'user',
            'content':prompt,
        }
    ]

    response = ollama.chat(model=model,messages=messages)
    return response['message']['content']

st.title("ChatZone")
st.write("Meet ChatZone, your smart companion for instant answers & helpful chats. Ask me anything & I'll do my best to assist!")

user_prompt=st.text_area("Enter the prompt")

if st.button("Generate Response"):
    if user_prompt.strip()!="":
        with st.spinner("Generating response.."):
            try:
                response=generate_llm_response(user_prompt)
                st.success("Response generated!")
                st.text_area("LLM Response:", value=response,height=200)
            except Exception as e:
                st.error(f"error: {str(e)}")
    else:
        st.warning("please enter a prompt.")

