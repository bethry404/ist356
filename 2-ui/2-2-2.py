import streamlit as st
# Use case for session state is to remember values between runs.

# mockup first
# then add in functionality

st.title('Order Total and History')

# initialize // only runs the very first time the page loads , that's why when it reloads it resets but not if you rerun etc,,,
if 'total_order' not in st.session_state:
    st.session_state.total_order = 0.0
    st.session_state.order_history = []

amount = st.number_input('Enter amount', min_value = 0.0)
add_to_order = st.button("Add to Order", type='primary')
clear = st.button("Clear Order", type='secondary')


# order accumulation logic
if add_to_order:
    st.session_state.total_order += amount
    st.session_state.order_history.append(amount)

# should be same code as intilization to set it back to defaults
if clear:
    st.session_state.total_order = 0.0
    st.session_state.order_history = []

st.text("Total Order: " + str(st.session_state.total_order))
for o in st.session_state.order_history:
    st.text("Order: " + str(o))


st.text("Order History: " + str(st.session_state.order_history))