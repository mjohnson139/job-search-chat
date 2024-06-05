import streamlit as st

def create_application():
    create_setup()

def create_setup():
    st.title("Job Seekers Knowledgebase.")
git
    st.info("Please add any files you want to use in your job application database. Once done, click on Process to add them to your knowledge base.")
    
    uploaded_files = st.file_uploader("Please upload your PDF files", type="pdf", accept_multiple_files=True)
    
    if st.button("Process", type="primary"):        
        with st.spinner('Moving your files into docs folder'):
            print("moving the files")
            # view_model.save_files(uploaded_files=uploaded_files)

        with st.spinner('Ingesting documents...'):
            # view_model.ingest_docs()
            st.session_state.show_chat = True
            st.rerun()
    
