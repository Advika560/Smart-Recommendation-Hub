import streamlit as st
import pandas as pd
import plotly.express as px
pastel_colors = [
    "#BFA3A3",  # Dusty Rose
    "#DCC6CC",  # Pale Mauve
    "#D7E3D4",  # Seafoam Mist
    "#BFC7D5",  # Blue Grey
    "#CFC3E8",  # Powder Lilac
    "#F2D6D0",  # Soft Blush
]
# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Smart Recommendation Hub",
    page_icon="🎯",
    layout="wide"
)
# Load Food Dataset
foods_df = pd.read_csv(
    "datasets/comprehensive_foods_usda.csv"
)
if "favorites" not in st.session_state:
    st.session_state.favorites = []
st.sidebar.markdown(f"""
<div style="
background:#F6F1F1;
padding:15px;
border-radius:12px;
border-left:5px solid #CDB7C5;
color:#6F5A64;
font-weight:600;
font-size:18px;
">
📊 Foods Loaded: {len(foods_df):,}
</div>
""", unsafe_allow_html=True)
# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
           
<style>
            button[data-testid="stNumberInputStepUp"],
button[data-testid="stNumberInputStepDown"] {
    background-color: #F6F1F1 !important;
    color: #2E2E2E !important;
    border: 1px solid #D8CACA !important;
}

button[data-testid="stNumberInputStepUp"]:hover,
button[data-testid="stNumberInputStepDown"]:hover {
    background-color: #E8D5D5 !important;
    color: black !important;
}
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}
            /* ===== PASTEL SIDEBAR ===== */

section[data-testid="stSidebar"] {
    background: #E8D5D5 !important; /* Soft Blush */
    border-right: 2px solid #D7C4C4;
}

section[data-testid="stSidebar"] * {
    color: #6F5A64 !important; /* Vintage Mauve */
}

section[data-testid="stSidebar"] .stButton > button {
    background: #DCC6CC !important; /* Pale Mauve */
    color: #6F5A64 !important;
    border: none !important;
    border-radius: 12px !important;
}

section[data-testid="stSidebar"] .stButton > button:hover {
    background: #CDB7C5 !important;
}
            .main .block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
}
.metric-card{
    background: linear-gradient(
        135deg,
        #E8D5D5,
        #F6EEEE
    );
    padding:20px;
    border-radius:20px;
    text-align:center;
    border:2px solid #DCC6CC;
    box-shadow:0 8px 20px rgba(0,0,0,0.08);
}
.metric-card h4 {
    color: #6F5A64 !important;
    font-size: 28px;
    font-weight: 700;
}

.metric-card p {
    color: #4A4A4A !important;
    font-size: 18px;
}
.metric-title{
    color:#7D6B73;
    font-size:16px;
    font-weight:600;
}
.metric-value{
    color:#6F5A64;
    font-size:36px;
    font-weight:700;
}

.stApp {
    background: #BFA3A3;
}

/* Buttons */
.stButton > button {
    background: #DCC6CC;
    color: #6F5A64;
    border: none;
    border-radius: 14px;
    height: 3rem;
    width: 100%;
    font-size: 16px;
    font-weight: 600;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
}

.stButton > button:hover {
    background: #CDB7C5;
    transform: translateY(-2px);
    transition: 0.3s;
}

/* Cards */
.card {
    background: #F6EEEE;
    padding:20px;
    border-radius:20px;
    margin-bottom: 25px;
    border: 1px solid #DCC6CC; /* Pale Mauve */
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
}

/* Recommendation Cards */
.rec-card {
    background: #E8D5D5;   /* Soft Blush */
    padding: 20px;
    border-radius: 20px;
    margin-bottom: 20px;
    border-left: 6px solid #A67C87; /* Vintage Mauve */
    min-height: 320px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
}
.rec-card h3 {
    color: #6F5A64 !important;   /* Vintage Mauve */
    font-weight: 700;
}

.rec-card p {
    color: #4E5968 !important;   /* Blue Grey */
    font-size: 17px;
    font-weight: 500;
}
.rec-card:hover {
    transform: translateY(-8px);
    transition: 0.3s ease;
}
.chart-card{
    background:#F6EEEE;
    padding:20px;
    border-radius:20px;
    box-shadow:0 6px 18px rgba(0,0,0,0.08);
    margin-bottom:20px;
}
/* Section Headers */
.section-title {
    color:#A67C87;
    font-size:36px;
    font-weight:700;
    letter-spacing:0.5px;
}
/* INPUT BOXES */

.stTextInput input,
.stNumberInput input,
.stTextArea textarea {
    background: #F6EEEE !important;
    color: #4E5968 !important;
    border: 2px solid #DCC6CC !important;
    border-radius: 12px !important;
}

/* DROPDOWNS */

.stSelectbox > div > div,
.stMultiSelect > div > div {
    background: #F6EEEE !important;
    color: #4E5968 !important;
    border: 2px solid #DCC6CC !important;
    border-radius: 12px !important;
}
button[data-testid="stNumberInputStepUp"],
button[data-testid="stNumberInputStepDown"] {
    background-color: #F6F1F1 !important;
    color: #2E2E2E !important;
    border: 1px solid #D8CACA !important;
}

button[data-testid="stNumberInputStepUp"]:hover,
button[data-testid="stNumberInputStepDown"]:hover {
    background-color: #F6F1F1 !important;
    color: #2E2E2E !important;
}
            /* Food Preference Dropdown */

div[data-baseweb="select"] > div {
    background-color: #F6F1F1 !important;
    border: 1px solid #D8CACA !important;
    color: #2E2E2E !important;
}

div[data-baseweb="select"] span {
    color: #6F5A64 !important;
}

div[data-baseweb="select"] svg {
    fill: #6F5A64 !important;
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
background: linear-gradient(
90deg,
#DCC6CC,
#E8D5D5,
#F6EEEE,
#D7E3D4
);
color:#6F5A64;
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

    st.markdown("""
<div style="
background:#F6F1F1;
padding:20px;
border-radius:15px;
border-left:5px solid #CDB7C5;
color:#4A4A4A;
box-shadow:0 4px 12px rgba(0,0,0,0.08);
">

<h4 style="color:#6F5A64;margin-top:0;">
✨ Smart Recommendation Hub
</h4>

<p style="color:#4A4A4A;">
Build your profile and get:
</p>

<p>🍕 Food Suggestions</p>
<p>🎬 Movie Suggestions</p>
<p>🛒 Product Suggestions</p>
<p>✈️ Travel Suggestions</p>

</div>
""", unsafe_allow_html=True)

# =====================================
# PERSONAL INFORMATION
# =====================================

st.markdown("<div class='card'>", unsafe_allow_html=True)

st.markdown(
    "<div class='section-title'>👤 Personal Information</div>",
    unsafe_allow_html=True
)

col1, col2 = st.columns([1,1])

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
protein_range = st.slider(
    "Protein Range (g)",
    0,
    50,
    (5, 25)
)
calorie_range = st.slider(
    "Calories Range",
    0,
    1000,
    (100, 500)
)
health_score_filter = st.slider(
    "Minimum Health Score",
    0,
    100,
    60
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

st.header("🍽️ Recommended Foods")
st.markdown("---")
st.subheader("🎯 Personalized Recommendations")
filtered_foods = foods_df.copy()

if "High Protein" in food_preferences:
        filtered_foods = filtered_foods[
            filtered_foods["protein_g"] > 20
        ]

if "Low Fat" in food_preferences:
        filtered_foods = filtered_foods[
            filtered_foods["fat_g"] < 10
        ]

if "Low Carb" in food_preferences:
        filtered_foods = filtered_foods[
            filtered_foods["carbs_g"] < 20
        ]

if "Diabetic Friendly" in food_preferences:
        filtered_foods = filtered_foods[
            filtered_foods["sugar_g"] < 10
        ]
if "Vegetarian" in food_preferences:
    filtered_foods = filtered_foods[
        filtered_foods["food_type"].isin([
            "Vegetables",
            "Fruits",
            "Grains",
            "Dairy"
        ])
    ]
if "Vegan" in food_preferences:
    filtered_foods = filtered_foods[
        filtered_foods["food_type"].isin([
            "Vegetables",
            "Fruits",
            "Grains"
        ])
    ]

# Create recommendation score
filtered_foods["score"] = 0

if "High Protein" in food_preferences:
    filtered_foods["score"] += filtered_foods["protein_g"] * 0.3

if "Low Fat" in food_preferences:
    filtered_foods["score"] += (100 - filtered_foods["fat_g"]) * 0.2

if "Low Carb" in food_preferences:
    filtered_foods["score"] += (100 - filtered_foods["carbs_g"]) * 0.2
filtered_foods["score"] += filtered_foods["health_score"] * 0.5
filtered_foods = filtered_foods[
    (filtered_foods["calories"] > 0) &
    (filtered_foods["calories"] < 1000)
]
filtered_foods = filtered_foods[
    ~filtered_foods["food_name"].str.contains(
        "protein|powder|supplement|shake|drink|collagen",
        case=False,
        na=False
    )
]
allowed_categories = [
    "Fruits",
    "Vegetables",
    "Grains",
    "Dairy",
    "Seafood",
    "Meat & Poultry"
]

filtered_foods = filtered_foods[
    filtered_foods["food_type"].isin(allowed_categories)
]
# Sort by score
recommended_foods = filtered_foods.sort_values(
    by="score",
    ascending=False
).head(20)
recommended_foods = recommended_foods[
    (recommended_foods["protein_g"] >= protein_range[0]) &
    (recommended_foods["protein_g"] <= protein_range[1]) &
    (recommended_foods["calories"] >= calorie_range[0]) &
    (recommended_foods["calories"] <= calorie_range[1]) &
    (recommended_foods["health_score"] >= health_score_filter)
]
if not recommended_foods.empty:
    top_food = recommended_foods.iloc[0]
score = top_food['health_score']

if score >= 80:
    badge = "🟢 Excellent Choice"
elif score >= 60:
    badge = "🟡 Good Choice"
else:
    badge = "🔴 Moderate Choice"
    st.markdown(f"""
<div style="
background:#F6F1F1;
padding:25px;
border-radius:15px;
border-left:6px solid #CDB7C5;
box-shadow:0 4px 10px rgba(0,0,0,0.08);
margin-bottom:20px;
">

<h3 style="color:#6F5A64;margin-top:0;">
💡 Why this recommendation?
</h3>

<p style="font-size:22px;font-weight:600;color:#4A4A4A;">
{top_food['food_name']}
</p>

<p style="color:#6F5A64;font-size:17px;">
• Protein: {top_food['protein_g']} g <br>
• Calories: {top_food['calories']} <br>
• Health Score: {top_food['health_score']}
</p>
<br><br>

<span style="
background:#D8E2D0;
padding:8px 15px;
border-radius:20px;
font-weight:600;
color:#4A4A4A;
">
{badge}
</span>

<br><br>
<p style="color:#4A4A4A;">
This food best matches your selected filters and preferences.
</p>

</div>
""", unsafe_allow_html=True)
st.subheader("📊 Recommendation Dashboard")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Foods Found",
        len(recommended_foods)
    )
with col2:
    st.metric(
        "Avg Protein",
        round(recommended_foods["protein_g"].mean(), 1))
with col3:
    st.metric(
        "Best Score",
        recommended_foods["score"].max()
    )
with col4:
    st.metric(
        "Avg Calories",
        round(recommended_foods["calories"].mean(), 1)
    )
st.divider()
st.subheader("📊 Nutrition Insights")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🔥 Avg Calories",
        round(recommended_foods["calories"].mean(), 1)
    )

with col2:
    st.metric(
        "💪 Avg Protein",
        round(recommended_foods["protein_g"].mean(), 1)
    )

with col3:
    st.metric(
        "❤️ Avg Health Score",
        round(recommended_foods["health_score"].mean(), 1)
    )

col1, col2, col3 = st.columns(3)

with col1:
    highest_protein = recommended_foods.loc[
        recommended_foods["protein_g"].idxmax()
    ]
    st.markdown(f"""
<div style="
background:#E8F1EC;
padding:20px;
border-radius:15px;
color:#2E8B7A;
font-weight:600;
">
💪 Highest Protein<br><br>
{highest_protein['food_name'][:30]}
</div>
""", unsafe_allow_html=True)

with col2:
    lowest_calorie = recommended_foods.loc[
        recommended_foods["calories"].idxmin()
    ]
    st.markdown(f"""
<div style="
background:#EEEAF7;
padding:20px;
border-radius:15px;
color:#6A5ACD;
font-weight:600;
">
🔥 Lowest Calories<br><br>
{lowest_calorie['food_name'][:30]}
</div>
""", unsafe_allow_html=True)
with col3:
    healthiest = recommended_foods.loc[
        recommended_foods["health_score"].idxmax()
    ]
    st.markdown(f"""
<div style="
background:#FDF1E8;
padding:20px;
border-radius:15px;
color:#C57A1F;
font-weight:600;
">
💖 Healthiest Choice<br><br>
{healthiest['food_name'][:30]}
</div>
""", unsafe_allow_html=True)
st.subheader(
    f"📋 Recommendation Summary for {name if name else 'Guest User'}"
)

st.markdown(f"""
<div style="
background:#EEF3FB;
padding:25px;
border-radius:18px;
color:#2F5DA8;
font-size:18px;
line-height:2;
">

🎯 Total Recommendations Found: {len(recommended_foods)}<br>

🥇 Best Match: {recommended_foods.iloc[0]['food_name']}<br>

📁 Category: {recommended_foods.iloc[0]['food_category']}<br>

❤️ Health Score: {recommended_foods.iloc[0]['health_score']}

</div>
""", unsafe_allow_html=True)
top_food = recommended_foods.iloc[0]

st.markdown(f"""
<div style="
background:#FAF7EA;
padding:25px;
border-radius:18px;
color:#C58A00;
font-size:18px;
line-height:2;
font-weight:600;
">

🌟 TODAY'S BEST RECOMMENDATION<br><br>

🥇 {top_food['food_name']}<br>

📁 Category: {top_food['food_category']}<br>

❤️ Health Score: {top_food['health_score']}

</div>
""", unsafe_allow_html=True)
search_food = st.text_input(
    "🔍 Search Recommended Foods",
    placeholder="Type food name..."
)
st.subheader("⭐ Top 5 Food Recommendations")
st.subheader("🎯 Recommendation Confidence")

confidence = round(
    recommended_foods["health_score"].mean(),
    1
)

st.progress(int(confidence))

st.write(f"Confidence Score: {confidence}%")
food_images = {
    "Vegetables": "🥦",
    "Fruits": "🍎",
    "Seafood": "🐟",
    "Dairy": "🥛",
    "Meat & Poultry": "🍗",
    "Beverages": "🥤",
    "Grains": "🌾",
    "Snacks & Sweets": "🍪",
    "Other": "🍽️"
}
display_foods = recommended_foods

if search_food:
    display_foods = display_foods[
        display_foods["food_name"]
        .str.contains(search_food, case=False, na=False)
    ]
col1, col2 = st.columns(2)
for i, (_, row) in enumerate(
    display_foods.head(5).iterrows(),
    start=1
):
    
    food_type = row["food_type"]
    emoji = food_images.get(food_type, "🍽️")

    reason = []

    if row["protein_g"] > 20:
        reason.append("High Protein")

    if row["fat_g"] < 5:
        reason.append("Low Fat")

    if row["carbs_g"] < 15:
        reason.append("Low Carb")

    if row["health_score"] >= 70:
        reason.append("Healthy Choice")
    if not reason:
        reason = ["Balanced Diet"]
    reason_text = ", ".join(reason) if reason else "General Healthy Choice"
    if row["health_score"] >= 80:
        quality = "Excellent Choice"
    elif row["health_score"] >= 70:
        quality = "Very Good Choice"
    elif row["health_score"] >= 60:
        quality = "Good Choice"
    else:
        quality = "Average Choice"
    if i == 1:
        badge = "🥇"
    elif i == 2:
        badge = "🥈"
    elif i == 3:
         badge = "🥉"
    else:
        badge = "🏅"
    if i == 1:
        card_type = "success"
    elif i <= 3:
        card_type = "info"
    else:
        card_type = "warning"
    
    card_text = f"""
    ### {badge} Rank #{i}

    **{row['food_name']}**

    <p style="color:#4A4A4A !important;">📁 {row['food_category']}</p>

    <p style="color:#4A4A4A !important;">🔥 Calories: {row['calories']}</p>

    <p style="color:#4A4A4A !important;">💪 Protein: {row['protein_g']} g</p>

    <p style="color:#4A4A4A !important;">❤️ Health Score: {row['health_score']}</p>

    <p style="color:#6F5A64 !important;font-weight:600;">🏆 {quality}</p>

    <p style="color:#A67C87 !important;font-weight:600;">⭐ {reason_text}</p>
    """
    st.markdown("---")
    target_col = col1 if i % 2 != 0 else col2
    with target_col:
      st.markdown(f"""
    <div style="
    background:#F6F1F1;
    padding:20px;
    border-radius:18px;
    border-left:6px solid #CDB7C5;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    margin-bottom:15px;
    ">
    
    <h3 style="
    color:#6F5A64;
    margin-bottom:15px;
    ">
    {badge} Rank #{i}
    </h3>

    <p style="font-size:20px;font-weight:700;color:#4A4A4A;">
    {row['food_name']}
    </p>

    <<p style="color:#4A4A4A;font-size:18px;">
    📁 {row['food_category']}
    </p>

    <p style="color:#4A4A4A;font-size:18px;">
    🔥 Calories: {row['calories']}
    </p>

    <p style="color:#4A4A4A;font-size:18px;">
    💪 Protein: {row['protein_g']} g
    </p>

    <p style="color:#4A4A4A;font-size:18px;">
    ❤️ Health Score: {row['health_score']}
    </p>

    <p style="color:#6F5A64;font-weight:600;">
    🏆 {quality}
    </p>

    <p style="color:#A67C87;font-weight:600;">
    ⭐ {reason_text}
    </p>

    </div>
    """, 
        unsafe_allow_html=True
    )
if st.button(
    f"⭐ Save {row['food_name'][:20]}",
    key=f"save_{i}"
):
    if row['food_name'] not in st.session_state.favorites:
        st.session_state.favorites.append(
            row['food_name']
        )
st.progress(min(row["score"] / recommended_foods["score"].max(), 1.0))
with st.expander(f"📋 View Details - {row['food_name'][:25]}"):
         st.write(f"🔥 Calories: {row['calories']}")
         st.write(f"💪 Protein: {row['protein_g']} g")
         st.write(f"🥑 Fat: {row['fat_g']} g")
         st.write(f"🍞 Carbs: {row['carbs_g']} g")
         st.write(f"❤️ Health Score: {row['health_score']}")
         st.write(f"📂 Category: {row['food_category']}")

st.subheader("🏆 Top Performers")
col1, col2, col3 = st.columns([1,1,1])

highest_protein = recommended_foods.loc[recommended_foods["protein_g"].idxmax()]
lowest_calorie = recommended_foods.loc[recommended_foods["calories"].idxmin()]
healthiest = recommended_foods.loc[recommended_foods["health_score"].idxmax()]
with col1:
    st.markdown(f"""
    <div class="metric-card">
    <h4>💪 Highest Protein</h4>
    <p><b>{highest_protein['food_name']}</b></p>
    <p>{highest_protein['protein_g']:.1f} g protein</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown(f"""
    <div class="metric-card">
    <h4>🥩 Highest Protein</h4>
    <p><b>{highest_protein['food_name']}</b></p>
    <p>{highest_protein['protein_g']:.1f} g protein</p>
    </div>
""", unsafe_allow_html=True)
with col2:
    st.markdown(f"""
    <div class="metric-card">
    <h4>🔥 Lowest Calories</h4>
    <p><b>{lowest_calorie['food_name'][:30]}</b></p>
    <p>{lowest_calorie['calories']} calories</p>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown(f"""
    <div class="metric-card">
    <h4>❤️ Healthiest Choice</h4>
    <p><b>{healthiest['food_name'][:30]}</b></p>
    <p>Score: {healthiest['health_score']}</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown("""
<style>
[data-testid="stDataFrame"] {
    background-color: #EEEAF7 !important;
}

[data-testid="stDataFrame"] table {
    background-color: #EEEAF7 !important;
    color: black !important;
}

[data-testid="stDataFrame"] th {
    background-color: #DCC6CC !important;
    color: black !important;
    font-weight: bold !important;
}

[data-testid="stDataFrame"] td {
    background-color: #EEEAF7 !important;
    color: black !important;
}
</style>
""", unsafe_allow_html=True)
st.subheader("📊 Nutrition Comparison Chart")

chart_df = recommended_foods.head(5)

fig = px.bar(
    chart_df,
    x="food_name",
    y=["protein_g", "calories"],
    barmode="group",
    title="Top 5 Foods: Protein vs Calories"
)
fig.update_layout(
    plot_bgcolor="#F6F1F1",
    paper_bgcolor="#F6F1F1",
    font=dict(
        color="#6F5A64",
        size=14
    ),
    title_font=dict(
        size=22,
        color="#6F5A64"
    ),
    xaxis_title="Food",
    yaxis_title="Value",
    legend_title="Nutrition"
)

fig.update_traces(
    marker_line_width=1
)
fig.data[0].marker.color = "#A67C87"   # Protein
fig.data[1].marker.color = "#CDB7C5"   # Calories
fig.update_xaxes(tickangle=-25)

st.plotly_chart(fig, use_container_width=True)
st.subheader("📈 Nutrition Insights")

kpi1, kpi2, kpi3, kpi4 = st.columns(4)
with kpi1:
    st.metric(
        "Foods Found",
        len(recommended_foods)
    )
with kpi2:
    st.metric(
        "Avg Protein",
        f"{recommended_foods['protein_g'].mean():.1f} g"
    )
with kpi3:
    st.metric(
        "Best Health Score",
        f"{recommended_foods['health_score'].max():.0f}"
    )
with kpi4:
    st.metric(
        "Avg Calories",
        f"{recommended_foods['calories'].mean():.0f}"
    )
st.subheader("🏷️ Food Category Insights")
category_count = (
    recommended_foods["food_category"]
    .value_counts()
    .reset_index()
)

category_count.columns = [
    "Category",
    "Count"
]
category_fig = px.pie(
    category_count,
    values="Count",
    names="Category",
    title="Food Category Distribution",
    color_discrete_sequence=[
        "#D8A7B1",  # Dusty Rose
        "#E8CFCF",  # Soft Blush
        "#DCC6CC",  # Pale Mauve
        "#CDB7C5",  # Powder Lilac
        "#D8E2D0",  # Sage Green
        "#F6F1F1",  # Ivory Blush
        "#DCEAF7"   # Baby Blue
    ]
)
category_fig.update_layout(
    plot_bgcolor="#F6F1F1",
    paper_bgcolor="#F6F1F1",
    font_color="#6F5A64",
    title_font_size=22
)

st.plotly_chart(
    category_fig,
    use_container_width=True
)
top_category = category_count.iloc[0]

st.markdown(f"""
<div style="
background:#F6F1F1;
padding:20px;
border-radius:15px;
border-left:6px solid #CDB7C5;
margin-top:10px;
">

<h3 style="color:#6F5A64;">
🏆 Top Food Category
</h3>

<p style="
font-size:22px;
font-weight:700;
color:#4A4A4A;
">
{top_category['Category']}
</p>

<p style="color:#6F5A64;">
{top_category['Count']} recommendations found
</p>

</div>
""", unsafe_allow_html=True)
st.subheader("📊 Food Comparison Table")
styled_df = recommended_foods[
    [
        "food_name",
        "food_category",
        "calories",
        "protein_g",
        "health_score"
    ]
].style\
.set_properties(**{
    'background-color': '#EEEAF7',
    'color': 'black',
    'border-color': '#DCC6CC'
})\
.set_table_styles([
    {
        'selector': 'th',
        'props': [
            ('background-color', '#E8D5D5'),
            ('color', 'black'),
            ('font-weight', 'bold')
        ]
    },
    {
        'selector': '.row_heading',
        'props': [
            ('background-color', '#DCC6CC'),
            ('color', 'black')
        ]
    },
    {
        'selector': '.blank',
        'props': [
            ('background-color', '#DCC6CC'),
        ]
    }
])

st.table(styled_df)
st.caption(
    "Compare calories, protein, carbs and health scores across recommendations."
)
csv = recommended_foods.to_csv(index=False)
st.markdown("""
<style>
div.stDownloadButton > button {
    background-color: #DDD6F3;
    color: #2E2E2E;
    border: 2px solid #CDB7C5;
    border-radius: 12px;
    font-weight: 600;
}
div.stDownloadButton > button:hover {
    background-color: #E8D5D5;
    color: black;
}
</style>
""", unsafe_allow_html=True)
st.download_button(
    label="📥 Download Recommendations CSV",
    data=csv,
    file_name="food_recommendations.csv",
    mime="text/csv"
)
st.markdown(f"""
<div style="
background-color:#EEEAF7;
padding:20px;
border-radius:15px;
border-left:6px solid #CDB7C5;
color:#2E2E2E;
font-size:20px;
font-weight:600;
">
✨ Hello {name}! Here are your personalized recommendations.
</div>
""", unsafe_allow_html=True)
st.markdown("""
<h2 style='
color:#6F5A64;
font-size:38px;
font-weight:700;
margin-top:20px;
margin-bottom:10px;
'>
📈 Analytics Dashboard
</h2>
""", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns([1,1])

with col1:
    st.markdown("""
<h3 style='color:#A67C87;font-size:28px;font-weight:600;'>
📊 Food Categories Distribution
</h3>
""", unsafe_allow_html=True)
    st.caption("Distribution of recommended foods by category")
    


    category_counts = recommended_foods["food_type"].value_counts()

    category_df = category_counts.reset_index()
    category_df.columns = ["Category", "Count"]
    category_fig = px.bar(
    category_df,
    x="Category",
    y="Count",
    text="Count",
    color_discrete_sequence=["#D8A7B1"]  # Dusty Rose
)

    category_fig.update_layout(
    height=280,
    width=450,
    plot_bgcolor="#F8F4F1",
    paper_bgcolor="#F8F4F1",
    font_color="#6F5A64",
    xaxis_title="",
    yaxis_title=""
)

    st.plotly_chart(category_fig, use_container_width=True)
with col2:
    st.markdown("""
<h3 style='color:#A67C87;font-size:28px;font-weight:600;'>
🧭 Category Percentage
</h3>
""", unsafe_allow_html=True)

    fig = px.pie(
    values=category_counts.values,
    names=category_counts.index,
    hole=0.5,
    color_discrete_sequence=pastel_colors
)

    fig.update_layout(
    height=350,
    plot_bgcolor="#F6EEEE",
    paper_bgcolor="#F6EEEE",
    font_color="#6F5A64"
)

    st.plotly_chart(fig, use_container_width=True)

col3, col4 = st.columns(2)

with col3:

    st.markdown("""
<h3 style='color:#A67C87;font-size:28px;font-weight:600;'>
💪 Top 5 Protein Comparison
</h3>
""", unsafe_allow_html=True)
    
    chart_data = recommended_foods.head(5).copy()
    chart_data["short_name"] = (
        chart_data["food_name"].str[:20] + "..."
    )
    protein_fig = px.bar(
        chart_data,
        x="short_name",
        y="protein_g",
        color="short_name",
        color_discrete_sequence=[
         "#D8A7B1",  # Dusty Rose
         "#E8CFCF",  # Soft Blush
         "#DCC6CC",  # Pale Mauve
         "#CDB7C5",  # Powder Lilac
         "#AFC8B8"   # Seafoam Mist
    ],
        text="protein_g"
    )
    protein_fig.update_layout(
    height=400,
    xaxis_tickangle=-30,
    coloraxis_showscale=False,
    plot_bgcolor="#F6EEEE",
    paper_bgcolor="#F6EEEE",
    font_color="#6F5A64",
    showlegend=False,
    xaxis_showgrid=False,
    yaxis_gridcolor="#E8DADA",
)
    protein_fig.update_traces(
    textposition="outside",
    textfont_size=14,
    marker_line_width=0
)
    st.plotly_chart(protein_fig, use_container_width=True)

with col4:

    st.markdown("""
<h3 style='color:#A67C87;font-size:28px;font-weight:600;'>
🔥 Top 5 Calories Comparison
</h3>
""", unsafe_allow_html=True)

    calories_fig = px.bar(
    chart_data,
    x="short_name",
    y="calories",
    text="calories",
    color_discrete_sequence=[
    "#D8A7B1",  # Dusty Rose
    "#E8CFCF",  # Soft Blush
    "#DCC6CC",  # Pale Mauve
    "#CDB7C5",  # Powder Lilac
    "#AFC8B8"   # Seafoam Mist
],
)

    calories_fig.update_layout(
    height=400,
    xaxis_tickangle=-30,
    coloraxis_showscale=False,
    plot_bgcolor="#F6EEEE",
    paper_bgcolor="#F6EEEE",
    font_color="#6F5A64",
    showlegend=False,
    xaxis_showgrid=False,
    yaxis_gridcolor="#E8DADA",
)
    calories_fig.update_traces(
    textposition="outside",
    textfont_size=14,
    marker_line_width=0
)

    st.plotly_chart(calories_fig, use_container_width=True)
    
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