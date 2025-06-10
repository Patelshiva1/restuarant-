import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Foodie Restaurant", layout="wide")

# --- Header ---
st.markdown("<h1 style='text-align: center; color: #D2691E;'>Welcome to Foodie Restaurant</h1>", unsafe_allow_html=True)
st.image("images/food-delivery-stickers-set-260nw-84845332.jpg", use_container_width=True)

# --- Navigation ---
menu = st.sidebar.radio("Go to", ["Home", "Menu", "Gallery", "About", "Contact"])

# --- Home Page ---
if menu == "Home":
    st.header("Home")
    st.image("images/croissant_chicken_salad_sandwich_4.jpg", use_container_width=True)
    st.write("""
    Welcome to Foodie Restaurant – your go-to place for delicious meals, warm ambiance, and fantastic service. 
    Our passion is crafting food that makes you smile.
    """)

# --- Menu Page ---
elif menu == "Menu":
    st.header("Our Menu")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🥪 Chicken Salad Sandwich")
        st.image("images/croissant_chicken_salad_sandwich_4.jpg", use_container_width=True)
        st.write("Fresh croissant filled with creamy chicken salad. **₹150**")

        st.subheader("🍝 Salmon Pasta")
        st.image("images/salmon-pasta-8e85b03.jpg", use_container_width=True)
        st.write("Pasta tossed in creamy sauce with grilled salmon. **₹320**")

        st.subheader("🍔 Double Patty Burger")
        st.image("images/large-burger-with-two-fried-cutlets-cheese-vegetables-round-wheat-flour-bun_1073222-6.jpg", use_container_width=True)
        st.write("Juicy burger with two patties, cheese, and veggies. **₹220**")

    with col2:
        st.subheader("🥩 Grilled Steak with Fries")
        st.image("images/plate-grilled-beef-steak-with-french-fries-dark-top-view_318269-949.jpg", use_container_width=True)
        st.write("Tender grilled steak served with crispy fries. **₹450**")

        st.subheader("🍷 Sangria")
        st.image("images/Sangria-1ef6fdc.jpg", use_container_width=True)
        st.write("Refreshing sangria with a fruity twist. **₹180**")

        st.subheader("🍛 Special Combo")
        st.image("images/news15027.jpg", use_container_width=True)
        st.write("A delightful chef's special combo meal. **₹299**")

# --- Gallery Page ---
elif menu == "Gallery":
    st.header("Food Gallery")
    gallery_images = [
        "images/croissant_chicken_salad_sandwich_4.jpg",
        "images/plate-grilled-beef-steak-with-french-fries-dark-top-view_318269-949.jpg",
        "images/large-burger-with-two-fried-cutlets-cheese-vegetables-round-wheat-flour-bun_1073222-6.jpg",
        "images/salmon-pasta-8e85b03.jpg",
        "images/news15027.jpg",
        "images/8bwpze1ygsr11.jpg"
    ]

    cols = st.columns(3)
    for i, img_path in enumerate(gallery_images):
        with cols[i % 3]:
            st.image(img_path, use_container_width=True)

# --- About Page ---
elif menu == "About":
    st.header("About Us")
    st.image("images/types-of-chefs.jpg", use_container_width=True)
    st.write("""
    Foodie Restaurant is more than just a place to eat – it's a place to experience culinary passion.
    
    Our chefs are dedicated professionals who love creating memorable meals for every guest.
    We pride ourselves on quality, freshness, and a welcoming environment.
    """)

# --- Contact Page ---
elif menu == "Contact":
    st.header("Contact Us")
    st.image("images/images.jpg", use_container_width=True)
    st.write("""
    📞 Phone: +91 9876543210  
    📧 Email: contact@foodierestaurant.com  
    📍 Address: 123 Foodie Lane, Taste Town, India
    """)
    st.text_input("Your Name")
    st.text_input("Your Email")
    st.text_area("Your Message")
    st.button("Send")
