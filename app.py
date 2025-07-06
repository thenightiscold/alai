
import streamlit as st
import json
import os

st.set_page_config(page_title="Al-Khwarizmi AI Scholar", layout="wide")
st.title("📚 Al-Khwarizmi AI Scholar")
st.markdown("An AI-powered platform to rediscover Muslim scientific heritage. 🇺🇸 English / 🇸🇦 Arabic")

# Load scholar data
with open("scholarpedia.json", "r", encoding="utf-8") as f:
    scholars = json.load(f)

with open("legacy_tech_tree.json", "r", encoding="utf-8") as f:
    legacy_tree = json.load(f)

with open("daily_spotlight.json", "r", encoding="utf-8") as f:
    spotlight = json.load(f)

# Tabbed UI
tab1, tab2, tab3, tab4 = st.tabs(["💬 AI Q&A", "👤 Scholarpedia", "🌿 LegacyTech Tree", "🔦 Daily Spotlight"])

with tab1:
    st.subheader("Ask about Muslim inventions or scholars")
    st.warning("Note: AI backend will be connected during full deployment.")
    user_input = st.text_input("Your question:")
    if user_input:
        st.success(f"🤖 (Sample Answer) Great question! Here's what I found about: '{user_input}'")

with tab2:
    st.subheader("Explore Scholars by Field and Century")
    field = st.selectbox("Filter by Field", sorted(set(s['field'] for s in scholars)))
    for scholar in [s for s in scholars if s['field'] == field]:
        st.markdown(f"**{scholar['name']}** ({scholar['century']} century, {scholar['region']})")
        st.markdown(f"🔬 {scholar['contribution']}")
        st.markdown("---")

with tab3:
    st.subheader("How Muslim Innovations Shaped the World")
    for name, impacts in legacy_tree.items():
        st.markdown(f"**{name}** → {' → '.join(impacts)}")

with tab4:
    st.subheader("Today's Spotlight")
    st.markdown(f"**Scholar**: {spotlight['scholar']}")
    st.markdown(f"**Invention**: {spotlight['invention']}")
    st.markdown(f"**Verse**: _{spotlight['verse']['text']}_")
    st.markdown(f"📖 **Reference**: {spotlight['verse']['reference']}")
