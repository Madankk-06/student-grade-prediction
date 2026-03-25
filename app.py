import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model/student_grade_model.pkl")

st.set_page_config(
    page_title="Student Grade Predictor",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main {
    padding-top: 1rem;
}
.title-box {
    background: linear-gradient(90deg, #0f172a, #1e3a8a);
    padding: 24px;
    border-radius: 18px;
    color: white;
    margin-bottom: 20px;
}
.metric-card {
    background-color: #111827;
    padding: 18px;
    border-radius: 16px;
    border: 1px solid #374151;
    text-align: center;
}
.result-box {
    padding: 20px;
    border-radius: 18px;
    margin-top: 15px;
    background: #0f172a;
    border: 1px solid #334155;
}
.small-text {
    font-size: 14px;
    color: #cbd5e1;
}
.footer-box {
    margin-top: 30px;
    padding: 15px;
    text-align: center;
    border-top: 1px solid #334155;
    color: #94a3b8;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="title-box">
    <h1>🎓 Student Grade Prediction System</h1>
    <p class="small-text">
        Predict final student performance using machine learning based on academic and support-related factors.
    </p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("📘 Project Info")
    st.write("**Model Used:** Random Forest Regressor")
    st.write("**Dataset:** UCI Student Performance Dataset")
    st.write("**Target Variable:** G3 (Final Grade)")
    st.write("**Frontend:** Streamlit")
    st.markdown("---")
    st.subheader("How to Use")
    st.write("1. Enter student details")
    st.write("2. Click on Predict")
    st.write("3. View predicted grade and performance level")

# Layout
left_col, right_col = st.columns([1.2, 1])

with left_col:
    st.subheader("📝 Enter Student Details")

    with st.form("grade_form"):
        c1, c2 = st.columns(2)

        with c1:
            age = st.number_input("Age", min_value=15, max_value=22, value=17, help="Student age")
            studytime = st.slider("Study Time", 1, 4, 2, help="1 = low, 4 = high")
            failures = st.slider("Past Failures", 0, 4, 0)
            absences = st.slider("Absences", 0, 100, 4)
            G1 = st.slider("First Period Grade (G1)", 0, 20, 10)

        with c2:
            internet = st.selectbox("Internet Access", ["yes", "no"])
            famsup = st.selectbox("Family Support", ["yes", "no"])
            higher = st.selectbox("Higher Education Interest", ["yes", "no"])
            G2 = st.slider("Second Period Grade (G2)", 0, 20, 10)

        predict_button = st.form_submit_button("🚀 Predict Grade", use_container_width=True)

with right_col:
    st.subheader("📊 Input Overview")
    st.markdown("""
    <div class="metric-card">
        <h3>Project Goal</h3>
        <p class="small-text">
            Estimate the student's final grade and classify performance level
            using selected academic and personal support features.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.info("Tip: G1 and G2 usually have a strong influence on final grade prediction.")

# Prediction block
if predict_button:
    input_df = pd.DataFrame([{
        "age": age,
        "studytime": studytime,
        "failures": failures,
        "absences": absences,
        "internet": internet,
        "famsup": famsup,
        "higher": higher,
        "G1": G1,
        "G2": G2
    }])

    prediction = model.predict(input_df)[0]
    prediction = max(0, min(20, prediction))  # keep within grade range

    st.markdown("---")
    st.subheader("✅ Prediction Result")

    result_col1, result_col2, result_col3 = st.columns(3)

    with result_col1:
        st.metric("Predicted Final Grade", f"{prediction:.2f} / 20")

    with result_col2:
        percentage = (prediction / 20) * 100
        st.metric("Predicted Percentage", f"{percentage:.1f}%")

    with result_col3:
        if prediction >= 16:
            level = "Excellent"
        elif prediction >= 12:
            level = "Good"
        elif prediction >= 8:
            level = "Average"
        else:
            level = "Needs Improvement"
        st.metric("Performance Level", level)

    st.progress(int((prediction / 20) * 100))

    st.markdown(f"""
    <div class="result-box">
        <h3>Performance Interpretation</h3>
        <p class="small-text">
            The model predicts that the student may score <b>{prediction:.2f}</b> out of 20
            in the final evaluation. Based on the selected inputs, the expected performance level is
            <b>{level}</b>.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📌 Entered Student Data")
    st.dataframe(input_df, use_container_width=True)

    st.subheader("💡 Suggestions")
    if prediction >= 16:
        st.success("Student is likely performing very well. Keep maintaining the same study consistency.")
    elif prediction >= 12:
        st.info("Student shows good performance. A little more focus on study time and consistency can improve results further.")
    elif prediction >= 8:
        st.warning("Student performance is average. Reducing absences and improving study habits may help.")
    else:
        st.error("Student may need academic support. Focus on basics, reduce failures, and improve learning support at home.")

# Footer
st.markdown("""
<div class="footer-box">
    Student Grade Prediction Project • Built with Streamlit and Machine Learning
</div>
""", unsafe_allow_html=True)