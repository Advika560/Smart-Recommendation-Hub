import streamlit as st

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Smart Recommendation Hub",
    page_icon="🎯",
    layout="wide"
)

# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

.stApp {
    background-color: #0E1117;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg,#ff4b4b,#ff8c00);
    color: white;
    border: none;
    border-radius: 10px;
    height: 3rem;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
}

/* Cards */
.card {
    background-color: #1e2430;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
}

/* Recommendation Cards */
.rec-card {
    background: linear-gradient(135deg,#232526,#414345);
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 10px;
    border-left: 5px solid orange;
}

/* Section Headers */
.section-title {
    color: #FFD700;
    font-size: 32px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# HEADER
# =====================================

st.markdown("""
<h1 style='text-align:center;
padding:20px;
border-radius:15px;
background: linear-gradient(90deg,#ff4b4b,#ff8c00,#ffd700);
color:white;'>
🎯 Smart Recommendation Hub
</h1>
""", unsafe_allow_html=True)

st.markdown(
    """
    <h4 style='text-align:center;'>
    Personalized AI Recommendations for Food, Movies, Products & Travel
    </h4>
    """,
    unsafe_allow_html=True
)

# =====================================
# SIDEBAR
# =====================================

with st.sidebar:
    st.title("🚀 Navigation")

    st.info("""
    Smart Recommendation Hub

    Build your profile and get:

    🍕 Food Suggestions

    🎬 Movie Suggestions

    🛒 Product Suggestions

    ✈️ Travel Suggestions
    """)

# =====================================
# PERSONAL INFORMATION
# =====================================

st.markdown("<div class='card'>", unsafe_allow_html=True)

st.markdown(
    "<div class='section-title'>👤 Personal Information</div>",
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Enter your Name")

with col2:
    age = st.number_input(
        "Enter your Age",
        min_value=1,
        max_value=100,
        step=1
    )

budget = st.number_input(
    "Enter your Budget (₹)",
    min_value=100,
    step=100
)

st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# FOOD PREFERENCES
# =====================================

st.markdown("<div class='card'>", unsafe_allow_html=True)

st.markdown(
    "<div class='section-title'>🍕 Food Preferences</div>",
    unsafe_allow_html=True
)

food_preferences = st.multiselect(
    "Select Food Preferences",
    [
        "Vegetarian",
        "Non-Vegetarian",
        "Eggetarian",
        "Vegan",
        "Jain Food",
        "Gluten Free",
        "Lactose Free",
        "Low Carb",
        "Keto",
        "High Protein",
        "Low Fat",
        "Diabetic Friendly"
    ]
)

allergies = st.text_area(
    "Food Allergies (Optional)",
    placeholder="Example: Peanuts, Milk, Soy, Shellfish"
)

st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# HEALTH INFORMATION
# =====================================

st.markdown("<div class='card'>", unsafe_allow_html=True)

st.markdown(
    "<div class='section-title'>🏥 Health Information</div>",
    unsafe_allow_html=True
)

medical_conditions = st.multiselect(
    "Medical Conditions",
    [
        "Diabetes",
        "High Blood Pressure",
        "Heart Disease",
        "PCOS",
        "Thyroid",
        "Obesity"
    ]
)

st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# MOVIE PREFERENCES
# =====================================

st.markdown("<div class='card'>", unsafe_allow_html=True)

st.markdown(
    "<div class='section-title'>🎬 Movie Preferences</div>",
    unsafe_allow_html=True
)

movie_genres = st.multiselect(
    "Favorite Movie Genres",
    [
        "Action",
        "Comedy",
        "Sci-Fi",
        "Romance",
        "Thriller",
        "Horror",
        "Drama",
        "Adventure",
        "Animation",
        "Biography",
        "Crime",
        "Documentary",
        "Fantasy",
        "Family",
        "History",
        "Mystery",
        "Musical",
        "Sport",
        "War",
        "Western"
    ]
)

st.markdown("</div>", unsafe_allow_html=True)

# =====================================
# PROFILE COMPLETION
# =====================================

completion = 0

if name:
    completion += 25

if food_preferences:
    completion += 25

if medical_conditions:
    completion += 25

if movie_genres:
    completion += 25

st.subheader("📊 Profile Completion")

st.progress(completion)

st.write(f"Profile Completion: {completion}%")

# =====================================
# BUTTON
# =====================================

if st.button("🚀 Generate Recommendations"):

    st.success(f"Hello {name}! Here are your personalized recommendations.")

    # =====================================
    # USER PROFILE
    # =====================================

    st.header("📋 Your Profile")

    st.write("**Name:**", name)
    st.write("**Age:**", age)
    st.write("**Budget:** ₹", budget)

    st.write("**Food Preferences:**")
    st.write(food_preferences)

    st.write("**Allergies:**")
    st.write(allergies if allergies else "None")

    st.write("**Medical Conditions:**")
    st.write(medical_conditions if medical_conditions else "None")

    st.write("**Favorite Movie Genres:**")
    st.write(movie_genres)

    # =====================================
    # FOOD RECOMMENDATIONS
    # =====================================

    st.header("🍕 Food Recommendations")

    if "Vegetarian" in food_preferences:
        st.markdown("""
        <div class='rec-card'>
        🍕 Paneer Tikka<br>
        ⭐ High Protein<br>
        🥗 Vegetarian
        </div>
        """, unsafe_allow_html=True)

    if "Non-Vegetarian" in food_preferences:
        st.markdown("""
        <div class='rec-card'>
        🍗 Chicken Biryani<br>
        ⭐ Popular Choice
        </div>
        """, unsafe_allow_html=True)

    if "Eggetarian" in food_preferences:
        st.markdown("""
        <div class='rec-card'>
        🥚 Egg Curry
        </div>
        """, unsafe_allow_html=True)

    if "Vegan" in food_preferences:
        st.markdown("""
        <div class='rec-card'>
        🥗 Vegan Buddha Bowl
        </div>
        """, unsafe_allow_html=True)

    if "High Protein" in food_preferences:
        st.markdown("""
        <div class='rec-card'>
        💪 Grilled Paneer & Quinoa
        </div>
        """, unsafe_allow_html=True)

    # =====================================
    # MOVIE RECOMMENDATIONS
    # =====================================

    st.header("🎬 Movie Recommendations")

    if "Sci-Fi" in movie_genres:
        st.markdown("""
        <div class='rec-card'>
        🎬 Interstellar<br>
        ⭐ IMDb 8.7
        </div>
        """, unsafe_allow_html=True)

    if "Action" in movie_genres:
        st.markdown("""
        <div class='rec-card'>
        🎬 Avengers: Endgame
        </div>
        """, unsafe_allow_html=True)

    if "Comedy" in movie_genres:
        st.markdown("""
        <div class='rec-card'>
        🎬 3 Idiots
        </div>
        """, unsafe_allow_html=True)

    if "Romance" in movie_genres:
        st.markdown("""
        <div class='rec-card'>
        🎬 The Notebook
        </div>
        """, unsafe_allow_html=True)

    if "Thriller" in movie_genres:
        st.markdown("""
        <div class='rec-card'>
        🎬 Se7en
        </div>
        """, unsafe_allow_html=True)

    if "Horror" in movie_genres:
        st.markdown("""
        <div class='rec-card'>
        🎬 The Conjuring
        </div>
        """, unsafe_allow_html=True)

    if "Drama" in movie_genres:
        st.markdown("""
        <div class='rec-card'>
        🎬 The Shawshank Redemption
        </div>
        """, unsafe_allow_html=True)

    if "Adventure" in movie_genres:
        st.markdown("""
        <div class='rec-card'>
        🎬 Indiana Jones
        </div>
        """, unsafe_allow_html=True)

    if "Animation" in movie_genres:
        st.markdown("""
        <div class='rec-card'>
        🎬 Coco
        </div>
        """, unsafe_allow_html=True)

    if "Crime" in movie_genres:
        st.markdown("""
        <div class='rec-card'>
        🎬 The Godfather
        </div>
        """, unsafe_allow_html=True)

    if "Fantasy" in movie_genres:
        st.markdown("""
        <div class='rec-card'>
        🎬 Harry Potter
        </div>
        """, unsafe_allow_html=True)