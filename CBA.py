# %%

#pip install streamlit

# %%
import streamlit as st

# %%
# Create input fields for the user to input values
st.title("4Runner vs Tesla Cost-Benefit Analysis")

# Inputs for 4Runner
st.header("4Runner")
gas_price_per_gallon = st.number_input("Gas price per gallon ($)", value=3.50)
mpg_4runner = st.number_input("4Runner MPG", value=18)
miles_per_year = st.number_input("Miles driven per year", value=12000)
maintenance_4runner = st.number_input("Annual maintenance cost for 4Runner ($)", value=1000)
#insurance_4runner = st.number_input("Annual insurance cost for 4Runner ($)", value=1200)
#depreciation_4runner = st.number_input("5-year depreciation for 4Runner ($)", value=3000)

# Inputs for Tesla
st.header("Tesla")
electricity_cost_per_kwh = st.number_input("Electricity cost per kWh ($)", value=0.15)
miles_per_kwh = st.number_input("Tesla efficiency (miles per kWh)", value=4)
#maintenance_tesla = st.number_input("Annual maintenance cost for Tesla ($)", value=500)
#insurance_tesla = st.number_input("Annual insurance cost for Tesla ($)", value=1500)
#depreciation_tesla = st.number_input("5-year depreciation for Tesla ($)", value=1500)
purchase_cost_tesla = st.number_input("Purchase cost for Tesla ($)", value=45000)
trade_in_value_4runner = st.number_input("Trade-in value for 4Runner ($)", value=15000)
tax_incentives = st.number_input("Tax incentives for Tesla ($)", value=7500)

# Calculate 4Runner Costs
fuel_cost_4runner = (miles_per_year / mpg_4runner) * gas_price_per_gallon
total_4runner_costs = (fuel_cost_4runner + maintenance_4runner) * 5

# Calculate Tesla Costs
electricity_cost_tesla = (miles_per_year / miles_per_kwh) * electricity_cost_per_kwh
total_tesla_costs = (electricity_cost_tesla) * 5 + (purchase_cost_tesla - trade_in_value_4runner - tax_incentives)

# Display results
st.subheader("Results")
st.write(f"5-year total cost of owning the 4Runner: ${total_4runner_costs:,.2f}")
st.write(f"5-year total cost of owning the Tesla: ${total_tesla_costs:,.2f}")

# Compare Costs
cost_difference = total_4runner_costs - total_tesla_costs
if cost_difference > 0:
    st.success(f"Switching to the Tesla will save you ${cost_difference:,.2f} over 5 years.")
else:
    st.error(f"Switching to the Tesla will cost you an additional ${abs(cost_difference):,.2f} over 5 years.")



