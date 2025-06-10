import streamlit as st
import base64

# Function to encode image as base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Load logo image
logo_base64 = get_base64_image("spicy-food-logo-vector-21348612.jpg")

# Set page config
st.set_page_config(page_title="Spicy Food Restaurant", layout="wide")

# Custom CSS styling
st.markdown("""
<style>
.centered {
    text-align: center;
}
.logo-img {
    width: 300px;
    height: auto;
    display: block;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 15px;
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
    cursor: pointer;
    margin: 5px;
    font-weight: bold;
}
.nav-buttons {
    margin-bottom: 30px;
}
input[type="text"] {
    padding: 8px;
    border-radius: 6px;
    border: 1px solid #ddd;
    width: 250px;
}
.menu-image {
    border-radius: 12px;
}
.ambiance-img {
    border-radius: 12px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = "Home"

def set_page(page_name):
    st.session_state.page = page_name

# Render logo and navigation
def render_header():
    st.markdown(f"""
    <div class="centered">
        <img src="data:image/jpeg;base64,{logo_base64}" class="logo-img" alt="Spicy Food Logo">
        <h1 style="color:#fd315a; margin-bottom: 5px;">Spicy Food</h1>
        <div class="nav-buttons">
    """, unsafe_allow_html=True)

    cols = st.columns(4)
    with cols[0]:
        if st.button("Home"):
            set_page("Home")
    with cols[1]:
        if st.button("Menu"):
            set_page("Menu")
    with cols[2]:
        if st.button("Order"):
            set_page("Order")
    with cols[3]:
        if st.button("Delivery"):
            set_page("Delivery")

    st.markdown("</div></div>", unsafe_allow_html=True)

# --- Home Page ---
def home_page():
    st.markdown("""
    <div class="centered">
        <p style="font-size:18px; max-width:600px; margin: auto; color:#555;">
            Welcome to Spicy Food Restaurant — your destination for delicious, fresh, and healthy meals made with love.
            Experience our diverse menu from breakfast to dinner, all crafted to satisfy your cravings.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""<h2 class="centered" style="margin-top: 50px;">Our Ambiance</h2>""", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1.image("interior.jpg", caption="Restaurant Interior", use_container_width=True)
    col2.image("balcony.jpg", caption="Balcony View", use_container_width=True)
    col3.image("rest.jpg", caption="Restaurant Exterior", use_container_width=True)

    st.markdown("""
    <div class="centered" style="margin-top: 40px;">
        <h1>Best Food for <span style="color: #fd315a;">Best Restaurants</span></h1>
        <p style="font-size:16px; max-width:500px; margin:auto; color:#666;">
            Local Fresh Healthy Food starting from just $4.99
        </p>
        <input type="text" placeholder="Enter your ZIP code" style="margin-top: 15px;">
        <br><br>
        <button class="red-button">Search Food</button>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="centered" style="margin-top: 50px;">
        <h2>Why Choose Spicy Food?</h2>
        <p style="max-width: 700px; margin: auto; color:#444; font-size:16px;">
            ✔️ Fresh Ingredients<br>
            ✔️ Friendly Staff & Quick Service<br>
            ✔️ Affordable Prices<br>
            ✔️ Cozy Ambiance & Family Friendly<br>
            ✔️ Multiple Cuisines to Explore
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- Menu Page ---
def menu_page():
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

# --- Order Page ---
def order_page():
    st.markdown("""
    <div class="centered">
        <h1 style="color:#fd315a;">Place Your Order</h1>
        <p style="max-width: 600px; margin:auto; color:#555; font-size:16px;">
            Select your favorite items and place an order with us!
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Order Form")
    name = st.text_input("Name")
    email = st.text_input("Email")
    menu_items = {
        "Veg Sandwich": 4.99,
        "Idli Sambar": 3.49,
        "Poori Bhaji": 4.29,
        "Veg Thali": 6.99,
        "Chicken Biryani": 8.49,
        "Paneer Butter Masala": 7.99,
        "Tandoori Roti": 2.99,
        "Dal Tadka": 5.99,
        "Fish Curry": 9.49,
    }
    selected_items = st.multiselect("Select Menu Items", options=list(menu_items.keys()))
    quantities = {}
    for item in selected_items:
        quantities[item] = st.number_input(f"Quantity for {item}", min_value=1, max_value=20, value=1, key=item)

    if st.button("Place Order"):
        if not name or not email or not selected_items:
            st.error("Please fill your name, email and select at least one item.")
        else:
            total = sum(menu_items[item] * quantities[item] for item in selected_items)
            st.success(f"Thank you {name}! Your order totaling ${total:.2f} has been placed successfully.")
            st.balloons()

# --- Delivery Page ---
def delivery_page():
    st.markdown("""
    <div class="centered">
        <h1 style="color:#fd315a;">Delivery Information</h1>
        <p style="max-width: 600px; margin: auto; font-size: 16px; color: #555;">
            We deliver hot, fresh, and delicious meals to your doorstep! Here's everything you need to know about our delivery service.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🚚 Delivery Areas")
    st.write("- Downtown City Center")
    st.write("- Sunrise Apartments, Block A-D")
    st.write("- Tech Park & Corporate Zones")
    st.write("- 5km radius from restaurant")

    st.markdown("### ⏱️ Delivery Time")
    st.write("- Average delivery time: **30–45 minutes**")
    st.write("- Live tracking available once dispatched")

    st.markdown("### 📞 Contact Us")
    st.write("Phone: +91-98765-43210")
    st.write("Email: delivery@spicyfood.com")
    st.write("Hours: 10:00 AM – 11:00 PM (Every day)")

# --- Render Layout ---
render_header()

# Routing
if st.session_state.page == "Home":
    home_page()
elif st.session_state.page == "Menu":
    menu_page()
elif st.session_state.page == "Order":
    order_page()
elif st.session_state.page == "Delivery":
    delivery_page()
