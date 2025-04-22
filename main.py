
import streamlit as st
import json

# تحميل البيانات من ملف JSON
with open("assets_data.json", "r", encoding="utf-8") as f:
    assets_data = json.load(f)

st.set_page_config(layout="wide", page_title="دليل الأصول")
st.title("📘 دليل الأصول")

# تنسيق CSS بسيط للجداول
st.markdown("""
    <style>
    .custom-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 1rem;
    }
    .custom-table th {
        background-color: #006c8c;
        color: white;
        padding: 8px;
        text-align: center;
    }
    .custom-table td {
        background-color: #f2f9fc;
        padding: 8px;
        border-bottom: 1px solid #ddd;
        text-align: right;
    }
    </style>
""", unsafe_allow_html=True)

categories = list(assets_data.keys())
selected_category = st.selectbox("🔍 اختر فئة الأصول:", categories)

if selected_category:
    chapter_info = assets_data[selected_category]
    st.header("📂 " + chapter_info["title"])

    for subsection in chapter_info["subsections"]:
        st.subheader("📑 " + subsection["title"])

        st.markdown("#### 🧾 قيود المحاسبة:")
        st.markdown("<table class='custom-table'><tr><th>🔢 القيد</th></tr>" +
                    "".join(f"<tr><td>{entry}</td></tr>" for entry in subsection["accounting_entry"]) +
                    "</table>", unsafe_allow_html=True)

        st.markdown("#### 📄 المتطلبات:")
        st.markdown("<table class='custom-table'><tr><th>📌 المستند</th></tr>" +
                    "".join(f"<tr><td>{req}</td></tr>" for req in subsection["requirements"]) +
                    "</table>", unsafe_allow_html=True)

        st.markdown("#### 📌 التوجيهات:")
        st.markdown("<table class='custom-table'><tr><th>💡 الإجراء</th></tr>" +
                    "".join(f"<tr><td>{guide}</td></tr>" for guide in subsection["guidelines"]) +
                    "</table>", unsafe_allow_html=True)
