import streamlit as st
import matplotlib.pyplot as plt
st.title("Expense Tracker")

#session state
if "expenses" not in st.session_state:
    st.session_state.expenses=[]
st.sidebar.header("Add Expense")
amount=st.sidebar.number_input("Enter amount",min_value=0)
category=st.sidebar.selectbox("Select category",["Food","Travel","shopping","other"])
add_btn=st.sidebar.button("add expense")
if add_btn:
    if amount>0:
        st.session_state.expenses.append({
            "amount":amount,
            "category":category
        })
        st.sidebar.success("Expense added!")
    else:
        st.sidebar.warning("Enter a valid amount")
st.subheader("Expense List")
for i, exp in enumerate(st.session_state.expenses):
    st.write(f"{i+1}. ₹{exp['amount']} - {exp['category']}")

st.subheader("Expense Summary")
category_totals={}
for exp in st.session_state.expenses:
    cat=exp["category"]
    category_totals[cat]=category_totals.get(cat,0)+exp["amount"]
if category_totals:
    fig,ax=plt.subplots()
    ax.pie(category_totals.values(),labels=category_totals.keys(),autopct="%1.1f%%")
    st.pyplot(fig)
else:
    st.info("No expense to show")
