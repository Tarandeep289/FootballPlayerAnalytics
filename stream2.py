 #  visualization + its page + about page + deploy + github + understand and read logic + prep each line left
# import streamlit as st
# import pandas as pd
# from streamlit_option_menu import option_menu
# import plotly.express as px

# # Page Configuration
# st.set_page_config(
#     page_title='Football Player Analytics',
#     layout='wide',
#     page_icon='⚽',
#     initial_sidebar_state='expanded'
# )

# # Load data
# df = pd.read_csv(r'C:\Users\ASUS\FootballPlayerAnalyticsProject\Streamlit2\FC26_20250921.csv')

# st.markdown("""
# <style>

# /* ---------- APP GLOBAL ---------- */
# .stApp{
#     background: linear-gradient(180deg, #EDF7ED, #F8FAFC);
# }

# /* Headings Global */
# h1, h2, h3 {
#     color: #0B3C2D;
#     font-weight: 800;
# }

# /* ---------- SIDEBAR ---------- */
# section[data-testid="stSidebar"]{
#     background: linear-gradient(180deg, #0B1F33, #12344D);
#     border-right: 4px solid #2ECC71;
# }

# section[data-testid="stSidebar"] h1,
# section[data-testid="stSidebar"] h2,
# section[data-testid="stSidebar"] h3{
#     color: #FFD54F !important;
# }

# section[data-testid="stSidebar"] label{
#     color: white !important;
#     font-weight: 600;
# }

# .nav-link{
#     border-radius: 12px !important;
#     margin: 6px 0;
#     font-size: 17px !important;
#     font-weight: 600 !important;
#     transition: 0.3s;
# }

# .nav-link:hover{
#     background: #2ECC71 !important;
#     transform: translateX(5px);
# }

# .nav-link-selected{
#     background: #27AE60 !important;
#     color: white !important;
#     box-shadow: 0 5px 15px rgba(0,0,0,.3);
# }

# div[data-baseweb="select"]{
#     border-radius: 10px;
# }

# div[data-baseweb="select"] svg{
#     fill: #444 !important;
# }

# /* ---------- SHARED COMPONENTS ---------- */
# img{
#     border-radius: 20px;
#     border: 5px solid white;
#     box-shadow: 0 15px 30px rgba(0,0,0,.25);
# }

# .kpi-card{
#     background: linear-gradient(135deg, #ffffff, #f4fff6);
#     border-radius: 18px;
#     padding: 25px;
#     text-align: center;
#     border-left: 8px solid #27AE60;
#     box-shadow: 0 10px 25px rgba(0,0,0,.12);
#     transition: 0.35s;
# }

# .kpi-card:hover{
#     transform: translateY(-8px);
#     box-shadow: 0 18px 35px rgba(39,174,96,.35);
# }

# .kpi-icon{ font-size: 36px; }
# .kpi-title{ margin-top: 10px; font-size: 18px; color: #555; font-weight: 600; }
# .kpi-value{ margin-top: 8px; font-size: 34px; color: #0B3C2D; font-weight: 800; }

# /* Custom Container Cards */
# .custom-card {
#     background: #FFFFFF;
#     border-radius: 16px;
#     padding: 24px;
#     box-shadow: 0 8px 20px rgba(0,0,0,0.06);
#     border: 1px solid #E2E8F0;
#     margin-bottom: 20px;
# }

# /* Pipeline Step Cards */
# .pipeline-step {
#     background: linear-gradient(135deg, #27AE60, #1E8449);
#     color: white !important;
#     text-align: center;
#     padding: 16px 10px;
#     border-radius: 14px;
#     font-weight: 700;
#     font-size: 14px;
#     line-height: 1.3;
#     box-shadow: 0 6px 15px rgba(39,174,96,0.3);
#     transition: all 0.3s ease;
#     min-height: 95px;
#     display: flex;
#     align-items: center;
#     justify-content: center;
# }

# .pipeline-step:hover {
#     transform: translateY(-5px);
#     box-shadow: 0 10px 20px rgba(39,174,96,0.45);
# }

# /* Streamlit Metrics Customization */
# div[data-testid="stMetric"] {
#     background: #FFFFFF;
#     padding: 15px 20px;
#     border-radius: 12px;
#     border-left: 5px solid #27AE60;
#     box-shadow: 0 4px 12px rgba(0,0,0,0.05);
# }

# /* Dataframe Container Customization */
# div[data-testid="stDataFrame"]{
#     border-radius: 15px;
#     overflow: hidden;
#     box-shadow: 0 8px 20px rgba(0,0,0,0.08);
# }

# /* Download & Action Buttons */
# .stDownloadButton button{
#     background: #27AE60;
#     color: white;
#     border-radius: 12px;
#     font-size: 16px;
#     font-weight: 700;
#     padding: 10px 20px;
#     border: none;
#     transition: 0.3s;
# }

# .stDownloadButton button:hover{
#     background: #1E8449;
#     transform: translateY(-3px);
# }

# /* Expander Styling */
# .streamlit-expanderHeader{
#     background: #F1F8E9;
#     border-radius: 12px;
#     font-size: 16px;
#     font-weight: 700;
#     color: #0B3C2D;
# }

# /* Scrollbar */
# ::-webkit-scrollbar{ width: 8px; }
# ::-webkit-scrollbar-thumb{ background: #2ECC71; border-radius: 20px; }

# </style>
# """, unsafe_allow_html=True)

# # Sidebar Routing
# with st.sidebar:
#     opt = option_menu(menu_title='Menu', options=['🏠 Home', '📄 Dataset', '🧹 Preprocessing', '📊 Visualizations', 'ℹ About'])
#     st.markdown('---')
#     st.subheader('🔍 Filters')
#     league = st.multiselect('Select league 🌍', options=df['league_name'].dropna().unique())
#     club = st.multiselect('Select club 🏟', options=df['club_name'].dropna().unique())
    
#     filtered = df.copy()
#     if league:
#         filtered = filtered[filtered['league_name'].isin(league)]
#     if club:
#         filtered = filtered[filtered['club_name'].isin(club)]

# # Home page
# if opt == '🏠 Home':
#     st.markdown("""
#     <div style="text-align:center; padding:15px;">
#         <h1 style="font-size:52px; margin-bottom:10px; text-shadow:2px 2px 8px rgba(0,0,0,0.15);">
#         ⚽ Football Player Analytics Dashboard
#         </h1>
#         <p style="font-size:20px; color:#555; font-style:italic; margin-top:0;">
#         Explore player performance, market value, club statistics, league comparisons, and transfer insights using interactive visualizations.
#         </p>
#     </div>
#     """, unsafe_allow_html=True)
#     st.image(
#         r"C:\Users\ASUS\FootballPlayerAnalyticsProject\Streamlit2\football-stadium-inside-at-night-with-lights-post-production-free-photo.jpg",
#         use_container_width=True
#     )
    
#     players = filtered['short_name'].shape[0]
#     leagues = filtered['league_name'].nunique()
#     clubs = filtered['club_name'].nunique()
#     avg_value = filtered['value_eur'].mean()
#     avg_overall = filtered["overall"].mean()
#     avg_potential = filtered["potential"].mean()
#     total_wages = filtered["wage_eur"].sum()

#     st.markdown("<br>", unsafe_allow_html=True)
#     col1, col2, col3, col4 = st.columns(4)
#     with col1:
#         st.markdown(f'<div class="kpi-card"><div class="kpi-icon">👤</div><div class="kpi-title">Total Players</div><div class="kpi-value">{players:,}</div></div>', unsafe_allow_html=True)
#     with col2:
#         st.markdown(f'<div class="kpi-card"><div class="kpi-icon">🌍</div><div class="kpi-title">Leagues</div><div class="kpi-value">{leagues}</div></div>', unsafe_allow_html=True)
#     with col3:
#         st.markdown(f'<div class="kpi-card"><div class="kpi-icon">🏟️</div><div class="kpi-title">Clubs</div><div class="kpi-value">{clubs}</div></div>', unsafe_allow_html=True)
#     with col4:
#         st.markdown(f'<div class="kpi-card"><div class="kpi-icon">💰</div><div class="kpi-title">Avg Market Value</div><div class="kpi-value">€{avg_value/1e6:.2f}M</div></div>', unsafe_allow_html=True)

#     st.markdown("<br>", unsafe_allow_html=True)
#     col5, col6, col7 = st.columns(3)
#     with col5:
#         st.markdown(f'<div class="kpi-card"><div class="kpi-icon">⭐</div><div class="kpi-title">Avg Overall</div><div class="kpi-value">{avg_overall:.1f}</div></div>', unsafe_allow_html=True)
#     with col6:
#         st.markdown(f'<div class="kpi-card"><div class="kpi-icon">🚀</div><div class="kpi-title">Avg Potential</div><div class="kpi-value">{avg_potential:.1f}</div></div>', unsafe_allow_html=True)
#     with col7:
#         st.markdown(f'<div class="kpi-card"><div class="kpi-icon">💵</div><div class="kpi-title">Total Weekly Wages</div><div class="kpi-value">€{total_wages/1e9:.2f}B</div></div>', unsafe_allow_html=True)

# # Dataset page
# elif opt == '📄 Dataset':
#     st.markdown("""
#     <div style="text-align:center; padding:10px;">
#         <h1 style="font-size:45px;">📊 Dataset Explorer</h1>
#         <p style="font-size:20px; color:#555; font-style:italic;">
#         Explore football player records, column information, statistical summaries, and filtered data insights.
#         </p>
#     </div>
#     """, unsafe_allow_html=True)

#     num_rows = filtered.shape[0]
#     num_cols = filtered.shape[1]
    
#     st.markdown(f"""
#     <div style="display:flex; gap:20px; flex-wrap:wrap; margin:20px 0;">
#         <span class="kpi-card" style="padding:15px 20px; flex:1;">📋 <strong>Rows:</strong> {num_rows}</span>
#         <span class="kpi-card" style="padding:15px 20px; flex:1;">📑 <strong>Columns:</strong> {num_cols}</span>
#         <span class="kpi-card" style="padding:15px 20px; flex:1;">🌍 <strong>Leagues:</strong> {filtered['league_name'].nunique()}</span>
#         <span class="kpi-card" style="padding:15px 20px; flex:1;">🏟️ <strong>Clubs:</strong> {filtered['club_name'].nunique()}</span>
#         <span class="kpi-card" style="padding:15px 20px; flex:1;">🌎 <strong>Nationalities:</strong> {filtered['nationality_name'].nunique()}</span>
#     </div>
#     """, unsafe_allow_html=True)

#     tab1, tab2, tab3 = st.tabs(['📂 Data Preview', '📋 Column Information', '📈 Summary'])
    
#     with tab1:
#         col_left, col_right = st.columns([3, 1])
#         with col_left:
#             st.subheader('Preview Filtered Data')
#         with col_right:
#             n_rows = st.slider('Rows to show', min_value=5, max_value=101, step=20, value=20)
#         st.dataframe(filtered.head(n_rows), use_container_width=True)
#         with st.expander('Show last 10 rows'):
#             st.dataframe(filtered.tail(10), use_container_width=True)

#         csv = filtered.to_csv(index=False, encoding='utf-8')
#         st.download_button(
#             label='📥 Download filtered data as csv',
#             data=csv,
#             file_name='FootballPlayerAnalytics_Cleaned.csv',
#             mime='text/csv',
#             use_container_width=True
#         )

#     with tab2:
#         column_info = pd.DataFrame({
#             'Column Name': filtered.columns,
#             'Data Type': filtered.dtypes.astype(str),
#             'Missing Values': filtered.isna().sum()
#         })
#         st.dataframe(column_info, use_container_width=True, height=400, hide_index=True)

#     with tab3:
#         st.subheader('Statistical Summary')
#         num_cols = filtered.select_dtypes(include=['int64', 'float64']).columns.tolist()
#         cat_cols = filtered.select_dtypes(include=['object', 'category']).columns.tolist()

#         if num_cols:
#             st.markdown('#### 📊 Numeric Columns')
#             st.dataframe(filtered[num_cols].describe(), use_container_width=True)

#         if cat_cols:
#             st.markdown('#### 🏷️ Categorical Columns')
#             categorical_cols = ["league_name", "club_name", "nationality_name", "player_positions"]
#             for col in categorical_cols:
#                 if col in filtered.columns:
#                     with st.expander(f"Top values in '{col}'"):
#                         top_values = filtered[col].dropna().value_counts().reset_index().head(10)
#                         top_values.columns = [col, "Player Count"]
#                         st.dataframe(top_values, use_container_width=True, hide_index=True)

# # Preprocessing page
# elif opt == '🧹 Preprocessing':
#     st.markdown("""
#     <div style="text-align:center; padding:10px;">
#         <h1 style="font-size:45px;">🧹 Data Preprocessing Pipeline</h1>
#         <p style="font-size:20px; color:#555; font-style:italic; margin-top:0; max-width:800px; 
#         margin:0 auto 20px auto">
#         This page demonstrates the data transformation steps performed on the <strong>FC26 Player Dataset</strong> 
#         to ensure high data quality by eliminating null values, handling redundant features, and standardizing values.
#         </p>
#     </div>
#     """, unsafe_allow_html=True)

#     st.subheader('📋 Processing Workflow')
#     steps = [
#         "1.<br>📂 Raw<br>Dataset",
#         "2.<br>🔍 Missing<br>Analysis",
#         "3.<br>🗑️ Drop<br>Columns",
#         "4.<br>🧹 Handle<br>Missing",
#         "5.<br>🧾 Remove<br>Duplicates",
#         "6.<br>✔️ Validate<br>Types",
#         "7.<br>📈 Growth<br>Feature",
#         "8.<br>✅ Clean<br>Dataset"
#     ]

#     cols = st.columns(len(steps))
#     for col, step in zip(cols, steps):
#         col.markdown(f'<div class="pipeline-step">{step}</div>', unsafe_allow_html=True)

#     st.markdown("<br>", unsafe_allow_html=True)

#     def get_missing_stats(df_input):
#         missing_df = df_input.isna().sum().reset_index()
#         missing_df.columns = ['Column Name', 'Missing Count']
#         missing_df['Missing %'] = (missing_df['Missing Count'] / len(df_input) * 100).round(1)
#         missing_df = missing_df[missing_df['Missing Count'] > 0]
#         return missing_df

#     # ---------- BEFORE PROCESSING ----------
#     st.markdown('<div class="custom-card">', unsafe_allow_html=True)
#     st.subheader('🔍 Dataset Before Processing')
    
#     col1, col2 = st.columns([3, 1])
#     missing_before = get_missing_stats(filtered)
    
#     with col1:
#         if not missing_before.empty:
#             st.markdown('**Columns with missing values:**')
#             st.dataframe(missing_before, use_container_width=True, height=220, hide_index=True)
#         else:
#             st.success('✅ No missing values found!')
            
#     with col2:
#         st.metric("Rows", f"{filtered.shape[0]:,}")
#         st.metric("Columns", filtered.shape[1])
#     st.markdown('</div>', unsafe_allow_html=True)

#     # Missing Plot
#     if not missing_before.empty:
#         st.subheader('📊 Missing Values Distribution')
#         fig = px.bar(
#             missing_before,
#             x="Column Name",
#             y="Missing Count",
#             color="Missing Count",
#             color_continuous_scale="Viridis",
#             text="Missing Count",
#             labels={"Column Name": "Columns", "Missing Count": "Missing Values"},
#             template="plotly_white"
#         )
#         fig.update_traces(
#             textposition="outside",
#             marker_line_color="black",
#             marker_line_width=1.2,
#             hovertemplate="<b>%{x}</b><br>Missing Values: %{y}<extra></extra>"
#         )
#         fig.update_layout(
#             xaxis=dict(title="", tickangle=-30, showgrid=False, tickfont=dict(size=12)),
#             yaxis=dict(title="Number of Missing Values", showgrid=True, gridcolor="rgba(200,200,200,0.3)"),
#             coloraxis_showscale=True,
#             plot_bgcolor="white",
#             paper_bgcolor="white",
#             margin=dict(t=30, l=40, r=20, b=100),
#             height=450
#         )
#         st.plotly_chart(fig, use_container_width=True)

#     st.info("""
#     📌 **Dropped Columns:** `club_jersey_number`, `club_loaned_from`, `club_team_id`,
#     `goalkeeping_speed`, `nation_jersey_number`, `nation_position`, `nation_team_id`,
#     `player_tags`, `player_traits`, and `work_rate`.

#     These features were removed because they contained high rates of missing values, served primarily as internal IDs, 
#     or lacked utility for performance analysis.
#     """)

#     # Processing Operations
#     processed_data = filtered.copy()
#     cols_to_drop = [
#         'club_jersey_number', 'club_loaned_from', 'club_team_id',
#         'goalkeeping_speed', 'nation_jersey_number', 'nation_position',
#         'nation_team_id', 'player_tags', 'player_traits', 'work_rate'
#     ]
#     existing_cols = [c for c in cols_to_drop if c in processed_data.columns]
#     processed_data.drop(columns=existing_cols, inplace=True, errors='ignore')

#     rows_before = processed_data.shape[0]
#     processed_data.dropna(inplace=True)
#     rows_after = processed_data.shape[0]
#     processed_data.reset_index(drop=True, inplace=True)

#     # ---------- AFTER PROCESSING ----------
#     st.markdown('<div class="custom-card">', unsafe_allow_html=True)
#     st.subheader("✅ Dataset After Processing")
#     st.markdown(f"""
#     The preprocessing removed **{len(existing_cols)} columns** and **{rows_before - rows_after:,} rows** containing null values.
    
#     **Final Clean Shape:** **{rows_after:,} rows × {processed_data.shape[1]} columns**
#     """)

#     col_a, col_b, col_c = st.columns(3)
#     with col_a:
#         st.metric("Rows Remaining", f"{rows_after:,}", delta=rows_after - rows_before, delta_color="inverse")
#     with col_b:
#         st.metric("Columns Remaining", processed_data.shape[1], delta=f"-{len(existing_cols)}")
#     with col_c:
#         st.metric("Rows Removed", f"{rows_before - rows_after:,}", delta=f"-{rows_before - rows_after}")
#     st.markdown('</div>', unsafe_allow_html=True)

#     missing_after = get_missing_stats(processed_data)
#     if missing_after.empty:
#         st.success("🎉 All missing values resolved cleanly!")
#     else:
#         st.dataframe(missing_after, use_container_width=True)

#     with st.expander("👁️ Preview Cleaned Dataset"):
#         st.dataframe(processed_data.head(10), use_container_width=True)

#     csv_clean = processed_data.to_csv(index=False).encode('utf-8')
#     st.download_button(
#         label="📥 Download Cleaned Data (CSV)",
#         data=csv_clean,
#         file_name="footballplayeranalytics_cleaned.csv",
#         mime="text/csv",
#         use_container_width=True,
#     )

#     st.session_state['cleaned_data'] = processed_data

# # elif opt=='📊 Visualizations':





# tested code with simple words to understand

import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.express as px
# Page Configuration
st.set_page_config(
    page_title='Football Player Analytics',
    layout='wide',
    page_icon='⚽',
    initial_sidebar_state='expanded'
)
# df=pd.read_csv(r'C:\Users\ASUS\FootballPlayerAnalyticsProject\Streamlit2\FC26_cleaned.csv')
df=pd.read_csv(r'C:\Users\ASUS\FootballPlayerAnalyticsProject\Streamlit2\FC26_20250921.csv')

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
    # TAB 1: DATA PREVIEW - filtered data means data that you get after applying filters
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


elif opt=='🧹 Preprocessing':
    st.title('🧹 Data Preprocessing Pipeline')
    st.markdown("""
This page demonstrates the preprocessing steps performed on the **FC26 Player Dataset**
before building the analytics dashboard.

The preprocessing pipeline improves data quality by handling missing values,
removing unnecessary columns, correcting data types, and preparing the dataset
for reliable visualizations and statistical analysis.
""") 
    st.subheader('📋 Processing Workflow')
    steps = [
    "1.\n📂 Raw\nDataset",
    "2.\n🔍 Missing\nAnalysis",
    "3.\n🗑️ Drop\nColumns",
    "4.\n🧹 Handle\nMissing",
    "5.\n🧾 Remove\nDuplicates",
    "6.\n✔️ Validate\nTypes",
    "7.\n📈 Growth\nFeature",
    "8.\n✅ Clean\nDataset"
]

    cols = st.columns(len(steps))

    for col, step in zip(cols, steps):
        col.markdown(
        f"""
        <div style="
        background:#27AE60;
        color:white;
        text-align:center;
        padding:15px;
        border-radius:10px;
        font-weight:bold;">
        {step.replace(chr(10), '<br>')} 
        </div>
        """,
        unsafe_allow_html=True,
    )
    # char(10) is ASCII CODE of \n
    
    #  Helper function to get missing stats
    def get_missing_stats(df):
        missing_df=df.isna().sum().reset_index()
        missing_df.columns=['Column Name','Missing Count']
        missing_df['Missing %']=(missing_df['Missing Count']/len(df)*100).round(1)
        missing_df=missing_df[missing_df['Missing Count']>0]
        return missing_df
    # Before Processing
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader('🔍 Dataset Before Processing')
    col1 , col2 = st.columns([3,1])
    with col1:
        # show missing values table
        missing_before=get_missing_stats(filtered)
        if not missing_before.empty:
            st.markdown('**Columns with missing values:**')
            st.dataframe(
                missing_before,
                missing_before.style.format({
                    'Missing Count':'{:,}',
                    'Missing %':'{:.1f %}'
                }),
                use_container_width=True,
                height=300
            )
        else:
            st.success('✅ No missing values found!')
    with col2:
        # Show shape information
        st.metric("Rows",filtered.shape[0])
        st.metric('Columns',filtered.shape[1])
        st.markdown("</div>", unsafe_allow_html=True)

    # Visualise missing values
    if not missing_before.empty:
       st.subheader('📊 Missing Values Before Preprocessing')
       fig = px.bar(
    missing_before,
    x="Column Name",
    y="Missing Count",
    color="Missing Count",
    color_continuous_scale="Viridis",
    text="Missing Count",
    # title="📊 Missing Values Before Preprocessing",
    labels={
        "Column Name": "Columns",
        "Missing Count": "Missing Values"
    },
    template="plotly_white"
)

       fig.update_traces(
    textposition="outside",
    marker_line_color="black",
    marker_line_width=1.2,
    hovertemplate=
    "<b>%{x}</b><br>"
    "Missing Values: %{y}<extra></extra>"
)

       fig.update_layout(
    # title={
    #     "xanchor": "center",
    #     "font": dict(size=24, color='black')
    # },
    xaxis=dict(
        title="",
        tickangle=-30,
        showgrid=False,
        tickfont=dict(size=12)
    ),
    yaxis=dict(
        title="Number of Missing Values",
        showgrid=True,
        gridcolor="rgba(200,200,200,0.3)"
    ),
    coloraxis_showscale=True,
    plot_bgcolor="white",
    paper_bgcolor="white",
    margin=dict(t=70, l=40, r=20, b=100),
    height=600,
    width=400,
    hoverlabel=dict(
        bgcolor="white",
        font_size=13,
        font_family="Arial"
    )
)

    st.plotly_chart(fig, use_container_width=True)
    st.info(
    """
📌 **Dropped Columns:** `club_jersey_number`, `club_loaned_from`, `club_team_id`,
`goalkeeping_speed`, `nation_jersey_number`, `nation_position`, `nation_team_id`,
`player_tags`, `player_traits`, and `work_rate`.

These features were removed because they contained many missing values, served mainly
as identifiers, or were not essential for the analyses and visualizations presented
in this dashboard.
"""
)    
    # Perform Cleaning
    # Use a copy to avoid modifying the original filtered data
    processed_data=filtered.copy()
    cols_to_drop=['club_jersey_number','club_loaned_from','club_team_id','goalkeeping_speed','nation_jersey_number','nation_position','nation_team_id','player_tags','player_traits','work_rate']
    existing_cols=[c for c in cols_to_drop if c in processed_data.columns]
    processed_data.drop(columns=existing_cols,inplace=True,errors='ignore')

    rows_before=processed_data.shape[0]
    processed_data.dropna(inplace=True)
    rows_after=processed_data.shape[0]
    processed_data.reset_index(drop=True,inplace=True)


    #  After Processing
    st.subheader("✅ After Processing")
    st.markdown(
    f"""
    The preprocessing removed **{len(existing_cols)} columns** and
    **{rows_before - rows_after:,} rows** containing missing values.

    **Final Dataset:** **{rows_after:,} rows × {len(existing_cols)} columns**
    """
)   

    col1 , col2, col3 =st.columns(3)
    with col1:
            st.metric("Rows After Cleaning", rows_after, delta=rows_after - rows_before, delta_color="inverse")
    with col2:
        st.metric("Columns Remaining", processed_data.shape[1])
    with col3:
        st.metric("Rows Removed", rows_before - rows_after, delta="-{}".format(rows_before - rows_after))

    # Show missing values again (should be all zeros)
    missing_after =get_missing_stats(processed_data)
    st.markdown("**Missing values after cleaning:**")
    if missing_after.empty:
        st.success("🎉 No missing values remaining!")
    else:
        st.dataframe(missing_after, use_container_width=True)

    with st.expander("Preview of Cleaned Data"):
        st.dataframe(processed_data.head(10), use_container_width=True)

    # ---------- Download Cleaned Data ----------
    csv_clean = processed_data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Cleaned Data (CSV)",
        data=csv_clean,
        file_name="footballplayeranalytics_cleaned.csv",
        mime="text/csv",
        use_container_width=True,
    )

    # ---------- Side note: storing cleaned data for other pages ----------
    # We'll store it in session_state so Visualization can use it directly
    st.session_state['cleaned_data'] = processed_data
    st.success(
"""
🎉 Data preprocessing completed successfully!

The cleaned dataset has been saved and is now available
for all visualization pages.
"""
)
# elif opt=='📊 Visualizations':
