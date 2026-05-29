import streamlit as st
from pathlib import Path
import pandas as pd

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

# ---------------- HELPER FUNCTIONS ---------------- #

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
    <h1>Dallas Wrightsoft Load Completion Guide</h1>
    <p>Interactive Dallas Division POC Workflow</p>
</div>
""", unsafe_allow_html=True)

# ---------------- DATA ---------------- #

steps = {
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
                "images": ["screenshots/CAD Conversion.png"]
            },
            {
                "title": "Add options into CAD",
                "rule": "If the project has options, put the options in CAD.",
                "details": [
                    "Options are needed for future design.",
                    "Options also help keep the load accurate.",
                    "Do not leave options out if they affect the selected load or future design."
                ],
                "images": ["screenshots/CAD Conversion 2.png"]
            },
            {
                "title": "Do not create scattered separate files",
                "rule": "It should be one file with the right elevation and options all in one.",
                "details": [
                    "Do not create multiple disconnected files for the same load.",
                    "The CAD should include the correct elevation and needed options in one file.",
                    "This keeps future design work cleaner and more accurate."
                ],
                "warning": "DO NOT DO THIS AT ALL: Do not make multiple scattered files when one complete file is required.",
                "images": ["screenshots/do_not_do_this.png"]
            },
            {
                "title": "Only change specific rooms to ambient",
                "rule": "If the load has a lip, do not change the whole floor to ambient.",
                "details": [
                    "Only change the specific rooms that need to be ambient.",
                    "Do not apply ambient settings across the entire floor unless required."
                ],
                "warning": "Do not change the whole floor to ambient. Only adjust the specific rooms needed.",
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
                    "Do not guess if the Dallas-specific setup is not obvious.",
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
                    "Do not use another division’s matchup logic unless specifically directed.",
                    "Dallas matchups should guide the final equipment selection."
                ],
                "images": []
            },
            {
                "title": "Add selected elevation to Project Information notes",
                "rule": "In Project Information notes, add which elevation was selected.",
                "details": [
                    "This helps the salesperson know which elevation was used for the load.",
                    "This also helps anyone reviewing the file understand the load basis.",
                    "Use clear wording so Sales and Design can quickly verify the elevation."
                ],
                "example": "Example note: Load completed using Elevation B with selected options shown on plan.",
                "images": []
            },
            {
                "title": "Lennox blower power before adding BTUH",
                "rule": "When adding BTUs to Lennox loads, increase blower power first.",
                "details": [
                    "Increase blower power between 500-750 first.",
                    "If more capacity is still needed after that, then add BTUH to the load.",
                    "Do not exceed the 500-750 blower power adjustment range."
                ],
                "warning": "Max blower power adjustment should be 500-750. Do not go beyond that.",
                "images": []
            },
            {
                "title": "Use 360 CFM per ton",
                "rule": "Dallas loads should use 360 CFM per ton.",
                "details": [
                    "Use this airflow rule during setup.",
                    "Verify airflow before final equipment selection."
                ],
                "images": []
            },
            {
                "title": "Select the correct template",
                "rule": "Start every project using the correct Wrightsoft template.",
                "details": [
                    "Template selection affects the entire load setup.",
                    "Verify the correct Dallas template before entering rooms, options, equipment, and weather data."
                ],
                "images": []
            },
            {
                "title": "Keep humidity at 30/50",
                "rule": "Do not change humidity settings unless directed by project-specific requirements.",
                "details": [
                    "Keep the standard Dallas humidity setup at 30/50.",
                    "Energy Star may have additional fresh air or humidity requirements, but the standard relative humidity remains 30/50 unless noted."
                ],
                "images": []
            },
            {
                "title": "Zone all 2-story homes",
                "rule": "All 2-story homes should be zoned.",
                "details": [
                    "Apply zoning setup on 2-story homes.",
                    "Confirm zoning before finalizing the load and equipment."
                ],
                "images": []
            }
        ]
    },

    "STEP 3 - Weather, County & Ceiling Setup": {
        "items": [
            {
                "title": "Select correct weather location",
                "rule": "Select the correct weather location on every project if listed on the plan or spec sheet.",
                "details": [
                    "Do not assume the closest major city is correct.",
                    "Use the weather location shown on the plan, spec sheet, or Energy Star information.",
                    "The correct weather location impacts cooling and heating load accuracy."
                ],
                "images": ["screenshots/weather_location.png"]
            },
            {
                "title": "Verify county using Energy Star",
                "rule": "Verify the county on the Energy Star website when needed.",
                "details": [
                    "Use the county to confirm the correct weather data.",
                    "Adjust the load’s annual cooling and heating dry bulb temperatures to match the specified county.",
                    "This helps ensure the load is tied to the correct county-specific design conditions."
                ],
                "images": ["screenshots/energy_star_county.png"]
            },
            {
                "title": "Adjust annual cooling and heating dry bulb",
                "rule": "Adjust annual cooling and heating dry bulb temperatures to match the specified county.",
                "details": [
                    "Confirm the county.",
                    "Use Energy Star and Bin City Data as needed.",
                    "Match the load setup to the correct weather station and design conditions."
                ],
                "images": ["screenshots/bin_city_data.png"]
            },
            {
                "title": "Select correct Bin City Data weather station",
                "rule": "Under Bin City Data, select the correct weather station.",
                "details": [
                    "The weather station should match the county/weather location requirements.",
                    "Do not leave the wrong default weather station if the project specifies another county or location."
                ],
                "images": ["screenshots/weather_station.png"]
            },
            {
                "title": "Foam ceiling insulation setup",
                "rule": "When using foam custom ceiling insulation, place the configuration under Roof/Ceiling.",
                "details": [
                    "Foam ceiling setup should not be treated the same as non-foam ceiling setup.",
                    "Use the custom roof/ceiling configuration when foam insulation is required."
                ],
                "images": ["screenshots/foam_ceiling.png"]
            },
            {
                "title": "Non-foam ceiling setup",
                "rule": "If it is a non-foam ceiling, leave it as shown in the standard setup.",
                "details": [
                    "Do not change the ceiling configuration unless the specs require it.",
                    "Only use the foam configuration when foam is actually specified."
                ],
                "images": ["screenshots/non_foam_ceiling.png"]
            }
        ]
    },

    "STEP 4 - Options & In-Lieu Rooms": {
        "items": [
            {
                "title": "Use parentheses for option rooms",
                "rule": "When placing other options on a load, place the optional room as the title and the option in parentheses.",
                "details": [
                    "This keeps the base room and option room tied together.",
                    "Use clear naming so the reviewer understands which room is being replaced by the option."
                ],
                "example": "If the base has a Flex room but the plan shows a Study option in lieu of that room, name it: Flex(Study).",
                "images": []
            },
            {
                "title": "Apply worst-case BTUH to in-lieu rooms",
                "rule": "Use the BTUH from the worst-case option room.",
                "details": [
                    "If the Study is in lieu of the Flex room and the Study is worse, use the Study BTUH for Flex(Study).",
                    "If the Study has worse windows than the Flex room, include the Study windows in the load.",
                    "The goal is to make the base load cover the worst-case option condition."
                ],
                "example": "Flex(Study) should include Study BTUH and Study windows if Study is the worst case.",
                "images": []
            },
            {
                "title": "Add selected elevation floor into CAD",
                "rule": "If the elevation chosen has a floor, add it to the CAD.",
                "details": [
                    "This allows the drawing to reflect the selected elevation accurately.",
                    "Do not leave out a floor that is part of the selected elevation."
                ],
                "warning": "If the elevation chosen has a floor, add it to CAD so the design reflects accuracy.",
                "images": []
            },
            {
                "title": "Match base tonnage for options when possible",
                "rule": "If there is an option, try to match the tonnage that was on the base.",
                "details": [
                    "If matching the base tonnage is possible, keep the option aligned with the base.",
                    "If matching is not possible, notify the POC."
                ],
                "warning": "If you cannot match the base tonnage for the option, let the POC know.",
                "images": []
            }
        ]
    },

    "STEP 5 - Room Load Rules": {
        "items": [
            {
                "title": "No blinds on loads",
                "rule": "Do not apply blinds to Dallas loads.",
                "details": [
                    "Leave blinds off the load calculation.",
                    "Do not use blinds as a way to reduce the load."
                ],
                "images": []
            },
            {
                "title": "R-3 exterior board insulation",
                "rule": "If R-3 sheathing is on the specs, select exterior board insulation R-3.",
                "details": [
                    "This applies when the specs show Sheathing 3/8 with R-3.",
                    "Make sure the exterior board insulation matches the specs."
                ],
                "images": []
            },
            {
                "title": "WIC merge rule",
                "rule": "All WIC rooms should be merged unless the Master WIC has a window.",
                "details": [
                    "Merge all WIC rooms by default.",
                    "If the Master WIC has a window, the Master WIC becomes its own room.",
                    "Do not apply the 10 ft exposure rule to WIC rooms."
                ],
                "warning": "NO 10 FT EXPOSURE RULE FOR WIC ROOMS.",
                "images": []
            },
            {
                "title": "Foyers should be separate rooms",
                "rule": "Foyers should be their own room, even if the foyer is very short.",
                "details": [
                    "Do not automatically merge foyer areas into nearby rooms.",
                    "Create the foyer as its own room for load accuracy."
                ],
                "images": []
            },
            {
                "title": "Pantry merge rule",
                "rule": "Pantry should always merge with the kitchen unless it has a window or heat load.",
                "details": [
                    "Merge pantry with kitchen by default.",
                    "If the pantry has a window, make it separate as needed.",
                    "If the pantry has a heat load such as a refrigerator, freezer, stove, or similar appliance, account for that condition."
                ],
                "images": []
            },
            {
                "title": "Place rooms accurately to walls",
                "rule": "Be as accurate as possible when placing rooms on the load.",
                "details": [
                    "Line the room up to the wall whenever possible.",
                    "Only adjust away from the wall if additional square footage is needed.",
                    "Room placement affects load accuracy and design accuracy."
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
                    "Verify that the square footage is within range.",
                    "Preferred OTB area is under 100 sq ft.",
                    "You may see areas over 100, but ideally keep it under 100 when possible."
                ],
                "images": []
            },
            {
                "title": "OTB square footage adjustment",
                "rule": "If square footage is needed, bump the walls out slightly on all floors.",
                "details": [
                    "Use small wall adjustments only where needed.",
                    "Do not over-adjust the drawing.",
                    "Keep the drawing aligned with the plan as much as possible."
                ],
                "images": []
            },
            {
                "title": "Remove OTB before equipment selection",
                "rule": "After OTB is used for square footage, remove it and reset areas before selecting equipment.",
                "details": [
                    "Set what is upstairs and downstairs in their proper respective areas.",
                    "Do this before selecting equipment.",
                    "The OTB is temporary for square footage setup."
                ],
                "images": []
            },
            {
                "title": "Boot placement for OTB",
                "rule": "Use OTB for square footage, then turn it back to a regular room.",
                "details": [
                    "A boot will be placed on that OTB area.",
                    "There should be 1 boot up and 1 boot down.",
                    "This helps the design reflect the actual airflow layout."
                ],
                "images": []
            }
        ]
    },

    "STEP 7 - Blower Door Settings": {
        "items": [
            {
                "title": "Beazer blower door setup",
                "rule": "Use the Beazer infiltration setup when applicable.",
                "details": [
                    "Select the fireplace first.",
                    "Then start the blower door setup.",
                    "Wind shielding: 3.",
                    "Select Single @ Test Pressure.",
                    "Click ACH: 1.5.",
                    "Enter 50 Pascals @ test pressure difference.",
                    "For additional help, reference the walkthrough document."
                ],
                "images": []
            },
            {
                "title": "D.R. Horton East blower door setup",
                "rule": "Use D.R. Horton East setup depending on specs.",
                "details": [
                    "Select the fireplace first.",
                    "Then start the blower door setup.",
                    "Wind shielding: 3.",
                    "Select Single @ Test Pressure.",
                    "Click ACH: 3.",
                    "Enter 50 Pascals @ test pressure difference.",
                    "For additional help, reference the walkthrough document."
                ],
                "images": []
            }
        ]
    },

    "STEP 8 - Energy Star": {
        "items": [
            {
                "title": "Location and control setup",
                "rule": "Use location by county and enter the proper control location.",
                "details": [
                    "Location: by county.",
                    "Control Location: Attic/Mech.",
                    "Confirm county before setting weather and Energy Star details."
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
                "rule": "The Fin-180P cycle range should be between 130 CFM and 180 CFM.",
                "details": [
                    "Round to whichever value you are nearest.",
                    "Run Time Per Cycle is the only number you can change.",
                    "Adjust Run Time Per Cycle to stay within the required vent airflow range."
                ],
                "warning": "Only change Run Time Per Cycle to stay within range on vent airflow rate.",
                "images": ["screenshots/energy_star_fin180p.png"]
            }
        ]
    },

    "STEP 9 - Equipment Matchups, Airflow & Special Conditions": {
        "items": [
            {
                "title": "Select correct equipment matchups",
                "rule": "Select the correct matchups when placing equipment.",
                "details": [
                    "Use Dallas matchups.",
                    "Confirm equipment is matched correctly before finalizing.",
                    "Incorrect matchup selection can affect the final load and equipment recommendation."
                ],
                "images": []
            },
            {
                "title": "Lennox blower power rule",
                "rule": "For Lennox, increase blower power before adding BTUH.",
                "details": [
                    "Use blower power adjustment from 500-750.",
                    "Do not exceed 750.",
                    "Only add BTUH after blower adjustment is no longer enough."
                ],
                "warning": "Max blower power adjustment is 500-750.",
                "images": []
            },
            {
                "title": "Spiral case and OTB alignment",
                "rule": "If the plan has spiral cases and OTB, they must be lined up accurately.",
                "details": [
                    "Follow the plan as accurately as possible.",
                    "Spiral case and OTB alignment matters for both the load and the future design."
                ],
                "images": []
            },
            {
                "title": "Merge outdoor air CFMs for two systems",
                "rule": "Merge CFMs for the CFM value when it comes to outdoor air if there are two systems.",
                "details": [
                    "If two systems are used, combine the outdoor air CFM values as needed.",
                    "Do not treat each system separately if the outdoor air value needs to be merged."
                ],
                "images": []
            },
            {
                "title": "Worst-case windows on base load",
                "rule": "Bay windows and box windows should be placed on the base load as worst case.",
                "details": [
                    "If the option creates a worse window condition, account for that in the base load.",
                    "Use worst-case logic so the load is covered."
                ],
                "images": []
            },
            {
                "title": "Custom R-value if not listed",
                "rule": "If the R-value is not listed, use a custom R-value.",
                "details": [
                    "Do not force an incorrect preset if the R-value is missing.",
                    "If you do not know how to enter the custom R-value, contact the POC."
                ],
                "images": []
            },
            {
                "title": "Static pressure settings",
                "rule": "Use the correct static pressure on the equipment selection screen.",
                "details": [
                    "Gas static pressure: .70",
                    "Heat pump static pressure: .50"
                ],
                "images": []
            },
            {
                "title": "Lennox documentation requirement",
                "rule": "For Lennox, save the Word document showing supporting equipment math.",
                "details": [
                    "The document should show the math.",
                    "Include expanded ratings.",
                    "Include manufacturer numbers."
                ],
                "warning": "If Lennox is used, do not forget the Word document with math, expanded ratings, and manufacturer numbers.",
                "images": []
            }
        ]
    },

    "STEP 10 - Equipment Sizing": {
        "items": [
            {
                "title": "100%-104% total capacity rule",
                "rule": "When a unit is at 100%-104% total, and sometimes 105%, attempt to go up 1/2 ton.",
                "details": [
                    "After going up 1/2 ton, add BTUs to fit at 115%.",
                    "This is especially common on Lennox systems.",
                    "Review the sensible and total percentages before deciding."
                ],
                "images": []
            },
            {
                "title": "100% total capacity usually upgrades",
                "rule": "If total is 100%, automatically upgrade to the next ton most of the time.",
                "details": [
                    "This is especially true if it is a Lennox system.",
                    "Still verify final total and sensible values after the upgrade."
                ],
                "images": []
            },
            {
                "title": "Do not upsize if it pushes too high",
                "rule": "If upsizing causes the total to go above 122%-124%, do not upsize.",
                "details": [
                    "If you have to add a lot of BTUH after upsizing, it is usually not worth it.",
                    "If the system is already around 104%-105%, be careful before increasing tonnage.",
                    "The goal is not just to upsize, but to select the best realistic match."
                ],
                "warning": "Do not upsize if it creates excessive total capacity or requires too much added BTUH.",
                "images": []
            },
            {
                "title": "Use sq ft per ton as secondary guidance",
                "rule": "Use square feet per ton as a rule of thumb, not a standard.",
                "details": [
                    "Standard homes: 600-700 sq ft per ton.",
                    "Foam homes: 700-800 sq ft per ton.",
                    "Use this only as a secondary check when choosing tonnage."
                ],
                "images": []
            },
            {
                "title": "105% total example",
                "rule": "If a load gives 105% total, usually do not upgrade if the next ton requires too much BTUH.",
                "details": [
                    "Most of the time, when 105% is upgraded, it takes a lot of added BTUH to get within 115%.",
                    "If the current tonnage is close and reasonable, keep the current tonnage.",
                    "Use judgment and contact the POC if uncertain."
                ],
                "example": "If the load has 105% total and 98% sensible, do not upgrade the tonnage. Leave it how it is.",
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
            "Use the Dallas internal gain table when entering room gains.",
            "Rooms with refrigerators or freezers require an additional internal gain.",
            "Use the minimum and maximum ranges shown unless the POC directs otherwise."
        ]
    },

    "STEP 12 - Save & Handoff": {
        "items": [
            {
                "title": "Save the load",
                "rule": "Save the load before final handoff.",
                "details": [
                    "Confirm the project is saved after completing load setup.",
                    "Do not hand off without saving."
                ],
                "images": []
            },
            {
                "title": "POC completes PDF portion",
                "rule": "The POC will complete the PDF portion.",
                "details": [
                    "Estimator completes the load.",
                    "POC completes the PDF portion after the load is saved."
                ],
                "images": []
            },
            {
                "title": "Dallas guide updates",
                "rule": "The POC will update this guide as more information becomes available.",
                "details": [
                    "More information may be added later.",
                    "If questions remain, contact the Dallas Division POC.",
                    "Dallas Division POC: Alberto Hernandez."
                ],
                "images": []
            }
        ]
    }
}

# ---------------- SIDEBAR ---------------- #

st.sidebar.markdown("## Table of Contents")

step_names = [
    "STEP 1 - CAD Cleanup",
    "STEP 2 - Project Setup & Notes",
    "STEP 3 - Weather, County & Ceiling Setup",
    "STEP 4 - Options & In-Lieu Rooms",
    "STEP 5 - Room Load Rules",
    "STEP 6 - Open To Below",
    "STEP 7 - Blower Door Settings",
    "STEP 8 - Energy Star",
    "STEP 9 - Equipment Matchups, Airflow & Special Conditions",
    "STEP 10 - Equipment Sizing",
    "STEP 11 - Internal Gains",
    "STEP 12 - Save & Handoff"
]

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

left, right = st.columns([1.35, .9])

with left:
    st.markdown(f"""
    <div class="step-card">
        <div class="step-header">{selected_step}</div>
        <div class="step-body">
    """, unsafe_allow_html=True)

    current_step = steps[selected_step]

    if selected_step == "STEP 2 - Project Setup & Notes":
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
        "Click any item on the left to expand the Dallas-specific rule, details, examples, warnings, and screenshots."
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
