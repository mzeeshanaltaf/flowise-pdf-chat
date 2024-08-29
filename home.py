from util import *


if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
if "response" not in st.session_state:
    st.session_state.response = None


def show_home():

    # TITLE PAGE
    st.title("Chat with PDF💬📄")
    st.write(":blue[***Powered by Flowise***]")

    #  UPLOAD SECTION
    st.subheader('Upload PDF⬆️:')
    uploaded_file = st.file_uploader("Upload your PDFs", type=['pdf'], label_visibility='collapsed')
    upload = st.button("Create Vector DB", type="primary", key="process", disabled=not uploaded_file)

    if upload:
        # Create Vector Database
        create_vectordb(uploaded_file)

    st.subheader('Chatbot🤖:')
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if question := st.chat_input(placeholder='Enter your question related to uploaded document',
                                 disabled=not uploaded_file):
        st.session_state.messages.append({"role": "user", "content": question})
        st.chat_message("user").write(question)
        with st.spinner('Processing...'):
            response = get_llm_response(question)
            st.session_state.response = response
            st.session_state.messages.append({"role": "assistant", "content": st.session_state.response})
            st.chat_message("assistant").write(st.session_state.response)
