import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from utils.parser import extract_resume
from utils.matcher import analyze_resume
from utils.skills import compare_skills
from utils.report import create_summary, generate_csv, generate_pdf

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# LOAD CSS
# ==========================================================

def load_css():
    try:
        with open("static/style.css") as css:
            st.markdown(
                f"<style>{css.read()}</style>",
                unsafe_allow_html=True
            )
    except FileNotFoundError:
        pass

load_css()

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.title("📄 AI Resume Screening System")

    st.markdown("---")

    st.subheader("About")

    st.write("""
This application analyzes resumes using
Natural Language Processing (NLP).

### Features

- Resume Parsing
- ATS Score
- Resume Matching
- Skill Detection
- Missing Skills
- AI Recommendation
- CSV & PDF Reports
""")

    st.markdown("---")

    st.success("✅ AI Powered")

# ==========================================================
# HERO SECTION
# ==========================================================

st.markdown(
"""
<div class="hero">

<h1>📄 AI Resume Screening System</h1>

<p>

Intelligent Resume Analysis using Artificial Intelligence

<br><br>

✔ ATS Score &nbsp;&nbsp;
✔ Resume Matching &nbsp;&nbsp;
✔ Skill Detection &nbsp;&nbsp;
✔ AI Recommendation

</p>

</div>
""",
unsafe_allow_html=True
)

# ==========================================================
# INPUT SECTION
# ==========================================================

left, right = st.columns(2)

with left:

    st.subheader("📄 Upload Resume")

    uploaded_resume = st.file_uploader(
        "Choose Resume",
        type=["pdf", "docx"]
    )

with right:

    st.subheader("💼 Job Description")

    job_description = st.text_area(
        "Paste Job Description",
        height=250
    )

st.markdown("---")

analyze = st.button(
    "🚀 Analyze Resume",
    use_container_width=True
)

# ==========================================================
# VALIDATION
# ==========================================================

if analyze:

    if uploaded_resume is None:

        st.error("Please upload a resume.")

        st.stop()

    if job_description.strip() == "":

        st.error("Please paste a Job Description.")

        st.stop()

    # ------------------------------------------------------

    resume_text = extract_resume(uploaded_resume)

    if resume_text.strip() == "":

        st.error("Unable to extract resume text.")

        st.stop()

    # ------------------------------------------------------

    analysis = analyze_resume(
        resume_text,
        job_description
    )

    clean_resume = analysis["clean_resume"]

    clean_job = analysis["clean_job"]

    match_percentage = analysis["match"]

    ats_score = analysis["ats"]

    keywords = analysis["keywords"]

    # ------------------------------------------------------

    skills = compare_skills(
        clean_resume,
        clean_job
    )

    resume_skills = skills["resume_skills"]

    job_skills = skills["job_skills"]

    found_skills = skills["found"]

    missing_skills = skills["missing"]
        # ==========================================================
    # RESUME PREVIEW
    # ==========================================================

    st.success("✅ Resume analyzed successfully!")

    tab1, tab2 = st.tabs(
        ["📄 Original Resume", "🧹 Processed Resume"]
    )

    with tab1:

        st.text_area(
            "Extracted Resume",
            resume_text,
            height=350
        )

    with tab2:

        st.text_area(
            "Processed Resume",
            clean_resume,
            height=350
        )

    st.markdown("---")

    # ==========================================================
    # DASHBOARD
    # ==========================================================

    st.markdown(
        """
        <div class="section-title">
        📊 AI Analysis Dashboard
        </div>
        """,
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "📈 ATS Score",
            f"{ats_score}%"
        )

    with c2:
        st.metric(
            "🎯 Resume Match",
            f"{match_percentage}%"
        )

    with c3:
        st.metric(
            "✅ Skills Found",
            len(found_skills)
        )

    with c4:
        st.metric(
            "❌ Missing Skills",
            len(missing_skills)
        )

    st.markdown("---")

    # ==========================================================
    # CHARTS
    # ==========================================================

    left_chart, right_chart = st.columns(2)

    with left_chart:

        gauge = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=ats_score,
                title={"text": "ATS Score"},
                gauge={
                    "axis": {"range": [0, 100]},
                    "bar": {"color": "#2563eb"},
                    "steps": [
                        {"range": [0, 50], "color": "#fee2e2"},
                        {"range": [50, 75], "color": "#fef3c7"},
                        {"range": [75, 100], "color": "#dcfce7"}
                    ]
                }
            )
        )

        gauge.update_layout(height=350)

        st.plotly_chart(
            gauge,
            use_container_width=True
        )

    with right_chart:

        pie_df = pd.DataFrame({

            "Category": [
                "Matched",
                "Remaining"
            ],

            "Value": [
                match_percentage,
                max(0, 100 - match_percentage)
            ]

        })

        pie = px.pie(
            pie_df,
            values="Value",
            names="Category",
            hole=0.60,
            title="Resume Match Distribution"
        )

        pie.update_traces(
            textposition="inside",
            textinfo="percent+label"
        )

        pie.update_layout(height=350)

        st.plotly_chart(
            pie,
            use_container_width=True
        )

    st.markdown("---")
        # ==========================================================
    # SKILLS SECTION
    # ==========================================================

    st.markdown(
        """
        <div class="section-title">
        🛠 Skills Analysis
        </div>
        """,
        unsafe_allow_html=True
    )

    left_skill, right_skill = st.columns(2)

    with left_skill:

        st.subheader("✅ Matching Skills")

        if found_skills:
            
            

            for skill in sorted(found_skills):
                

                st.markdown(f"✅ {skill.title()}")

        else:

            st.info("No matching skills found.")

    with right_skill:

        st.subheader("❌ Missing Skills")

        if missing_skills:
            

            for skill in sorted(missing_skills):
                

                st.markdown(f"❌ {skill.title()}")

        else:
            

            st.success("No missing skills detected.")

    st.markdown("---")

    # ==========================================================
    # AI RECOMMENDATION
    # ==========================================================

    st.markdown(
        """
        <div class="section-title">
        ⭐ AI Recruiter Recommendation
        </div>
        """,
        unsafe_allow_html=True
    )

    if ats_score >= 85:

        recommendation = "Strong Fit"

        confidence = 95

        recommendation_color = "🟢"

    elif ats_score >= 70:

        recommendation = "Moderate Fit"

        confidence = 80

        recommendation_color = "🟡"

    else:

        recommendation = "Needs Improvement"

        confidence = 60

        recommendation_color = "🔴"

    st.success(
        f"{recommendation_color} {recommendation}"
    )

    st.progress(confidence / 100)

    st.caption(
        f"AI Confidence : {confidence}%"
    )

    st.markdown("---")

    # ==========================================================
    # RESUME STATISTICS
    # ==========================================================

    st.markdown(
        """
        <div class="section-title">
        📄 Resume Statistics
        </div>
        """,
        unsafe_allow_html=True
    )

    s1, s2, s3 = st.columns(3)

    with s1:

        st.metric(
            "Words",
            len(resume_text.split())
        )

    with s2:

        st.metric(
            "Characters",
            len(resume_text)
        )

    with s3:

        st.metric(
            "Keywords",
            len(keywords)
        )

    st.markdown("---")

    # ==========================================================
    # TOP KEYWORDS
    # ==========================================================

    st.markdown(
        """
        <div class="section-title">
        🔑 Top Resume Keywords
        </div>
        """,
        unsafe_allow_html=True
    )

    keyword_df = pd.DataFrame({

        "Keyword": keywords

    })

    st.dataframe(
        keyword_df,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")
        # ==========================================================
    # ANALYSIS SUMMARY
    # ==========================================================

    st.markdown(
        """
        <div class="section-title">
        📋 Analysis Summary
        </div>
        """,
        unsafe_allow_html=True
    )

    summary = create_summary(
        ats_score,
        match_percentage,
        found_skills,
        missing_skills,
        recommendation
    )

    summary_df = pd.DataFrame(
        list(summary.items()),
        columns=["Metric", "Value"]
    )

    st.dataframe(
        summary_df,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    # ==========================================================
    # DOWNLOAD REPORTS
    # ==========================================================

    st.markdown(
        """
        <div class="section-title">
        📥 Export Reports
        </div>
        """,
        unsafe_allow_html=True
    )

    csv_report = generate_csv(summary)
    pdf_report = generate_pdf(summary)

    col1, col2 = st.columns(2)

    with col1:

        st.download_button(
            label="⬇ Download CSV Report",
            data=csv_report,
            file_name="resume_analysis.csv",
            mime="text/csv",
            use_container_width=True
        )

    with col2:

        st.download_button(
            label="⬇ Download PDF Report",
            data=pdf_report,
            file_name="resume_analysis.pdf",
            mime="application/pdf",
            use_container_width=True
        )

    st.markdown("---")

    # ==========================================================
    # FINAL DECISION
    # ==========================================================

    st.markdown(
        """
        <div class="section-title">
        🏆 Hiring Decision
        </div>
        """,
        unsafe_allow_html=True
    )

    if ats_score >= 85:

        st.success("✅ Recommended for Interview")

    elif ats_score >= 70:

        st.warning("⚠ Consider for Interview")

    else:

        st.error("❌ Not Recommended")

    st.markdown("---")

    # ==========================================================
    # DISCLAIMER
    # ==========================================================

    with st.expander("ℹ Disclaimer"):

        st.write(
            """
This application is intended for educational purposes.

The ATS score, recommendation and resume match are generated
using NLP techniques and should be used only as decision-support
metrics. Final hiring decisions should always involve manual
review and technical evaluation.
            """
        )

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.markdown(
    """
<div class="footer">

© 2026 AI Resume Screening System

Built with ❤️ using Python, Streamlit, Scikit-learn & NLP

</div>
""",
    unsafe_allow_html=True
)