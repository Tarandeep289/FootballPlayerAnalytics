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

# Load data
df = pd.read_csv(r'C:\Users\ASUS\FootballPlayerAnalyticsProject\Streamlit2\FC26_20250921.csv')

st.markdown("""
<style>

/* ---------- APP GLOBAL ---------- */
.stApp{
    background: linear-gradient(180deg, #EDF7ED, #F8FAFC);
}

/* Headings Global */
h1, h2, h3 {
    color: #0B3C2D;
    font-weight: 800;
}

/* ---------- SIDEBAR ---------- */
section[data-testid="stSidebar"]{
    background: linear-gradient(180deg, #0B1F33, #12344D);
    border-right: 4px solid #2ECC71;
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3{
    color: #FFD54F !important;
}

section[data-testid="stSidebar"] label{
    color: white !important;
    font-weight: 600;
}

.nav-link{
    border-radius: 12px !important;
    margin: 6px 0;
    font-size: 17px !important;
    font-weight: 600 !important;
    transition: 0.3s;
}

.nav-link:hover{
    background: #2ECC71 !important;
    transform: translateX(5px);
}

.nav-link-selected{
    background: #27AE60 !important;
    color: white !important;
    box-shadow: 0 5px 15px rgba(0,0,0,.3);
}

div[data-baseweb="select"]{
    border-radius: 10px;
}

div[data-baseweb="select"] svg{
    fill: #444 !important;
}

/* ---------- SHARED COMPONENTS ---------- */
img{
    border-radius: 20px;
    border: 5px solid white;
    box-shadow: 0 15px 30px rgba(0,0,0,.25);
}

.kpi-card{
    background: linear-gradient(135deg, #ffffff, #f4fff6);
    border-radius: 18px;
    padding: 25px;
    text-align: center;
    border-left: 8px solid #27AE60;
    box-shadow: 0 10px 25px rgba(0,0,0,.12);
    transition: 0.35s;
}

.kpi-card:hover{
    transform: translateY(-8px);
    box-shadow: 0 18px 35px rgba(39,174,96,.35);
}

.kpi-icon{ font-size: 36px; }
.kpi-title{ margin-top: 10px; font-size: 18px; color: #555; font-weight: 600; }
.kpi-value{ margin-top: 8px; font-size: 34px; color: #0B3C2D; font-weight: 800; }

/* Custom Container Cards */
.custom-card {
    background: #FFFFFF;
    border-radius: 16px;
    padding: 24px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.06);
    border: 1px solid #E2E8F0;
    margin-bottom: 20px;
}

/* Pipeline Step Cards */
.pipeline-step {
    background: linear-gradient(135deg, #27AE60, #1E8449);
    color: white !important;
    text-align: center;
    padding: 16px 10px;
    border-radius: 14px;
    font-weight: 700;
    font-size: 14px;
    line-height: 1.3;
    box-shadow: 0 6px 15px rgba(39,174,96,0.3);
    transition: all 0.3s ease;
    min-height: 95px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.pipeline-step:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(39,174,96,0.45);
}

/* Streamlit Metrics Customization */
div[data-testid="stMetric"] {
    background: #FFFFFF;
    padding: 15px 20px;
    border-radius: 12px;
    border-left: 5px solid #27AE60;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}

/* Dataframe Container Customization */
div[data-testid="stDataFrame"]{
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
}

/* Download & Action Buttons */
.stDownloadButton button{
    background: #27AE60;
    color: white;
    border-radius: 12px;
    font-size: 16px;
    font-weight: 700;
    padding: 10px 20px;
    border: none;
    transition: 0.3s;
}

.stDownloadButton button:hover{
    background: #1E8449;
    transform: translateY(-3px);
}

/* Expander Styling */
.streamlit-expanderHeader{
    background: #F1F8E9;
    border-radius: 12px;
    font-size: 16px;
    font-weight: 700;
    color: #0B3C2D;
}

/* Scrollbar */
::-webkit-scrollbar{ width: 8px; }
::-webkit-scrollbar-thumb{ background: #2ECC71; border-radius: 20px; }

</style>
""", unsafe_allow_html=True)

# Sidebar Routing
with st.sidebar:
    # opt = option_menu(menu_title='Menu', options=['🏠 Home', '📄 Dataset', '🧹 Preprocessing', '📊 Visualizations', 'ℹ About'])
    opt = option_menu(
    menu_title='Menu',
    options=['Home', 'Dataset', 'Preprocessing', 'Visualizations', 'About'],
    icons=['house', 'file-text', 'tools', 'bar-chart-line', 'info-circle'],
    default_index=0,
    menu_icon="cast")
    st.markdown('---')
    st.subheader('🔍 Filters')
    league = st.multiselect('Select league 🌍', options=df['league_name'].dropna().unique())
    club = st.multiselect('Select club 🏟', options=df['club_name'].dropna().unique())
    
    filtered = df.copy()
    if league:
        filtered = filtered[filtered['league_name'].isin(league)]
    if club:
        filtered = filtered[filtered['club_name'].isin(club)]

# Home page
if opt == 'Home':
    st.markdown("""
    <div style="text-align:center; padding:15px;">
        <h1 style="font-size:52px; margin-bottom:10px; text-shadow:2px 2px 8px rgba(0,0,0,0.15);">
        ⚽ FC26 Player Analytics Dashboard
        </h1>
        <p style="font-size:20px; color:#555; font-style:italic; margin-top:0;">
        Explore player performance, market value, club statistics, league comparisons, and transfer insights using interactive visualizations.
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.image(
        r"C:\Users\ASUS\FootballPlayerAnalyticsProject\Streamlit2\football-stadium-inside-at-night-with-lights-post-production-free-photo.jpg",
        use_container_width=True
    )
    
    players = filtered['short_name'].shape[0]
    leagues = filtered['league_name'].nunique()
    clubs = filtered['club_name'].nunique()
    avg_value = filtered['value_eur'].mean()
    avg_overall = filtered["overall"].mean()
    avg_potential = filtered["potential"].mean()
    total_wages = filtered["wage_eur"].sum()

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f'<div class="kpi-card"><div class="kpi-icon">👤</div><div class="kpi-title">Total Players</div><div class="kpi-value">{players:,}</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="kpi-card"><div class="kpi-icon">🌍</div><div class="kpi-title">Leagues</div><div class="kpi-value">{leagues}</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="kpi-card"><div class="kpi-icon">🏟️</div><div class="kpi-title">Clubs</div><div class="kpi-value">{clubs}</div></div>', unsafe_allow_html=True)
    with col4:
        st.markdown(f'<div class="kpi-card"><div class="kpi-icon">💰</div><div class="kpi-title">Avg Market Value</div><div class="kpi-value">€{avg_value/1e6:.2f}M</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col5, col6, col7 = st.columns(3)
    with col5:
        st.markdown(f'<div class="kpi-card"><div class="kpi-icon">⭐</div><div class="kpi-title">Avg Overall</div><div class="kpi-value">{avg_overall:.1f}</div></div>', unsafe_allow_html=True)
    with col6:
        st.markdown(f'<div class="kpi-card"><div class="kpi-icon">🚀</div><div class="kpi-title">Avg Potential</div><div class="kpi-value">{avg_potential:.1f}</div></div>', unsafe_allow_html=True)
    with col7:
        st.markdown(f'<div class="kpi-card"><div class="kpi-icon">💵</div><div class="kpi-title">Total Weekly Wages</div><div class="kpi-value">€{total_wages/1e9:.2f}B</div></div>', unsafe_allow_html=True)

# Dataset page
elif opt == 'Dataset':
    st.markdown("""
    <div style="text-align:center; padding:10px;">
        <h1 style="font-size:45px;">📊 Dataset Explorer</h1>
        <p style="font-size:20px; color:#555; font-style:italic;">
        Explore football player records, column information, statistical summaries, and filtered data insights.
        </p>
    </div>
    """, unsafe_allow_html=True)

    num_rows = filtered.shape[0]
    num_cols = filtered.shape[1]
    
    st.markdown(f"""
    <div style="display:flex; gap:20px; flex-wrap:wrap; margin:20px 0;">
        <span class="kpi-card" style="padding:15px 20px; flex:1;">📋 <strong>Rows:</strong> {num_rows}</span>
        <span class="kpi-card" style="padding:15px 20px; flex:1;">📑 <strong>Columns:</strong> {num_cols}</span>
        <span class="kpi-card" style="padding:15px 20px; flex:1;">🌍 <strong>Leagues:</strong> {filtered['league_name'].nunique()}</span>
        <span class="kpi-card" style="padding:15px 20px; flex:1;">🏟️ <strong>Clubs:</strong> {filtered['club_name'].nunique()}</span>
        <span class="kpi-card" style="padding:15px 20px; flex:1;">🌎 <strong>Nationalities:</strong> {filtered['nationality_name'].nunique()}</span>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(['📂 Data Preview', '📋 Column Information', '📈 Summary'])
    
    with tab1:
        col_left, col_right = st.columns([3, 1])
        with col_left:
            st.subheader('Preview Filtered Data')
        with col_right:
            n_rows = st.slider('Rows to show', min_value=5, max_value=101, step=20, value=20)
        st.dataframe(filtered.head(n_rows), use_container_width=True)
        with st.expander('Show last 10 rows'):
            st.dataframe(filtered.tail(10), use_container_width=True)

        csv = filtered.to_csv(index=False, encoding='utf-8')
        st.download_button(
            label='📥 Download filtered data as csv',
            data=csv,
            file_name='FootballPlayerAnalytics_Cleaned.csv',
            mime='text/csv',
            use_container_width=True
        )

    with tab2:
        column_info = pd.DataFrame({
            'Column Name': filtered.columns,
            'Data Type': filtered.dtypes.astype(str),
            'Missing Values': filtered.isna().sum()
        })
        st.dataframe(column_info, use_container_width=True, height=400, hide_index=True)

    with tab3:
        st.subheader('Statistical Summary')
        num_cols = filtered.select_dtypes(include=['int64', 'float64']).columns.tolist()
        cat_cols = filtered.select_dtypes(include=['object', 'category']).columns.tolist()

        if num_cols:
            st.markdown('#### 📊 Numeric Columns')
            st.dataframe(filtered[num_cols].describe(), use_container_width=True)

        if cat_cols:
            st.markdown('#### 🏷️ Categorical Columns')
            categorical_cols = ["league_name", "club_name", "nationality_name", "player_positions"]
            for col in categorical_cols:
                if col in filtered.columns:
                    with st.expander(f"Top values in '{col}'"):
                        top_values = filtered[col].dropna().value_counts().reset_index().head(10)
                        top_values.columns = [col, "Player Count"]
                        st.dataframe(top_values, use_container_width=True, hide_index=True)

# Preprocessing page
elif opt == 'Preprocessing':
    st.markdown("""
    <div style="text-align:center; padding:10px;">
        <h1 style="font-size:45px;">🧹 Data Preprocessing Pipeline</h1>
        <p style="font-size:20px; color:#555; font-style:italic; margin-top:0; max-width:800px; 
        margin:0 auto 20px auto">
        This page demonstrates the data transformation steps performed on the <strong>FC26 Player Dataset</strong> 
        to ensure high data quality by eliminating null values, handling redundant features, and standardizing values.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader('📋 Processing Workflow')
    steps = [
        "1.<br>📂 Raw<br>Dataset",
        "2.<br>🔍 Missing<br>Analysis",
        "3.<br>🗑️ Drop<br>Columns",
        "4.<br>🧹 Handle<br>Missing",
        "5.<br>🧾 Remove<br>Duplicates",
        "6.<br>✔️ Validate<br>Types",
        "7.<br>📈 Growth<br>Feature",
        "8.<br>✅ Clean<br>Dataset"
    ]

    cols = st.columns(len(steps))
    for col, step in zip(cols, steps):
        col.markdown(f'<div class="pipeline-step">{step}</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    def get_missing_stats(df_input):
        missing_df = df_input.isna().sum().reset_index()
        missing_df.columns = ['Column Name', 'Missing Count']
        missing_df['Missing %'] = (missing_df['Missing Count'] / len(df_input) * 100).round(1)
        missing_df = missing_df[missing_df['Missing Count'] > 0]
        return missing_df

    # ---------- BEFORE PROCESSING ----------
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader('🔍 Dataset Before Processing')
    
    col1, col2 = st.columns([3, 1])
    missing_before = get_missing_stats(filtered)
    
    with col1:
        if not missing_before.empty:
            st.markdown('**Columns with missing values:**')
            st.dataframe(missing_before, use_container_width=True, height=220, hide_index=True)
        else:
            st.success('✅ No missing values found!')
            
    with col2:
        st.metric("Rows", f"{filtered.shape[0]:,}")
        st.metric("Columns", filtered.shape[1])
    st.markdown('</div>', unsafe_allow_html=True)

    # Missing Plot
    if not missing_before.empty:
        st.subheader('📊 Missing Values Distribution')
        fig = px.bar(
            missing_before,
            x="Column Name",
            y="Missing Count",
            color="Missing Count",
            color_continuous_scale="Viridis",
            text="Missing Count",
            labels={"Column Name": "Columns", "Missing Count": "Missing Values"},
            template="plotly_white"
        )
        fig.update_traces(
            textposition="outside",
            marker_line_color="black",
            marker_line_width=1.2,
            hovertemplate="<b>%{x}</b><br>Missing Values: %{y}<extra></extra>"
        )
        fig.update_layout(
            xaxis=dict(title="", tickangle=-30, showgrid=False, tickfont=dict(size=12)),
            yaxis=dict(title="Number of Missing Values", showgrid=True, gridcolor="rgba(200,200,200,0.3)"),
            coloraxis_showscale=True,
            plot_bgcolor="white",
            paper_bgcolor="white",
            margin=dict(t=30, l=40, r=20, b=100),
            height=450
        )
        st.plotly_chart(fig, use_container_width=True)

    st.info("""
    📌 **Dropped Columns:** `club_jersey_number`, `club_loaned_from`, `club_team_id`,
    `goalkeeping_speed`, `nation_jersey_number`, `nation_position`, `nation_team_id`,
    `player_tags`, `player_traits`, and `work_rate`.

    These features were removed because they contained high rates of missing values, served primarily as internal IDs, 
    or lacked utility for performance analysis.
    """)

    # Processing Operations
    processed_data = filtered.copy()
    cols_to_drop = [
        'club_jersey_number', 'club_loaned_from', 'club_team_id',
        'goalkeeping_speed', 'nation_jersey_number', 'nation_position',
        'nation_team_id', 'player_tags', 'player_traits', 'work_rate'
    ]
    existing_cols = [c for c in cols_to_drop if c in processed_data.columns]
    processed_data.drop(columns=existing_cols, inplace=True, errors='ignore')

    rows_before = processed_data.shape[0]
    processed_data.dropna(inplace=True)
    rows_after = processed_data.shape[0]
    processed_data.reset_index(drop=True, inplace=True)

    # ---------- AFTER PROCESSING ----------
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.subheader("✅ Dataset After Processing")
    st.markdown(f"""
    The preprocessing removed **{len(existing_cols)} columns** and **{rows_before - rows_after:,} rows** containing null values.
    
    **Final Clean Shape:** **{rows_after:,} rows × {processed_data.shape[1]} columns**
    """)

    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.metric("Rows Remaining", f"{rows_after:,}", delta=rows_after - rows_before, delta_color="inverse")
    with col_b:
        st.metric("Columns Remaining", processed_data.shape[1], delta=f"-{len(existing_cols)}")
    with col_c:
        st.metric("Rows Removed", f"{rows_before - rows_after:,}", delta=f"-{rows_before - rows_after}")
    st.markdown('</div>', unsafe_allow_html=True)

    missing_after = get_missing_stats(processed_data)
    if missing_after.empty:
        st.success("🎉 All missing values resolved cleanly!")
    else:
        st.dataframe(missing_after, use_container_width=True)

    with st.expander("👁️ Preview Cleaned Dataset"):
        st.dataframe(processed_data.head(10), use_container_width=True)

    csv_clean = processed_data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Cleaned Data (CSV)",
        data=csv_clean,
        file_name="footballplayeranalytics_cleaned.csv",
        mime="text/csv",
        use_container_width=True,
    )

    st.session_state['cleaned_data'] = processed_data

elif opt=='Visualizations':

    # -----------------------------------------------------
    # HEADER (matching Home / Dataset / Preprocessing style)
    # -----------------------------------------------------
    st.markdown("""
    <div style="text-align:center; padding:10px 0 5px 0;">
        <h1 style="font-size:45px; margin-bottom:8px;">📈 Interactive Data Visualization</h1>
        <p style="font-size:19px; color:#555; font-style:italic; max-width:900px; margin:0 auto 15px auto;">
            Dive into the FC26 Player Analytics Dashboard and explore detailed insights about 
            football players worldwide. Visualize player ratings, potential, market values, 
            club performances, and skill distributions through interactive data visualizations.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # -----------------------------------------------------
    # DATA LOADING PIPELINE (SESSION STATE OR FALLBACK)
    # -----------------------------------------------------
    if "cleaned_data" in st.session_state:
        plot_data = st.session_state["cleaned_data"].copy()
    else:
        # Fallback: Process raw filtered data on the fly if user skipped Preprocessing tab
        plot_data = filtered.copy()
        cols_to_drop = [
            "club_jersey_number", "club_loaned_from", "club_team_id",
            "goalkeeping_speed", "nation_jersey_number", "nation_position",
            "nation_team_id", "player_tags", "player_traits", "work_rate",
        ]
        cols_exist = [c for c in cols_to_drop if c in plot_data.columns]
        plot_data.drop(columns=cols_exist, inplace=True, errors="ignore")
        plot_data.dropna(inplace=True)
        plot_data.reset_index(drop=True, inplace=True)

    if plot_data.empty:
        st.warning("No data available after cleaning. Please check your filters or the Preprocessing page.")
    else:
        # Feature engineering
        plot_data["growth"] = plot_data["potential"] - plot_data["overall"]

        # -----------------------------------------------------
        # VISUALIZATION TABS
        # -----------------------------------------------------
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "💰 Market Analytics",
            "🏆 League & Club Analysis",
            "🏃 Player Profiles",
            "🔮 Talent Scouting",
            "📊 Performance Correlation",
        ])

        # =====================================================
        # TAB 1 : MARKET & FINANCIAL ANALYTICS
        # =====================================================
        with tab1:
            st.markdown("""
            <div class="custom-card">
                <h3 style="margin-top:0; color:#0B3C2D;">💰 Executive Market & Financial Analytics</h3>
                <p style="color:#555; margin-bottom:0;">
                    Analyze football's financial landscape through player valuations, 
                    rating-based market trends, and club wage investments.
                </p>
            </div>
            """, unsafe_allow_html=True)

            # GRAPH 1 : PLAYER VALUE DISTRIBUTION
            st.markdown("### 📊 Player Market Value Distribution")

            fig = px.histogram(
            data_frame=df,
            x="value_eur",
            nbins=12,
            # title="Player Value Distribution Matrix",
            template="plotly_white",
            color_discrete_sequence=px.colors.qualitative.Set2,
            opacity=0.85
        )

            fig.update_traces(
    marker=dict(
        line=dict(color="black", width=1)
    ),
    hovertemplate=
    "<b>Market Value:</b> €%{x:,.0f}<br>"
    "<b>Players:</b> %{y}<extra></extra>"
)

            fig.update_layout(
    # title=dict(
    #     text="Player Value Distribution Matrix",
    #     x=0.5,
    #     xanchor="center",
    #     font=dict(size=24, family="Arial", color="#0B0C0C")
    # ),

    xaxis=dict(
        title="Player Market Value (€)",
        showgrid=True,
        gridcolor="lightgray",
        gridwidth=1,
        zeroline=False,
        tickformat=","
    ),

    yaxis=dict(
        title="Number of Players",
        showgrid=True,
        gridcolor="lightgray",
        gridwidth=1,
        zeroline=False
    ),

    width=700,
    height=500,

    font=dict(
        family="Arial",
        size=14,
        color="#55555E"
    ),

    bargap=0.04,
    hovermode="x unified",

    margin=dict(
        l=70,
        r=40,
        t=80,
        b=70
    ),
)

            # fig.show()
            st.plotly_chart(fig, use_container_width=True)

            st.info("""
            💡 **Insight:** The football market follows a highly uneven distribution. 
            Most players are valued below €5M, while only a small group of elite players 
            reach extremely high transfer valuations.
            """)

            # GRAPH 2 : OVERALL VS MARKET VALUE
            st.markdown("### 📈 Overall Rating vs Market Value")

            fig=px.scatter(df,
               x='overall',
               y='value_eur',
               color='age',
               template='plotly_white',
            #  title='Relationship between overall rating and market value',
               color_continuous_scale='Viridis', # applies for numerical data else legend or color_discrete_sequence for categorical
               opacity=0.75,
               hover_data={
                   "short_name":True,
                   "club_name":True,
                   "overall":True,
                   'value_eur':":,",
                   'age':True   
               })
            fig.update_traces(
    marker=dict(
        line=dict(color='white',width=0.5),
        symbol='triangle-up',
        size=10
    ),
    hovertemplate=(
           "<b>%{customdata[0]}</b><br>" +
    "Club: %{customdata[1]}<br>" +
    "Overall Rating: %{x}<br>" +
    "Market Value: €%{y:,.0f}<br>" +
    "Age: %{marker.color}<extra></extra>"
    ),
)
            fig.update_layout(
    # title=dict(
    #     text="Relationship Between Overall Rating and Market Value",
    #     x=0.5,
    #     font=dict(size=24)
    # ),

    xaxis_title="Overall Rating",
    yaxis_title="Market Value (€)",

    width=700,
    height=500,

    font=dict(
        family="Arial",
        size=14
    ),

    margin=dict(
        l=70,
        r=40,
        t=80,
        b=70
    ),

    hovermode="closest",

    coloraxis_colorbar=dict(
        title="Age"
    )
)

            fig.update_xaxes(
    showgrid=True,
    gridcolor="lightgray",
    showline=True,
    linewidth=1,
    linecolor="black",
)

            fig.update_yaxes(
    showgrid=True,
    gridcolor="lightgray",
    tickformat=",",
    showline=True,
    linewidth=1,
    linecolor="black",
)
            # fig.show()
            st.plotly_chart(fig, use_container_width=True)

            st.info("""
            💡 **Insight:** Market value increases sharply when players cross higher overall ratings. 
            Younger high-rated players usually receive additional value due to future potential.
            """)

            # GRAPH 3 : TOP CLUBS BY WAGE
            st.markdown("### 💰 Top 15 Clubs by Total Wage Commitment")

            club_wages = (
                plot_data.groupby("club_name")["wage_eur"]
                .sum()
                .reset_index()
                .sort_values(by="wage_eur", ascending=False)
                .head(15)
            )
            club_wages = (
    df.groupby("club_name")["wage_eur"]
      .sum()
      .reset_index()
      .sort_values(by="wage_eur", ascending=False)
      .head(15)
)

            fig = px.bar(
    club_wages,
    x="wage_eur",
    y="club_name",
    orientation="h",
    color="wage_eur",
    color_continuous_scale="Viridis",
    text="wage_eur",
    template="plotly_white",
    # title="Top 15 Clubs by Aggregate Wage Commitments"
)

            fig.update_traces(
    texttemplate="€%{text:,.0f}",
    textposition="outside"
)

            fig.update_layout(
    # title_x=0.5,
    xaxis_title="Total Wage (€)",
    yaxis_title="Club Name",
    showlegend=False,
    height=650,
    width=1000,
    margin=dict(l=180, r=40, t=80, b=60)
)

            fig.update_yaxes(categoryorder="total ascending", showline=True,
    linewidth=1,
    linecolor="black")

            # fig.show()

            
            st.plotly_chart(fig, use_container_width=True)

            st.info("""
            💡 **Insight:** Wage spending is concentrated among football's biggest clubs. 
            These teams maintain competitive advantage by investing heavily in player salaries.
            """)

        # =====================================================
        # TAB 2 : LEAGUE & CLUB ANALYSIS
        # =====================================================
        with tab2:
            st.markdown("""
            <div class="custom-card">
                <h3 style="margin-top:0; color:#0B3C2D;">🏆 League & Club Structural Evaluation</h3>
                <p style="color:#555; margin-bottom:0;">
                    Compare player quality, technical attributes, and financial structures 
                    across the world's top football leagues.
                </p>
            </div>
            """, unsafe_allow_html=True)

            top5 = ["Premier League", "La Liga", "Serie A", "Bundesliga", "Ligue 1"]
            df_top5 = plot_data[plot_data["league_name"].isin(top5)]

            # GRAPH 4 : TECHNICAL SKILLS
            st.markdown("### 📈 Average Technical Skills Across Top 5 European Leagues")

            skill_avg = (
                df_top5.groupby("league_name")[
                    ["pace", "shooting", "passing", "dribbling", "defending", "physic"]
                ]
                .mean()
                .reset_index()
            )
            skill_avg = skill_avg.melt(
                id_vars="league_name",
                var_name="Technical Skill",
                value_name="Average Rating",
            )

            fig4 = px.bar(
                skill_avg,
                x="league_name",
                y="Average Rating",
                barmode="group",
                color="Technical Skill",
                template="plotly_white",
                color_discrete_sequence=px.colors.qualitative.Set3,
                text_auto=".1f",
            )
            fig4.update_traces(
                hovertemplate="<b>%{x}</b><br>Skill: %{fullData.name}<br>Average Rating: %{y:.1f}<extra></extra>",
                marker=dict(line=dict(color="black", width=1)),
                textposition="outside",
            )
            fig4.update_layout(
                width=1000, height=550,
                xaxis_title="League",
                yaxis_title="Average Technical Rating",
                legend_title="Technical Skill",
                font=dict(size=14, family="Arial"),
                margin=dict(t=40, r=40, l=70, b=70),
                bargap=0.1, bargroupgap=0.03,
            )
            fig4.update_xaxes(showgrid=False, showline=True, linewidth=1, linecolor="black")
            fig4.update_yaxes(showgrid=True, gridcolor="lightgray", showline=True, linewidth=1,
                              linecolor="black", range=[0, 100])
            st.plotly_chart(fig4, use_container_width=True)

            st.info("""
            💡 **Insight:** The comparison highlights differences in playing styles across major European leagues. 
            Some leagues show stronger attacking attributes (passing & dribbling), while others emphasize 
            physical and defensive qualities.
            """)

            # GRAPH 5 : SQUAD RATING VARIANCES
            st.markdown("### 📊 Squad Rating Distribution within Top 5 Leagues")

            fig5 = px.box(
                df_top5,
                x="league_name",
                y="overall",
                color="league_name",
                template="plotly_white",
                points="outliers",
                color_discrete_sequence=px.colors.qualitative.Dark2,
                hover_data=["short_name", "club_name", "age", "overall"],
            )
            fig5.update_traces(
                hovertemplate="<b>%{customdata[0]}</b><br>Club: %{customdata[1]}<br>League: %{x}<br>"
                              "Overall Rating: %{y}<br>Age: %{customdata[2]}<extra></extra>",
                boxmean=True,
                whiskerwidth=0.8,
                marker=dict(size=5, opacity=0.8, line=dict(color="black", width=0.5)),
            )
            fig5.update_layout(
                xaxis_title="League",
                yaxis_title="Overall Player Rating",
                font=dict(family="Arial", size=14),
                height=550, width=1000,
                legend_title="League",
                margin=dict(l=70, r=40, t=40, b=70),
                hovermode="closest",
            )
            fig5.update_xaxes(showgrid=False, showline=True, linecolor="black", linewidth=1)
            fig5.update_yaxes(showgrid=True, gridcolor="lightgray", gridwidth=1, zeroline=False,
                              showline=True, linewidth=1, linecolor="black", range=[40, 100])
            st.plotly_chart(fig5, use_container_width=True)

            st.info("""
            💡 **Insight:** Higher median overall ratings indicate stronger average squads. 
            Wider boxes show greater variation in player quality. Outliers represent exceptional players 
            significantly above or below the league average.
            """)

            # GRAPH 6 : TREEMAP WAGES
            st.markdown("### 💰 League Financial Wage Architecture (Top 10 Clubs per League)")

            df_sum = (
                df_top5.groupby(["league_name", "club_name"])["wage_eur"]
                .sum()
                .reset_index()
            )
            df_sum = (
                df_sum.sort_values("wage_eur", ascending=False)
                .groupby("league_name")
                .head(10)
            )

            fig6 = px.treemap(
                df_sum,
                path=["league_name", "club_name"],
                values="wage_eur",
                color="wage_eur",
                color_continuous_scale="Viridis",
                template="plotly_white",
                hover_data={"wage_eur": ":,"},
            )
            fig6.update_traces(
                textinfo="label+value+percent parent",
                hovertemplate="<b>%{label}</b><br>Total Wage: €%{value:,.0f}<br>"
                              "League Share: %{percentParent}<br>Overall Share: %{percentRoot}<extra></extra>",
                marker=dict(line=dict(color="white", width=2)),
            )
            fig6.update_layout(
                width=1100, height=650,
                margin=dict(l=20, r=20, t=40, b=20),
                font=dict(family="Arial", size=14),
                coloraxis_colorbar=dict(title="Total Wage (€)"),
            )
            st.plotly_chart(fig6, use_container_width=True)

            st.info("""
            💡 **Insight:** The wage structure is highly concentrated among a small number of elite leagues and clubs. 
            Larger segments represent organisations with greater financial commitment, highlighting the economic gap 
            between football's biggest clubs and the rest of the market.
            """)

        # =====================================================
        # TAB 3 : PLAYER PROFILES
        # =====================================================
        with tab3:
            st.markdown("""
            <div class="custom-card">
                <h3 style="margin-top:0; color:#0B3C2D;">🏃 Player Archetype & Physical Attribute Profiling</h3>
                <p style="color:#555; margin-bottom:0;">
                    Explore physical attributes, preferred foot patterns, and positional value distributions.
                </p>
            </div>
            """, unsafe_allow_html=True)

            # GRAPH 7
            st.markdown("### ⚡ Sprint Speed vs Strength by Preferred Foot")

            agg_df = (
                plot_data.groupby(["preferred_foot", "league_name"])[
                    ["movement_sprint_speed", "power_strength"]
                ]
                .mean()
                .reset_index()
            )

            fig7 = px.scatter(
                agg_df,
                x="movement_sprint_speed",
                y="power_strength",
                color="preferred_foot",
                color_discrete_sequence=["#3B528B", "#5DC863"],
                template="plotly_white",
                hover_data=["league_name"],
            )
            fig7.update_traces(
                marker=dict(size=12, opacity=0.8, line=dict(color="black", width=0.5), symbol="circle"),
                hovertemplate="<b>%{customdata[0]}</b><br>League: %{customdata[0]}<br>"
                              "Average Sprint Speed: %{x:.2f}<br>Average Strength: %{y:.2f}<extra></extra>",
            )
            fig7.update_layout(
                xaxis_title="Average Sprint Speed",
                yaxis_title="Average Strength",
                legend_title="Preferred Foot",
                width=900, height=550,
                font=dict(family="Arial", size=14),
                margin=dict(l=70, r=40, t=40, b=70),
            )
            fig7.update_xaxes(showgrid=True, gridcolor="lightgray", showline=True, linecolor="black")
            fig7.update_yaxes(showgrid=True, gridcolor="lightgray", showline=True, linecolor="black")
            st.plotly_chart(fig7, use_container_width=True)

            st.info("""
            **Analytical Insights:**
            - **Trade-Off Dynamics:** Highlights the inherent physical trade-off between explosive pace and raw power across different league profiles.
            - **Footedness Footprint:** Groups mean physical profiles by preferred foot and league to identify physical advantages in specific tactical ecosystems.
            - **Scouting Archetypes:** Quickly identifies league outliers that prioritize high-tempo athleticism versus physically dominant players.
            """)

            # GRAPH 8
            st.markdown("### 📅 Age Distribution by Preferred Foot")

            fig8 = px.histogram(
                plot_data,
                x="age",
                color="preferred_foot",
                barmode="overlay",
                nbins=25,
                opacity=0.85,
                template="plotly_white",
                color_discrete_sequence=["#3B528B", "#5EC962"],
                hover_data=["short_name", "club_name", "overall"],
            )
            fig8.update_traces(
                hovertemplate="<b>Age:</b> %{x}<br><b>Players:</b> %{y}<br><extra></extra>",
                marker=dict(line=dict(color="black", width=1)),
            )
            fig8.update_layout(
                xaxis_title="Age (Years)",
                yaxis_title="Number of Players",
                legend_title="Preferred Foot",
                height=550, width=950,
                font=dict(family="Arial", size=14),
                margin=dict(l=70, r=40, t=40, b=70),
                bargap=0.05,
            )
            fig8.update_xaxes(showgrid=False, showline=True, linecolor="black")
            fig8.update_yaxes(showgrid=True, gridcolor="lightgray", showline=True, linecolor="black")
            st.plotly_chart(fig8, use_container_width=True)

            st.info("""
            **Analytical Insights:**
            - **Demographic Volume:** Shows the volume distribution of right- vs left-footed players across age brackets, highlighting the relative scarcity of left-footed assets.
            - **Career Lifecycle Peak:** Maps player density across early development, prime athletic age (24–28), and veteran phases.
            - **Roster Longevity:** Evaluates whether physical degradation or positional demand shifts the age distribution profile between foot preferences.
            """)

            # GRAPH 9
            st.markdown("### 💪 Physical Rating Distribution by Preferred Foot")

            fig9 = px.violin(
                plot_data,
                x="preferred_foot",
                y="physic",
                color="preferred_foot",
                box=True,
                color_discrete_sequence=["#3B528B", "#5EC962"],
                points="outliers",
                template="plotly_white",
                hover_data=["short_name", "club_name", "league_name", "overall", "age"],
            )
            fig9.update_traces(
                meanline_visible=True,
                hovertemplate="<b>%{customdata[0]}</b><br>Club: %{customdata[1]}<br>"
                              "League: %{customdata[2]}<br>Overall: %{customdata[3]}<br>"
                              "Age: %{customdata[4]}<br>Physic: %{y}<br>Preferred Foot: %{x}<extra></extra>",
            )
            fig9.update_layout(
                xaxis_title="Preferred Foot",
                yaxis_title="Physical Rating",
                legend_title="Preferred Foot",
                width=950, height=550,
                font=dict(family="Arial", size=14),
                margin=dict(l=70, r=40, t=40, b=70),
            )
            fig9.update_xaxes(showgrid=False, showline=True, linecolor="black")
            fig9.update_yaxes(showgrid=True, gridcolor="lightgray", showline=True, linecolor="black", range=[0, 100])
            st.plotly_chart(fig9, use_container_width=True)

            st.info("""
            **Analytical Insights:**
            - **Distribution & Density:** Combines KDE with box-plot metrics to reveal the underlying probability density of physical ratings.
            - **Median & IQR:** Clearly depicts median physical score, interquartile range, and full spread across footedness categories.
            - **Outlier Detection:** Isolates exceptionally strong or weak players relative to their dominant-foot cohort.
            """)

            # GRAPH 10
            st.markdown("### 🗺️ Market Value by League & Preferred Foot")

            treemap_df = plot_data.dropna(subset=["league_name", "preferred_foot"])

            fig10 = px.treemap(
                treemap_df,
                path=["league_name", "preferred_foot"],
                values="value_eur",
                color="value_eur",
                color_continuous_scale="Viridis",
                template="plotly_white",
            )
            fig10.update_traces(
                textinfo="label+percent parent",
                hovertemplate="<b>%{label}</b><br>Market Value: €%{value:,.0f}<br>"
                              "Share in Parent: %{percentParent}<br>Share Overall: %{percentRoot}<extra></extra>",
            )
            fig10.update_layout(
                width=950, height=650,
                margin=dict(l=20, r=20, t=40, b=20),
                font=dict(family="Arial", size=14),
                coloraxis_colorbar=dict(title="Market Value (€)"),
            )
            st.plotly_chart(fig10, use_container_width=True)

            st.info("""
            **Analytical Insights:**
            - **Asset Concentration:** Visually partitions total market value hierarchically across leagues and footedness categories.
            - **Proportional Value Share:** Reveals which leagues hold the largest concentration of financial capital tied to left- or right-footed talent.
            - **Macro-Financial Mapping:** Offers a top-down view for technical directors evaluating global market valuation density.
            """)

        # =====================================================
        # TAB 4 : TALENT SCOUTING
        # =====================================================
        with tab4:
            st.markdown("""
            <div class="custom-card">
                <h3 style="margin-top:0; color:#0B3C2D;">🔮 Talent Scouting & Hidden Gem Discovery</h3>
                <p style="color:#555; margin-bottom:0;">
                    Discover high-potential players by analyzing growth potential, market value, 
                    and wage efficiency. Identify emerging talent and undervalued players.
                </p>
            </div>
            """, unsafe_allow_html=True)

            # GRAPH 11
            st.markdown("### ⭐ Age vs Future Growth Capacity")

            fig11 = px.scatter(
                plot_data,
                x="age",
                y="growth",
                color="overall",
                template="plotly_white",
                color_continuous_scale="Viridis",
                hover_name="short_name",
                hover_data=["club_name", "league_name", "potential", "overall", "growth"],
            )
            fig11.update_traces(
                marker=dict(size=9, line=dict(color="black", width=0.5), symbol="square"),
                hovertemplate="<b>%{hovertext}</b><br>Age: %{x} years<br>Growth: %{y}<br>"
                              "Overall: %{marker.color}<br><extra></extra>",
            )
            fig11.update_layout(
                xaxis_title="Age (Years)",
                yaxis_title="Growth (Potential − Overall)",
                coloraxis_colorbar=dict(title="Overall Rating"),
                width=800, height=550,
                font=dict(family="Arial", size=14),
                margin=dict(l=70, r=40, t=40, b=70),
            )
            fig11.update_xaxes(showgrid=False, showline=True, linecolor="black")
            fig11.update_yaxes(showgrid=True, gridcolor="lightgray", showline=True, linecolor="black")
            st.plotly_chart(fig11, use_container_width=True)

            st.info("""
            **Analytical Insights:**
            - **Development Window:** High-growth capacity peaks primarily in players under 22 years old.
            - **Outlier Targets:** Isolates high-growth prospects who already possess solid baseline overall ratings.
            - **Roster Planning:** Reveals the precise age thresholds where development potential plateaus or decays.
            """)

            # GRAPH 12
            st.markdown("### 🌍 Top 15 Countries by Average Player Potential")

            country_potential = (
                plot_data.groupby("nationality_name")["potential"]
                .mean()
                .reset_index()
                .sort_values(by="potential", ascending=False)
                .head(15)
            )

            fig12 = px.bar(
                country_potential,
                x="nationality_name",
                y="potential",
                color="potential",
                color_continuous_scale="Viridis",
                template="plotly_white",
                text_auto=".1f",
            )
            fig12.update_traces(
                marker=dict(line=dict(color="black", width=0.8)),
                hovertemplate="<b>%{x}</b><br>Average Potential: %{y:.1f}<extra></extra>",
            )
            fig12.update_layout(
                xaxis_title="Nationality",
                yaxis_title="Average Potential Rating",
                width=900, height=550,
                font=dict(family="Arial", size=14),
                margin=dict(l=70, r=40, t=40, b=120),
                coloraxis_colorbar=dict(title="Potential"),
            )
            fig12.update_xaxes(showgrid=False, showline=True, linecolor="black")
            fig12.update_yaxes(showgrid=True, gridcolor="lightgray", showline=True, linecolor="black", range=[0, 100])
            st.plotly_chart(fig12, use_container_width=True)

            st.info("""
            **Analytical Insights:**
            - **Geographic Talent Hotspots:** Ranks the top 15 national cohorts by average potential rating.
            - **National Ecosystem Quality:** Reveals which development programs consistently produce higher ceilings.
            - **Strategic Sourcing:** Guides prioritization of scouting budgets across international markets.
            """)

            # GRAPH 13
            st.markdown("### 💵 Wage Efficiency: Weekly Wage vs Potential")

            # fig13 = px.scatter(
            #     plot_data,
            #     x="wage_eur",
            #     y="potential",
            #     color="overall",
            #     hover_name="short_name",
            #     template="plotly_white",
            #     hover_data=["club_name", "league_name", "age", "overall"],
            #     color_continuous_scale="Viridis",
            # )
            # fig13.update_traces(
            #     marker=dict(size=7, line=dict(color="black", width=0.5), symbol="square"),
            #     hovertemplate="<b>%{hovertext}</b><br>Weekly Wage: €%{x:,.0f}<br>Potential: %{y}<br>"
            #                   "Club: %{customdata[0]}<br>League: %{customdata[1]}<br>"
            #                   "Age: %{customdata[2]}<br>Overall: %{customdata[3]}<extra></extra>",
            # )
            # fig13.update_layout(
            #     height=550, width=800,
            #     xaxis_title="Weekly Wage (€)",
            #     yaxis_title="Potential Rating",
            #     coloraxis_colorbar=dict(title="Overall"),
            #     font=dict(family="Arial", size=14),
            #     margin=dict(l=70, r=40, t=40, b=70),
            # )
            # fig13.update_xaxes(showgrid=False, showline=True, linecolor="black")
            # fig13.update_yaxes(showgrid=True, gridcolor="lightgray", showline=True, linecolor="black", range=[0, 100])
            # st.plotly_chart(fig13, use_container_width=True)
            fig13 = px.scatter(
    plot_data,
    x="wage_eur",
    y="potential",
    color="overall",
    hover_name="short_name",
    template="plotly_white",
    color_continuous_scale="Viridis",
    hover_data=[
        "club_name",
        "league_name",
        "age",
        "overall"
    ]
)

            fig13.update_traces(
    marker=dict(
        size=5,
        opacity=0.45,
        line=dict(
            width=0.3,
            color="white"
        )
    )
)

            fig13.update_xaxes(
    type="log",# log is useful because wages are typically very right-skewed.
    title="Weekly Wage (€)",
    showgrid=True,
    gridcolor="lightgray"
)

            fig13.update_yaxes(
    title="Potential Rating",
    range=[50, 100],
    dtick=5,
    showgrid=True,
    gridcolor="lightgray"
)

            fig13.update_layout(
    height=550,
    paper_bgcolor="#F8FAFC",
    plot_bgcolor="white",
    font=dict(
        family="Arial",
        size=13
    ),
    margin=dict(
        l=70,
        r=70,
        t=50,
        b=70
    )
)
            fig13.update_xaxes(showline=True, linecolor="black")
            fig13.update_yaxes(showgrid=True, gridcolor="lightgray", showline=True, linecolor="black", )

            st.plotly_chart(fig13, use_container_width=True)

            st.info("""
            **Analytical Insights:**
            - **Financial Arbitrage:** Pinpoints low-wage players with high potential — high-value targets below market compensation.
            - **Wage Structure Benchmarking:** Contrasts weekly compensation against future upside.
            - **Undervalued Assets:** Isolates players delivering top-tier potential without premium wage expenditure.
            """)

        # =====================================================
        # TAB 5 : PERFORMANCE CORRELATION
        # =====================================================
        with tab5:
            st.markdown("""
            <div class="custom-card">
                <h3 style="margin-top:0; color:#0B3C2D;">📊 Core Attribute & Performance Correlation</h3>
                <p style="color:#555; margin-bottom:0;">
                    Examine interdependencies between key performance attributes and the relationship 
                    between overall rating and market valuation.
                </p>
            </div>
            """, unsafe_allow_html=True)

            # GRAPH 14
            st.markdown("### 🔥 Performance Attribute Correlation Heatmap")

            performance = plot_data[["pace", "shooting", "passing", "dribbling", "defending", "physic"]]
            corr = performance.corr()

            fig14 = px.imshow(
                corr,
                template="plotly_white",
                color_continuous_scale="Viridis",
                text_auto=".2f",
                aspect="auto",
                labels=dict(color="Correlation"),
            )
            fig14.update_traces(
                hovertemplate="<b>%{x}</b> vs <b>%{y}</b><br>Correlation: %{z:.2f}<extra></extra>"
            )
            fig14.update_layout(
                width=800, height=550,
                font=dict(family="Arial", size=14),
                margin=dict(l=70, r=40, t=40, b=70),
            )
            fig14.update_xaxes(title="Performance Attributes", showgrid=False, showline=True, linecolor="black")
            fig14.update_yaxes(title="Performance Attributes", showgrid=False, showline=True, linecolor="black")
            st.plotly_chart(fig14, use_container_width=True)

            st.info("""
            **Analytical Insights:**
            - **Technical Synergy:** Strong positive correlations between passing, dribbling, and shooting indicate shared developmental profiles among attacking playmakers.
            - **Defensive vs Offensive Trade-offs:** Inverse or neutral correlations between defending and attacking skills illustrate positional specialization.
            - **Physical Foundation:** Physical rating (`physic`) acts as an anchor for defensive metrics.
            """)

            # GRAPH 15
            st.markdown("### 📈 Average Market Value by Overall Rating")

            data = plot_data.groupby("overall")["value_eur"].mean().reset_index()

            fig15 = px.line(
                data,
                x="overall",
                y="value_eur",
                markers=True,
                template="plotly_white",
                color_discrete_sequence=["#3B528B"],
            )
            fig15.update_traces(
                line=dict(width=4),
                marker=dict(size=8, symbol="circle", color="#3B528B", line=dict(color="black", width=1)),
                hovertemplate="<b>Overall Rating:</b> %{x}<br><b>Average Market Value:</b> €%{y:,.0f}<extra></extra>",
            )
            fig15.update_layout(
                xaxis_title="Overall Rating",
                yaxis_title="Average Market Value (€)",
                width=800, height=550,
                font=dict(family="Arial", size=14),
                margin=dict(l=70, r=40, t=40, b=70),
            )
            fig15.update_xaxes(showgrid=False, showline=True, linecolor="black")
            fig15.update_yaxes(showgrid=True, gridcolor="lightgray", showline=True, linecolor="black", tickprefix="€")
            st.plotly_chart(fig15, use_container_width=True)

            st.info("""
            **Analytical Insights:**
            - **Exponential Valuation Curve:** Player valuations rise exponentially once overall rating crosses elite thresholds (80+).
            - **Baseline Value Parity:** Relatively flat increments across mid-to-lower tier ratings help benchmark standard pricing.
            - **Elite Talent Premium:** Highlights the steep financial premium required to acquire world-class players.
            """)

elif opt == "About":

    # -----------------------------------------------------
    # HEADER
    # -----------------------------------------------------
    st.markdown("""
    <div style="text-align:center; padding:10px 0 5px 0;">
        <h1 style="font-size:45px; margin-bottom:8px;">ℹ️ About This Dashboard</h1>
        <p style="font-size:19px; color:#555; font-style:italic; max-width:850px; margin:0 auto 20px auto;">
            Learn more about the FC26 Player Analytics Dashboard, its purpose, features, 
            data sources, and the technologies powering this interactive experience.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # -----------------------------------------------------
    # MAIN CONTENT
    # -----------------------------------------------------
    col1, col2 = st.columns([2.2, 1], gap="large")

    with col1:
        st.markdown("""
        <div class="custom-card">
            <h3 style="margin-top:0; color:#0B3C2D;">⚽ FC26 Player Analytics Dashboard</h3>
            <p style="color:#555; line-height:1.6; margin-bottom:0;">
                This interactive dashboard was built to explore and analyse football player data 
                from the <strong>FC26</strong> dataset. It provides scouts, analysts, data enthusiasts, 
                and students with powerful tools to understand player performance, market valuations, 
                league structures, physical attributes, and talent potential.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("")  # spacing

        st.markdown("#### ✨ Key Features")
        st.markdown("""
        - **Multi-page navigation** – Home, Dataset, Preprocessing, Visualizations, and About  
        - **Interactive filters** – Filter by League and Club in real time  
        - **Data cleaning pipeline** – Transparent preprocessing steps with before/after comparison  
        - **Rich interactive visualizations** – Market analytics, league comparisons, player profiling, talent scouting, and correlation analysis  
        - **KPI cards & download options** – Quick insights and exportable cleaned data
        """)

        st.markdown("#### 🎯 Use Cases")
        st.markdown("""
        - Talent identification and scouting support  
        - Market value and wage efficiency analysis  
        - League and club structural comparison  
        - Educational tool for data visualization & preprocessing techniques  
        - Quick exploratory data analysis for football analytics projects
        """)

    with col2:
        st.markdown("""
        <div class="custom-card" style="text-align:center;">
            <h3 style="margin-top:0; color:#0B3C2D;">🛠️ Tech Stack</h3>
            <p style="color:#555; font-size:15px; line-height:1.8;">
                <strong>Streamlit</strong><br>
                Web application framework<br><br>
                <strong>Pandas</strong><br>
                Data manipulation & cleaning<br><br>
                <strong>Plotly Express</strong><br>
                Interactive charts & visualizations<br><br>
                <strong>streamlit-option-menu</strong><br>
                Modern sidebar navigation
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="custom-card" style="margin-top:20px;">
            <h3 style="margin-top:0; color:#0B3C2D;">📁 Data Source</h3>
            <p style="color:#555; font-size:15px; line-height:1.6;">
                The primary dataset is <code>FC26_20250921.csv</code>, containing detailed player attributes from the FC26 game.
            </p>
            <p style="color:#555; font-size:14px; margin-bottom:0;">
                <strong>Key columns include:</strong><br>
                • Player identity (name, age, nationality)<br>
                • Club & League information<br>
                • Overall & Potential ratings<br>
                • Market Value & Wage<br>
                • Technical & Physical attributes<br>
                • Preferred foot and positions
            </p>
        </div>
        """, unsafe_allow_html=True)

    # -----------------------------------------------------
    # DEVELOPER SECTION
    # -----------------------------------------------------
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="custom-card" style="text-align:center;">
        <h3 style="margin-top:0; color:#0B3C2D;">👨‍💻 Developer</h3>
        <p style="font-size:18px; color:#0B3C2D; font-weight:700; margin-bottom:6px;">
            Tarandeep Kaur
        </p>
        <p style="color:#555; margin-bottom:12px;">
            Data Science & Football Analytics Enthusiast
        </p>
        <p style="color:#555; font-size:15px;">
            📧 tarandeepkaur0824@gmail.com<br>
            🔗 <a href="https://github.com/Tarandeep289" target="_blank" style="color:#27AE60; text-decoration:none; font-weight:600;">GitHub</a>
        </p>
        <p style="color:#777; font-size:14px; margin-top:18px; margin-bottom:0;">
            Built with ❤️ for educational and analytical purposes.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center; margin-top:30px; color:#888; font-size:13px;">
        FC26 Player Analytics Dashboard • Powered by Streamlit & Plotly
    </div>
    """, unsafe_allow_html=True)






















# tested code with simple words to understand

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
# # df=pd.read_csv(r'C:\Users\ASUS\FootballPlayerAnalyticsProject\Streamlit2\FC26_cleaned.csv')
# df=pd.read_csv(r'C:\Users\ASUS\FootballPlayerAnalyticsProject\Streamlit2\FC26_20250921.csv')

# st.markdown("""
# <style>

# /* ---------- APP ---------- */
# .stApp{
#     background:linear-gradient(180deg,#EDF7ED,#F8FAFC);
# }

# /* ---------- SIDEBAR ---------- */
# section[data-testid="stSidebar"]{
#     background:linear-gradient(180deg,#0B1F33,#12344D);
#     border-right:4px solid #2ECC71;
# }

# /* Sidebar headings only */
# section[data-testid="stSidebar"] h1,
# section[data-testid="stSidebar"] h2,
# section[data-testid="stSidebar"] h3{
#     color:#FFD54F !important;
# }

# /* Sidebar labels */
# section[data-testid="stSidebar"] label{
#     color:white !important;
#     font-weight:600;
# }

# /* Option Menu */
# .nav-link{
#     border-radius:12px !important;
#     margin:6px 0;
#     font-size:17px !important;
#     font-weight:600 !important;
#     transition:0.3s;
# }

# .nav-link:hover{
#     background:#2ECC71 !important;
#     transform:translateX(5px);
# }

# .nav-link-selected{
#     background:#27AE60 !important;
#     color:white !important;
#     box-shadow:0 5px 15px rgba(0,0,0,.3);
# }

# /* Multiselect */
# div[data-baseweb="select"]{
#     border-radius:10px;
# }

# /* Keep clear (×) icon visible */
# div[data-baseweb="select"] svg{
#     fill:#444 !important;
# }

# /* ---------- IMAGE ---------- */

# img{
#     border-radius:20px;
#     border:5px solid white;
#     box-shadow:0 15px 30px rgba(0,0,0,.25);
# }

# /* ---------- KPI CARD ---------- */

# .kpi-card{

#     background:linear-gradient(135deg,#ffffff,#f4fff6);

#     border-radius:18px;

#     padding:25px;

#     text-align:center;

#     border-left:8px solid #27AE60;

#     box-shadow:0 10px 25px rgba(0,0,0,.12);

#     transition:0.35s;

# }

# .kpi-card:hover{

#     transform:translateY(-8px);

#     box-shadow:0 18px 35px rgba(39,174,96,.35);

# }

# .kpi-icon{

#     font-size:36px;

# }

# .kpi-title{

#     margin-top:10px;

#     font-size:18px;

#     color:#555;

#     font-weight:600;

# }

# .kpi-value{

#     margin-top:8px;

#     font-size:34px;

#     color:#0B3C2D;

#     font-weight:800;

# }

# /* ---------- SCROLLBAR ---------- */

# ::-webkit-scrollbar{
#     width:8px;
# }

# ::-webkit-scrollbar-thumb{
#     background:#2ECC71;
#     border-radius:20px;
# }

# </style>
# """, unsafe_allow_html=True)
# with st.sidebar:
#     opt=option_menu(menu_title='Menu',options=['🏠 Home','📄 Dataset','🧹 Preprocessing','📊 Visualizations','ℹ About'])
#     st.markdown('---')
#     st.subheader('🔍 Filters')
#     league=st.multiselect('Select league 🌍',options=df['league_name'].dropna().unique())
#     club=st.multiselect('Select club 🏟',options=df['club_name'].dropna().unique())
#     filtered=df.copy()
#     if league:
#         filtered=filtered[filtered['league_name'].isin(league)]# use filtered term from now onwards
#     if club:
#         filtered=filtered[filtered['club_name'].isin(club)]


# # Home page
# if opt=='🏠 Home':
#     st.markdown("""
# <div style="text-align:center; padding:15px;">

# <h1 style="
# color:#0B3C2D;
# font-size:52px;
# font-weight:800;
# margin-bottom:10px;
# text-shadow:2px 2px 8px rgba(0,0,0,0.15);
# ">
# ⚽ FC26 Player Analytics Dashboard
# </h1>

# <p style="
# font-size:20px;
# color:#555;
# font-style:italic;
# margin-top:0;
# ">
# Explore player performance, market value, club statistics,
# league comparisons, and transfer insights using interactive visualizations.
# </p>

# </div>
# """, unsafe_allow_html=True)

#     st.image(
#             r"C:\Users\ASUS\FootballPlayerAnalyticsProject\Streamlit2\football-stadium-inside-at-night-with-lights-post-production-free-photo.jpg",   # Replace with your image path
#             use_container_width=True)
#     # KPI Cards
#     players=filtered['short_name'].shape[0]
#     leagues=filtered['league_name'].nunique()
#     clubs=filtered['club_name'].nunique()
#     avg_value=filtered['value_eur'].mean()
#     avg_overall = filtered["overall"].mean()
#     avg_potential = filtered["potential"].mean()
#     total_wages = filtered["wage_eur"].sum()

#     # ===================== KPI CARDS =====================

#     st.markdown("<br>", unsafe_allow_html=True)

# # ---------- First Row ----------
#     col1, col2, col3, col4 = st.columns(4)

#     with col1:
#         st.markdown(f"""
#     <div class="kpi-card">
#         <div class="kpi-icon">👤</div>
#         <div class="kpi-title">Total Players</div>
#         <div class="kpi-value">{players:,}</div>
#     </div>
#     """, unsafe_allow_html=True)

#     with col2:
#         st.markdown(f"""
#     <div class="kpi-card">
#         <div class="kpi-icon">🌍</div>
#         <div class="kpi-title">Leagues</div>
#         <div class="kpi-value">{leagues}</div>
#     </div>
#     """, unsafe_allow_html=True)

#     with col3:
#         st.markdown(f"""
#     <div class="kpi-card">
#         <div class="kpi-icon">🏟️</div>
#         <div class="kpi-title">Clubs</div>
#         <div class="kpi-value">{clubs}</div>
#     </div>
#     """, unsafe_allow_html=True)

#     with col4:
#         st.markdown(f"""
#     <div class="kpi-card">
#         <div class="kpi-icon">💰</div>
#         <div class="kpi-title">Avg Market Value</div>
#         <div class="kpi-value">€{avg_value/1e6:.2f}M</div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown("<br>", unsafe_allow_html=True)

# # ---------- Second Row ----------
#     col5, col6, col7 = st.columns(3)

#     with col5:
#         st.markdown(f"""
#     <div class="kpi-card">
#         <div class="kpi-icon">⭐</div>
#         <div class="kpi-title">Avg Overall</div>
#         <div class="kpi-value">{avg_overall:.1f}</div>
#     </div>
#     """, unsafe_allow_html=True)

#     with col6:
#         st.markdown(f"""
#     <div class="kpi-card">
#         <div class="kpi-icon">🚀</div>
#         <div class="kpi-title">Avg Potential</div>
#         <div class="kpi-value">{avg_potential:.1f}</div>
#     </div>
#     """, unsafe_allow_html=True)

#     with col7:
#         st.markdown(f"""
#     <div class="kpi-card">
#         <div class="kpi-icon">💵</div>
#         <div class="kpi-title">Total Weekly Wages</div>
#         <div class="kpi-value">€{total_wages/1e9:.2f}B</div>
#     </div>
#     """, unsafe_allow_html=True)



#   # Dataset page
# # streamlit of dataset page
# elif opt=='📄 Dataset':
#     # st.title('📊 Dataset Explorer')
#     # st.text('Explore the complete football player dataset with filtering, summary information, and data preview.')
#     st.markdown("""
# <div style="
# text-align:center;
# padding:10px;
# ">

# <h1 style="
# font-size:45px;
# color:#0B3C2D;
# font-weight:800;
# ">
# 📊 Dataset Explorer
# </h1>

# <p style="
# font-size:20px;
# color:#555;
# font-style:italic;
# ">
# Explore football player records, column information,
# statistical summaries, and filtered data insights.
# </p>

# </div>
# """, unsafe_allow_html=True)
# # Dataset information bar
#     num_rows=filtered.shape[0]
#     num_cols=filtered.shape[1]
#     st.markdown(f"""
# <div class="dataset-info">
#     <span class="dataset-info-item">📋 <strong>Rows:</strong> {num_rows}</span>
#     <span class="dataset-info-item">📑 <strong>Columns:</strong> {num_cols}</span>
#     <span class="dataset-info-item">🌍 <strong>Leagues:</strong> {filtered['league_name'].nunique()}</span>
#     <span class="dataset-info-item">🏟️ <strong>Clubs:</strong> {filtered['club_name'].nunique()}</span>
#     <span class="dataset-info-item">🌎 <strong>Nationalities:</strong> {filtered['nationality_name'].nunique()}</span>
# </div>
# """, unsafe_allow_html=True)
#     # st.write(filtered.columns.tolist())

#     # ---------- Tabs: Data | Columns | Summary ----------
#     tab1, tab2, tab3 = st.tabs(['📂 Data Preview','📋 Column Information','📈 Summary'])
#     # TAB 1: DATA PREVIEW - filtered data means data that you get after applying filters
#     with tab1:
#         col_left,col_right=st.columns([3,1])
#         with col_left:
#             st.subheader('Preview Filtered Data')
#         with col_right:
#             #slider for no. of rows to display
#             n_rows=st.slider('Rows to show',min_value=5,max_value=101,step=20,value=20)
#         # display the first n rows
#         st.dataframe(filtered.head(n_rows),use_container_width=True)
#         #optionally display the last 10 rows
#         with st.expander('Show last 10 rows'):
#             st.dataframe(filtered.tail(10),use_container_width=True)

#         # Download button for the filtered data
#         csv=filtered.to_csv(index=False,encoding='utf-8')
#         st.download_button(
#             label='📥 Download filtered data as csv',
#             data=csv,
#             file_name='FootballPlayerAnalytics_Cleaned.csv',
#             mime='text/csv',
#             use_container_width=True
#         )
#     # TAB 2: COLUMN DETAILS
#     with tab2:
#         # compute missing values and give the column a clear name
#         column_info=pd.DataFrame({
#             'Column Name':filtered.columns,
#             'Data Type':filtered.dtypes.astype(str),
#             'Missing Values':filtered.isna().sum()
#         })
#         st.dataframe(
#         column_info,
#         use_container_width=True,
#         height=400,
#         hide_index=True)

#     # TAB 3: SUMMARY
#     with tab3:
#         st.subheader('Statistical Summary')

#     # Separate numeric and categorical columns
#         num_cols = filtered.select_dtypes(include=['int64','float64']).columns.tolist()
#         cat_cols = filtered.select_dtypes(include=['object','category']).columns.tolist()

#     # Numeric Summary
#         if num_cols:
#             st.markdown('#### 📊 Numeric Columns')

#             st.dataframe(
#                filtered[num_cols].describe(),
#                use_container_width=True
#         )

#     # Categorical Summary
#         if cat_cols:
#            st.markdown('#### 🏷️ Categorical Columns')

#            categorical_cols = [
#             "league_name",
#             "club_name",
#             "nationality_name",
#             "player_positions"
#         ]

#         for col in categorical_cols:
#             if col in filtered.columns:

#                 with st.expander(f"Top values in '{col}'"):

#                     top_values = (
#                         filtered[col]
#                         .dropna()
#                         .value_counts()
#                         .reset_index()
#                         .head(10)
#                     )

#                     top_values.columns = [col, "Player Count"]

#                     st.dataframe(
#                         top_values,
#                         use_container_width=True,
#                         hide_index=True
#                     )

#     # its css
#     st.markdown("""
# <style>

# /* ================= DATASET PAGE ================= */

# /* Dataset Title */
# h1, h2, h3 {
#     color:#0B3C2D;
#     font-weight:800;
# }


# /* Dataset Description */
# .stText {
#     font-size:18px;
#     color:#555;
# }


# /* Dataset Information Cards */
# .dataset-info{
#     display:flex;
#     gap:20px;
#     flex-wrap:wrap;
#     margin:20px 0;
# }


# .dataset-info-item{
#     background:linear-gradient(135deg,#ffffff,#f4fff6);
#     padding:18px 25px;
#     border-radius:15px;
#     font-size:17px;
#     color:#1E293B;
#     font-weight:600;
#     border-left:6px solid #27AE60;
#     box-shadow:0 8px 20px rgba(0,0,0,0.12);
#     transition:0.3s;
# }


# .dataset-info-item:hover{
#     transform:translateY(-5px);
#     box-shadow:0 15px 30px rgba(39,174,96,0.25);
# }



# /* Tabs Styling */

# button[data-baseweb="tab"]{
#     font-size:17px;
#     font-weight:700;
#     color:#0B3C2D;
# }


# button[data-baseweb="tab"]:hover{
#     background:#E8F5E9;
#     border-radius:10px;
# }


# button[aria-selected="true"]{
#     background:#27AE60 !important;
#     color:white !important;
#     border-radius:10px;
# }



# /* Dataframe Styling */

# div[data-testid="stDataFrame"]{
#     border-radius:15px;
#     overflow:hidden;
#     box-shadow:0 8px 20px rgba(0,0,0,0.12);
# }



# /* Download Button */

# .stDownloadButton button{
#     background:#27AE60;
#     color:white;
#     border-radius:12px;
#     font-size:16px;
#     font-weight:700;
#     padding:10px 20px;
#     border:none;
#     transition:0.3s;
# }


# .stDownloadButton button:hover{
#     background:#1E8449;
#     transform:translateY(-3px);
# }



# /* Expander Styling */

# .streamlit-expanderHeader{
#     background:#F1F8E9;
#     border-radius:12px;
#     font-size:17px;
#     font-weight:700;
#     color:#0B3C2D;
# }



# /* Slider Label */

# div[data-testid="stSlider"] label{
#     color:#0B3C2D;
#     font-weight:700;
# }

# </style>
# """, unsafe_allow_html=True)

# # Preprocessing page


# elif opt=='🧹 Preprocessing':
#     st.title('🧹 Data Preprocessing Pipeline')
#     st.markdown("""
# This page demonstrates the preprocessing steps performed on the **FC26 Player Dataset**
# before building the analytics dashboard.

# The preprocessing pipeline improves data quality by handling missing values,
# removing unnecessary columns, correcting data types, and preparing the dataset
# for reliable visualizations and statistical analysis.
# """) 
#     st.subheader('📋 Processing Workflow')
#     steps = [
#     "1.\n📂 Raw\nDataset",
#     "2.\n🔍 Missing\nAnalysis",
#     "3.\n🗑️ Drop\nColumns",
#     "4.\n🧹 Handle\nMissing",
#     "5.\n🧾 Remove\nDuplicates",
#     "6.\n✔️ Validate\nTypes",
#     "7.\n📈 Growth\nFeature",
#     "8.\n✅ Clean\nDataset"
# ]

#     cols = st.columns(len(steps))

#     for col, step in zip(cols, steps):
#         col.markdown(
#         f"""
#         <div style="
#         background:#27AE60;
#         color:white;
#         text-align:center;
#         padding:15px;
#         border-radius:10px;
#         font-weight:bold;">
#         {step.replace(chr(10), '<br>')} 
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )
#     # char(10) is ASCII CODE of \n
    
#     #  Helper function to get missing stats
#     def get_missing_stats(df):
#         missing_df=df.isna().sum().reset_index()
#         missing_df.columns=['Column Name','Missing Count']
#         missing_df['Missing %']=(missing_df['Missing Count']/len(df)*100).round(1)
#         missing_df=missing_df[missing_df['Missing Count']>0]
#         return missing_df
#     # Before Processing
#     st.markdown('<div class="custom-card">', unsafe_allow_html=True)
#     st.subheader('🔍 Dataset Before Processing')
#     col1 , col2 = st.columns([3,1])
#     with col1:
#         # show missing values table
#         missing_before=get_missing_stats(filtered)
#         if not missing_before.empty:
#             st.markdown('**Columns with missing values:**')
#             st.dataframe(
#                 missing_before,
#                 missing_before.style.format({
#                     'Missing Count':'{:,}',
#                     'Missing %':'{:.1f %}'
#                 }),
#                 use_container_width=True,
#                 height=300
#             )
#         else:
#             st.success('✅ No missing values found!')
#     with col2:
#         # Show shape information
#         st.metric("Rows",filtered.shape[0])
#         st.metric('Columns',filtered.shape[1])
#         st.markdown("</div>", unsafe_allow_html=True)

#     # Visualise missing values
#     if not missing_before.empty:
#        st.subheader('📊 Missing Values Before Preprocessing')
#        fig = px.bar(
#     missing_before,
#     x="Column Name",
#     y="Missing Count",
#     color="Missing Count",
#     color_continuous_scale="Viridis",
#     text="Missing Count",
#     # title="📊 Missing Values Before Preprocessing",
#     labels={
#         "Column Name": "Columns",
#         "Missing Count": "Missing Values"
#     },
#     template="plotly_white"
# )

#        fig.update_traces(
#     textposition="outside",
#     marker_line_color="black",
#     marker_line_width=1.2,
#     hovertemplate=
#     "<b>%{x}</b><br>"
#     "Missing Values: %{y}<extra></extra>"
# )

#        fig.update_layout(
#     # title={
#     #     "xanchor": "center",
#     #     "font": dict(size=24, color='black')
#     # },
#     xaxis=dict(
#         title="",
#         tickangle=-30,
#         showgrid=False,
#         tickfont=dict(size=12)
#     ),
#     yaxis=dict(
#         title="Number of Missing Values",
#         showgrid=True,
#         gridcolor="rgba(200,200,200,0.3)"
#     ),
#     coloraxis_showscale=True,
#     plot_bgcolor="white",
#     paper_bgcolor="white",
#     margin=dict(t=70, l=40, r=20, b=100),
#     height=600,
#     width=400,
#     hoverlabel=dict(
#         bgcolor="white",
#         font_size=13,
#         font_family="Arial"
#     )
# )

#     st.plotly_chart(fig, use_container_width=True)
#     st.info(
#     """
# 📌 **Dropped Columns:** `club_jersey_number`, `club_loaned_from`, `club_team_id`,
# `goalkeeping_speed`, `nation_jersey_number`, `nation_position`, `nation_team_id`,
# `player_tags`, `player_traits`, and `work_rate`.

# These features were removed because they contained many missing values, served mainly
# as identifiers, or were not essential for the analyses and visualizations presented
# in this dashboard.
# """
# )    
#     # Perform Cleaning
#     # Use a copy to avoid modifying the original filtered data
#     processed_data=filtered.copy()
#     cols_to_drop=['club_jersey_number','club_loaned_from','club_team_id','goalkeeping_speed','nation_jersey_number','nation_position','nation_team_id','player_tags','player_traits','work_rate']
#     existing_cols=[c for c in cols_to_drop if c in processed_data.columns]
#     processed_data.drop(columns=existing_cols,inplace=True,errors='ignore')

#     rows_before=processed_data.shape[0]
#     processed_data.dropna(inplace=True)
#     rows_after=processed_data.shape[0]
#     processed_data.reset_index(drop=True,inplace=True)


#     #  After Processing
#     st.subheader("✅ After Processing")
#     st.markdown(
#     f"""
#     The preprocessing removed **{len(existing_cols)} columns** and
#     **{rows_before - rows_after:,} rows** containing missing values.

#     **Final Dataset:** **{rows_after:,} rows × {len(existing_cols)} columns**
#     """
# )   

#     col1 , col2, col3 =st.columns(3)
#     with col1:
#             st.metric("Rows After Cleaning", rows_after, delta=rows_after - rows_before, delta_color="inverse")
#     with col2:
#         st.metric("Columns Remaining", processed_data.shape[1])
#     with col3:
#         st.metric("Rows Removed", rows_before - rows_after, delta="-{}".format(rows_before - rows_after))

#     # Show missing values again (should be all zeros)
#     missing_after =get_missing_stats(processed_data)
#     st.markdown("**Missing values after cleaning:**")
#     if missing_after.empty:
#         st.success("🎉 No missing values remaining!")
#     else:
#         st.dataframe(missing_after, use_container_width=True)

#     with st.expander("Preview of Cleaned Data"):
#         st.dataframe(processed_data.head(10), use_container_width=True)

#     # ---------- Download Cleaned Data ----------
#     csv_clean = processed_data.to_csv(index=False).encode('utf-8')
#     st.download_button(
#         label="📥 Download Cleaned Data (CSV)",
#         data=csv_clean,
#         file_name="footballplayeranalytics_cleaned.csv",
#         mime="text/csv",
#         use_container_width=True,
#     )

#     # ---------- Side note: storing cleaned data for other pages ----------
#     # We'll store it in session_state so Visualization can use it directly
#     st.session_state['cleaned_data'] = processed_data
#     st.success(
# """
# 🎉 Data preprocessing completed successfully!

# The cleaned dataset has been saved and is now available
# for all visualization pages.
# """
# )
    
# elif opt == "📊 Visualizations":
#     st.title("📈 Interactive Data Visualization")
#     st.markdown(
#         "Dive into the FC26 Player Analytics Dashboard and explore detailed insights about "
#         "football players worldwide. Visualize player ratings, potential, market values, "
#         "club performances, and skill distributions through interactive data visualizations."
#     )

#     # -----------------------------------------------------
#     # DATA LOADING PIPELINE (SESSION STATE OR FALLBACK)
#     # -----------------------------------------------------
#     if "cleaned_data" in st.session_state:
#         plot_data = st.session_state["cleaned_data"].copy()
#     else:
#         # Fallback: Process raw filtered data on the fly if user skipped Preprocessing tab
#         plot_data = filtered.copy()
#         cols_to_drop = [
#             "club_jersey_number",
#             "club_loaned_from",
#             "club_team_id",
#             "goalkeeping_speed",
#             "nation_jersey_number",
#             "nation_position",
#             "nation_team_id",
#             "player_tags",
#             "player_traits",
#             "work_rate",
#         ]
#         cols_exist = [c for c in cols_to_drop if c in plot_data.columns]
#         plot_data.drop(columns=cols_exist, inplace=True, errors="ignore")
#         plot_data.dropna(inplace=True)
#         plot_data.reset_index(drop=True, inplace=True)

#     if plot_data.empty:
#         st.warning(
#             "No data available after cleaning. Please check your filters or the Preprocessing page."
#         )
#     else:
#         # -----------------------------------------------------
#         # VISUALIZATION TABS DEFINITION
#         # -----------------------------------------------------
#         tab1, tab2, tab3, tab4, tab5 = st.tabs(
#             [
#                 "💰 Market Analytics",
#                 "🏆 League & Club Analysis",
#                 "🏃 Player Profiles",
#                 "🔮 Talent Scouting",
#                 "📊 Performance Correlation",
#             ]
#         )

#         # =====================================================
#         # TAB 1 : EXECUTIVE MARKET & FINANCIAL ANALYTICS
#         # =====================================================
#         with tab1:
#             st.subheader("💰 Executive Market & Financial Analytics")
#             st.markdown(
#                 """
#                 Analyze football's financial landscape through player valuations, 
#                 rating-based market trends, and club wage investments.
#                 """
#             )

#             # -----------------------------------------------------
#             # GRAPH 1 : PLAYER VALUE DISTRIBUTION
#             # -----------------------------------------------------
#             fig1 = px.histogram(
#                 data_frame=plot_data,
#                 x="value_eur",
#                 nbins=12,
#                 template="plotly_white",
#                 color_discrete_sequence=px.colors.qualitative.Set2,
#                 opacity=0.85,
#             )

#             fig1.update_traces(
#                 marker=dict(line=dict(color="black", width=1)),
#                 hovertemplate="<b>Market Value:</b> €%{x:,.0f}<br><b>Players:</b> %{y}<extra></extra>",
#             )

#             fig1.update_layout(
#                 xaxis=dict(
#                     title="Player Market Value (€)",
#                     showgrid=True,
#                     gridcolor="lightgray",
#                     gridwidth=1,
#                     zeroline=False,
#                     tickformat=",",
#                 ),
#                 yaxis=dict(
#                     title="Number of Players",
#                     showgrid=True,
#                     gridcolor="lightgray",
#                     gridwidth=1,
#                     zeroline=False,
#                 ),
#                 width=800,
#                 height=600,
#                 font=dict(family="Arial", size=14, color="#55555E"),
#                 bargap=0.04,
#                 hovermode="x unified",
#                 margin=dict(l=70, r=40, t=80, b=70),
#             )

#             st.plotly_chart(fig1, use_container_width=True)

#             st.info(
#                 """
#                 💡 **Insight:**
                
#                 The football market follows a highly uneven distribution. 
#                 Most players are valued below €5M, while only a small group of 
#                 elite players reach extremely high transfer valuations.
#                 """
#             )

#             # -----------------------------------------------------
#             # GRAPH 2 : OVERALL VS MARKET VALUE
#             # -----------------------------------------------------
#             st.markdown("### 📈 Skill Rating vs Market Value")

#             fig2 = px.scatter(
#                 plot_data,
#                 x="overall",
#                 y="value_eur",
#                 color="age",
#                 template="plotly_white",
#                 color_continuous_scale="Viridis",
#                 opacity=0.75,
#                 hover_data={
#                     "short_name": True,
#                     "club_name": True,
#                     "overall": True,
#                     "value_eur": ":,",
#                     "age": True,
#                 },
#             )

#             fig2.update_traces(
#                 marker=dict(
#                     line=dict(color="white", width=0.5),
#                     symbol="triangle-up",
#                     size=10,
#                 ),
#                 hovertemplate=(
#                     "<b>%{customdata[0]}</b><br>"
#                     + "Club: %{customdata[1]}<br>"
#                     + "Overall Rating: %{x}<br>"
#                     + "Market Value: €%{y:,.0f}<br>"
#                     + "Age: %{marker.color}<extra></extra>"
#                 ),
#             )

#             fig2.update_layout(
#                 xaxis_title="Overall Rating",
#                 yaxis_title="Market Value (€)",
#                 width=900,
#                 height=600,
#                 font=dict(family="Arial", size=14),
#                 margin=dict(l=70, r=40, t=80, b=70),
#                 hovermode="closest",
#                 coloraxis_colorbar=dict(title="Age"),
#             )

#             fig2.update_xaxes(
#                 showgrid=True,
#                 gridcolor="lightgray",
#                 showline=True,
#                 linewidth=1,
#                 linecolor="black",
#             )
#             fig2.update_yaxes(
#                 showgrid=True,
#                 gridcolor="lightgray",
#                 tickformat=",",
#                 showline=True,
#                 linewidth=1,
#                 linecolor="black",
#             )

#             st.plotly_chart(fig2, use_container_width=True)

#             st.info(
#                 """
#                 💡 **Insight:**
                
#                 Market value increases sharply when players cross 
#                 higher overall ratings. Younger high-rated players 
#                 usually receive additional value due to future potential.
#                 """
#             )

#             # -----------------------------------------------------
#             # GRAPH 3 : CLUB WAGES
#             # -----------------------------------------------------
#             st.markdown("### 💰 Top 15 Clubs by Wage Commitment")

#             club_wages = (
#                 plot_data.groupby("club_name")["wage_eur"]
#                 .sum()
#                 .reset_index()
#                 .sort_values(by="wage_eur", ascending=False)
#                 .head(15)
#             )

#             fig3 = px.bar(
#                 club_wages,
#                 x="wage_eur",
#                 y="club_name",
#                 orientation="h",
#                 color="wage_eur",
#                 color_continuous_scale="Viridis",
#                 text="wage_eur",
#                 template="plotly_white",
#             )

#             fig3.update_traces(
#                 texttemplate="€%{text:,.0f}", textposition="outside"
#             )

#             fig3.update_layout(
#                 xaxis_title="Total Wage (€)",
#                 yaxis_title="Club Name",
#                 showlegend=False,
#                 height=600,
#                 width=800,
#                 margin=dict(l=180, r=40, t=80, b=60),
#             )

#             fig3.update_yaxes(
#                 categoryorder="total ascending",
#                 showline=True,
#                 linewidth=1,
#                 linecolor="black",
#             )

#             st.plotly_chart(fig3, use_container_width=True)

#             st.info(
#                 """
#                 💡 **Insight:**
                
#                 Wage spending is concentrated among football's biggest clubs. 
#                 These teams maintain competitive advantage by investing heavily 
#                 in player salaries.
#                 """
#             )

#         # =====================================================
#         # TAB 2 : LEAGUE & CLUB STRUCTURAL EVALUATION
#         # =====================================================
#         with tab2:
#             st.subheader("🏆 League & Club Structural Evaluation")
#             st.markdown(
#                 """
#                 Compare player quality, technical attributes, and financial 
#                 structures across the world's top football leagues.
#                 """
#             )

#             top5 = [
#                 "Premier League",
#                 "La Liga",
#                 "Serie A",
#                 "Bundesliga",
#                 "Ligue 1",
#             ]
#             df_top5 = plot_data[plot_data["league_name"].isin(top5)]

#             # -----------------------------------------------------
#             # GRAPH 4 : TECHNICAL SKILLS ACROSS LEAGUES
#             # -----------------------------------------------------
#             st.markdown(
#                 "### 📈 Average Technical Skills Across Top 5 European Leagues"
#             )

#             skill_avg = (
#                 df_top5.groupby("league_name")[
#                     [
#                         "pace",
#                         "shooting",
#                         "passing",
#                         "dribbling",
#                         "defending",
#                         "physic",
#                     ]
#                 ]
#                 .mean()
#                 .reset_index()
#             )

#             # Wide to long conversion
#             skill_avg = skill_avg.melt(
#                 id_vars="league_name",
#                 var_name="Technical Skill",
#                 value_name="Average Rating",
#             )

#             fig4 = px.bar(
#                 skill_avg,
#                 x="league_name",
#                 y="Average Rating",
#                 barmode="group",
#                 color="Technical Skill",
#                 template="plotly_white",
#                 color_discrete_sequence=px.colors.qualitative.Set3,
#                 text_auto=".1f",
#             )

#             fig4.update_traces(
#                 hovertemplate="<b>%{x}</b><br>Skill: %{fullData.name}<br>Average Rating: %{y:.1f}<extra></extra>",
#                 marker=dict(line=dict(color="black", width=1)),
#                 textposition="outside",
#             )

#             fig4.update_layout(
#                 width=1000,
#                 height=600,
#                 xaxis_title="League",
#                 yaxis_title="Average Technical Rating",
#                 legend_title="Technical Skill",
#                 font=dict(size=14, family="Arial"),
#                 margin=dict(t=80, r=40, l=70, b=70),
#                 bargap=0.1,
#                 bargroupgap=0.03,
#             )

#             fig4.update_xaxes(
#                 showgrid=False, showline=True, linewidth=1, linecolor="black"
#             )
#             fig4.update_yaxes(
#                 showgrid=True,
#                 gridcolor="lightgray",
#                 showline=True,
#                 linewidth=1,
#                 linecolor="black",
#                 range=[0, 100],
#             )

#             st.plotly_chart(fig4, use_container_width=True)

#             st.info(
#                 """
#                 💡 **Insight:**
                
#                 The comparison highlights differences in playing styles across 
#                 major European leagues. Some leagues show stronger attacking 
#                 attributes such as passing and dribbling, while others display 
#                 greater emphasis on physical and defensive qualities.
#                 """
#             )

#             # -----------------------------------------------------
#             # GRAPH 5 : SQUAD RATING VARIANCES
#             # -----------------------------------------------------
#             st.markdown(
#                 "### 📊 Squad Rating Variances within Top 5 European Leagues"
#             )

#             fig5 = px.box(
#                 df_top5,
#                 x="league_name",
#                 y="overall",
#                 color="league_name",
#                 template="plotly_white",
#                 points="outliers",
#                 color_discrete_sequence=px.colors.qualitative.Dark2,
#                 hover_data=["short_name", "club_name", "age", "overall"],
#             )

#             fig5.update_traces(
#                 hovertemplate="<b>%{customdata[0]}</b><br>Club: %{customdata[1]}<br>League: %{x}<br>Overall Rating: %{y}<br>Age: %{customdata[2]}<extra></extra>",
#                 boxmean=True,
#                 whiskerwidth=0.8,
#                 marker=dict(
#                     size=5,
#                     opacity=0.8,
#                     line=dict(color="black", width=0.5),
#                 ),
#             )

#             fig5.update_layout(
#                 xaxis_title="League",
#                 yaxis_title="Overall Player Rating",
#                 font=dict(family="Arial", size=14),
#                 height=600,
#                 width=1000,
#                 legend_title="League",
#                 margin=dict(l=70, r=40, t=80, b=70),
#                 hovermode="closest",
#             )

#             fig5.update_xaxes(
#                 showgrid=False, showline=True, linecolor="black", linewidth=1
#             )
#             fig5.update_yaxes(
#                 showgrid=True,
#                 gridcolor="lightgray",
#                 gridwidth=1,
#                 zeroline=False,
#                 showline=True,
#                 linewidth=1,
#                 linecolor="black",
#                 range=[40, 100],
#             )

#             st.plotly_chart(fig5, use_container_width=True)

#             st.info(
#                 """
#                 💡 **Insight:**
                
#                 The box plot highlights the distribution and consistency of player 
#                 quality across major European leagues. Leagues with higher median 
#                 overall ratings indicate stronger average squads, while wider boxes 
#                 show greater variation in player quality. Outliers represent 
#                 exceptional players whose ratings are significantly above or below 
#                 the league average.
#                 """
#             )

#             # -----------------------------------------------------
#             # GRAPH 6 : LEAGUE FINANCIAL WAGE MIX
#             # -----------------------------------------------------
#             st.markdown("### 💰 League Financial Wage Mix Architecture")

#             df_sum = (
#                 df_top5.groupby(["league_name", "club_name"])["wage_eur"]
#                 .sum()
#                 .reset_index()
#             )

#             # Keep top 10 clubs per league by wage
#             df_sum = (
#                 df_sum.sort_values("wage_eur", ascending=False)
#                 .groupby("league_name")
#                 .head(10)
#             )

#             fig6 = px.treemap(
#                 df_sum,
#                 path=["league_name", "club_name"],
#                 values="wage_eur",
#                 color="wage_eur",
#                 color_continuous_scale="Viridis",
#                 template="plotly_white",
#                 hover_data={"wage_eur": ":,"},
#             )

#             fig6.update_traces(
#                 textinfo="label+value+percent parent",
#                 hovertemplate="<b>%{label}</b><br>Total Wage: €%{value:,.0f}<br>League Share: %{percentParent}<br>Overall Share: %{percentRoot}<extra></extra>",
#                 marker=dict(line=dict(color="white", width=2)),
#             )

#             fig6.update_layout(
#                 width=1100,
#                 height=700,
#                 margin=dict(l=20, r=20, t=80, b=20),
#                 font=dict(family="Arial", size=14),
#                 coloraxis_colorbar=dict(title="Total Wage (€)"),
#             )

#             st.plotly_chart(fig6, use_container_width=True)

#             st.info(
#                 """
#                 💡 **Insight:**

#                 The wage structure is highly concentrated among a small number of 
#                 elite leagues and clubs. Larger segments represent organisations 
#                 with greater financial commitment, highlighting the economic gap 
#                 between football's biggest clubs and the rest of the market.
#                 """
#             )

#         with tab3:
#             # ==============================================================================
# # TAB 3: PLAYER ARCHETYPE & PHYSICAL ATTRIBUTE PROFILING
# # ==============================================================================
#            st.header("Page 3: Player Archetype & Physical Attribute Profiling")

# # ------------------------------------------------------------------------------
# # 7. SPRINT SPEED VS. STRENGTH CORRELATIVE ANALYSIS
# # ------------------------------------------------------------------------------
#            st.markdown("###  Sprint Speed vs. Strength Correlative Analysis")

#            agg_df = (
#            df.groupby(['preferred_foot', 'league_name'])[
#         ['movement_sprint_speed', 'power_strength']
#     ]
#     .mean()
#     .reset_index()
# )

#            fig7 = px.scatter(
#     agg_df,
#     x='movement_sprint_speed',
#     y='power_strength',
#     color='preferred_foot',
#     # title='Average Sprint Speed vs Strength by Preferred Foot',
#     color_discrete_sequence=['#3B528B', '#5DC863'],
#     template='plotly_white',
#     hover_data=['league_name'],
# )

#            fig7.update_traces(
#     marker=dict(
#         size=12, opacity=0.8, line=dict(color='black', width=0.5), symbol='circle'
#     ),
#     hovertemplate='<b>%{customdata[0]}</b><br>'
#     + 'League: %{customdata[0]}<br>'
#     + 'Average Sprint Speed: %{x:.2f}<br>'
#     + 'Average Strength: %{y:.2f}<extra></extra>',
# )

#            fig7.update_layout(
#     # title=dict(
#     #     text='Average Sprint Speed vs Strength by Preferred Foot',
#     #     x=0.5,
#     #     font=dict(size=24),
#     # ),
#     xaxis_title='Average Sprint Speed',
#     yaxis_title='Average Strength',
#     legend_title='Preferred Foot',
#     width=900,
#     height=650,
#     font=dict(family='Arial', size=14),
#     margin=dict(l=70, r=40, t=80, b=70),
# )

#            fig7.update_xaxes(
#     showgrid=True, gridcolor='lightgray', showline=True, linecolor='black'
# )
#            fig7.update_yaxes(
#            showgrid=True, gridcolor='lightgray', showline=True, linecolor='black'
# )

#            st.plotly_chart(fig7, use_container_width=True)

#            st.info("""
# **Analytical Insights:**
# * **Trade-Off Dynamics:** Highlights the inherent physical trade-off between explosive pace (`movement_sprint_speed`) and raw power (`power_strength`) across different league profiles.
# * **Footedness Footprint:** Groups mean physical profiles by preferred foot and league to pinpoint whether left- or right-footed cohorts hold physical advantages in specific tactical ecosystems.
# * **Scouting Archetypes:** Facilitates quick identification of league outliers—pinpointing leagues that prioritize high-tempo athleticism versus those favoring physically dominant players.
# """)


# # ------------------------------------------------------------------------------
# # 8. AGE SPREAD PATTERNS BY DOMINANT FOOT
# # ------------------------------------------------------------------------------
#            st.markdown("###  Age Spread Patterns by Dominant Foot")

#            fig8 = px.histogram(
#     df,
#     x='age',
#     color='preferred_foot',
#     barmode='overlay',
#     nbins=25,
#     opacity=0.85,
#     # title='Age Distribution by Preferred Foot',
#     template='plotly_white',
#     color_discrete_sequence=['#3B528B', '#5EC962'],
#     hover_data=['short_name', 'club_name', 'overall'],
# )

#            fig8.update_traces(
#     hovertemplate='<b>Age:</b> %{x}<br>'
#     + '<b>Players:</b> %{y}<br><extra></extra>',
#     marker=dict(line=dict(color='black', width=1)),
# )

#            fig8.update_layout(
#     # title=dict(
#     #     text='Age Distribution by Preferred Foot', font=dict(size=24), x=0.5
#     # ),
#     xaxis_title='Age (Years)',
#     yaxis_title='Number of Players',
#     legend_title='Preferred Foot',
#     height=600,
#     width=950,
#     font=dict(family='Arial', size=14),
#     margin=dict(l=70, r=40, t=80, b=70),
#     bargap=0.05,
# )

#            fig8.update_xaxes(showgrid=False, showline=True, linecolor='black')
#            fig8.update_yaxes(
#     showgrid=True, gridcolor='lightgray', showline=True, linecolor='black'
# )

#            st.plotly_chart(fig8, use_container_width=True)

#            st.info("""
# **Analytical Insights:**
# * **Demographic Volume:** Shows the volume distribution of right- vs. left-footed players across age brackets, highlighting the scarcity of left-footed assets across all age cohorts.
# * **Career Lifecycle Peak:** Maps player density across early development, prime athletic age (24–28), and veteran phases.
# * **Roster Longevity:** Evaluates whether physical degradation or positional demand shifts the age distribution profile between right- and left-dominant players.
# """)


# # ------------------------------------------------------------------------------
# # 9. PHYSICALITY RATINGS BASED ON PREFERRED FOOT
# # ------------------------------------------------------------------------------
#            st.markdown("###  Physicality Ratings Based on Preferred Foot")

#            fig9 = px.violin(
#     df,
#     x='preferred_foot',
#     y='physic',
#     color='preferred_foot',
#     box=True,
#     color_discrete_sequence=['#3B528B', '#5EC962'],
#     points='outliers',
#     template='plotly_white',
#     # title='Physical Rating Distribution by Preferred Foot',
#     hover_data=['short_name', 'club_name', 'league_name', 'overall', 'age'],
# )

#            fig9.update_traces(
#     meanline_visible=True,
#     hovertemplate='<b>%{customdata[0]}</b><br>'
#     + 'Club: %{customdata[1]}<br>'
#     + 'League: %{customdata[2]}<br>'
#     + 'Overall: %{customdata[3]}<br>'
#     + 'Age: %{customdata[4]}<br>'
#     + 'Physic: %{y}<br>'
#     + 'Preferred Foot: %{x}<extra></extra>',
# )

#            fig9.update_layout(
#     # title=dict(
#     #     text='Physical Rating Distribution by Preferred Foot',
#     #     x=0.5,
#     #     font=dict(size=24, family='Arial'),
#     # ),
#     xaxis_title='Preferred Foot',
#     yaxis_title='Physical Rating',
#     legend_title='Preferred Foot',
#     width=950,
#     height=600,
#     font=dict(family='Arial', size=14),
#     margin=dict(l=70, r=40, t=80, b=70),
# )

#            fig9.update_xaxes(showgrid=False, showline=True, linecolor='black')
#            fig9.update_yaxes(
#     showgrid=True,
#     gridcolor='lightgray',
#     showline=True,
#     linecolor='black',
#     range=[0, 100],
# )

#            st.plotly_chart(fig9, use_container_width=True)

#            st.info("""
# **Analytical Insights:**
# * **Distribution & Density:** Combines Kernel Density Estimation (KDE) with box plot metrics to reveal the underlying probability density of physical ratings (`physic`).
# * **Median & Interquartile Ranges:** Clearly depicts the median physical score, IQR, and full spread across footedness categories to assess baseline parity.
# * **Outlier Detection:** Isolates statistical physical outliers—identifying exceptionally strong or weak players relative to their dominant foot cohort.
# """)


# # ------------------------------------------------------------------------------
# # 10. POSITIONAL HIERARCHIES AND DOMINANT FOOT LAYOUTS
# # ------------------------------------------------------------------------------
#            st.markdown("###  Positional Hierarchies and Dominant Foot Layouts")

#            # 10. Positional Hierarchies and Dominant Foot Layouts-Visually groups player values based on regional leagues and preferred foot combinations to display asset concentrations.
#            # ------------------------------------------------------------------------------
#            # Drop null values in hierarchy columns to prevent Plotly Treemap ValueError
#            treemap_df = df.dropna(subset=['league_name', 'preferred_foot'])

#            fig10 = px.treemap(
#     treemap_df,
#     path=['league_name', 'preferred_foot'],
#     values='value_eur',
#     color='value_eur',
#     color_continuous_scale='Viridis',
#     template='plotly_white',
#     # title='Player Market Value Distribution by League and Preferred Foot',
# )

#            fig10.update_traces(
#     textinfo='label+percent parent',
#     hovertemplate='<b>%{label}</b><br>'
#     + 'Market Value: €%{value:,.0f}<br>'
#     + 'Share in Parent: %{percentParent}<br>'
#     + 'Share Overall: %{percentRoot}<extra></extra>',
# )

#            fig10.update_layout(
#     # title=dict(
#     #     text='Player Market Value Distribution by League and Preferred Foot',
#     #     x=0.5,
#     #     font=dict(size=24),
#     # ),
#     width=950,
#     height=700,
#     margin=dict(l=20, r=20, t=80, b=20),
#     font=dict(family='Arial', size=14),
#     coloraxis_colorbar=dict(title='Market Value (€)'),
# )

#            st.plotly_chart(fig10, use_container_width=True)

#            st.info("""
# **Analytical Insights:**
# * **Asset Concentration:** Visually partitions total market value (`value_eur`) hierarchically across leagues and footedness categories.
# * **Proportional Value Share:** Calculates exact parent and root percentage shares, revealing which leagues hold the largest concentration of financial capital tied to left- or right-footed talent.
# * **Macro-Financial Mapping:** Offers an intuitive top-down view for technical directors to evaluate global market valuation density across regional competitions.
# """)
#     with tab4:
#            # Feature engineering for growth
#            df['growth'] = df['potential'] - df['overall']

# # ==============================================================================
# # TAB 4: TALENT SCOUTING & HIDDEN GEM DISCOVERY
# # ==============================================================================

#            st.header("🔍 Talent Scouting & Hidden Gem Discovery")

#            st.markdown(
#     """
#     Discover high-potential players by analyzing growth potential, market value,
#     and wage efficiency. These visualizations help identify emerging talent and
#     undervalued players who could become valuable future investments.
#     """
# )

# # ------------------------------------------------------------------------------
# # 11. AGE VS. FUTURE CAPACITY GROWTH WINDOW
# # ------------------------------------------------------------------------------
#            st.markdown("### ⭐ Age vs. Future Capacity Growth Window")

#            fig11 = px.scatter(
#     df,
#     x='age',
#     y='growth',
#     color='overall',
#     template='plotly_white',
#     # title='Age vs. Future Capacity Growth Window',
#     color_continuous_scale='Viridis',
#     hover_name='short_name',
#     hover_data=['club_name', 'league_name', 'potential', 'overall', 'growth'],
# )

#            fig11.update_traces(
#     marker=dict(
#         size=9, line=dict(color='black', width=0.5), symbol='square'
#     ),
#     hovertemplate='<b>%{hovertext}</b><br>'
#     + 'Age: %{x} years<br>'
#     + 'Growth: %{y}<br>'
#     + 'Overall: %{marker.color}<br>'
#     + '<extra></extra>',
# )

#            fig11.update_layout(
#     # title=dict(
#     #     text='Age vs. Future Capacity Growth Window',
#     #     x=0.5,
#     #     font=dict(size=24, family='Arial'),
#     # ),
#     xaxis_title='Age (Years)',
#     yaxis_title='Growth (Potential - Overall)',
#     coloraxis_colorbar=dict(title='Overall Rating'),
#     width=800,
#     height=650,
#     font=dict(family='Arial', size=14),
#     margin=dict(l=70, r=40, t=80, b=70),
# )

#            fig11.update_xaxes(showgrid=False, showline=True, linecolor='black')
#            fig11.update_yaxes(
#     showgrid=True, gridcolor='lightgray', showline=True, linecolor='black'
# )

#            st.plotly_chart(fig11, use_container_width=True)

#            st.info("""
# **Analytical Insights:**
# * **Development Window Identification:** Highlights the inverse relationship between age and growth capacity, demonstrating that high-growth windows (`potential - overall`) peak primarily in players under 22 years old.
# * **Outlier Scouting Targets:** Isolates high-growth prospects who already possess solid baseline `overall` ratings, signaling immediate first-team utility combined with high ceiling value.
# * **Roster Planning Strategy:** Informs talent acquisition timing by revealing the precise age thresholds where development potential plateaus or decays.
# """)


# # ------------------------------------------------------------------------------
# # 12. MOST EFFICIENT VALUE GENERATION ECOSYSTEMS (TOP 15 COUNTRIES)
# # ------------------------------------------------------------------------------
#            st.markdown(
#     "###  Most Efficient Value Generation Ecosystems (Top 15 Countries)"
# )

#            country_potential = (
#     df.groupby('nationality_name')['potential']
#     .mean()
#     .reset_index()
#     .sort_values(by='potential', ascending=False)
#     .head(15)
# )

#            fig12 = px.bar(
#     country_potential,
#     x='nationality_name',
#     y='potential',
#     color='potential',
#     color_continuous_scale='Viridis',
#     # title='Top 15 Countries by Average Player Potential',
#     template='plotly_white',
#     text_auto='.1f',
# )

#            fig12.update_traces(
#     marker=dict(line=dict(color='black', width=0.8)),
#     hovertemplate='<b>%{x}</b><br>' + 'Average Potential: %{y:.1f}<extra></extra>',
# )

#            fig12.update_layout(
#     # title=dict(
#     #     text='Top 15 Countries by Average Player Potential',
#     #     x=0.5,
#     #     font=dict(size=24),
#     # ),
#     xaxis_title='Nationality',
#     yaxis_title='Average Potential Rating',
#     width=900,
#     height=650,
#     font=dict(family='Arial', size=14),
#     margin=dict(l=70, r=40, t=80, b=120),
#     coloraxis_colorbar=dict(title='Potential'),
# )

#            fig12.update_xaxes(showgrid=False, showline=True, linecolor='black')
#            fig12.update_yaxes(
#     showgrid=True,
#     gridcolor='lightgray',
#     showline=True,
#     linecolor='black',
#     range=[0, 100],
# )

#            st.plotly_chart(fig12, use_container_width=True)

#            st.info("""
# **Analytical Insights:**
# * **Geographic Talent Hotspots:** Ranks the top 15 national cohorts by average potential rating, mapping regional talent density for global scouting networks.
# * **National Ecosystem Quality:** Reveals which national development programs consistently produce higher baseline ceilings for emerging talent.
# * **Strategic Sourcing:** Provides technical directors with macro-level guidance on prioritizing scouting budgets across international markets.
# """)


# # ------------------------------------------------------------------------------
# # 13. WAGE EFFICIENCY SCATTER MATRIX
# # ------------------------------------------------------------------------------
#            st.markdown("###  Wage Efficiency Scatter Matrix")

#            fig13 = px.scatter(
#     df,
#     x='wage_eur',
#     y='potential',
#     color='overall',
#     hover_name='short_name',
#     template='plotly_white',
#     hover_data=['club_name', 'league_name', 'age', 'overall'],
#     # title='Wage Efficiency Scatter Matrix',
#     color_continuous_scale='Viridis',
# )

#            fig13.update_traces(
#     marker=dict(
#         size=7, line=dict(color='black', width=0.5), symbol='square'
#     ),
#     hovertemplate='<b>%{hovertext}</b><br>'
#     + 'Weekly Wage: €%{x:,.0f}<br>'
#     + 'Potential: %{y}<br>'
#     + 'Club: %{customdata[0]}<br>'
#     + 'League: %{customdata[1]}<br>'
#     + 'Age: %{customdata[2]}<br>'
#     + 'Overall: %{customdata[3]}<extra></extra>',
# )

#            fig13.update_layout(
#     # title=dict(
#     #     text='Wage Efficiency Scatter Matrix',
#     #     font=dict(size=24, family='Arial'),
#     #     x=0.5,
#     # ),
#     height=600,
#     width=800,
#     xaxis_title='Weekly Wage (€)',
#     yaxis_title='Potential Rating',
#     coloraxis_colorbar=dict(title='Overall'),
#     font=dict(family='Arial', size=14),
#     margin=dict(l=70, r=40, t=80, b=70),
# )

#            fig13.update_xaxes(showgrid=False, showline=True, linecolor='black')
#            fig13.update_yaxes(
#     showgrid=True,
#     gridcolor='lightgray',
#     showline=True,
#     linecolor='black',
#     range=[0, 100],
# )

#            st.plotly_chart(fig13, use_container_width=True)

#            st.info("""
# **Analytical Insights:**
# * **Financial Arbitrage Scouting:** Pinpoints low-wage players positioned high on the y-axis (`potential`), identifying high-value targets operating below market compensation.
# * **Wage Structure Benchmarking:** Evaluates payroll efficiency by contrasting weekly compensation against player output and future upside.
# * **Undervalued Asset Discovery:** Isolates players in lower-tier leagues or clubs who deliver top-tier potential without requiring premium wage expenditure.
# """)
#            # ==============================================================================
# # TAB 5: CORE ATTRIBUTE & PERFORMANCE CORRELATION
# # ==============================================================================
#     with tab5:
#            st.header("Page 5: Core Attribute & Performance Correlation")

# # ------------------------------------------------------------------------------
# # 14. PERFORMANCE ATTRIBUTE INTERDEPENDENCY HEATMAP
# # ------------------------------------------------------------------------------
#            st.markdown("### 14. Performance Attribute Interdependency Heatmap")

#            performance = df[['pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic']]
#            corr = performance.corr()

#            fig14 = px.imshow(
#     corr,
#     template='plotly_white',
#     color_continuous_scale='Viridis',
#     # title="Performance Attribute Interdependency Heatmap",
#     text_auto='.2f',
#     aspect='auto',
#     labels=dict(color='Correlation')
# )

#            fig14.update_traces(
#     hovertemplate="<b>%{x}</b> vs <b>%{y}</b><br>Correlation: %{z:.2f}<extra></extra>"
# )

#            fig14.update_layout(
#     # title=dict(
#     #     text="Performance Attribute Interdependency Heatmap",
#     #     x=0.5,
#     #     font=dict(size=24, family="Arial")
#     # ),
#     width=800,
#     height=600,
#     font=dict(family="Arial", size=14),
#     margin=dict(l=70, r=40, t=80, b=70)
# )

#            fig14.update_xaxes(
#     title="Performance Attributes",
#     showgrid=False,
#     showline=True,
#     linecolor="black"
# )

#            fig14.update_yaxes(
#     title="Performance Attributes",
#     showgrid=False,
#     showline=True,
#     linecolor="black"
# )

#            st.plotly_chart(fig14, use_container_width=True)

#            st.info("""
# **Analytical Insights:**
# * **Technical Synergy Mapping:** Reveals strong positive correlations between technical categories such as passing, dribbling, and shooting, indicating shared developmental profiles among attacking playmakers.
# * **Defensive vs. Offensive Trade-Offs:** Highlights inverse or neutral correlations between defensive capability (`defending`) and attacking skills (`shooting`/`pace`), illustrating positional specialization in tactical setups.
# * **Physical Foundation Correlation:** Demonstrates how physical rating (`physic`) acts as an anchor for defensive metrics, providing tactical direction when scouting resilient ball-winners.
# """)


# # ------------------------------------------------------------------------------
# # 15. TOTAL WAGE VS. TOTAL MARKET VALUE PROGRESSION
# # ------------------------------------------------------------------------------
#            st.markdown("### 15. Average Market Value by Overall Rating")

#            data = df.groupby('overall')['value_eur'].mean().reset_index()

#            fig15 = px.line(
#     data,
#     x="overall",
#     y="value_eur",
#     markers=True,
#     template="plotly_white",
#     color_discrete_sequence=["#3B528B"],
#     # title="Average Market Value by Overall Rating"
# )

#            fig15.update_traces(
#     line=dict(width=4),
#     marker=dict(
#         size=8,
#         symbol="circle",
#         color="#3B528B",
#         line=dict(color="black", width=1)
#     ),
#     hovertemplate="<b>Overall Rating:</b> %{x}<br><b>Average Market Value:</b> €%{y:,.0f}<extra></extra>"
# )

#            fig15.update_layout(
#     # title=dict(
#     #     text="Average Market Value by Overall Rating",
#     #     x=0.5,
#     #     font=dict(size=24, family="Arial")
#     # ),
#     xaxis_title="Overall Rating",
#     yaxis_title="Average Market Value (€)",
#     width=800,
#     height=600,
#     font=dict(family="Arial", size=14),
#     margin=dict(l=70, r=40, t=80, b=70)
# )

#            fig15.update_xaxes(
#     showgrid=False,
#     showline=True,
#     linecolor="black"
# )

#            fig15.update_yaxes(
#     showgrid=True,
#     gridcolor="lightgray",
#     showline=True,
#     linecolor="black",
#     tickprefix="€"
# )

#            st.plotly_chart(fig15, use_container_width=True)

#            st.info("""
# **Analytical Insights:**
# * **Exponential Valuation Curve:** Demonstrates an exponential curve in player valuations once an overall rating crosses key elite thresholds (e.g., 80+ rating), showing how premium talent commands non-linear valuation jumps.
# * **Baseline Value Parity:** Shows relatively flat valuation increments across mid-to-lower tier overall ratings, helping club executives benchmark standard player pricing.
# * **Elite Talent Premium:** Highlights the steep financial premium required to acquire world-class players compared to standard squad options.
# """)
