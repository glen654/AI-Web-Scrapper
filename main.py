import streamlit as st
from scrape import scrape_website, split_dom_content, clean_body_content, extract_body_content
from parse import parse_with_ollama

st.title("AI Web Scrapper")
url = st.text_input("Enter a website URL: ")

if st.button("Scrape Site"):
    st.write("Scraping the website")
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)
     # Save the cleaned content into Streamlit's session state to be used later
    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)

# Check if there's any 'dom_content' stored in session state (i.e., after scraping)
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse?")

    # When the user clicks the "Parse Content" button
    if st.button("Parse Content"):
        if parse_description: # Check if the user has entered a description
            st.write("Parsing the content") # Inform the user that parsing is happening
            # Split the DOM content into smaller chunks using the split_dom_content function
            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_description)
            st.write(result)