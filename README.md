# Hybrid Multimodal Plagiarism Detection System

Implementation of the system described in the paper:

"Hybrid Multimodal Plagiarism Detection System Integrating Lexical–Semantic Analysis with OCR-Based Image Processing"

---

## Overview

This project presents a Hybrid Multimodal Plagiarism Detection System that combines lexical similarity, semantic similarity, OCR-based extraction, and PDF text processing within a unified framework.

The system is designed to detect plagiarism in both text-based and image-based academic documents.

---

## Features

* TF-IDF Similarity for direct text matching
* Sentence-BERT Similarity for semantic and paraphrased content detection
* OCR Support using Tesseract for image files
* PDF Text Extraction
* Hybrid Weighted Similarity Scoring
* Interactive Streamlit User Interface
* Downloadable Similarity Reports

---

## Live Demo

[https://hybridplagiarismdetector.streamlit.app/](https://hybridplagiarismdetector.streamlit.app/)

---

## Technologies Used

* Python
* Streamlit
* Sentence-Transformers
* Scikit-learn
* PyMuPDF
* Pytesseract
* Pillow
* NLTK

---

## Supported Input Formats

* .txt
* .pdf
* .png
* .jpg
* .jpeg

---

## Project Structure

Hybrid-Plagiarism-Detector/

│
├── app.py
├── plagiarism_detector.py
├── requirements.txt
├── README.md

---

## System Workflow

User Upload
↓
Input Processing
↓
OCR / PDF Text Extraction
↓
Text Preprocessing
↓
TF-IDF Similarity Analysis
↓
Sentence-BERT Similarity Analysis
↓
Hybrid Score Aggregation
↓
Result Generation

---

## Setup Instructions

### Install Python Dependencies

pip install -r requirements.txt

### Install Tesseract OCR

Windows:
Download and install from:
[https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)

Ubuntu:

sudo apt install tesseract-ocr

macOS:

brew install tesseract

---

## Usage

Run the application using Streamlit:

streamlit run app.py

Open your browser and go to:

[http://localhost:8501](http://localhost:8501)

---

## Modules

Input Module – Accepts uploaded text, image, and PDF files
OCR Module – Extracts text from images using Tesseract
Preprocessing Module – Cleans and prepares text
TF-IDF Engine – Measures lexical similarity
Sentence-BERT Engine – Measures semantic similarity
Similarity Aggregator – Combines similarity scores
Report Generator – Displays plagiarism results

---

## Verdict Thresholds

≥ 65% → High Plagiarism
35% – 64% → Moderate Similarity
< 35% → Low Similarity

---

## Graceful Degradation

* If Sentence-Transformers is unavailable, the system falls back to TF-IDF similarity.
* If Pytesseract is unavailable, image-based inputs are disabled.
* If PyMuPDF is unavailable, PDF extraction is disabled.
* Text-based inputs remain functional even without optional dependencies.

---

## Advantages

* Supports multiple input formats
* Detects paraphrased plagiarism
* Handles scanned and image documents
* Easy-to-use web interface
* Fast and efficient similarity comparison

---

## Future Scope

* Highlight plagiarized sentences
* Add database storage
* AI-generated content detection
* Cloud deployment integration
* Advanced analytics dashboard

---

## Conclusion

This project combines OCR, TF-IDF, and Sentence-BERT to create a hybrid plagiarism detection framework.

The system improves plagiarism detection by supporting multimodal document analysis and semantic understanding.
