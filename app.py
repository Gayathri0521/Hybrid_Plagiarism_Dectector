import streamlit as st
from utils import extract_text, compute_similarity

# Page Title
st.title("Hybrid Multimodal Plagiarism Detection System")

st.write("Upload two files to check plagiarism similarity.")

# Upload Files
file1 = st.file_uploader("Upload File 1", type=["txt", "png", "jpg", "jpeg"])
file2 = st.file_uploader("Upload File 2", type=["txt", "png", "jpg", "jpeg"])

# Button
if st.button("Check Plagiarism"):

    if file1 and file2:

        text1 = extract_text(file1)
        text2 = extract_text(file2)

        tfidf, bert, final = compute_similarity(text1, text2)

        st.success("Analysis Completed")

        st.write(f"TF-IDF Similarity: {round(tfidf*100,2)}%")
        st.write(f"BERT Similarity: {round(bert*100,2)}%")
        st.write(f"Final Score: {round(final*100,2)}%")

        if final > 0.7:
            st.error("High Plagiarism Detected")
        elif final > 0.4:
            st.warning("Moderate Similarity")
        else:
            st.success("Low Plagiarism")

    else:
        st.warning("Upload both files")