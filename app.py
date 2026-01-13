import streamlit as st
import pandas as pd
import plotly.express as px
import random

from database import *
from settlement import *
from gemini_summary import generate_funny_summary

# 🔐 Put your Gemini API key here (local only)
GEMINI_API_KEY = "AIzaSyB10pKTltN3rk3Y-JSI_ch71GxwsVsvTZw"

# ---------------- Init ----------------
init_db()
st.title("💰 Group Expense Manager (INR)")

# ---------------- Add Participant ----------------
st.header("Add Participant")
name = st.text_input("Name")

if st.button("Add Participant"):
    if not name.strip():
        st.error("Name cannot be empty")
    else:
        try:
            add_participant(name.strip())
            st.success("Participant added")
        except:
            st.error("Participant already exists")

people = get_participants()

# ---------------- Spin the Payer ----------------
st.header("🎡 Spin the Payer")
st.caption("Randomly suggests who should pay next")

if people:
    if st.button("Spin"):
        st.success(f"Suggested payer: **{random.choice(people)}**")
else:
    st.info("Add participants to enable spin")

# ---------------- Add Expense ----------------
st.header("Add Expense")

if people:
    payer = st.selectbox("Payer", people)
    category = st.text_input("Category")
    amount = st.number_input("Amount (₹)", min_value=0.0, step=1.0)

    if st.button("Add Expense"):
        if amount <= 0:
            st.error("Amount must be greater than 0")
        else:
            add_expense(payer, category, amount)
            st.success("Expense added")
else:
    st.warning("Add participants before adding expenses")

# ---------------- Expense Table ----------------
expenses = get_expenses()
df = pd.DataFrame(expenses, columns=["Payer", "Category", "Amount", "Time"])

st.header("Expense Table")
st.dataframe(df, use_container_width=True)

# ---------------- Charts + Settlement ----------------
if not df.empty and people:
    st.header("Category-wise Spending")
    fig = px.pie(df, names="Category", values="Amount")
    st.plotly_chart(fig, use_container_width=True)

    per_head, settlements = calculate_settlement(expenses, people)

    st.header("Final Settlement")
    st.write(f"Per Head Amount: ₹{per_head:.2f}")
    for s in settlements:
        st.write(s)

    # ---------------- Gemini Summary ----------------
    st.header("🤖 Gemini’s Take (Just for Fun)")

    if st.button("Generate Funny Summary"):
        with st.spinner("Gemini is assigning nicknames and judging expenses..."):
            summary = generate_funny_summary(
                expenses,
                settlements,
                GEMINI_API_KEY
            )
            st.success(summary)

    st.download_button(
        "Export CSV",
        df.to_csv(index=False),
        file_name="expenses.csv",
        mime="text/csv"
    )
