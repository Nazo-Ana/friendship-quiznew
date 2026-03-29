import streamlit as st

st.set_page_config(
    page_title="How Well Do You Know Me?",
    page_icon="💖",
    layout="centered"
)

questions = [
    {"q": "My favorite color is pink.", "a": True},
    {"q": "Chicken wings are my favorite food.", "a": True},
    {"q": "My favorite drink is hot chocolate coffee with a little bit of milk, and sometimes cappuccino.", "a": True},
    {"q": "There is someone in my life whom I truly consider a very close friend.", "a": False},
    {"q": "I find it easy to trust the people I call my friends.", "a": False},
    {"q": "Even when I recognize fake people, they somehow still remain in my life.", "a": True},
    {"q": "When I truly care about someone, I genuinely love listening to them.", "a": True},
    {"q": "Trust issues are a constant part of how I deal with people.", "a": True},
    {"q": "Most of my friends understand my personality better than I think they do.", "a": False},
    {"q": "People often assume they know the real me, but very few actually do.", "a": True},
]

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f172a, #111827, #1e1b4b);
        color: white;
    }

    .main-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        text-align: center;
        font-size: 1.1rem;
        color: #d1d5db;
        margin-bottom: 2rem;
    }

    .glass-box {
        background: rgba(255, 255, 255, 0.08);
        padding: 1.5rem;
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.15);
        box-shadow: 0 8px 30px rgba(0,0,0,0.25);
        margin-bottom: 1.5rem;
    }

    .result-good {
        background: linear-gradient(135deg, #14532d, #166534);
        padding: 1.2rem;
        border-radius: 18px;
        color: white;
        font-size: 1.1rem;
        font-weight: 600;
        margin-top: 1rem;
        text-align: center;
    }

    .result-mid {
        background: linear-gradient(135deg, #92400e, #b45309);
        padding: 1.2rem;
        border-radius: 18px;
        color: white;
        font-size: 1.1rem;
        font-weight: 600;
        margin-top: 1rem;
        text-align: center;
    }

    .result-low {
        background: linear-gradient(135deg, #7f1d1d, #b91c1c);
        padding: 1.2rem;
        border-radius: 18px;
        color: white;
        font-size: 1.1rem;
        font-weight: 600;
        margin-top: 1rem;
        text-align: center;
    }

    .score-box {
        background: linear-gradient(135deg, #db2777, #7c3aed);
        padding: 1rem;
        border-radius: 18px;
        text-align: center;
        color: white;
        font-size: 1.3rem;
        font-weight: bold;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    div[data-testid="stTextInput"] input {
        border-radius: 12px;
    }

    div[data-testid="stRadio"] {
        background: rgba(255,255,255,0.05);
        padding: 0.8rem 1rem;
        border-radius: 16px;
        margin-bottom: 1rem;
    }

    .footer-note {
        text-align: center;
        color: #cbd5e1;
        margin-top: 2rem;
        font-size: 0.95rem;
    }
    </style>
""", unsafe_allow_html=True)

if "submitted" not in st.session_state:
    st.session_state.submitted = False

st.markdown('<div class="main-title">How Well Do You Know Me? 💖</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Answer honestly, let’s see how well you really know me.</div>', unsafe_allow_html=True)

st.markdown('<div class="glass-box">', unsafe_allow_html=True)
name = st.text_input("Enter your name")
email = st.text_input("Enter your email")
st.caption("Your name and email are requested before submission.")
st.markdown('</div>', unsafe_allow_html=True)

score = 0
all_answered = True
user_answers = []

for i, q in enumerate(questions):
    answer = st.radio(
        f"Q{i+1}: {q['q']}",
        ["True", "False"],
        key=f"q_{i}",
        index=None
    )

    if answer is None:
        all_answered = False
        user_answers.append(None)
    else:
        user_bool = answer == "True"
        user_answers.append(user_bool)
        if user_bool == q["a"]:
            score += 1

if st.button("Submit Quiz 💌", use_container_width=True):
    if not name.strip():
        st.warning("Please enter your name first.")
    elif not email.strip():
        st.warning("Please enter your email first.")
    elif "@" not in email or "." not in email:
        st.warning("Please enter a valid email address.")
    elif not all_answered:
        st.warning("Please answer all questions first.")
    else:
        st.session_state.submitted = True
        st.session_state.final_name = name
        st.session_state.final_email = email
        st.session_state.final_score = score

if st.session_state.submitted:
    final_name = st.session_state.final_name
    final_score = st.session_state.final_score
    total = len(questions)

    st.markdown(
        f'<div class="score-box">✨ {final_name}, your score is {final_score} / {total} ✨</div>',
        unsafe_allow_html=True
    )

    if final_score >= 8:
        st.balloons()
        st.markdown(
            '<div class="result-good">🎉 Wow, you really know me well. You are definitely one of my close people 💖✨</div>',
            unsafe_allow_html=True
        )
    elif final_score >= 5:
        st.markdown(
            '<div class="result-mid">😊 Not bad at all. You know me fairly well, but there is still more to discover 💭</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<div class="result-low">😅 You are not as close as you think. Time to know me better 👀</div>',
            unsafe_allow_html=True
        )

st.markdown('<div class="footer-note">Made with Python, Streamlit, and a little bit of personality ✨</div>', unsafe_allow_html=True)