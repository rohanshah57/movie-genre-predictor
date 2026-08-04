import time

import streamlit as st

st.set_page_config(
    page_title="Aura // Minimalist Hub",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Custom CSS for Sleek Aesthetics
st.markdown("""
    <style>
    /* Remove padding around main container */
    .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
        max-width: 1100px;
    }
    
    /* Make metric cards pop slightly */
    [data-testid="stMetricSimpleValue"] {
        font-family: 'Courier New', monospace;
        font-weight: bold;
    }
    
    /* Smooth button transitions */
    .stButton>button {
        border-radius: 20px;
        padding: 0.5rem 2rem;
        transition: all 0.3s ease;
    }
    
    /* Subtitle styling */
    .hero-subtitle {
        font-size: 1.2rem;
        color: #888888;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_index=True)

# 3. Sidebar (Minimal Settings)
with st.sidebar:
    st.title("Settings")
    st.caption("Customize your view")
    theme_mode = st.toggle("Enable Premium Node Layout", value=True)
    st.divider()
    st.info("System Status: Operational")

# 4. Hero Section
st.title("✨ Project Aura")
st.markdown("<p class='hero-subtitle'>A hyper-minimal workspace designed for clarity, data composition, and deep work.</p>", unsafe_allow_html=True)
st.divider()

# 5. Core Layout: Grid Matrix
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Network Pulse", value="98.4 ms", delta="-12.1 ms")
    with st.expander("View Routing Data"):
        st.caption("Active nodes routing through US-East edge tunnels.")

with col2:
    st.metric(label="Storage Index", value="41.2 GB", delta="2.4 GB", delta_color="inverse")
    with st.expander("Storage Optimization"):
        st.caption("System cache cleared 4 hours ago.")

with col3:
    st.metric(label="API Gateway Load", value="14.2%", delta="Optimal")
    with st.expander("Thread Diagnostics"):
        st.caption("Asynchronous pools running with 0 errors.")

st.subheader("Live Operational Matrix")

# 6. Interactive Placeholder Tabs
tab_analytics, tab_logs, tab_actions = st.tabs(["📊 Analytics", "📄 Activity Logs", "🛠️ Quick Operations"])

with tab_analytics:
    # A perfectly styled built-in chart
    chart_data = {
        "efficiency": [72, 74, 78, 81, 85, 88, 91, 94, 96, 98],
        "latency": [90, 85, 70, 64, 61, 50, 40, 31, 20, 12]
    }
    st.line_chart(chart_data, height=250)
    st.caption("System efficiency optimization scale plotted over 24-hour cycle runs.")

with tab_logs:
    st.code("""
[2026-08-04 11:53:21] INFO: Aura kernel sequence initiated.
[2026-08-04 11:53:22] SUCCESS: Handshake established with remote node cluster.
[2026-08-04 11:53:25] WARNING: Aesthetic levels exceeding standard thresholds.
    """, language="bash")

with tab_actions:
    st.write("Trigger micro-interactions below to test interface reactive behavior.")
    
    col_btn1, col_btn2 = st.columns([1, 4])
    with col_btn1:
        if st.button("Refresh Grid", type="primary"):
            with st.spinner("Reindexing environment..."):
                time.sleep(1.5)
            st.toast("Grid environment fully synchronized!", icon="⚡")
            
    with col_btn2:
        if st.button("Simulate System Burst"):
            st.balloons()

