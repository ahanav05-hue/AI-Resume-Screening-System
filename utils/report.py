"""
==========================================================
Report Generator Module
==========================================================

Features

1. CSV Report Generation
2. PDF Report Generation
3. Summary Dictionary

==========================================================
"""

import io
import pandas as pd

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph


# ==========================================================
# SUMMARY DATA
# ==========================================================

def create_summary(
    ats_score,
    match_percentage,
    found_skills,
    missing_skills,
    recommendation
):

    return {

        "ATS Score": f"{ats_score}%",
        "Resume Match": f"{match_percentage}%",
        "Skills Found": ", ".join(found_skills) if found_skills else "None",
        "Missing Skills": ", ".join(missing_skills) if missing_skills else "None",
        "Recommendation": recommendation

    }


# ==========================================================
# CSV REPORT
# ==========================================================

def generate_csv(summary):

    df = pd.DataFrame(

        summary.items(),

        columns=["Metric", "Value"]

    )

    return df.to_csv(index=False).encode("utf-8")


# ==========================================================
# PDF REPORT
# ==========================================================

def generate_pdf(summary):

    buffer = io.BytesIO()

    document = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    story.append(

        Paragraph("<b>AI Resume Screening Report</b>", styles["Title"])

    )

    story.append(

        Paragraph("<br/><br/>", styles["BodyText"])

    )

    for key, value in summary.items():

        story.append(

            Paragraph(

                f"<b>{key}:</b> {value}",

                styles["BodyText"]

            )

        )

    document.build(story)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf