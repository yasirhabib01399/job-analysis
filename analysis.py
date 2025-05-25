import pandas as pd
from collections import Counter

def analyze_jobs(csv_path="jobs.csv"):
    df = pd.read_csv(csv_path)

    # Basic cleanup
    df.dropna(inplace=True)

    # Top 5 job titles
    top_titles = df['title'].value_counts().head(5)

    # If you had 'location' or 'skills', you could use them like this:
    top_cities = df['location'].value_counts().head(5) if 'location' in df.columns else None

    # Placeholder for skills analysis (if added later)
    top_skills = None
    if 'skills' in df.columns:
        all_skills = []
        for skills in df['skills'].dropna():
            all_skills.extend([s.strip().lower() for s in skills.split(',')])
        top_skills = Counter(all_skills).most_common(5)

    return {
        "top_titles": top_titles.to_dict(),
        "top_cities": top_cities.to_dict() if top_cities is not None else {},
        "top_skills": dict(top_skills) if top_skills else {}
    }