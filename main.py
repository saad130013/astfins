
import streamlit as st

# بيانات الأصول
assets_data = {
  "4.2": {
    "title": "العقار والآلات والمعدات",
    "subsections": [
      {
        "title": "مشاريع قيد التنفيذ",
        "accounting_entry": ["قيد المحاسبة: يتم تسجيل المشروع عند بدء التنفيذ.", "قيود التسجيل: ..."],
        "requirements": ["متطلبات: اتفاقية المشروع، تقرير الجدوى الاقتصادية."],
        "guidelines": ["توجيهات: تتبع التقدم الدوري للمشروع."]
      },
      {
        "title": "الاستثمارات العقارية",
        "accounting_entry": ["قيد المحاسبة: يتم تسجيل الاستثمار عند الدفع الأولي.", "قيود التسجيل: ..."],
        "requirements": ["متطلبات: عقد الاستثمار، تقرير التقييم العقاري."],
        "guidelines": ["توجيهات: مراجعة العائدات بشكل دوري."]
      }
    ]
  },
  "5.2": {
    "title": "الأصول غير الملموسة",
    "subsections": [
      {
        "title": "مشاريع قيد التنفيذ",
        "accounting_entry": ["قيد المحاسبة: يتم تسجيل المشروع عند بدء التنفيذ.", "قيود التسجيل: ..."],
        "requirements": ["متطلبات: اتفاقية المشروع، تقرير الجدوى الاقتصادية."],
        "guidelines": ["توجيهات: تتبع التقدم الدوري للمشروع."]
      },
      {
        "title": "الاستثمارات المالية",
        "accounting_entry": ["قيد المحاسبة: يتم تسجيل الاستثمار عند الدفع الأولي.", "قيود التسجيل: ..."],
        "requirements": ["متطلبات: عقد الاستثمار، تقرير التقييم المالي."],
        "guidelines": ["توجيهات: متابعة العائدات بشكل دوري."]
      }
    ]
  },
  "6.2": {
    "title": "مشاريع قيد التنفيذ",
    "subsections": [
      {
        "title": "مشاريع قيد التنفيذ",
        "accounting_entry": ["قيد المحاسبة: يتم تسجيل المشروع عند بدء التنفيذ.", "قيود التسجيل: ..."],
        "requirements": ["متطلبات: اتفاقية المشروع، تقرير الجدوى الاقتصادية."],
        "guidelines": ["توجيهات: تتبع التقدم الدوري للمشروع."]
      }
    ]
  },
  "7.2": {
    "title": "العقارات الاستثمارية",
    "subsections": [
      {
        "title": "العقارات الاستثمارية",
        "accounting_entry": ["قيد المحاسبة: يتم تسجيل العقار عند التعاقد.", "قيود التسجيل: ..."],
        "requirements": ["متطلبات: عقد البيع أو الإيجار، تقرير التقييم العقاري."],
        "guidelines": ["توجيهات: مراجعة العقود بشكل دوري."]
      }
    ]
  },
  "8.2": {
    "title": "ترتيبات تقديم الخدمات",
    "subsections": [
      {
        "title": "ترتيبات تقديم الخدمات",
        "accounting_entry": ["قيد المحاسبة: يتم تسجيل الاتفاقية عند توقيع العقد.", "قيود التسجيل: ..."],
        "requirements": ["متطلبات: عقد الخدمة، تقرير الجدوى الاقتصادية."],
        "guidelines": ["توجيهات: متابعة تنفيذ الخدمات بشكل دوري."]
      }
    ]
  },
  "9.2": {
    "title": "الاستثمارات المالية",
    "subsections": [
      {
        "title": "الاستثمارات المالية",
        "accounting_entry": ["قيد المحاسبة: يتم تسجيل الاستثمار عند الدفع الأولي.", "قيود التسجيل: ..."],
        "requirements": ["متطلبات: عقد الاستثمار، تقرير التقييم المالي."],
        "guidelines": ["توجيهات: متابعة العائدات بشكل دوري."]
      }
    ]
  },
  "2.10": {
    "title": "الأصول البيولوجية",
    "subsections": [
      {
        "title": "الأصول البيولوجية",
        "accounting_entry": ["قيد المحاسبة: يتم تسجيل الأصل البيولوجي عند الشراء.", "قيود التسجيل: ..."],
        "requirements": ["متطلبات: فاتورة الشراء، تقرير الصحة البيولوجية."],
        "guidelines": ["توجيهات: مراقبة الحالة الصحية."]
      }
    ]
  }
}

# تكوين الصفحة
st.set_page_config(layout="wide", page_title="دليل الأصول")
st.title("دليل الأصول")

# قائمة الفئات الرئيسية
categories = list(assets_data.keys())
selected_category = st.selectbox("اختر فئة الأصول:", categories)

if selected_category:
    chapter_info = assets_data[selected_category]
    st.header(chapter_info["title"])

    # عرض الفئات الفرعية
    for subsection in chapter_info["subsections"]:
        st.subheader(subsection["title"])

        st.markdown("##### قيد المحاسبة:")
        for entry in subsection["accounting_entry"]:
            st.write(entry)

        st.markdown("##### المتطلبات:")
        for requirement in subsection["requirements"]:
            st.write(requirement)

        st.markdown("##### التوجيهات:")
        for guideline in subsection["guidelines"]:
            st.write(guideline)
