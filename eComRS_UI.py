# Install streamlit
# import pip
# pip.main(['install', 'streamlit'])

# To check whether streamlit is installed or not
# import pkgutil

# if not pkgutil.find_loader("streamlit"):
#    print("streamlit package is not installed.")
# else:
#    print("streamlit package is installed.")


# To activate real time streamlit by using command prompt, use this code:
# streamlit run C:\Users\User\OneDrive\Desktop\Pycharm\eComRS_UI.py


import streamlit as st

# Define home page
def home():
    # Set page title and favicon
    st.set_page_config(page_title="E-commerce Recommender System", page_icon=":moneybag:")

    # Set up top navigation bar
    shop_url = "https://www.amazon.com"  # replace with your shop URL
    st.markdown(
    """
    <style>
        .topbar {
            background-color: #232f3e;
            padding: 5px 0px;
            margin-bottom: 30px;
        }
        .topbar img {
            height: 50px;
            margin: 0px 20px;
        }
        .topbar a {
            color: white;
            font-weight: bold;
            font-size: 20px;
            text-decoration: none;
            margin: 0px 10px;
        }
    </style>
    """,
    unsafe_allow_html=True,
    )

    # Set query parameter for Home page
    st.experimental_set_query_params(page="home")

    st.markdown(
    """
    <div class="topbar">
        <a href="#"><img src="https://www.logo.wine/a/logo/Amazon_(company)/Amazon_(company)-Logo.wine.svg" alt="Logo"></a>
        <a href="/">Home</a>
        <a href="/search">Search</a>
        <a href="/cart">Cart</a>
        <a href="/account">Account</a>
    </div>
    """,
    unsafe_allow_html=True,
    )

    # Add page content
    st.write("""
    # Welcome to the E-commerce Recommender System! 
    (Click 'Search' to find products you're looking for!)

    ## Hottest Products Of The Day
    Here are some products we think you might be interested in:
    """)

    # Add recommended products
    st.markdown("<a href='https://www.amazon.sg/HIRUNCE-Absorbent-Microfiber-Swimming-Climbing/dp/B09VYVHB3V/ref=sr_1_3_sspa?crid=3KJ415SDGJW9Z&keywords=sports+bag&qid=1682162997&sprefix=%2Caps%2C272&sr=8-3-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyTVBDOVNXQTdZN08xJmVuY3J5cHRlZElkPUEwMzcwODA4M1VEVjZHN1k0MlBHNiZlbmNyeXB0ZWRBZElkPUEzUjRSTlpNSDc3VU40JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==' target='_blank'><img src='https://m.media-amazon.com/images/I/61U0G0KFgQL._AC_SL1000_.jpg' width='500'></a>".format(shop_url), unsafe_allow_html=True)
    st.write("HIRUNCE Quick Dry Super Absorbent Microfiber Sweat Towel,Sports Towel With Compact net Bag,for Yoga Camping Travel Fitness Swimming Cycling Bathing Hiking(mix) (M)")

    st.markdown("<a href='https://www.amazon.sg/Barefoot-Quick-Dry-Athletic-Drainage-Kayaking/dp/B09VSDY6MV/ref=sr_1_7?crid=SAQ5YC9SV4OK&keywords=sport+shoe&qid=1682162154&sprefix=sport+shoe%2Caps%2C438&sr=8-7' target='_blank'><img src='https://m.media-amazon.com/images/I/612C2aUeDzL._AC_.jpg' width='500'></a>".format(shop_url), unsafe_allow_html=True)
    st.write("Water Shoes for Men and Women Barefoot Quick-Dry Aqua Sock Light Outdoor Athletic Sport Shoes with Drainage for Kayaking, Boating, Hiking, Surfing, Walking")

    st.markdown("<a href='https://www.amazon.sg/Motivational-Leakproof-Drinking-Fitness-Enthusiasts/dp/B09G3135MQ/ref=sr_1_1_sspa?crid=3AP65UZICJK33&keywords=sport%2Bbottle&qid=1682162220&sprefix=sport%2Bbottl%2Caps%2C432&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyUDBRNlczT0dXTVZVJmVuY3J5cHRlZElkPUEwNTQ0ODE4MUhUR0xQM0xINkZQNiZlbmNyeXB0ZWRBZElkPUEzNllGQUtYUzdXT0xEJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1' target='_blank'><img src='https://m.media-amazon.com/images/I/61-Jyh5S4AL._AC_SX679_.jpg' width='500'></a>", unsafe_allow_html=True)
    st.write("Sports Water Bottle 1L Motivational Smart Water Bottle, Sport Bottle with Handle, 32oz Leakproof BPA Free Drinking Water Bottle with Daily Time Marker for Fitness Gym and Outdoor Enthusiasts- Grey")


if st.experimental_get_query_params().get("page") == "Home":
    home()
elif st.experimental_get_query_params().get("page") == "Search":
    # Add code for search page
    pass
elif st.experimental_get_query_params().get("page") == "Cart":
    # Add code for cart page
    pass
elif st.experimental_get_query_params().get("page") == "Account":
    # Add code for account page
    pass

home()
# Define search page
#def search_page

#def search():
#    # Set query parameter for Search page
#    st.experimental_set_query_params(page="search")

#    st.write("""
    # Search Products
#    Use the search bar below to find products:
#    """)

#    # Add search bar
#    search_term = st.text_input("Search")

    # Add search results
#    if search_term:
#        st.write("Search Results:")

        # Query the search engine with the search term
#        results = search_engine.search(search_term)

        # Filter results based on recommendation score
 #       filtered_results = filter_results_by_score(results, recommend_score)

        # Display filtered results
#        for product in filtered_results:
#            st.write(product.name)
#            st.write(product.price)
#            st.write(product.image)

            # Add button to add item to cart
#            if st.button("Add to Cart"):
#                cart.add_item(product)
#                st.success(f"{product.name} added to cart!")


