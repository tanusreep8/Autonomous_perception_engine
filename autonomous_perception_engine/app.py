import streamlit as st

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Autonomous Perception Engine",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------
# PREMIUM FUTURISTIC CSS
# -------------------------------
st.markdown("""
<style>

/* 🌌 Animated Gradient Background */
.stApp {
    background: linear-gradient(-45deg, #020617, #0f172a, #1e293b, #020617);
    background-size: 400% 400%;
    animation: gradientBG 12s ease infinite;
    color: #e2e8f0;
}

/* Gradient Animation */
@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* ✨ Glow Effects */
.stApp::before {
    content: "";
    position: fixed;
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, rgba(99,102,241,0.25), transparent 70%);
    top: -150px;
    left: -150px;
    z-index: 0;
}

.stApp::after {
    content: "";
    position: fixed;
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, rgba(139,92,246,0.25), transparent 70%);
    bottom: -150px;
    right: -150px;
    z-index: 0;
}

/* 🟣 Glass Cards */
.card {
    background: rgba(30, 41, 59, 0.6);
    padding: 25px;
    border-radius: 18px;
    backdrop-filter: blur(12px);
    box-shadow: 0px 10px 30px rgba(0,0,0,0.5);
    transition: 0.3s;
    text-align: center;
}

.card:hover {
    transform: translateY(-6px) scale(1.02);
    box-shadow: 0px 20px 50px rgba(99,102,241,0.4);
}

/* 🧾 Text Styling */
h1 {
    text-align: center;
    font-size: 3rem;
    letter-spacing: 1px;
}

.subtitle {
    text-align: center;
    color: #94a3b8;
    margin-bottom: 30px;
}

/* Divider */
.divider {
    height: 1px;
    background: linear-gradient(to right, transparent, #334155, transparent);
    margin: 30px 0;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #020617;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #6366f1, #8b5cf6);
    color: white;
    border-radius: 12px;
    padding: 10px 20px;
    border: none;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0px 0px 20px rgba(139,92,246,0.7);
}

/* Metrics */
[data-testid="stMetric"] {
    background: rgba(30, 41, 59, 0.6);
    padding: 15px;
    border-radius: 12px;
    backdrop-filter: blur(10px);
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# HEADER
# -------------------------------
st.markdown("<h1>🚗 Autonomous Perception Engine</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Detection • Tracking • Analytics</p>", unsafe_allow_html=True)

# -------------------------------
# SIDEBAR NAVIGATION
# -------------------------------
st.sidebar.title("🧭 Navigation")
st.sidebar.markdown("""
- 🎥 Detection Page  
- 📊 Analytics Page  
""")

# -------------------------------
# MAIN CARDS
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h3>🎥 Detection</h3>
        <p>Upload video and track vehicles & pedestrians</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>📊 Analytics</h3>
        <p>Visualize object distribution and trends</p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------
# DIVIDER
# -------------------------------
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

# -------------------------------
# STATUS METRICS
# -------------------------------
col1, col2, col3 = st.columns(3)

col1.metric("🚗 System", "Active")
col2.metric("⚡ Model", "YOLOv8")
col3.metric("📡 Mode", "Offline")

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)
st.markdown(
    "<center style='color:#64748b;'>🤖 User Friendly Engine</center>",
    unsafe_allow_html=True
)
