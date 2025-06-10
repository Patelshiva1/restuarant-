import streamlit as st
import base64

# Function to encode image as base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Load logo image
logo_base64 = get_base64_image("spicy-food-logo-vector-21348612.jpg")

# Page setup
st.set_page_config(page_title="Spicy Food Restaurant", layout="wide")

# --- Custom CSS ---
st.markdown("""
<style>
.centered {
    text-align: center;
}
.logo-img {
    width: 100%;
    height: auto;
    max-height: 500px;
    display: block;
    margin-left: auto;
    margin-right: auto;
}
h1, h2, h3 {
    font-family: 'Arial Black', sans-serif;
}
.red-button {
    background-color: #fd315a;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# --- Logo Section ---
st.markdown(f"""
<div class="centered">
    <img src="data:image/jpeg;base64,{logo_base64}" class="logo-img">
    <h1 style="color:#fd315a;">Spicy Food</h1>
</div>
""", unsafe_allow_html=True)

# --- Hero Section ---
st.markdown("""
<div class="centered">
    <h1>Best Food for <span style="color: #fd315a;">Best Restaurants</span></h1>
    <p>Local Fresh Healthy Food From $4.99</p>
    <input type="text" placeholder="Enter your ZIP code">
    <br><br>
    <button class="red-button">Search Food</button>
</div>
""", unsafe_allow_html=True)

# --- Menu Section ---
st.markdown("""<div class="centered"><h2>Delicious Menus</h2></div>""", unsafe_allow_html=True)
cols = st.columns(3)

with cols[0]:
    st.image("breakfast.jpg", caption="Breakfast Menu", use_container_width=True)
    st.markdown("### Breakfast")
    st.markdown("- Veg Sandwich - $4.99\n- Idli Sambar - $3.49\n- Poori Bhaji - $4.29")

with cols[1]:
    st.image("lunch.jpg", caption="Lunch Menu", use_container_width=True)
    st.markdown("### Lunch")
    st.markdown("- Veg Thali - $6.99\n- Chicken Biryani - $8.49\n- Paneer Butter Masala - $7.99")

with cols[2]:
    st.image("dinner.jpg", caption="Dinner Menu", use_container_width=True)
    st.markdown("### Dinner")
    st.markdown("- Tandoori Roti - $2.99\n- Dal Tadka - $5.99\n- Fish Curry - $9.49")

# --- Services ---
st.markdown("""
<div class="centered">
    <h2>We Provide Best Services</h2>
    <p>✔️ Afternoon Tea & Wine<br>✔️ Takeaway & Delivery<br>✔️ Wine & Cocktails<br>✔️ All-hours Dining</p>
</div>
""", unsafe_allow_html=True)

# --- Deal of the Week ---
st.markdown("""<div class="centered"><h2>Deal of the Week</h2></div>""", unsafe_allow_html=True)
burger_col, text_col = st.columns([1, 1])

with burger_col:
    st.image("bur.jpg", caption="Shroom Bacon Burger", use_container_width=True)

with text_col:
    st.markdown("""
    <div style="background-color: #fd315a; color: white; padding: 2rem; border-radius: 12px;" class="centered">
        <h3>🍔 Shroom Bacon Burger</h3>
        <p>Now only <strong>$11.76</strong></p>
        <button style="background-color:white; color:#fd315a; padding:10px 20px; border:none; border-radius:5px;">Order Now</button>
    </div>
    """, unsafe_allow_html=True)

# --- Events ---
st.markdown("""
<div class="centered">
    <h2>Private Dining & Events</h2>
    <p>Book for your celebrations, private parties, and corporate events.</p>
</div>
""", unsafe_allow_html=True)

# --- Highlights ---
st.markdown("""
<div class="centered" style="background-color:#fd315a; color:white; padding:2rem; border-radius:12px;">
    <h2>Highlighting Its Unique Features and Experiences</h2>
    <p>✨ 12 Years of Excellence</p>
</div>
""", unsafe_allow_html=True)

# --- News ---
st.markdown("""
<div class="centered">
    <h2>Recent News</h2>
    <p>📰 Chicken Alfredo Launch | 📰 New Salmon Dish | 📰 Secret Food Flavors</p>
</div>
""", unsafe_allow_html=True)

# --- Reservation ---
st.markdown("""<div class="centered"><h2>Reservation Table & Enjoy Dining</h2></div>""", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    st.text_input("Name")
with c2:
    st.text_input("Email")
with c3:
    st.date_input("Date")
st.button("Book Now")

# --- Navigation Button to Voice-to-Text App ---
st.markdown("---")
st.markdown("### 🎤 Want to Try Our Voice-to-Text Assistant?")
if st.button("Go to Voice-to-Text App"):
    st.markdown(
        '<meta http-equiv="refresh" content="0;URL=\'http://192.168.164.89:8502/\'" />',
        unsafe_allow_html=True
    )

# --- Footer ---
st.markdown("""
<div class="centered" style="font-size:14px; padding-top: 2rem;">
    <hr>
    <p>📍 Spicy Food Restaurant | Open 9AM - 11PM | 7 Days a Week</p>
    <p>📬 Subscribe to our newsletter</p>
    <input type="text" placeholder="Your email">
    <button style="margin-left: 10px;" class="red-button">Submit</button>
    <p style="margin-top: 20px;">© 2025 Spicy Food. All Rights Reserved.</p>
</div>
""", unsafe_allow_html=True)