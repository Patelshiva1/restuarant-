import streamlit as st

st.set_page_config(page_title="Tasty Restaurant", layout="wide")

# --- Custom Styling ---
st.markdown("""
<style>
body {
    background-color: #fff;
}
.section {
    padding: 4rem 1rem;
}
.red-bg {
    background-color: #fd315a;
    color: white;
    padding: 3rem 1rem;
    border-radius: 12px;
}
.card {
    background-color: white;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.05);
}
.centered {
    text-align: center;
}
h1, h2, h3 {
    font-family: 'Arial Black', sans-serif;
}
</style>
""", unsafe_allow_html=True)

# --- Header Section ---
st.markdown("""
<div class="section centered">
    <h1>Best Food for <span style="color: #fd315a;">Best Restaurants</span></h1>
    <p>Local Fresh Healthy Food From $4.99</p>
    <input type="text" placeholder="Enter your ZIP code">
    <button style="margin-top: 10px; padding: 10px 20px; background-color:#fd315a; color:white; border:none; border-radius:5px;">Search Food</button>
</div>
""", unsafe_allow_html=True)

# --- Welcome Section ---
st.markdown("""
<div class="section">
    <div class="centered">
        <h2>Feel The Taste of Foods</h2>
        <p>We deliver the best meals in town, fresh & hot!</p>
        <h3>Good Food, Steak & Great Restaurant</h3>
        <p><strong>20% OFF</strong> on your first order</p>
        <button style="padding: 10px 20px; background-color:#fd315a; color:white; border:none; border-radius:5px;">Reserve a Table</button>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Menu Section ---
st.markdown("""
<div class="section centered">
    <h2>Delicious Menus</h2>
</div>
""", unsafe_allow_html=True)

menu_cols = st.columns(3)
with menu_cols[0]:
    st.markdown("### Breakfast")
    st.markdown("- Egg Sandwich - $4.99\n- Tofu Scramble - $5.49\n- Greek Yogurt - $3.99")
with menu_cols[1]:
    st.markdown("### Lunch")
    st.markdown("- Chicken Salad - $6.99\n- Pasta Alfredo - $7.99\n- Fried Rice - $5.99")
with menu_cols[2]:
    st.markdown("### Dinner")
    st.markdown("- Beef Stroganoff - $8.99\n- Grilled Salmon - $9.99\n- Veggie Curry - $6.99")

# --- Services Section ---
st.markdown("""
<div class="section centered">
    <h2>We Provide Best Services</h2>
    <p>✔️ Afternoon Tea & Wine<br>✔️ Takeaway & Delivery<br>✔️ Wine & Cocktails<br>✔️ All-hours Dining</p>
</div>
""", unsafe_allow_html=True)

# --- Deal of the Week ---
st.markdown("""
<div class="section centered red-bg">
    <h2>Deal of the Week</h2>
    <h3>🍔 Shroom Bacon Burger</h3>
    <p>Now only <strong>$11.76</strong></p>
    <button style="padding: 10px 20px; background-color:white; color:#fd315a; border:none; border-radius:5px;">Order Now</button>
</div>
""", unsafe_allow_html=True)

# --- Events Section ---
st.markdown("""
<div class="section centered">
    <h2>Private Dining & Events</h2>
    <p>Book for your celebrations, private parties, and corporate events.</p>
</div>
""", unsafe_allow_html=True)

# --- Highlight Section ---
st.markdown("""
<div class="section red-bg centered">
    <h2>Highlighting Its Unique Features and Experiences</h2>
    <p>✨ 12 Years of Excellence</p>
</div>
""", unsafe_allow_html=True)

# --- Recent News Section ---
st.markdown("""
<div class="section centered">
    <h2>Recent News</h2>
    <p>📰 Chicken Alfredo Launch | 📰 New Salmon Dish | 📰 Secret Food Flavors</p>
</div>
""", unsafe_allow_html=True)

# --- Reservation Section ---
st.markdown("""
<div class="section">
    <h2 class="centered">Reservation Table & Enjoy Dining Table</h2>
""", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    name = st.text_input("Name")
with col2:
    email = st.text_input("Email")
with col3:
    date = st.date_input("Date")
st.button("Book Now")

# --- Footer ---
st.markdown("""
<div class="section centered" style="font-size: 14px;">
    <hr>
    <p>📍 Tasty Restaurant | Open 9AM - 11PM | 7 Days a Week</p>
    <p>📬 Subscribe to our newsletter</p>
    <input type="text" placeholder="Your email"><button style="margin-left: 10px; background-color: #fd315a; color:white;">Submit</button>
    <p style="margin-top: 20px;">© 2025 Tasty Restaurant. All Rights Reserved.</p>
</div>
""", unsafe_allow_html=True)