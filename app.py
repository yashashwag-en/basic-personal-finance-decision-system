import streamlit as st
import matplotlib.pyplot as plt
from advisor import analyze_budget

st.set_page_config(page_title="Financial Intelligence Engine", layout="wide")

st.title("📊 Financial Intelligence Engine")
st.caption("Advanced Cashflow & Risk Analytics System")

col1, col2, col3 = st.columns(3)

with col1:
    income = st.number_input("Monthly Income", min_value=1.0)

with col2:
    fixed_expenses = st.number_input("Fixed Expenses", min_value=0.0)

with col3:
    variable_expenses = st.number_input("Variable Expenses", min_value=0.0)

savings_goal = st.number_input("Savings Goal", min_value=0.0)
annual_return = st.slider("Expected Annual Investment Return (%)", 0, 20, 8)

if st.button("Run Deep Financial Analysis"):

    result = analyze_budget(
        income, fixed_expenses, variable_expenses,
        savings_goal, annual_return
    )

    st.divider()

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Net Cashflow", f"₹ {result['net_cashflow']}")
    m2.metric("Stability Index", f"{result['score']}/100")
    m3.metric("Risk Level", result['risk'])
    m4.metric("Emergency Runway (months)", result['runway_months'])

    st.divider()

    st.subheader("Income Allocation Analysis")

    labels = ['Fixed', 'Variable', 'Savings']
    values = [
        fixed_expenses,
        variable_expenses,
        max(result['net_cashflow'], 0)
    ]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    st.pyplot(fig)

    st.divider()

    st.subheader("Ratio Diagnostics")
    r1, r2, r3 = st.columns(3)
    r1.metric("Fixed Ratio (%)", result['fixed_ratio'])
    r2.metric("Variable Ratio (%)", result['variable_ratio'])
    r3.metric("Savings Ratio (%)", result['savings_ratio'])

    st.divider()

    st.subheader("Goal & Emergency Analytics")

    st.write(f"Required Emergency Fund (6 months): ₹ {result['emergency_required']}")
    st.write(f"Months to Build Emergency Fund: {result['months_to_emergency']}")
    st.write(f"Months to Reach Savings Goal (with return): {result['months_to_goal']}")

    st.divider()

    st.subheader("Optimization Simulator")
    st.write(f"If you reduce variable expenses by 10%, new monthly surplus: ₹ {result['optimized_cashflow']}")

    st.divider()

    st.subheader("AI Strategic Recommendations")
    for rec in result["recommendations"]:
        st.write("•", rec)