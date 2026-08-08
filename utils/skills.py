"""
==========================================================
Skill Detection Module
==========================================================

Features

1. Skill Database
2. Resume Skill Detection
3. Missing Skill Detection
4. Skill Match Percentage

==========================================================
"""

# ==========================================================
# MASTER SKILL DATABASE
# ==========================================================

SKILLS = [

    # Programming Languages
    "python",
    "java",
    "c",
    "c++",
    "c#",
    "javascript",
    "typescript",
    "go",
    "rust",

    # Web Development
    "html",
    "css",
    "bootstrap",
    "react",
    "angular",
    "vue",
    "node",
    "express",

    # Backend
    "flask",
    "django",
    "fastapi",

    # Database
    "sql",
    "mysql",
    "sqlite",
    "postgresql",
    "mongodb",

    # Data Science
    "numpy",
    "pandas",
    "matplotlib",
    "seaborn",

    # Machine Learning
    "scikit-learn",
    "tensorflow",
    "keras",
    "pytorch",
    "machine learning",
    "deep learning",
    "nlp",

    # Cloud
    "aws",
    "azure",
    "gcp",

    # DevOps
    "docker",
    "kubernetes",
    "jenkins",

    # Tools
    "git",
    "github",
    "linux",
    "postman",
    "vscode",

    # Others
    "rest api",
    "api",
    "oop",
    "data structures",
    "algorithms"

]

# ==========================================================
# EXTRACT SKILLS
# ==========================================================

def extract_skills(text):

    text = text.lower()

    detected = []

    for skill in SKILLS:

        if skill in text:

            detected.append(skill)

    return sorted(list(set(detected)))

# ==========================================================
# COMPARE SKILLS
# ==========================================================

def compare_skills(resume_text, job_text):

    resume_skills = extract_skills(resume_text)

    job_skills = extract_skills(job_text)

    found = []

    missing = []

    for skill in job_skills:

        if skill in resume_skills:

            found.append(skill)

        else:

            missing.append(skill)

    return {

        "resume_skills": resume_skills,

        "job_skills": job_skills,

        "found": sorted(found),

        "missing": sorted(missing)

    }

# ==========================================================
# MATCH PERCENTAGE
# ==========================================================

def skill_match_percentage(found, job_skills):

    if len(job_skills) == 0:

        return 0

    return round(

        (len(found) / len(job_skills)) * 100,

        2

    )

# ==========================================================
# TOP SKILLS
# ==========================================================

def top_resume_skills(text, limit=10):

    skills = extract_skills(text)

    return skills[:limit]