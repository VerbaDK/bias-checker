import streamlit as st
import pandas as pd

# ✅ Gender-coded word lists (Danish) with suggestions
male_words = {
    "ambitiøs": "engageret",
    "konkurrerende": "målrettet",
    "handlekraftig": "beslutsom",
    "selvstændig": "teamorienteret",
    "modig": "tryg ved udfordringer",
    "dominerende": "ansvarsbevidst",
    "aggressiv": "handlekraftig",
    "beslutsom": "afbalanceret"
}

female_words = {
    "empatisk": "lyttende",
    "støttende": "opmuntrende",
    "omsorgsfuld": "respektfuld",
    "lyttende": "dialogsøgende",
    "samarbejdsvillig": "teamorienteret",
    "venlig": "inkluderende",
    "omhyggelig": "systematisk",
    "forstående": "reflekteret"
}
male_words = {
    "ambitiøs": "engageret",
    "ambitiøse": "engageret",           # plural/adjective form
    "konkurrerende": "målrettet",
    "handlekraftig": "beslutsom",
    "handlekraftige": "beslutsom",      # plural/adjective form
    "selvstændig": "teamorienteret",
    "selvstændige": "teamorienteret",   # plural/adjective form
    "modig": "tryg ved udfordringer",
    "modige": "tryg ved udfordringer",  # plural/adjective form
    "dominerende": "ansvarsbevidst",
    "aggressiv": "handlekraftig",
    "aggressive": "handlekraftig",      # plural/adjective form
    "beslutsom": "afbalanceret",
    "beslutsomme": "afbalanceret"       # plural/adjective form
}

female_words = {
    "empatisk": "lyttende",
    "empatiske": "lyttende",            # plural/adjective form
    "støttende": "opmuntrende",
    "omsorgsfuld": "respektfuld",
    "omsorgsfulde": "respektfuld",      # plural/adjective form
    "lyttende": "dialogsøgende",
    "samarbejdsvillig": "teamorienteret",
    "samarbejdsvillige": "teamorienteret", # plural/adjective form
    "venlig": "inkluderende",
    "venlige": "inkluderende",          # plural/adjective form
    "omhyggelig": "systematisk",
    "omhyggelige": "systematisk",       # plural/adjective form
    "forstående": "reflekteret"
}

# 🔍 Function to analyze job description
def analyze_text(text):
    words = text.lower().split()
    male_hits, female_hits, suggestions = [], [], {}

    for word in words:
        clean = word.strip('.,!?()[]{}"\'')
        if clean in male_words:
            male_hits.append(clean)
            suggestions[clean] = male_words[clean]
        elif clean in female_words:
            female_hits.append(clean)
            suggestions[clean] = female_words[clean]

    return male_hits, female_hits, suggestions

# 🎨 Streamlit layout
st.set_page_config(page_title="Bias Checker 🇩🇰", page_icon="🔍")
st.title("🔍 Dansk Bias Checker for Jobopslag")
st.markdown("Indsæt dit jobopslag nedenfor for at analysere kønspræget sprog og få forslag til inkluderende formuleringer.")

# 📝 Input box
job_text = st.text_area("📄 Jobopslag", placeholder="Indsæt din jobannonce her...", height=300)

# 🧪 Run analysis
if st.button("Analysér"):
    if not job_text.strip():
        st.warning("⚠️ Skriv venligst en jobannonce først.")
    else:
        male_hits, female_hits, suggestions = analyze_text(job_text)

        st.subheader("🚹 Maskulint-kodede ord")
        st.write(male_hits if male_hits else "Ingen fundet.")

        st.subheader("🚺 Feminint-kodede ord")
        st.write(female_hits if female_hits else "Ingen fundet.")

        st.subheader("💡 Inkluderende alternativer")
        if suggestions:
            for original, replacement in suggestions.items():
                st.markdown(f"- **{original}** → *{replacement}*")
        else:
            st.write("Ingen forslag. Sproget ser neutralt ud 👌")

        st.success("✅ Analyse afsluttet.")
