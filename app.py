import streamlit as st
from pathlib import Path

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
    padding: 13px 16px;
    border-radius: 10px;
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 12px;
}

.note-box {
    background: #FFF200;
    color: black;
    padding: 12px 16px;
    border-radius: 8px;
    font-weight: 800;
    margin-bottom: 14px;
    border: 1px solid #D9C900;
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
    "STEP 1 - Project Setup & Notes": {
        "bullets": [
            "If an example or clarification is needed, contact the Dallas POC. Do not overwork the file.",
            "Use Dallas matchups.",
            "In Project Information notes, add the selected elevation so Sales knows which elevation was used.",
            "When adding BTUs to Lennox loads, increase blower power between 500–750 first. Add more BTUs only if still needed.",
            "Use 360 CFM per ton.",
            "Select the correct template.",
            "Keep humidity set to 30/50.",
            "Zone all 2-story homes."
        ]
    },

    "STEP 2 - Weather, County & Ceiling Setup": {
        "bullets": [
            "Select the correct weather location for every project when listed on the plan or spec sheet.",
            "Verify the county using the Energy Star website when required.",
            "Adjust annual cooling and heating dry bulb temperatures to match the specified county.",
            "Under Bin City Data, select the correct weather station.",
            "For foam custom ceiling insulation, place the configuration under Roof/Ceiling.",
            "For non-foam ceiling insulation, leave the standard ceiling setup as shown."
        ]
    },

    "STEP 3 - Options & In-Lieu Rooms": {
        "bullets": [
            "When placing options on a load, use the optional room as the title and place the option in parentheses.",
            "Example: If the base has a Flex room and the option is Study, label the room Flex(Study).",
            "Apply the Study BTUH to the Flex room if Study is the worst-case in-lieu option.",
            "If the Study windows are worse than the Flex room windows, include those windows in the load.",
            "If the selected elevation has a floor, add it to CAD so the drawing reflects accuracy.",
            "If there is an option, try to match the tonnage from the base. If not possible, notify the POC."
        ]
    },

    "STEP 4 - Room Load Rules": {
        "bullets": [
            "No blinds on loads.",
            "Sheathing 3/8: if R-3 sheathing is on the specs, select exterior board insulation R-3.",
            "Merge all WIC rooms unless the master WIC has a window; then the WIC should be its own room.",
            "Do not use the 10 ft exposure rule for WIC rooms.",
            "Make foyers their own room, even if they are very short.",
            "Always merge pantry with kitchen unless it has a window or heat load such as a fridge, stove, or similar appliance.",
            "Place rooms as accurately as possible and line them up to walls unless additional square footage is needed."
        ]
    },

    "STEP 5 - CAD Cleanup": {
        "bullets": [
            "Clean as much electrical information as possible.",
            "Leave lights and fans visible so boot placement can be accurate.",
            "Boot placement should be realistic so the HVAC design reflects the actual plan.",
            "If options exist, place the options in CAD because they are needed for future design and load accuracy.",
            "Do not create separate scattered files.",
            "Use one CAD file with the correct elevation and all options included.",
            "If the load has a lip, do not change the whole floor to ambient; only change the specific rooms needed."
        ]
    },

    "STEP 6 - Equipment Matchups & Airflow": {
        "bullets": [
            "Select the correct matchups when placing equipment.",
            "For Lennox, remember blower power first. If BTUH must be added, increase blower power 500–750 before adding BTUH to the load.",
            "Do not exceed 750 for blower power adjustment.",
            "If spiral cases and OTB are present, line up the spiral case and OTB accurately with the plan.",
            "Merge CFMs for outdoor air when there are two systems.",
            "Worst-case window placement: bay windows and box windows should be placed on the base load.",
            "For in-lieu rooms, put the in-lieu room in parentheses and use the worst-case BTUH for that room.",
            "If the in-lieu room has more windows, add those windows to the base load unless the options are separated.",
            "If an R-value is not listed, use a custom R-value. Contact the POC if help is needed.",
            "Equipment static pressure: GAS = .70.",
            "Equipment static pressure: HP = .50.",
            "For Lennox, save the Word document showing the math, expanded ratings, and manufacturer numbers."
        ]
    },

    "STEP 7 - Internal Gains": {
        "table": [
            ["Bedroom", "1 person"],
            ["Owner Suite", "2 people + Min 500 / Max 1000"],
            ["Great Room / Family", "Min 900 / Max 1800"],
            ["Kitchen < 3 Large Appliances", "Min 1200 / Max 2400"],
            ["Kitchen > 3 Large Appliances", "Min 2000 / Max 4000"],
            ["Bar", "Min 600 / Max 1200"],
            ["Utility / Laundry", "Min 500 / Max 1000"],
            ["Media / Theater", "Min 1200 / Max 2400"],
            ["Loft / Game / Bonus", "Min 900 / Max 1800"],
            ["Study / Library / Office", "Min 600 / Max 1200"],
            ["Exercise", "Min 600 / Max 1200"],
            ["Room with Refrigerator / Freezer", "Add Min 600 / Max 1200"]
        ]
    },

    "STEP 8 - Equipment Sizing": {
        "bullets": [
            "When a unit is at 100%–104% total, and sometimes 105%, attempt to go up 1/2 ton and add BTUs to fit at 115%.",
            "If total is 100%, usually upgrade to the next ton, especially on Lennox systems.",
            "If the system gives 105% total, and upsizing causes total to exceed 122%–124% or requires a lot of added BTUH, do not upsize.",
            "If upsizing requires a lot of added BTUH, it is usually not worth upgrading at 104%–105%.",
            "When deciding tonnage based on percentage, also consider square feet per ton.",
            "Standard homes: 600–700 sq ft per ton.",
            "Foam homes: 700–800 sq ft per ton.",
            "These are rules of thumb, not standards.",
            "If a load gives 105% total and 98% sensible, do not upgrade the tonnage; leave the tonnage as-is.",
            "A 105% total / 98% sensible condition is a strong example of when to keep the current tonnage."
        ]
    },

    "STEP 9 - Open To Below": {
        "bullets": [
            "Set open to below in required areas and verify that the square footage is within range.",
            "Preferred OTB area is under 100 sq ft.",
            "If square footage is needed, bump the walls out slightly on all floors.",
            "Afterward, remove open to below and set what is upstairs and downstairs in their proper areas before selecting equipment.",
            "Use OTB for square footage only, then turn it back to a regular room.",
            "A boot will be placed on that OTB area: 1 up and 1 down."
        ]
    },

    "STEP 10 - Blower Door Settings": {
        "bullets": [
            "Beazer: select the fireplace first, then start blower door setup.",
            "Beazer wind shielding: 3.",
            "Beazer: select Single @ Test Pressure.",
            "Beazer ACH: 1.5.",
            "Beazer test pressure difference: 50 Pascals.",
            "D.R. Horton East: settings depend on specs.",
            "D.R. Horton East: select the fireplace first, then start blower door setup.",
            "D.R. Horton East wind shielding: 3.",
            "D.R. Horton East: select Single @ Test Pressure.",
            "D.R. Horton East ACH: 3.",
            "D.R. Horton East test pressure difference: 50 Pascals.",
            "For additional help, reference the walkthrough document."
        ]
    },

    "STEP 11 - Energy Star": {
        "bullets": [
            "Use location by county.",
            "Control Location: Attic/Mech.",
            "Fresh Air Settings: 20/60.",
            "Relative Humidity: 30/50.",
            "Beazer Estar: 60/60.",
            "Fin-180P: cycle range should be 130 CFM–180 CFM, rounded to the nearest value.",
            "Run Time Per Cycle is the only number that can be changed to stay within the required vent airflow range."
        ]
    },

    "STEP 12 - Save & Handoff": {
        "bullets": [
            "Save the load.",
            "POC will complete the PDF portion.",
            "The POC will update this guide as more information becomes available.",
            "If questions remain, contact the Dallas Division POC.",
            "Dallas Division POC: Alberto Hernandez."
        ]
    }
}

# ---------------- SCREENSHOTS ---------------- #

image_map = {
    "STEP 1 - Project Setup & Notes": [
        "screenshots/step1.png"
    ],
    "STEP 2 - Weather, County & Ceiling Setup": [
        "screenshots/step2.png"
    ],
    "STEP 3 - Options & In-Lieu Rooms": [
        "screenshots/step3.png"
    ],
    "STEP 4 - Room Load Rules": [
        "screenshots/step4.png"
    ],
    "STEP 5 - CAD Cleanup": [
        "screenshots/CAD Conversion.png",
        "screenshots/CAD Conversion 2.png"
    ],
    "STEP 6 - Equipment Matchups & Airflow": [
        "screenshots/step6.png"
    ],
    "STEP 7 - Internal Gains": [
        "screenshots/internal_gains.png"
    ],
    "STEP 8 - Equipment Sizing": [
        "screenshots/equipment_sizing.png"
    ],
    "STEP 9 - Open To Below": [
        "screenshots/open_to_below.png"
    ],
    "STEP 10 - Blower Door Settings": [
        "screenshots/blower_door_beazer.png",
        "screenshots/blower_door_dr_horton.png"
    ],
    "STEP 11 - Energy Star": [
        "screenshots/energy_star.png"
    ],
    "STEP 12 - Save & Handoff": [
        "screenshots/save_handoff.png"
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

    if selected_step == "STEP 1 - Project Setup & Notes":
        st.markdown("""
        <div class="note-box">
            IF NEED EXAMPLE OR HELP CONTACT POC. PLEASE DO NOT OVERWORK.
        </div>
        """, unsafe_allow_html=True)

    current_step = steps[selected_step]

    if "bullets" in current_step:
        for item in current_step["bullets"]:
            st.markdown(f"""
            <div class="bullet-box">
                • {item}
            </div>
            """, unsafe_allow_html=True)

    if "table" in current_step:
        st.dataframe(
            {
                "Room Type": [row[0] for row in current_step["table"]],
                "Internal Gains": [row[1] for row in current_step["table"]]
            },
            use_container_width=True,
            hide_index=True
        )

    st.markdown("</div></div>", unsafe_allow_html=True)

with right:
    st.markdown("## Screenshot / Reference Area")

    images = image_map.get(selected_step, [])

    if len(images) > 0:
        for img in images:
            if Path(img).exists():
                st.image(
                    img,
                    use_container_width=True
                )
            else:
                st.info(f"Screenshot not uploaded yet: {img}")
    else:
        st.info("No screenshots assigned to this step.")

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

