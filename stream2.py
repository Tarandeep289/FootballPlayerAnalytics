import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
# Page Configuration
st.set_page_config(
    page_title='Football Player Analytics',
    layout='wide',
    page_icon='⚽',
    initial_sidebar_state='expanded'
)
df=pd.read_csv('FC26_20250921.csv')
# st.dataframe(df)
# Sidebar
st.markdown("""
<style>

/* ===========================================================
                    GOOGLE FONT
=========================================================== */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"]{
    font-family: 'Poppins', sans-serif;
}

/* ===========================================================
                    APP BACKGROUND
=========================================================== */

.stApp{
    background:#F8FAFC;
}

/* ===========================================================
                    SIDEBAR
=========================================================== */

section[data-testid="stSidebar"]{
    background:#0F172A;
    border-right:3px solid #16A34A;
}

/* Sidebar text */

section[data-testid="stSidebar"] *{
    color:white;
}

/* ===========================================================
                    OPTION MENU
=========================================================== */

.nav-link{
    font-size:18px !important;
    font-weight:600 !important;
    border-radius:12px !important;
    margin-bottom:8px !important;
    transition:0.3s;
}

.nav-link:hover{
    background:#16A34A !important;
    color:white !important;
}

.nav-link-selected{
    background:#16A34A !important;
    color:white !important;
    font-weight:bold !important;
}

/* ===========================================================
                    SIDEBAR HEADINGS
=========================================================== */

h3{
    color:#F59E0B !important;
    font-weight:700;
}

/* ===========================================================
                    MAIN TITLE
=========================================================== */

h1{
    color:#0F172A;
    font-size:46px !important;
    font-weight:800 !important;
}

/* ===========================================================
                    SUBTITLE
=========================================================== */

h5{
    color:#475569;
    font-size:18px !important;
    font-style:italic;
}

/* ===========================================================
                    IMAGE
=========================================================== */

img{
    border-radius:18px;
    box-shadow:0px 8px 25px rgba(0,0,0,0.25);
}

/* ===========================================================
                    KPI CARDS
=========================================================== */

.kpi-card{

    background:white;

    border-radius:18px;

    padding:22px;

    text-align:center;

    box-shadow:0px 5px 18px rgba(0,0,0,0.15);

    border-top:6px solid #16A34A;

    transition:0.3s;

}

.kpi-card:hover{

    transform:translateY(-8px);

    box-shadow:0px 12px 28px rgba(0,0,0,0.25);

}

.kpi-title{

    color:#0F172A;

    font-size:18px;

    font-weight:700;

}

.kpi-value{

    color:#16A34A;

    font-size:34px;

    font-weight:800;

}

/* ===========================================================
                    FILTERS
=========================================================== */

div[data-baseweb="select"]{

    border-radius:12px;

}

/* ===========================================================
                    BUTTONS
=========================================================== */

.stButton>button{

    background:#16A34A;

    color:white;

    border:none;

    border-radius:10px;

    font-weight:600;

}

.stButton>button:hover{

    background:#15803D;

}

/* ===========================================================
                    DATAFRAME
=========================================================== */

[data-testid="stDataFrame"]{

    border-radius:15px;

    overflow:hidden;

    box-shadow:0px 5px 15px rgba(0,0,0,0.15);

}

/* ===========================================================
                    METRIC
=========================================================== */

[data-testid="metric-container"]{

    background:white;

    border-radius:15px;

    padding:15px;

    box-shadow:0px 5px 15px rgba(0,0,0,0.12);

}

/* ===========================================================
                    HR
=========================================================== */

hr{

    border:1px solid #16A34A;

}

/* ===========================================================
                    SCROLLBAR
=========================================================== */

::-webkit-scrollbar{

    width:10px;

}

::-webkit-scrollbar-thumb{

    background:#16A34A;

    border-radius:20px;

}

::-webkit-scrollbar-track{

    background:#F1F5F9;

}

</style>
""", unsafe_allow_html=True)
with st.sidebar:
    opt=option_menu(menu_title='Menu',options=['🏠 Home','📄 Dataset','🧹 Preprocessing','📊 Visualizations','ℹ About'])
    st.markdown('---')
    st.subheader('🔍 Filters')
    league=st.multiselect('Select league 🌍',options=df['league_name'].dropna().unique())
    club=st.multiselect('Select club 🏟',options=df['club_name'].dropna().unique())
    filtered=df.copy()
    if league:
        filtered=filtered[filtered['league_name'].isin(league)]# use filtered term from now onwards
    if club:
        filtered=filtered[filtered['club_name'].isin(club)]
# Home page
if opt=='🏠 Home':
    st.title('⚽ Football Player Analytics Dashboard')
    st.markdown('##### ***Explore player performance, market value, club statistics, league comparisons, and transfer insights using interactive visualizations.***')
    st.image(
            r"C:\Users\ASUS\FootballPlayerAnalyticsProject\Streamlit2\football-stadium-inside-at-night-with-lights-post-production-free-photo.jpg",   # Replace with your image path
            use_container_width=True)
    # KPI Cards
    players=filtered['short_name'].nunique()
    leagues=filtered['league_name'].nunique()
    clubs=filtered['club_name'].nunique()
    avg_value=filtered['value_eur'].mean()
    avg_overall = filtered["overall"].mean()
    avg_potential = filtered["potential"].mean()
    total_wages = filtered["wage_eur"].sum()

    #row1
    col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">👤 Players</div>
        <div class="kpi-value">{players:,}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">🌍 Leagues</div>
        <div class="kpi-value">{leagues}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">🏟 Clubs</div>
        <div class="kpi-value">{clubs}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">💰 Avg Value</div>
        <div class="kpi-value">€{avg_value/1e6:.2f}M</div>
    </div>
    """, unsafe_allow_html=True)


    #row 2
    col5, col6, col7 = st.columns(3)

with col5:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">⭐ Avg Overall</div>
        <div class="kpi-value">{avg_overall:.1f}</div>
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">🚀 Avg Potential</div>
        <div class="kpi-value">{avg_potential:.1f}</div>
    </div>
    """, unsafe_allow_html=True)

with col7:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">💵 Total Wages</div>
        <div class="kpi-value">€{total_wages/1e9:.2f}B</div>
    </div>
    """, unsafe_allow_html=True)
