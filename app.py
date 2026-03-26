import streamlit as st

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="Logic Simulator", layout="centered")

# -------------------------------
# Title
# -------------------------------
st.title("🧠 Logic Simulator")
st.write("Propositional Logic & Predicate Logic (AI Project)")

# ===============================
# SECTION 1: PROPOSITIONAL LOGIC
# ===============================
st.header("🔷 Propositional Logic")

# Inputs
col1, col2 = st.columns(2)

with col1:
    P = st.selectbox("Select value for P", [True, False])

with col2:
    Q = st.selectbox("Select value for Q", [True, False])

# Operation selection
operation = st.selectbox(
    "Choose Operation",
    ["AND", "OR", "NOT P", "P → Q (Implication)"]
)

# Logic processing
if operation == "AND":
    result = P and Q

elif operation == "OR":
    result = P or Q

elif operation == "NOT P":
    result = not P

elif operation == "P → Q (Implication)":
    result = (not P) or Q   # logical rule

# Output
st.success(f"Result: {result}")

# Divider
st.markdown("---")

# ===============================
# SECTION 2: PREDICATE LOGIC
# ===============================
st.header("🔶 Predicate Logic")

st.write("Example Rule: If Human(x) → Mortal(x)")

# Knowledge base (simple AI concept)
humans = ["Ali", "Ahmed", "Sara"]

# Input
name = st.text_input("Enter a name (e.g., Ali):")

# Predicate function
def is_mortal(x):
    return x in humans

# Button
if st.button("Check"):
    if name.strip() == "":
        st.warning("Please enter a name.")
    else:
        result = is_mortal(name)
        if result:
            st.success(f"{name} is Mortal ✅")
        else:
            st.error(f"{name} is NOT Mortal ❌")

# Footer
st.markdown("---")
st.caption("Built with Streamlit | AI Logic Simulation Project")
