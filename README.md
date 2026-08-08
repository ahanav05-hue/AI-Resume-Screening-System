# 📄 AI Resume Screening System

An AI-powered Resume Screening System that helps recruiters evaluate resumes by comparing them with Job Descriptions using Natural Language Processing (NLP).

The application automatically parses resumes, calculates ATS scores, extracts technical skills, measures semantic similarity, and generates downloadable analysis reports.

---

## 🚀 Features

- 📄 Upload PDF and DOCX resumes
- 🤖 AI-powered resume analysis
- 📊 ATS Score calculation
- 🎯 Resume Match Percentage
- 🧠 NLP-based text preprocessing
- ✅ Skill Extraction
- ❌ Missing Skill Detection
- 📈 Interactive Dashboard
- 📉 ATS Gauge Chart
- 🥧 Resume Match Visualization
- ⭐ AI Recruiter Recommendation
- 📄 PDF Report Generation
- 📊 CSV Report Generation

---

## 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Framework | Streamlit |
| NLP | NLTK |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Charts | Plotly |
| PDF Parsing | pdfplumber |
| DOCX Parsing | python-docx |
| Report Generation | ReportLab |

---

## 📂 Project Structure

```text
AI-Resume-Screening-System
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── utils/
│   ├── parser.py
│   ├── matcher.py
│   ├── skills.py
│   └── report.py
│
├── uploads/
├── sample_resumes/
├── sample_job_descriptions/
├── screenshots/
└── data/
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/ahanav05-hue/AI-Resume-Screening-System.git
```

Navigate into the project:

```bash
cd AI-Resume-Screening-System
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

**macOS/Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📊 Output

The application provides:

- ATS Score
- Resume Match Percentage
- Resume Skills
- Required Skills
- Missing Skills
- AI Recommendation
- Resume Statistics
- CSV Report
- PDF Report

---

## 🚀 Future Enhancements

- Sentence Transformer embeddings
- BERT-based resume matching
- OCR support for scanned resumes
- Multi-resume ranking
- Resume ranking dashboard
- AI interview question generation
- Recruiter login system
- Database integration

---

## 👩‍💻 Author

**Ahana V**

GitHub: https://github.com/ahanav05-hue