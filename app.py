import streamlit as st
import re
import pandas as pd
from datetime import datetime

from graph import graph
from memory import init_db, save_record, get_history

init_db()

st.set_page_config(
    page_title="AI Fake News Detector", 
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)
#5G networks cause coronavirus in humans
#5G causes COVID-19
#Drinking hot water kills coronavirus
st.markdown("""
<style>
    /* Main container styling */
    .main-header {
        background: linear-gradient(135deg, 0%, 100%);
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        text-align: center;
    }
    
    .main-header h1 {
        color: white;
        margin: 0;
        font-size: 2.5rem;
    }
    
    .main-header p {
        color: rgba(255,255,255,0.9);
        margin-top: 0.5rem;
    }
    
    /* Card styling */
    .result-card {
        background: white;
        color: #111827;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 1.5rem;
        border-left: 5px solid;
        transition: transform 0.3s ease;
    }
    
    .result-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(0,0,0,0.15);
    }
    
    .verdict-true {
        border-left-color: #10b981;
        background: linear-gradient(to right, #f0fdf4, white);
    }
    
    .verdict-fake {
        border-left-color: #ef4444;
        background: linear-gradient(to right, #fef2f2, white);
    }
    
    .verdict-mixed {
        border-left-color: #f59e0b;
        background: linear-gradient(to right, #fffbeb, white);
    }
    
    /* Metric cards */
    .metric-card {
        background: linear-gradient(135deg, #667ea 0%, #7ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        color: white;
    }
    
    .metric-card h3 {
        margin: 0;
        font-size: 2rem;
        font-weight: bold;
    }
    
    .metric-card p {
        margin: 0.5rem 0 0 0;
        opacity: 0.9;
    }
    
    /* History card */
    .history-card {
        background: #f8f9fa;
            color: #111827;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border: 1px solid #e5e7eb;
    }
    
    .history-card:hover {
        background: #f3f4f6;
            color: #111827;
        border-color: #667eea;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #6eea 0%, #76a2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        border-radius: 10px;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
    }
    
    /* Text area styling */
    .stTextArea > div > div > textarea {
        border-radius: 10px;
        border: 2px solid #e5e7eb;
        font-size: 1rem;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 2px rgba(102, 126, 234, 0.1);
    }
    
    /* Progress bar styling */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #10b981, #f59e0b, #ef4444);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: #f8f9fa;
    }
    
    /* Badge styling */
    .badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-right: 0.5rem;
    }
    
    .badge-high {
        background: #10b981;
        color: white;
    }
    
    .badge-medium {
        background: #f59e0b;
        color: white;
    }
    
    .badge-low {
        background: #ef4444;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar with info and stats
with st.sidebar:
    st.markdown("### About")
    st.info(
        "This AI-powered tool analyzes news claims and detects potential "
        "fake news using advanced language models and fact-checking techniques."
    )
    
    st.markdown("###  Statistics")
    history_data = get_history()
    if history_data:
        total_checks = len(history_data)
        avg_confidence = sum([h[3] for h in history_data]) / total_checks
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Checks", total_checks)
        with col2:
            st.metric("Avg Confidence", f"{avg_confidence:.1f}%")
    
    st.markdown("###  Tips")
    st.markdown("""
    - Enter the complete news claim
    - Include sources if available
    - Check multiple claims for better accuracy
    """)
    
    st.markdown("###  Features")
    st.markdown("""
    1. Real-time analysis  
    2. Evidence-based verification  
    3. Confidence scoring  
    4. History tracking  
    """)

# Main header
st.markdown("""
<div class="main-header">
    <h1> AI Fake News Detector</h1>
    <p>Advanced AI-powered fact checking and fake news detection system</p>
</div>
""", unsafe_allow_html=True)

# Main content
col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    st.markdown("### 📝 Enter News Claim")
    claim = st.text_area(
        "", 
        placeholder="Example: 'Scientists discover that drinking coffee cures cancer...'",
        height=120,
        label_visibility="collapsed"
    )

with col2:
    st.markdown("### ⚡ Quick Actions")
    if st.button("🔍 Analyze Claim", use_container_width=True):
        if claim.strip():
            with st.spinner("Analyzing claim..."):
                result = graph.invoke({"claim": claim})
                
                # Store in session state for display
                st.session_state['current_result'] = result
                st.session_state['current_claim'] = claim
                st.rerun()
        else:
            st.warning("Please enter a claim to analyze")

with col3:
    st.markdown("### 🧹 Options")
    if st.button("🗑️ Clear Input", use_container_width=True):
        claim = ""
        st.rerun()

# Display results if available
if 'current_result' in st.session_state:
    result = st.session_state['current_result']
    claim = st.session_state['current_claim']
    
    # Extract confidence
    match = re.search(r"(\d{1,3})", result["verdict"])
    confidence = int(match.group(1)) if match else 70
    
    # Determine verdict class
    verdict_lower = result["verdict"].lower()
    if "true" in verdict_lower or "real" in verdict_lower:
        verdict_class = "verdict-true"
        verdict_icon = "✅"
        verdict_text = "REAL / TRUE"
    elif "fake" in verdict_lower or "false" in verdict_lower:
        verdict_class = "verdict-fake"
        verdict_icon = "❌"
        verdict_text = "FAKE / FALSE"
    else:
        verdict_class = "verdict-mixed"
        verdict_icon = "⚠️"
        verdict_text = "MIXED / UNCLEAR"
    
    # Metrics row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3>{confidence}%</h3>
            <p>Confidence Score</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card" style="background: linear-gradient(135deg, #3b82f6, #8b5cf6);">
            <h3>{len(str(result['evidence']).split())}</h3>
            <p>Evidence Points</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card" style="background: linear-gradient(135deg, #06b6d4, #3b82f6);">
            <h3>{len(str(result['analysis']).split())}</h3>
            <p>Analysis Length</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-card" style="background: linear-gradient(135deg, #ec4899, #8b5cf6);">
            <h3>{datetime.now().strftime('%H:%M')}</h3>
            <p>Analyzed At</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Results cards
    st.markdown(f"""
    <div class="result-card {verdict_class}">
        <h3>⚖️ Verdict {verdict_icon}</h3>
        <p style="font-size: 1.2rem; font-weight: bold; margin-top: 0.5rem;">{result['verdict']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="result-card" style="border-left-color: #3b82f6;">
        <h3>📊 Analysis</h3>
        <p>{str(result['analysis'])}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="result-card" style="border-left-color: #8b5cf6;">
        <h3>🔍 Evidence</h3>
        <p>{str(result['evidence'])}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Confidence progress
    st.markdown("### 🎯 Confidence Meter")
    col1, col2 = st.columns([3, 1])
    with col1:
        progress_color = (
            "#10b981" if confidence >= 70 
            else "#f59e0b" if confidence >= 40 
            else "#ef4444"
        )
        st.progress(confidence / 100)
    
    with col2:
        badge_class = (
            "badge-high" if confidence >= 70 
            else "badge-medium" if confidence >= 40 
            else "badge-low"
        )
        st.markdown(f'<span class="badge {badge_class}">{confidence}% Confidence</span>', 
                   unsafe_allow_html=True)
    
    # Save to memory
    save_record(claim, result["verdict"], confidence)
    st.success("✅ Analysis saved to memory!")

# History section
st.markdown("---")
st.markdown("### 📜 Analysis History")

history = get_history()

if history:
    # Convert to DataFrame for better display
    df_history = pd.DataFrame(
    history,
    columns=["ID", "Claim", "Verdict", "Confidence"]
)
    
    # Add color coding to verdicts in DataFrame display
    def color_verdict(val):
        if "true" in str(val).lower() or "real" in str(val).lower():
            return 'color: #10b981'
        elif "fake" in str(val).lower():
            return 'color: #ef4444'
        return 'color: #f59e0b'
    
    # Display as styled dataframe
    st.dataframe(
        df_history[["Claim", "Verdict", "Confidence"]],
        use_container_width=True,
        height=300,
        column_config={
            "Claim": st.column_config.TextColumn("Claim", width="large"),
            "Verdict": st.column_config.TextColumn("Verdict", width="medium"),
            "Confidence": st.column_config.ProgressColumn(
                "Confidence",
                format="%d%%",
                min_value=0,
                max_value=100,
            ),
        },
        hide_index=True,
    )
    
    # Show last 3 entries in cards
    st.markdown("#### 🕒 Recent Checks")
    cols = st.columns(3)
    for idx, h in enumerate(history[-3:]):
        with cols[idx]:
            confidence_class = (
                "badge-high" if h[3] >= 70 
                else "badge-medium" if h[3] >= 40 
                else "badge-low"
            )
            st.markdown(f"""
            <div class="history-card">
                <p style="font-size: 0.9rem; margin-bottom: 0.5rem;">{h[1][:100]}...</p>
                <p style="margin: 0.25rem 0;"><strong>Verdict:</strong> {h[2][:50]}</p>
                <span class="badge {confidence_class}">{h[3]}% Confidence</span>
            </div>
            """, unsafe_allow_html=True)
else:
    st.info("No analysis history yet. Start by analyzing a news claim!")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #6b7280; font-size: 0.85rem;'>"
    "Powered by Advanced AI • Real-time Fact Checking • Evidence-based Analysis"
    "</p>",
    unsafe_allow_html=True
)  