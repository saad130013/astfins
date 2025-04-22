
import streamlit as st
import json

# تحميل البيانات من ملف JSON
with open("assets_data.json", "r", encoding="utf-8") as f:
    assets_data = json.load(f)

st.set_page_config(layout="wide", page_title="دليل الأصول")
st.title("📘 دليل الأصول")

# CSS لتنسيق الجداول
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
    .custom-section-title {
        margin-top: 2rem;
        font-size: 20px;
        color: #006c8c;
        font-weight: bold;
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

        st.markdown("<div class='custom-section-title'>🧾 قيود المحاسبة:</div>", unsafe_allow_html=True)
        st.markdown("<table class='custom-table'><tr><th>🔢 القيد</th></tr>" +
                    "".join(f"<tr><td>{entry}</td></tr>" for entry in subsection["accounting_entry"]) +
                    "</table>", unsafe_allow_html=True)

        st.markdown("<div class='custom-section-title'>📄 المتطلبات:</div>", unsafe_allow_html=True)
        st.markdown("<table class='custom-table'><tr><th>📌 المستند</th></tr>" +
                    "".join(f"<tr><td>{req}</td></tr>" for req in subsection["requirements"]) +
                    "</table>", unsafe_allow_html=True)

        st.markdown("<div class='custom-section-title'>💡 التوجيهات:</div>", unsafe_allow_html=True)
        st.markdown("<table class='custom-table'><tr><th>📋 الإجراء</th></tr>" +
                    "".join(f"<tr><td>{guide}</td></tr>" for guide in subsection["guidelines"]) +
                    "</table>", unsafe_allow_html=True)

        st.markdown("<div class='custom-section-title'>📊 دورة القيد المحاسبي:</div>", unsafe_allow_html=True)
        st.markdown("""
        <table class='custom-table'>
        <tr><th>🔁 المرحلة</th><th>📝 الوصف</th></tr>
        <tr><td>📋 إعداد القيد</td><td>يتم بواسطة الموظف المختص استنادًا إلى مستندات رسمية (عقود، فواتير، تقارير).</td></tr>
        <tr><td>🧐 مراجعة القيد</td><td>يتم مراجعته من قبل محاسب للتأكد من صحته محاسبياً ومطابقته للسياسات.</td></tr>
        <tr><td>🖋️ مصادقة القيد</td><td>يوقع عليه المسؤول أو المشرف المختص بعد المراجعة.</td></tr>
        <tr><td>✅ اعتماد القيد</td><td>يعتمد القيد من قبل مدير الإدارة المالية أو المفوض بالصلاحية.</td></tr>
        <tr><td>📁 أرشفة القيد</td><td>يُحفظ القيد وجميع مستنداته إلكترونيًا أو ورقيًا وربطه بالأصل.</td></tr>
        <tr><td>📤 ترحيل القيد</td><td>يتم ترحيله إلى دفاتر الأستاذ العام في نهاية اليوم أو الشهر.</td></tr>
        </table>
        """, unsafe_allow_html=True)


# -------------------------------
st.markdown("<hr style='margin-top:3rem;'>", unsafe_allow_html=True)
st.subheader("🤖 الذكاء الصناعي: اقتراح قيد محاسبي حسب الوصف")

user_input = st.text_input("🧠 اكتب وصف العملية أو الأصل (مثال: شراء جهاز حاسب آلي):")

if user_input:
    import joblib
    import numpy as np

    # تحميل النموذج والبيانات
    vectorizer = joblib.load("tfidf_vectorizer.pkl")
    matrix = joblib.load("tfidf_matrix.pkl")
    with open("tfidf_metadata.json", "r", encoding="utf-8") as f:
        meta = json.load(f)

    # معالجة النص وإيجاد أقرب وصف
    user_vec = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_vec, matrix).flatten()
    best_idx = np.argmax(similarities)
    result = meta[best_idx]

    st.success(f"📂 تطابق مع: {result['section']} - {result['sub_title']}")

    st.markdown("#### 🔢 القيد المقترح:")
    for e in result["entries"]:
        st.write(f"- {e}")

    st.markdown("#### 📌 المتطلبات:")
    for r in result["requirements"]:
        st.write(f"- {r}")

    st.markdown("#### 💡 التوجيهات:")
    for g in result["guidelines"]:
        st.write(f"- {g}")
