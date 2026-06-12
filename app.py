import streamlit as st
import pandas as pd
import plotly.express as px
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
st.sidebar.success(f"Foods Loaded: {len(foods_df):,}")
# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
            
<style>
            .main .block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
}
            .metric-card{
    background: linear-gradient(135deg,#1f2937,#111827);
    padding:20px;
    border-radius:15px;
    text-align:center;
    border:1px solid #374151;
    box-shadow:0px 4px 15px rgba(0,0,0,0.4);
}

.metric-title{
    color:#9ca3af;
    font-size:15px;
}

.metric-value{
    color:white;
    font-size:32px;
    font-weight:bold;
}

.stApp {
    background-color: #0E1117;
}

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
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 20px;
    border-left: 5px solid orange;
    min-height: 320px;
}
.rec-card:hover {
    transform: translateY(-5px);
    transition: 0.3s;
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
    st.success(
        f"💪 Highest Protein\n\n{highest_protein['food_name'][:30]}"
    )

with col2:
    lowest_calorie = recommended_foods.loc[
        recommended_foods["calories"].idxmin()
    ]
    st.info(
        f"🔥 Lowest Calories\n\n{lowest_calorie['food_name'][:30]}"
    )

with col3:
    healthiest = recommended_foods.loc[
        recommended_foods["health_score"].idxmax()
    ]
    st.warning(
        f"❤️ Healthiest Choice\n\n{healthiest['food_name'][:30]}"
    )
st.subheader(
    f"📋 Recommendation Summary for {name if name else 'Guest User'}"
)

st.info(
    f"""
🎯 Total Recommendations Found: {len(recommended_foods)}

🥇 Best Match: {recommended_foods.iloc[0]['food_name']}


📂 Category: {recommended_foods.iloc[0]['food_category']}

❤️ Health Score: {recommended_foods.iloc[0]['health_score']}
"""
)
top_food = recommended_foods.iloc[0]

st.success(
    f"""
🌟 TODAY'S BEST RECOMMENDATION

🥇 {top_food['food_name']}

📁 Category: {top_food['food_category']}

❤️ Health Score: {top_food['health_score']}
"""
)
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

    📂 Category: {row['food_category']}

    🔥 Calories: {row['calories']:.1f}

    💪 Protein: {row['protein_g']:.1f} g

    ❤️ Health Score: {row['health_score']}

    🏆 Quality: {quality}

    ⭐ {reason_text}
    """
    st.markdown("---")
    target_col = col1 if i % 2 != 0 else col2
    with target_col:
        st.markdown(f"""
        <div class="rec-card">
        <h3>{badge} Rank #{i}</h3>

        <p><b>{row['food_name']}</b></p>

        <p>📁 {row['food_category']}</p>

        <p>🔥 Calories: {row['calories']}</p>

        <p>💪 Protein: {row['protein_g']} g</p>

        <p>❤️ Health Score: {row['health_score']}</p>

        <p>🏆 {quality}</p>

        <p>⭐ {reason_text}</p>

        </div>
""", unsafe_allow_html=True)
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
st.subheader("📊 Food Comparison Table")
st.dataframe(
        recommended_foods[
            [
                "food_name",
                "food_category",
                "calories",
                "protein_g",
                "health_score"
            ]
        ]
    )
st.caption(
    "Compare calories, protein, carbs and health scores across recommendations."
)
csv = recommended_foods.to_csv(index=False)

st.download_button(
    label="📥 Download Recommendations CSV",
    data=csv,
    file_name="food_recommendations.csv",
    mime="text/csv"
)
st.success(
        f"Hello {name}! Here are your personalized recommendations."
    )
st.subheader("📊 Food Categories Distribution")
st.caption("Distribution of recommended foods by category")
category_counts = recommended_foods["food_type"].value_counts()

st.bar_chart(category_counts, height=400)
import plotly.express as px

st.subheader("🥧 Category Percentage")

st.subheader("💪 Top 5 Protein Comparison")

protein_fig = px.bar(
    recommended_foods.head(5),
    x="food_name",
    y="protein_g",
    title="💪 Top 5 Protein Rich Foods",
    text="protein_g"
)

protein_fig.update_layout(
    xaxis_title="Food",
    yaxis_title="Protein (g)",
    height=500
)

protein_fig.update_traces(
    textposition="outside"
)
st.plotly_chart(protein_fig, use_container_width=True)
st.subheader("🔥 Top 5 Calories Comparison")

calories_fig = px.bar(
    recommended_foods.head(5),
    x="food_name",
    y="calories",
    title="🔥 Top 5 Calories Comparison",
    text="calories"
)

calories_fig.update_layout(
    xaxis_title="Food",
    yaxis_title="Calories",
    height=500
)

calories_fig.update_traces(
    textposition="outside"
)

st.plotly_chart(calories_fig, use_container_width=True)
fig = px.pie(
    values=category_counts.values,
    names=category_counts.index,
    hole=0.4
)
fig.update_traces(
    textposition="inside",
    textinfo="percent+label"
)
st.plotly_chart(fig, use_container_width=True)   

    
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