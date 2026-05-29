import streamlit as st
from pathlib import Path
import pandas as pd

st.set_page_config(
    page_title="Wrightsoft Division Guides",
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
    margin-bottom: 25px;
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

.note-box {
    background: #FFF200;
    color: black;
    padding: 12px 16px;
    border-radius: 8px;
    font-weight: 800;
    margin-bottom: 14px;
    border: 1px solid #D9C900;
}

.warning-box {
    background: #FFE5E5;
    color: #7A0000;
    padding: 12px 16px;
    border-radius: 8px;
    font-weight: 700;
    margin: 12px 0;
    border: 1px solid #CC0000;
}

.example-box {
    background: #EAF4FF;
    color: #003E7E;
    padding: 12px 16px;
    border-radius: 8px;
    font-weight: 600;
    margin: 12px 0;
    border: 1px solid #9CC9F5;
}

.rule-box {
    background: #F2F7F2;
    color: #1F5B2E;
    padding: 12px 16px;
    border-radius: 8px;
    font-weight: 600;
    margin: 12px 0;
    border: 1px solid #B7D8B7;
}

.stExpander {
    background-color: #EEF3F8;
    border: 1px solid #BFD0DF;
    border-radius: 10px;
    margin-bottom: 12px;
}

.stExpander summary {
    font-size: 18px;
    font-weight: 700;
}

img {
    border-radius: 10px;
    border: 1px solid #D0D7DE;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HELPERS ---------------- #

def show_images(images):
    for img in images:
        if Path(img).exists():
            st.image(img, use_container_width=True)
        else:
            st.info(f"Screenshot not uploaded yet: {img}")

def bullet_list(items):
    for item in items:
        st.write("• " + item)

# ---------------- HEADER ---------------- #

st.markdown("""
<div class="main-header">
    <h1>Wrightsoft Load Completion Guides</h1>
    <p>Division-Specific Interactive Workflow</p>
</div>
""", unsafe_allow_html=True)

# ---------------- DALLAS DATA ---------------- #

dallas_steps = {
    "STEP 1 - CAD Cleanup": {
        "items": [
            {
                "title": "Clean electrical but leave lights and fans",
                "rule": "Clean as much electrical information as possible, but leave lights and fans.",
                "details": [
                    "Lights and fans help with boot placement.",
                    "Leaving these items makes the design more realistic.",
                    "Clean unnecessary electrical clutter so the drawing is readable."
                ],
                "example": "Leave lights and fans visible so boot placement can be accurate.",
                "images": ["screenshots/Dallas/CAD Conversion.png"]
            },
            {
                "title": "Add options into CAD",
                "rule": "If the project has options, put the options in CAD.",
                "details": [
                    "Options are needed for future design.",
                    "Options also help keep the load accurate.",
                    "Do not leave options out if they affect the selected load or future design."
                ],
                "images": ["screenshots/Dallas/CAD Conversion 2.png"]
            },
            {
                "title": "Do not create scattered separate files",
                "rule": "It should be one file with the right elevation and options all in one.",
                "details": [
                    "Do not create multiple disconnected files for the same load.",
                    "The CAD should include the correct elevation and needed options in one file."
                ],
                "warning": "DO NOT DO THIS AT ALL: Do not make multiple scattered files.",
                "images": ["screenshots/Dallas/do_not_do_this.png"]
            },
            {
                "title": "Only change specific rooms to ambient",
                "rule": "If the load has a lip, do not change the whole floor to ambient.",
                "details": [
                    "Only change the specific rooms that need to be ambient.",
                    "Do not apply ambient settings across the entire floor unless required."
                ],
                "images": []
            }
        ]
    },

    "STEP 2 - Project Setup & Notes": {
        "items": [
            {
                "title": "Contact Dallas POC if help is needed",
                "rule": "If you need an example or help, contact the Dallas POC. Do not overwork the file.",
                "details": [
                    "Use the POC when something is unclear.",
                    "Dallas Division POC: Alberto Hernandez."
                ],
                "warning": "PLEASE DO NOT OVERWORK THE FILE.",
                "images": []
            },
            {
                "title": "Use Dallas matchups",
                "rule": "Use Dallas-specific equipment matchups when selecting equipment.",
                "details": [
                    "Confirm the selected matchup before finalizing equipment.",
                    "Dallas matchups should guide final equipment selection."
                ],
                "images": []
            },
            {
                "title": "Add selected elevation to Project Information notes",
                "rule": "In Project Information notes, add which elevation was selected.",
                "details": [
                    "This helps Sales know which elevation was used.",
                    "This helps anyone reviewing the file understand the load basis."
                ],
                "example": "Load completed using Elevation B with selected options shown on plan.",
                "images": []
            },
            {
                "title": "Lennox blower power before adding BTUH",
                "rule": "When adding BTUs to Lennox loads, increase blower power first.",
                "details": [
                    "Increase blower power between 500-750 first.",
                    "If more capacity is still needed, then add BTUH.",
                    "Do not exceed 750."
                ],
                "images": []
            },
            {
                "title": "Use 360 CFM per ton",
                "rule": "Dallas loads should use 360 CFM per ton.",
                "details": ["Verify airflow before final equipment selection."],
                "images": []
            },
            {
                "title": "Keep humidity at 30/50",
                "rule": "Keep the standard Dallas humidity setup at 30/50.",
                "details": ["Do not change unless directed by project-specific requirements."],
                "images": []
            },
            {
                "title": "Zone all 2-story homes",
                "rule": "All 2-story homes should be zoned.",
                "details": ["Confirm zoning before finalizing the load."],
                "images": []
            }
        ]
    },

    "STEP 3 - Weather, County & Ceiling Setup": {
        "items": [
            {
                "title": "Select correct weather location",
                "rule": "Select the correct weather location if listed on the plan or spec sheet.",
                "details": [
                    "Do not assume the closest major city is correct.",
                    "Use the weather location shown on the plan or spec sheet."
                ],
                "images": ["screenshots/Dallas/weather_location.png"]
            },
            {
                "title": "Verify county using Energy Star",
                "rule": "Verify county on Energy Star when needed.",
                "details": [
                    "Adjust annual cooling and heating dry bulb temperatures to match the specified county.",
                    "Under Bin City Data, select the correct weather station."
                ],
                "images": ["screenshots/Dallas/energy_star_county.png"]
            },
            {
                "title": "Foam ceiling insulation setup",
                "rule": "Foam custom ceiling insulation should be placed under Roof/Ceiling.",
                "details": [
                    "Do not treat foam ceiling projects the same as non-foam projects."
                ],
                "images": ["screenshots/Dallas/foam_ceiling.png"]
            },
            {
                "title": "Non-foam ceiling setup",
                "rule": "If it is non-foam ceiling, leave it as shown in standard setup.",
                "details": [
                    "Only use foam configuration when foam is specified."
                ],
                "images": ["screenshots/Dallas/non_foam_ceiling.png"]
            }
        ]
    },

    "STEP 4 - Options & In-Lieu Rooms": {
        "items": [
            {
                "title": "Use parentheses for option rooms",
                "rule": "Place the optional room as the title and the option in parentheses.",
                "details": [
                    "This keeps the base room and option room tied together."
                ],
                "example": "Flex(Study)",
                "images": []
            },
            {
                "title": "Apply worst-case BTUH to in-lieu rooms",
                "rule": "Use the BTUH from the worst-case option room.",
                "details": [
                    "If Study is in lieu of Flex and Study is worse, use Study BTUH.",
                    "If Study windows are worse, include those windows."
                ],
                "images": []
            },
            {
                "title": "Add selected elevation floor into CAD",
                "rule": "If the elevation chosen has a floor, add it to CAD.",
                "details": [
                    "The drawing needs to reflect the selected elevation accurately."
                ],
                "images": []
            },
            {
                "title": "Match base tonnage for options when possible",
                "rule": "Try to match the tonnage that was on the base.",
                "details": [
                    "If not possible, notify the POC."
                ],
                "images": []
            }
        ]
    },

    "STEP 5 - Room Load Rules": {
        "items": [
            {
                "title": "No blinds on loads",
                "rule": "Do not apply blinds to Dallas loads.",
                "details": ["Leave blinds off the load calculation."],
                "images": []
            },
            {
                "title": "R-3 exterior board insulation",
                "rule": "If R-3 sheathing is on the specs, select exterior board insulation R-3.",
                "details": ["This applies when specs show Sheathing 3/8 with R-3."],
                "images": []
            },
            {
                "title": "WIC merge rule",
                "rule": "All WIC rooms should be merged unless the Master WIC has a window.",
                "details": [
                    "If Master WIC has a window, it becomes its own room.",
                    "Do not apply the 10 ft exposure rule to WIC rooms."
                ],
                "warning": "NO 10 FT EXPOSURE RULE FOR WIC ROOMS.",
                "images": []
            },
            {
                "title": "Foyers should be separate rooms",
                "rule": "Foyers should be their own room, even if very short.",
                "details": ["Do not automatically merge foyer areas into nearby rooms."],
                "images": []
            },
            {
                "title": "Pantry merge rule",
                "rule": "Pantry should merge with kitchen unless it has a window or heat load.",
                "details": [
                    "Heat load examples: refrigerator, freezer, stove, or similar appliance."
                ],
                "images": []
            }
        ]
    },

    "STEP 6 - Open To Below": {
        "items": [
            {
                "title": "Set OTB only where required",
                "rule": "Set open to below in required areas only.",
                "details": [
                    "Preferred OTB area is under 100 sq ft.",
                    "Verify square footage is within range."
                ],
                "images": []
            },
            {
                "title": "Remove OTB before equipment selection",
                "rule": "After OTB is used for square footage, remove it before selecting equipment.",
                "details": [
                    "Set upstairs and downstairs areas properly.",
                    "OTB is temporary for square footage setup."
                ],
                "images": []
            },
            {
                "title": "Boot placement for OTB",
                "rule": "Use OTB for square footage, then turn it back to regular room.",
                "details": [
                    "There should be 1 boot up and 1 boot down."
                ],
                "images": []
            }
        ]
    },

    "STEP 7 - Blower Door Settings": {
        "items": [
            {
                "title": "Beazer blower door setup",
                "rule": "Use Beazer infiltration setup when applicable.",
                "details": [
                    "Select fireplace first.",
                    "Wind shielding: 3.",
                    "Select Single @ Test Pressure.",
                    "ACH: 1.5.",
                    "Test pressure difference: 50 Pascals."
                ],
                "images": []
            },
            {
                "title": "D.R. Horton East blower door setup",
                "rule": "Use D.R. Horton East setup depending on specs.",
                "details": [
                    "Select fireplace first.",
                    "Wind shielding: 3.",
                    "Select Single @ Test Pressure.",
                    "ACH: 3.",
                    "Test pressure difference: 50 Pascals."
                ],
                "images": []
            }
        ]
    },

    "STEP 8 - Energy Star": {
        "items": [
            {
                "title": "Location and control setup",
                "rule": "Use location by county and proper control location.",
                "details": [
                    "Location: by county.",
                    "Control Location: Attic/Mech."
                ],
                "images": []
            },
            {
                "title": "Fresh air and humidity settings",
                "rule": "Use Dallas Energy Star fresh air and humidity settings.",
                "details": [
                    "Fresh air settings: 20/60.",
                    "Relative humidity: 30/50.",
                    "Beazer Estar: 60/60."
                ],
                "images": []
            },
            {
                "title": "Fin-180P airflow range",
                "rule": "Fin-180P cycle range should be between 130 CFM and 180 CFM.",
                "details": [
                    "Run Time Per Cycle is the only number you can change.",
                    "Adjust it to stay within required vent airflow range."
                ],
                "images": ["screenshots/Dallas/energy_star_fin180p.png"]
            }
        ]
    },

    "STEP 9 - Equipment Matchups, Airflow & Special Conditions": {
        "items": [
            {
                "title": "Select correct equipment matchups",
                "rule": "Select the correct Dallas matchups when placing equipment.",
                "details": ["Confirm equipment is matched correctly before finalizing."],
                "images": []
            },
            {
                "title": "Static pressure settings",
                "rule": "Use correct static pressure on equipment selection screen.",
                "details": [
                    "Gas static pressure: .70",
                    "Heat pump static pressure: .50"
                ],
                "images": []
            },
            {
                "title": "Lennox documentation requirement",
                "rule": "For Lennox, save Word document showing supporting equipment math.",
                "details": [
                    "Include math.",
                    "Include expanded ratings.",
                    "Include manufacturer numbers."
                ],
                "images": []
            }
        ]
    },

    "STEP 10 - Equipment Sizing": {
        "items": [
            {
                "title": "100%-104% total capacity rule",
                "rule": "When unit is 100%-104% total, sometimes 105%, attempt to go up 1/2 ton.",
                "details": [
                    "After going up 1/2 ton, add BTUs to fit at 115%."
                ],
                "images": []
            },
            {
                "title": "Do not upsize if it pushes too high",
                "rule": "If upsizing causes total to go above 122%-124%, do not upsize.",
                "details": [
                    "If you have to add a lot of BTUH, it is usually not worth it."
                ],
                "images": []
            },
            {
                "title": "Use sq ft per ton as secondary guidance",
                "rule": "Use square feet per ton as a rule of thumb, not a standard.",
                "details": [
                    "Standard homes: 600-700 sq ft per ton.",
                    "Foam homes: 700-800 sq ft per ton."
                ],
                "images": []
            },
            {
                "title": "105% total example",
                "rule": "If load gives 105% total, usually do not upgrade if next ton requires too much BTUH.",
                "example": "If load has 105% total and 98% sensible, do not upgrade tonnage.",
                "details": ["Leave it how it is unless POC directs otherwise."],
                "images": []
            }
        ]
    },

    "STEP 11 - Internal Gains": {
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
            ["Add for Room with Refrigerator / Freezer", "Min 600 / Max 1200"]
        ],
        "notes": [
            "Use Dallas internal gain table when entering room gains.",
            "Rooms with refrigerators or freezers require additional internal gain."
        ]
    },

    "STEP 12 - Save & Handoff": {
        "items": [
            {
                "title": "Save the load",
                "rule": "Save the load before final handoff.",
                "details": ["Do not hand off without saving."],
                "images": []
            },
            {
                "title": "POC completes PDF portion",
                "rule": "The POC will complete the PDF portion.",
                "details": ["Estimator completes the load first."],
                "images": []
            }
        ]
    }
}

# ---------------- NEW DIVISION TEMPLATES ---------------- #

dayton_steps = {
    "STEP 1 - CAD Cleanup": {
        "items": [
            {
                "title": "Dayton CAD cleanup rule",
                "rule": "Add Dayton-specific CAD cleanup rule here.",
                "details": [
                    "Add Dayton-specific details here."
                ],
                "images": ["screenshots/Dayton/example.png"]
            }
        ]
    },
    "STEP 2 - Project Setup & Notes": {
        "items": [
            {
                "title": "Dayton project setup rule",
                "rule": "Add Dayton-specific project setup rule here.",
                "details": [
                    "Add Dayton-specific details here."
                ],
                "images": []
            }
        ]
    }
}

austin_steps = {
    "STEP 1 - CAD Cleanup": {
        "items": [
            {
                "title": "Austin CAD cleanup rule",
                "rule": "Add Austin-specific CAD cleanup rule here.",
                "details": [
                    "Add Austin-specific details here."
                ],
                "images": ["screenshots/Austin/example.png"]
            }
        ]
    }
}

charlotte_steps = {
    "STEP 1 - CAD Cleanup": {
        "items": [
            {
                "title": "Charlotte CAD cleanup rule",
                "rule": "Add Charlotte-specific CAD cleanup rule here.",
                "details": [
                    "Add Charlotte-specific details here."
                ],
                "images": ["screenshots/Charlotte/example.png"]
            }
        ]
    }
}

# ---------------- DIVISION GUIDE STORAGE ---------------- #

division_guides = {
    "Dallas": dallas_steps,
    "Dayton": dayton_steps,
    "Austin": austin_steps,
    "Charlotte": charlotte_steps
}

# ---------------- SIDEBAR ---------------- #

st.sidebar.markdown("## Division")

selected_division = st.sidebar.selectbox(
    "Select Division",
    list(division_guides.keys())
)

steps = division_guides[selected_division]

st.sidebar.markdown("## Table of Contents")

step_names = list(steps.keys())

if "step_index" not in st.session_state:
    st.session_state.step_index = 0

if st.session_state.step_index >= len(step_names):
    st.session_state.step_index = 0

selected_step = st.sidebar.radio(
    "Select Step",
    step_names,
    index=st.session_state.step_index,
    label_visibility="collapsed"
)

st.session_state.step_index = step_names.index(selected_step)

# ---------------- MAIN LAYOUT ---------------- #

left, right = st.columns([1.35, .9])

with left:
    st.markdown(f"""
    <div class="step-card">
        <div class="step-header">{selected_division} | {selected_step}</div>
        <div class="step-body">
    """, unsafe_allow_html=True)

    current_step = steps[selected_step]

    if selected_division == "Dallas" and selected_step == "STEP 2 - Project Setup & Notes":
        st.markdown("""
        <div class="note-box">
            IF NEED EXAMPLE OR HELP CONTACT POC. PLEASE DO NOT OVERWORK.
        </div>
        """, unsafe_allow_html=True)

    if "items" in current_step:
        for item in current_step["items"]:
            with st.expander("• " + item["title"]):

                if item.get("rule"):
                    st.markdown(f"""
                    <div class="rule-box">
                        <strong>Rule:</strong> {item["rule"]}
                    </div>
                    """, unsafe_allow_html=True)

                if item.get("details"):
                    st.markdown("### Details")
                    bullet_list(item["details"])

                if item.get("example"):
                    st.markdown(f"""
                    <div class="example-box">
                        <strong>Example:</strong> {item["example"]}
                    </div>
                    """, unsafe_allow_html=True)

                if item.get("warning"):
                    st.markdown(f"""
                    <div class="warning-box">
                        <strong>Warning:</strong> {item["warning"]}
                    </div>
                    """, unsafe_allow_html=True)

                show_images(item.get("images", []))

    if "table" in current_step:
        st.markdown("### Internal Gains Table")

        df = pd.DataFrame(
            current_step["table"],
            columns=["Room Type", "Internal Gains"]
        )

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
            height=500
        )

        st.markdown("### Notes")
        bullet_list(current_step.get("notes", []))

    st.markdown("</div></div>", unsafe_allow_html=True)

with right:
    st.markdown("## Instructions")

    st.info(
        "Select a division from the dropdown, then click a step. Photos only appear inside the clickable dropdown sections."
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
