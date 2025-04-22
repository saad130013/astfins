
import streamlit as st
import json

# تحميل البيانات من ملف JSON
with open("assets_data.json", "r", encoding="utf-8") as f:
    assets_data = json.load(f)

st.set_page_config(layout="wide", page_title="دليل الأصول")
st.title("دليل الأصول")

categories = list(assets_data.keys())
selected_category = st.selectbox("اختر فئة الأصول:", categories)

if selected_category:
    chapter_info = assets_data[selected_category]
    st.header(chapter_info["title"])

    for subsection in chapter_info["subsections"]:
        st.subheader(subsection["title"])

        st.markdown("##### قيد المحاسبة:")
        for entry in subsection["accounting_entry"]:
            st.write(f"- {entry}")

        st.markdown("##### المتطلبات:")
        for req in subsection["requirements"]:
            st.write(f"- {req}")

        st.markdown("##### التوجيهات:")
        for guide in subsection["guidelines"]:
            st.write(f"- {guide}")
