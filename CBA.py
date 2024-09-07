# %%

#pip install streamlit

# %%
import streamlit as st

# %%
# Create input fields for the user to input values
st.title("Cost-Benefit Analysis")
st.markdown("""<style>.big-font {font-size:30px;}</style><div class='big-font'>Trading a 4Runner for a Tesla Model 3</div>""", unsafe_allow_html=True)
st.text("")

# Inputs for 4Runner
st.header("4Runner")
gas_price_per_gallon = st.number_input("Gas price per gallon ($)", value=3.00)
miles_per_year = st.number_input("Miles driven per year", value=20000)
mpg_4runner = st.number_input("4Runner MPG", value=18)
maintenance_4runner = st.number_input("Annual maintenance cost for 4Runner ($)", value=400)
insurance_4runner = st.number_input("Annual insurance cost for 4Runner ($)", value=618)
trade_in_value_4runner = st.number_input("Trade-in value for 4Runner ($)", value=31000)
amount_owed_4runner = st.number_input("Amount owed on 4Runner ($)", value=0)
#depreciation_4runner = st.number_input("5-year depreciation for 4Runner ($)", value=3000)

# Inputs for Tesla
st.header("Tesla")
electricity_cost_per_kwh = st.number_input("Electricity cost per kWh ($)", value=0.15)
miles_per_kwh = st.number_input("Tesla efficiency (miles per kWh)", value=4)
#maintenance_tesla = st.number_input("Annual maintenance cost for Tesla ($)", value=500)
insurance_tesla = st.number_input("Annual insurance cost for Tesla ($)", value=2260)
#depreciation_tesla = st.number_input("5-year depreciation for Tesla ($)", value=1500)
purchase_cost_tesla = st.number_input("Purchase cost for Tesla ($)", value=27000)
tax_incentives = st.number_input("Tax incentives for Tesla ($)", value=0)

# Calculate 4Runner Costs
fuel_cost_4runner = (miles_per_year / mpg_4runner) * gas_price_per_gallon
total_4runner_costs = (fuel_cost_4runner + maintenance_4runner + insurance_4runner) * 5

# Calculate Tesla Costs
electricity_cost_tesla = (miles_per_year / miles_per_kwh) * electricity_cost_per_kwh
total_tesla_costs = (electricity_cost_tesla + insurance_tesla) * 5 + (purchase_cost_tesla - trade_in_value_4runner + amount_owed_4runner - tax_incentives)

# Display results
st.subheader("Results")
st.write(f"5-year total cost of owning the 4Runner: ${total_4runner_costs:,.2f}")
st.write(f"5-year total cost of owning the Tesla: ${total_tesla_costs:,.2f}")

# Compare Costs
cost_difference = total_4runner_costs - total_tesla_costs
monthly_difference = cost_difference / 60
if cost_difference > 0:
    st.success(f"Switching to the Tesla will save you ${cost_difference:,.2f} over 5 years.")
    st.success(f"This is a savings of ${monthly_difference:,.2f} per month over the next 5 years.")
else:
    st.error(f"Switching to the Tesla will cost you an additional ${abs(cost_difference):,.2f} over 5 years.")
    st.error(f"This will cost an extra ${abs(monthly_difference):,.2f} per month over the next 5 years.")




