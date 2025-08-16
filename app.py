import streamlit as st

st.title("💧 Solution Concentration Calculator")

st.markdown("""
This tool helps you design a working solution so that **each 1 mL dose = desired ppm** 
in your target jar.
""")

# Inputs
v_prep_ml = st.number_input("Volume of working solution to prepare (mL)", value=1000)
v_target_ml = st.number_input("Target jar volume (mL)", value=500)
ppm_per_ml = st.number_input("Desired ppm per 1 mL dose", value=1.0)

# Calculation
mg_needed = ppm_per_ml * (v_target_ml / 1000.0)    # mg needed per 1 mL dose
mg_per_mL_solution = mg_needed
g_per_100mL = (mg_per_mL_solution / 1000.0) * 100
percent_wv = g_per_100mL

# Output
st.subheader("📊 Results")
st.write(f"- Each 1 mL dose must contain **{mg_needed:.3f} mg active**.")
st.write(f"- Required working solution concentration: **{percent_wv:.4f} % w/v**")

# Optional: total active needed for all solution
total_active_g = (mg_per_mL_solution * v_prep_ml) / 1000.0
st.write(f"- To prepare {v_prep_ml} mL working solution, you need **{total_active_g:.3f} g active**.")
