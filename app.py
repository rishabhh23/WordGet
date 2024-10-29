import streamlit as st
from utils.processing import extract_text

def main():
    st.title("OCR Web Application with Tesseract")
    st.write("Upload an image to extract text.")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        with st.spinner("Extracting text..."):
            extracted_text = extract_text(uploaded_file)
            st.write("Extracted Text:")
            st.text_area("OCR Output", extracted_text, height=250)

        search_query = st.text_input("Enter keywords to search within the extracted text:")
        if search_query:
            if search_query.lower() in extracted_text.lower():
                highlighted_text = extracted_text.replace(search_query, f"**<span style='color: red;'>{search_query}</span>**")
                st.markdown(highlighted_text, unsafe_allow_html=True)
            else:
                st.write("No matches found.")

if __name__ == "__main__":
    main()
