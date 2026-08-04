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
df=pd.read_csv(r'C:\Users\ASUS\FootballPlayerAnalyticsProject\Streamlit2\FC26_cleaned.csv')


st.markdown("""
<style>

/* ---------- APP ---------- */
.stApp{
    background:linear-gradient(180deg,#EDF7ED,#F8FAFC);
}

/* ---------- SIDEBAR ---------- */
section[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#0B1F33,#12344D);
    border-right:4px solid #2ECC71;
}

/* Sidebar headings only */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3{
    color:#FFD54F !important;
}

/* Sidebar labels */
section[data-testid="stSidebar"] label{
    color:white !important;
    font-weight:600;
}

/* Option Menu */
.nav-link{
    border-radius:12px !important;
    margin:6px 0;
    font-size:17px !important;
    font-weight:600 !important;
    transition:0.3s;
}

.nav-link:hover{
    background:#2ECC71 !important;
    transform:translateX(5px);
}

.nav-link-selected{
    background:#27AE60 !important;
    color:white !important;
    box-shadow:0 5px 15px rgba(0,0,0,.3);
}

/* Multiselect */
div[data-baseweb="select"]{
    border-radius:10px;
}

/* Keep clear (×) icon visible */
div[data-baseweb="select"] svg{
    fill:#444 !important;
}

/* ---------- IMAGE ---------- */

img{
    border-radius:20px;
    border:5px solid white;
    box-shadow:0 15px 30px rgba(0,0,0,.25);
}

/* ---------- KPI CARD ---------- */

.kpi-card{

    background:linear-gradient(135deg,#ffffff,#f4fff6);

    border-radius:18px;

    padding:25px;

    text-align:center;

    border-left:8px solid #27AE60;

    box-shadow:0 10px 25px rgba(0,0,0,.12);

    transition:0.35s;

}

.kpi-card:hover{

    transform:translateY(-8px);

    box-shadow:0 18px 35px rgba(39,174,96,.35);

}

.kpi-icon{

    font-size:36px;

}

.kpi-title{

    margin-top:10px;

    font-size:18px;

    color:#555;

    font-weight:600;

}

.kpi-value{

    margin-top:8px;

    font-size:34px;

    color:#0B3C2D;

    font-weight:800;

}

/* ---------- SCROLLBAR ---------- */

::-webkit-scrollbar{
    width:8px;
}

::-webkit-scrollbar-thumb{
    background:#2ECC71;
    border-radius:20px;
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
    st.markdown("""
<div style="text-align:center; padding:15px;">

<h1 style="
color:#0B3C2D;
font-size:52px;
font-weight:800;
margin-bottom:10px;
text-shadow:2px 2px 8px rgba(0,0,0,0.15);
">
⚽ Football Player Analytics Dashboard
</h1>

<p style="
font-size:20px;
color:#555;
font-style:italic;
margin-top:0;
">
Explore player performance, market value, club statistics,
league comparisons, and transfer insights using interactive visualizations.
</p>

</div>
""", unsafe_allow_html=True)

    st.image(
            r"C:\Users\ASUS\FootballPlayerAnalyticsProject\Streamlit2\football-stadium-inside-at-night-with-lights-post-production-free-photo.jpg",   # Replace with your image path
            use_container_width=True)
    # KPI Cards
    players=filtered['short_name'].shape[0]
    leagues=filtered['league_name'].nunique()
    clubs=filtered['club_name'].nunique()
    avg_value=filtered['value_eur'].mean()
    avg_overall = filtered["overall"].mean()
    avg_potential = filtered["potential"].mean()
    total_wages = filtered["wage_eur"].sum()

    # ===================== KPI CARDS =====================

    st.markdown("<br>", unsafe_allow_html=True)

# ---------- First Row ----------
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-icon">👤</div>
        <div class="kpi-title">Total Players</div>
        <div class="kpi-value">{players:,}</div>
    </div>
    """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-icon">🌍</div>
        <div class="kpi-title">Leagues</div>
        <div class="kpi-value">{leagues}</div>
    </div>
    """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-icon">🏟️</div>
        <div class="kpi-title">Clubs</div>
        <div class="kpi-value">{clubs}</div>
    </div>
    """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-icon">💰</div>
        <div class="kpi-title">Avg Market Value</div>
        <div class="kpi-value">€{avg_value/1e6:.2f}M</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

# ---------- Second Row ----------
    col5, col6, col7 = st.columns(3)

    with col5:
        st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-icon">⭐</div>
        <div class="kpi-title">Avg Overall</div>
        <div class="kpi-value">{avg_overall:.1f}</div>
    </div>
    """, unsafe_allow_html=True)

    with col6:
        st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-icon">🚀</div>
        <div class="kpi-title">Avg Potential</div>
        <div class="kpi-value">{avg_potential:.1f}</div>
    </div>
    """, unsafe_allow_html=True)

    with col7:
        st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-icon">💵</div>
        <div class="kpi-title">Total Weekly Wages</div>
        <div class="kpi-value">€{total_wages/1e9:.2f}B</div>
    </div>
    """, unsafe_allow_html=True)



  # Dataset page
# streamlit of dataset page
elif opt=='📄 Dataset':
    # st.title('📊 Dataset Explorer')
    # st.text('Explore the complete football player dataset with filtering, summary information, and data preview.')
    st.markdown("""
<div style="
text-align:center;
padding:10px;
">

<h1 style="
font-size:45px;
color:#0B3C2D;
font-weight:800;
">
📊 Dataset Explorer
</h1>

<p style="
font-size:20px;
color:#555;
font-style:italic;
">
Explore football player records, column information,
statistical summaries, and filtered data insights.
</p>

</div>
""", unsafe_allow_html=True)
# Dataset information bar
    num_rows=filtered.shape[0]
    num_cols=filtered.shape[1]
    st.markdown(f"""
<div class="dataset-info">
    <span class="dataset-info-item">📋 <strong>Rows:</strong> {num_rows}</span>
    <span class="dataset-info-item">📑 <strong>Columns:</strong> {num_cols}</span>
    <span class="dataset-info-item">🌍 <strong>Leagues:</strong> {filtered['league_name'].nunique()}</span>
    <span class="dataset-info-item">🏟️ <strong>Clubs:</strong> {filtered['club_name'].nunique()}</span>
    <span class="dataset-info-item">🌎 <strong>Nationalities:</strong> {filtered['nationality_name'].nunique()}</span>
</div>
""", unsafe_allow_html=True)
    # st.write(filtered.columns.tolist())

    # ---------- Tabs: Data | Columns | Summary ----------
    tab1, tab2, tab3 = st.tabs(['📂 Data Preview','📋 Column Information','📈 Summary'])
    # TAB 1: DATA PREVIEW
    with tab1:
        col_left,col_right=st.columns([3,1])
        with col_left:
            st.subheader('Preview Filtered Data')
        with col_right:
            #slider for no. of rows to display
            n_rows=st.slider('Rows to show',min_value=5,max_value=101,step=20,value=20)
        # display the first n rows
        st.dataframe(filtered.head(n_rows),use_container_width=True)
        #optionally display the last 10 rows
        with st.expander('Show last 10 rows'):
            st.dataframe(filtered.tail(10),use_container_width=True)

        # Download button for the filtered data
        csv=filtered.to_csv(index=False,encoding='utf-8')
        st.download_button(
            label='📥 Download filtered data as csv',
            data=csv,
            file_name='FootballPlayerAnalytics_Cleaned.csv',
            mime='text/csv',
            use_container_width=True
        )
    # TAB 2: COLUMN DETAILS
    with tab2:
        # compute missing values and give the column a clear name
        column_info=pd.DataFrame({
            'Column Name':filtered.columns,
            'Data Type':filtered.dtypes.astype(str),
            'Missing Values':filtered.isna().sum()
        })
        st.dataframe(
        column_info,
        use_container_width=True,
        height=400,
        hide_index=True)

    # TAB 3: SUMMARY
    with tab3:
        st.subheader('Statistical Summary')

    # Separate numeric and categorical columns
        num_cols = filtered.select_dtypes(include=['int64','float64']).columns.tolist()
        cat_cols = filtered.select_dtypes(include=['object','category']).columns.tolist()

    # Numeric Summary
        if num_cols:
            st.markdown('#### 📊 Numeric Columns')

            st.dataframe(
               filtered[num_cols].describe(),
               use_container_width=True
        )

    # Categorical Summary
        if cat_cols:
           st.markdown('#### 🏷️ Categorical Columns')

           categorical_cols = [
            "league_name",
            "club_name",
            "nationality_name",
            "player_positions"
        ]

        for col in categorical_cols:
            if col in filtered.columns:

                with st.expander(f"Top values in '{col}'"):

                    top_values = (
                        filtered[col]
                        .dropna()
                        .value_counts()
                        .reset_index()
                        .head(10)
                    )

                    top_values.columns = [col, "Player Count"]

                    st.dataframe(
                        top_values,
                        use_container_width=True,
                        hide_index=True
                    )

    # its css
    st.markdown("""
<style>

/* ================= DATASET PAGE ================= */

/* Dataset Title */
h1, h2, h3 {
    color:#0B3C2D;
    font-weight:800;
}


/* Dataset Description */
.stText {
    font-size:18px;
    color:#555;
}


/* Dataset Information Cards */
.dataset-info{
    display:flex;
    gap:20px;
    flex-wrap:wrap;
    margin:20px 0;
}


.dataset-info-item{
    background:linear-gradient(135deg,#ffffff,#f4fff6);
    padding:18px 25px;
    border-radius:15px;
    font-size:17px;
    color:#1E293B;
    font-weight:600;
    border-left:6px solid #27AE60;
    box-shadow:0 8px 20px rgba(0,0,0,0.12);
    transition:0.3s;
}


.dataset-info-item:hover{
    transform:translateY(-5px);
    box-shadow:0 15px 30px rgba(39,174,96,0.25);
}



/* Tabs Styling */

button[data-baseweb="tab"]{
    font-size:17px;
    font-weight:700;
    color:#0B3C2D;
}


button[data-baseweb="tab"]:hover{
    background:#E8F5E9;
    border-radius:10px;
}


button[aria-selected="true"]{
    background:#27AE60 !important;
    color:white !important;
    border-radius:10px;
}



/* Dataframe Styling */

div[data-testid="stDataFrame"]{
    border-radius:15px;
    overflow:hidden;
    box-shadow:0 8px 20px rgba(0,0,0,0.12);
}



/* Download Button */

.stDownloadButton button{
    background:#27AE60;
    color:white;
    border-radius:12px;
    font-size:16px;
    font-weight:700;
    padding:10px 20px;
    border:none;
    transition:0.3s;
}


.stDownloadButton button:hover{
    background:#1E8449;
    transform:translateY(-3px);
}



/* Expander Styling */

.streamlit-expanderHeader{
    background:#F1F8E9;
    border-radius:12px;
    font-size:17px;
    font-weight:700;
    color:#0B3C2D;
}



/* Slider Label */

div[data-testid="stSlider"] label{
    color:#0B3C2D;
    font-weight:700;
}

</style>
""", unsafe_allow_html=True)

# Preprocessing page
