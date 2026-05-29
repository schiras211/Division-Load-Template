import streamlit as st

st.set_page_config(
    page_title="Dallas Wrightsoft Guide",
    layout="wide"
)

# ---------------- STYLE ---------------- #

st.markdown("""
<style>

[data-testid="stSidebar"] {
    background-color: #EEF3F8;
    padding-top: 25px;
}

.main-header {
    background-color: #003E7E;
    color: white;
    padding: 28px 32px;
    margin: -60px -80px 25px -80px;
}

.main-header h1 {
    font-size: 38px;
    margin: 0;
}

.main-header p {
    font-size: 18px;
    margin-top: 8px;
}

.step-card {
    background: white;
    border-radius: 18px;
    box-shadow: 0 4px 16px rgba(0,0,0,.15);
    overflow: hidden;
    border: 1px solid #D0D7DE;
}

.step-header {
    background: #003E7E;
    color: white;
    padding: 18px 24px;
    font-size: 28px;
    font-weight: bold;
}

.step-body {
    padding: 24px;
}

.bullet-box {
    background: #EEF3F8;
    border: 1px solid #BFD0DF;
    padding: 16px 18px;
    border-radius: 10px;
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 16px;
}

.reference-box {
    background: #F7FAFC;
    border: 2px dashed #8AA6C1;
    border-radius: 16px;
    min-height: 340px;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    color: #475569;
    font-size: 20px;
    padding: 25px;
}

.nav-button {
    background-color: #003E7E;
    color: white;
    border-radius: 10px;
    padding: 14px 28px;
    font-size: 18px;
    font-weight: bold;
    text-align: center;
}

.top-button {
    background-color: #FFD62E;
    color: black;
    border-radius: 10px;
    padding: 12px 22px;
    font-weight: bold;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.markdown("""
<div class="main-header">
    <h1>Dallas Wrightsoft Load Completion Guide</h1>
    <p>Interactive Navigation Guide</p>
</div>
""", unsafe_allow_html=True)

# ---------------- DATA ---------------- #

steps = {
    "STEP 1 - Start Job & Template": [
        "Select correct Wrightsoft template.",
        "Use Dallas matchups.",
        "Add selected elevation in Project Information notes.",
        "Use 360 CFM per ton.",
        "Keep humidity set to 30/50.",
        "Zone all 2-story homes."
    ],

    "STEP 2 - Weather Setup": [
        "Select correct weather location from plan/spec sheet.",
        "Verify county using Energy Star data.",
        "Adjust dry bulb temperatures to match county.",
        "Select correct weather station under Bin City Data.",
        "Foam insulation goes under Roof/Ceiling.",
        "Non-foam uses standard ceiling setup.",
        "Test to see if this works",
        "Hello",
        "Ok then"
    ],

    "STEP 3 - Room Load Rules": [
        "No blinds on loads.",
        "Merge WIC rooms unless master WIC has a window.",
        "Foyers should be their own room.",
        "Merge pantry with kitchen unless heat load exists.",
        "Use R-3 exterior board insulation when specified.",
        "Place rooms accurately and align to walls."
    ],

    "STEP 4 - CAD Cleanup": [
        "Clean electrical items as much as possible.",
        "Leave lights and fans for accurate boot placement.",
        "Place all options into CAD for future design accuracy.",
        "Use one CAD file with correct elevation and options.",
        "Only set specific rooms to ambient when needed."
    ],

    "STEP 5 - Equipment Matchups": [
        "Select correct equipment matchups.",
        "For Lennox, increase blower power 500–750 first.",
        "Do not exceed 750 blower adjustment.",
        "Use worst-case windows on base load.",
        "GAS static = .70.",
        "HP static = .50."
    ],

    "STEP 6 - Equipment Sizing": [
        "100–104% total may stay same tonnage.",
        "105% may be acceptable if sensible is good.",
        "Avoid over 122–124% when upsizing.",
        "Standard homes: 600–700 sqft/ton.",
        "Foam homes: 700–800 sqft/ton.",
        "Verify sensible before upsizing."
    ]
}

# ---------------- SIDEBAR ---------------- #

st.sidebar.markdown("## Table of Contents")

step_names = list(steps.keys())

if "step_index" not in st.session_state:
    st.session_state.step_index = 0

selected_step = st.sidebar.radio(
    "Select Step",
    step_names,
    index=st.session_state.step_index,
    label_visibility="collapsed"
)

st.session_state.step_index = step_names.index(selected_step)

# ---------------- MAIN LAYOUT ---------------- #

left, right = st.columns([1.2, 1])

with left:

    st.markdown(f"""
    <div class="step-card">
        <div class="step-header">{selected_step}</div>
        <div class="step-body">
    """, unsafe_allow_html=True)

    for item in steps[selected_step]:
        st.markdown(f"""
        <div class="bullet-box">
            • {item}
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)

with right:

    if selected_step == "STEP 1 - Start Job & Template":

        st.image(
            "screenshots/step1.png",
            use_container_width=True
        )

    elif selected_step == "STEP 2 - Weather Setup":

        st.image(
            "screenshots/step2.png",
            use_container_width=True
        )

    elif selected_step == "STEP 3 - Room Load Rules":

        st.image(
            "screenshots/step3.png",
            use_container_width=True
        )

    elif selected_step == "STEP 4 - CAD Cleanup":

        st.image(
            "screenshots/step4.png",
            use_container_width=True
        )

    elif selected_step == "STEP 5 - Equipment Matchups":

        st.image(
            "screenshots/step5.png",
            use_container_width=True
        )

    elif selected_step == "STEP 6 - Equipment Sizing":

        st.image(
            "screenshots/step6.png",
            use_container_width=True
        )

# ---------------- BUTTONS ---------------- #

st.markdown("<br>", unsafe_allow_html=True)

btn1, btn2, btn3 = st.columns([1, 5, 1])

with btn1:
    if st.button("Top"):
        st.session_state.step_index = 0
        st.rerun()

with btn3:
    if st.button("Next →"):
        if st.session_state.step_index < len(step_names) - 1:
            st.session_state.step_index += 1
            st.rerun()
