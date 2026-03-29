import streamlit as st

st.set_page_config(page_title="How Well Do You Know Me?", page_icon="💭")

# QUESTIONS
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

# TITLE
st.title("How Well Do You Know Me?")
st.write("Answer honestly... let's see how well you really know me.")

score = 0

# QUIZ LOOP
for i, q in enumerate(questions):
    answer = st.radio(
        f"Q{i+1}: {q['q']}",
        ["True", "False"],
        key=i
    )

    if answer == "True":
        user_answer = True
    else:
        user_answer = False

    if user_answer == q["a"]:
        score += 1

# SUBMIT BUTTON
if st.button("Submit Quiz"):
    st.subheader(f"Your Score: {score} / {len(questions)}")

    if score >= 8:
        st.success("You are my close friend.")
    elif score >= 5:
        st.warning("You know me fairly well.")
    else:
        st.error("You are not as close as you think.")