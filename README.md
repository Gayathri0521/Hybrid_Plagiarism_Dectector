# Hybrid Multimodal Plagiarism Detection System

Implementation of the system described in the paper:

**"Hybrid Multimodal Plagiarism Detection System Integrating Lexical–Semantic Analysis with OCR-Based Image Processing"**

---

# Overview

This project is a Hybrid Multimodal Plagiarism Detection System developed using Python and Streamlit.

The system detects plagiarism by combining:

- OCR (Optical Character Recognition)
- TF-IDF Similarity
- Sentence-BERT Semantic Similarity

The project supports both text-based and image-based documents.

---

# Features

- TF-IDF Similarity for direct text matching
- Sentence-BERT Similarity for semantic/paraphrased detection
- OCR Support using Tesseract
- Supports image and text files
- Hybrid weighted similarity score
- Interactive Streamlit UI
- Plagiarism verdict generation

---

# Technologies Used

- Python
- Streamlit
- Sentence-Transformers
- Scikit-learn
- Pytesseract
- Pillow
- NLTK

---

# Supported Input Formats

- `.txt`
- `.png`
- `.jpg`
- `.jpeg`

---

# Project Structure

```text
Hybrid_Plagiarism_Detector/
│
├── app.py
├── utils.py
├── requirements.txt
├── README.md
├── uploads/



Workflow
User Uploads Files        ↓File Type Detection        ↓OCR Processing (if image)        ↓Text Preprocessing        ↓TF-IDF Similarity        ↓Sentence-BERT Similarity        ↓Hybrid Score Calculation        ↓Plagiarism Result

Module Description
Input Module
Accepts uploaded files from the user.
OCR Module
Extracts text from images using Tesseract OCR.
Preprocessing Module
Performs:


Lowercase conversion


Stopword removal


Tokenization


Punctuation removal


TF-IDF Module
Measures lexical similarity between documents.
Sentence-BERT Module
Measures semantic similarity between documents.
Similarity Aggregator
Combines TF-IDF and BERT similarity.

Similarity Formula
Final Score = (TF-IDF Score + BERT Score) / 2

Verdict Thresholds
Similarity ScoreVerdict> 70%High Plagiarism40% – 70%Moderate Similarity< 40%Low Similarity

Installation
Install required packages:
pip install -r requirements.txt

Run Project
streamlit run app.py
Open browser:
http://localhost:8501

Advantages


Supports multiple file formats


Detects semantic plagiarism


Handles image documents


User-friendly interface


Fast plagiarism detection



Future Scope


PDF support


Highlight copied text


Database integration


AI-generated text detection



Conclusion
This project combines OCR, TF-IDF, and Sentence-BERT to build a hybrid plagiarism detection framework.
It improves plagiarism detection by supporting both textual and image-based content.
