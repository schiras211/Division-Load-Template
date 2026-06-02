import streamlit as st
from pathlib import Path
import pandas as pd

st.set_page_config(page_title="Wrightsoft Division Guides", layout="wide")

# ---------------- STYLE ---------------- #

st.markdown("""
<style>
[data-testid="stSidebar"] {background-color:#EEF3F8;padding-top:25px;}
.main-header {background-color:#003E7E;color:white;padding:28px 32px;margin:-60px -80px 25px -80px;}
.main-header h1 {font-size:38px;margin:0;}
.main-header p {font-size:18px;margin-top:8px;}
.step-card {background:white;border-radius:18px;box-shadow:0 4px 16px rgba(0,0,0,.15);overflow:hidden;border:1px solid #D0D7DE;margin-bottom:25px;}
.step-header {background:#003E7E;color:white;padding:18px 24px;font-size:28px;font-weight:bold;}
.step-body {padding:24px;}
.note-box {background:#FFF200;color:black;padding:12px 16px;border-radius:8px;font-weight:800;margin-bottom:14px;border:1px solid #D9C900;}
.warning-box {background:#FFE5E5;color:#7A0000;padding:12px 16px;border-radius:8px;font-weight:700;margin:12px 0;border:1px solid #CC0000;}
.example-box {background:#EAF4FF;color:#003E7E;padding:12px 16px;border-radius:8px;font-weight:600;margin:12px 0;border:1px solid #9CC9F5;}
.rule-box {background:#F2F7F2;color:#1F5B2E;padding:12px 16px;border-radius:8px;font-weight:600;margin:12px 0;border:1px solid #B7D8B7;}
.stExpander {background-color:#EEF3F8;border:1px solid #BFD0DF;border-radius:10px;margin-bottom:12px;}
.stExpander summary {font-size:18px;font-weight:700;}
img {border-radius:10px;border:1px solid #D0D7DE;}
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

def show_custom_table(table_data):
    df = pd.DataFrame(table_data["rows"], columns=table_data["columns"])
    st.dataframe(df, use_container_width=True, hide_index=True)

def make_placeholder_steps(division_name, folder_name):
    return {
        "STEP 1 - CAD Cleanup": {
            "items": [{
                "title": f"{division_name} CAD cleanup rule",
                "rule": f"Add {division_name}-specific CAD cleanup rules here.",
                "details": ["Add division-specific CAD cleanup notes."],
                "images": [f"screenshots/{folder_name}/example.png"]
            }]
        },
        "STEP 2 - Project Setup & Notes": {
            "items": [{
                "title": f"{division_name} project setup rule",
                "rule": f"Add {division_name}-specific setup rules here.",
                "details": ["Add template, notes, airflow, zoning, and POC rules here."],
                "images": []
            }]
        },
        "STEP 3 - Weather, County & Ceiling Setup": {
            "items": [{
                "title": f"{division_name} weather setup",
                "rule": "Add weather, county, and ceiling setup rules here.",
                "details": ["Add Energy Star, county, weather station, foam, and non-foam rules."],
                "images": []
            }]
        },
        "STEP 4 - Options & In-Lieu Rooms": {
            "items": [{
                "title": f"{division_name} option room rules",
                "rule": "Add option and in-lieu room rules here.",
                "details": ["Add naming, worst-case BTUH, windows, and option tonnage rules."],
                "images": []
            }]
        },
        "STEP 5 - Room Load Rules": {
            "items": [{
                "title": f"{division_name} room load rules",
                "rule": "Add room-specific load rules here.",
                "details": ["Add WIC, pantry, foyer, blinds, insulation, and room placement rules."],
                "images": []
            }]
        },
        "STEP 6 - Open To Below": {
            "items": [{
                "title": f"{division_name} OTB rules",
                "rule": "Add open-to-below rules here.",
                "details": ["Add square footage, temporary OTB, and boot placement rules."],
                "images": []
            }]
        },
        "STEP 7 - Blower Door Settings": {
            "items": [{
                "title": f"{division_name} blower door setup",
                "rule": "Add blower door setup rules here.",
                "details": ["Add ACH, wind shielding, test pressure, and builder-specific settings."],
                "images": []
            }]
        },
        "STEP 8 - Energy Star": {
            "items": [{
                "title": f"{division_name} Energy Star setup",
                "rule": "Add Energy Star setup rules here.",
                "details": ["Add fresh air, humidity, county, control location, and ventilation rules."],
                "images": []
            }]
        },
        "STEP 9 - Equipment Matchups, Airflow & Special Conditions": {
            "items": [{
                "title": f"{division_name} equipment matchup rules",
                "rule": "Add equipment matchup and airflow rules here.",
                "details": ["Add matchup, static pressure, airflow, manufacturer, and documentation rules."],
                "images": []
            }]
        },
        "STEP 10 - Equipment Sizing": {
            "items": [{
                "title": f"{division_name} equipment sizing rules",
                "rule": "Add equipment sizing rules here.",
                "details": ["Add total capacity, sensible capacity, tonnage, and sq ft per ton rules."],
                "images": []
            }]
        },
        "STEP 11 - Internal Gains": {
            "table": [
                ["Bedroom", "Add division-specific value"],
                ["Owner Suite", "Add division-specific value"],
                ["Great Room / Family", "Add division-specific value"],
                ["Kitchen", "Add division-specific value"],
                ["Utility / Laundry", "Add division-specific value"],
                ["Study / Office", "Add division-specific value"]
            ],
            "notes": [f"Add {division_name}-specific internal gain rules here."]
        },
        "STEP 12 - Save & Handoff": {
            "items": [{
                "title": f"{division_name} save and handoff",
                "rule": "Add final save and handoff rules here.",
                "details": ["Add POC, PDF, review, and final completion rules."],
                "images": []
            }]
        }
    }

# ---------------- HEADER ---------------- #

st.markdown("""
<div class="main-header">
    <h1>Wrightsoft Load Completion Guides</h1>
    <p>Division-Specific Interactive Workflow</p>
</div>
""", unsafe_allow_html=True)

# ---------------- CINCINNATI / DAYTON DATA ---------------- #

cincinnati_dayton_steps = {
    "STEP 1 - CAD Cleanup": {
        "items": [
            {
                "title": "Garage setup",
                "rule": "Draw the garage as a room, then remove it from the calculations.",
                "details": [
                    "Heating: none.",
                    "Cooling: none.",
                    "Use this unless the Builder Spec Sheet states differently."
                ],
                "images": []
            },
            {
                "title": "Basement / crawl / slab setup",
                "rule": "Use the correct foundation condition shown on the plan.",
                "details": [
                    "Finished basement should be set up as finished basement.",
                    "Unfinished basement should be set up as unfinished basement.",
                    "Crawl should be set up as crawl.",
                    "Slab should be set up as slab.",
                    "If there is a walkout basement, use the wall tool to override the walkout above-grade walls."
                ],
                "images": [
                    "screenshots/Cincinnati_Dayton/finished_basement.png",
                    "screenshots/Cincinnati_Dayton/unfinished_basement.png",
                    "screenshots/Cincinnati_Dayton/crawl.png",
                    "screenshots/Cincinnati_Dayton/slab.png",
                    "screenshots/Cincinnati_Dayton/walkout_basement.png"
                ]
            },
            {
                "title": "Open to below setup",
                "rule": "Only make Open To Below if it has closed walls surrounding it.",
                "details": [
                    "If the Open To Below has open railing, do not make it Open To Below.",
                    "Use the actual plan condition to determine if it is closed wall or open railing."
                ],
                "images": ["screenshots/Cincinnati_Dayton/open_to_below.png"]
            }
        ]
    },

    "STEP 2 - Project Setup & Notes": {
        "items": [
            {
                "title": "Structure setup",
                "rule": "Use Cincinnati / Dayton structure defaults unless the Builder Spec Sheet states differently.",
                "details": [
                    "Zone upon request only.",
                    "Knee Walls: Yes.",
                    "Outside Air: No by default.",
                    "Use outside air only for foam insulation, Energy Star, or if requested in specs.",
                    "Sloped Ceilings: No.",
                    "Garage: Yes, draw it as a room and then remove it from calculations."
                ],
                "warning": "Builder Spec Sheet overrides these defaults if it states something different.",
                "images": []
            },
            {
                "title": "Reports included",
                "rule": "Include the required reports for Cincinnati / Dayton jobs.",
                "details": [
                    "Loads: Short Room Summary.",
                    "Equipment: ACCA Manual S Compliance Report.",
                    "Upon request: Energy Star Form.",
                    "Upon request: 310 HVAC Design.",
                    "LEED requires Energy Star, ACCA 310, and Manual D."
                ],
                "images": []
            }
        ]
    },

    "STEP 3 - Weather, County & Ceiling Setup": {
        "items": [
            {
                "title": "Standard wall setup",
                "rule": "Change the outside wall type if it is not vinyl.",
                "details": [
                    "If there are multiple wall types, use the wall tool.",
                    "Use 2x4 wall for R-13 and R-15.",
                    "Use 2x6 wall for R-19 and R-21."
                ],
                "images": ["screenshots/Cincinnati_Dayton/standard_walls.png"]
            },
            {
                "title": "Knee wall setup",
                "rule": "Knee walls are areas with attic on the opposing side.",
                "details": [
                    "Do not draw the attic in as a room.",
                    "Account for attic on the opposing side using the wall tool and Knee Wall tab.",
                    "Wrightsoft does not read sloped walls. It uses 90-degree angles.",
                    "If there is a sloped roof in an 8 ft room and the knee wall is only 5 ft tall, enter the wall tool at 8 ft tall.",
                    "If you enter it at 5 ft, Wrightsoft will read 5 ft of knee wall and 3 ft of regular outside wall."
                ],
                "images": [
                    "screenshots/Cincinnati_Dayton/knee_wall.png",
                    "screenshots/Cincinnati_Dayton/knee_wall_detail.png"
                ]
            },
            {
                "title": "Sloped ceilings",
                "rule": "Sloped ceilings are not used by default.",
                "details": [
                    "Sloped Ceilings: No.",
                    "Use knee wall/wall tool logic instead of trying to draw the attic as a room."
                ],
                "images": []
            }
        ]
    },

    "STEP 4 - Options & In-Lieu Rooms": {
        "items": [
            {
                "title": "Study / Library classification",
                "rule": "Study / Library gets no internal gain unless it qualifies as a bedroom.",
                "details": [
                    "Study / Library: None by default.",
                    "Count it as a bedroom if it has a closet and egress window.",
                    "Count it as a bedroom if it is listed as an optional bedroom."
                ],
                "images": []
            }
        ]
    },

    "STEP 5 - Room Load Rules": {
        "items": [
            {
                "title": "Blinds and insect screens",
                "rule": "Blinds only go on Bed, WIC, or Bathroom windows.",
                "details": [
                    "Blinds: Bed windows only.",
                    "Blinds: WIC windows only.",
                    "Blinds: Bathroom windows only.",
                    "Insect screens are left as they are on the template."
                ],
                "images": []
            },
            {
                "title": "Freezer / fridge / under-counter fridge",
                "rule": "Any room with a freezer, fridge, or under-counter fridge gets 600 BTU added.",
                "details": [
                    "Apply 600 BTU to any applicable room.",
                    "This is in addition to the normal room internal gain."
                ],
                "images": []
            }
        ]
    },

    "STEP 6 - Open To Below": {
        "items": [
            {
                "title": "Closed wall OTB rule",
                "rule": "Only create Open To Below if the opening has closed walls surrounding it.",
                "details": [
                    "If it has open railing, do not make it Open To Below.",
                    "Use the actual construction shown on the plan."
                ],
                "images": [
                    "screenshots/Cincinnati_Dayton/open_to_below_closed_wall.png",
                    "screenshots/Cincinnati_Dayton/open_to_below_open_railing.png"
                ]
            }
        ]
    },

    "STEP 7 - Blower Door Settings": {
        "items": [
            {
                "title": "Green Building infiltration rate",
                "rule": "Use the correct ACH50 based on project type.",
                "details": [
                    "Gut Rehab project: use 5 ACH50.",
                    "New Construction without exterior rigid insulation: use 4 ACH50.",
                    "New Construction with exterior rigid insulation: use 3 ACH50.",
                    "Go to Options > Infiltration Method > Blower Door.",
                    "Then go to Load > Infiltration > Single Point > Test Pressure Difference.",
                    "Input 50 PA.",
                    "Click Airflow from ACH box.",
                    "Input the correct ACH value."
                ],
                "warning": "Green Building projects require the correct ACH50 input.",
                "images": [
                    "screenshots/Cincinnati_Dayton/green_building_infiltration_1.png",
                    "screenshots/Cincinnati_Dayton/green_building_infiltration_2.png"
                ]
            },
            {
                "title": "SOL / Think Green infiltration",
                "rule": "Set infiltration to Tight.",
                "details": [
                    "Use this for SOL / Think Green projects.",
                    "These projects should be set to Tight unless the specs say otherwise."
                ],
                "images": ["screenshots/Cincinnati_Dayton/sol_think_green.png"]
            }
        ]
    },

    "STEP 8 - Energy Star": {
        "items": [
            {
                "title": "Ventilation setup",
                "rule": "Use ASHRAE 62.2-2010.",
                "details": [
                    "Set Energy Star paperwork to the corrected infiltration method.",
                    "Confirm the ventilation setup before final reports."
                ],
                "images": ["screenshots/Cincinnati_Dayton/ventilation_ashrae.png"]
            },
            {
                "title": "Duct loss setup",
                "rule": "Leave duct loss on default percentages and set leakage type to Energy Star.",
                "details": [
                    "Use this setup for Energy Star duct loss requirements.",
                    "Do not manually change duct loss percentages unless directed."
                ],
                "images": ["screenshots/Cincinnati_Dayton/duct_loss_energy_star.png"]
            },
            {
                "title": "LEED homes only",
                "rule": "LEED requires Energy Star, ACCA 310, and Manual D.",
                "details": [
                    "There are three levels of LEED houses: Silver, Gold, Platinum.",
                    "Silver: 5-year tax abatement.",
                    "Gold: 10-year tax abatement.",
                    "Platinum: 15-year tax abatement.",
                    "Currently, the house must be located in the City limits of Cincinnati.",
                    "Use the right template.",
                    "Use default temperatures."
                ],
                "images": []
            },
            {
                "title": "LEED information needed before starting",
                "rule": "Collect all LEED project requirements before starting.",
                "details": [
                    "Ceiling insulation.",
                    "Wall insulation.",
                    "Zip board, typically R-3 foam board.",
                    "Exterior board insulation and sheathing board together.",
                    "Window specs with .1 variance.",
                    "Direction of the house.",
                    "Type of fresh air: ERV, bath fan, ducted, etc.",
                    "Equipment depends on LEED level.",
                    "Number of systems requested.",
                    "Keep supplies overhead on 2nd floor. If needed, ask for 2nd system.",
                    "Address if not listed on plans.",
                    "Thermostat type.",
                    "Size of hood vent.",
                    "Do not worry about makeup air unless specified.",
                    "LEED contractor is one of the most important items."
                ],
                "warning": "Do not start LEED without collecting the required information.",
                "images": []
            }
        ]
    },

    "STEP 9 - Equipment Matchups, Airflow & Special Conditions": {
        "items": [
            {
                "title": "Select equipment",
                "rule": "Equipment varies based on LEED level and should stay within 100%-130%.",
                "details": [
                    "Review equipment selection based on the project type.",
                    "LEED level may impact equipment requirements.",
                    "Confirm ACCA Manual S Compliance Report."
                ],
                "images": []
            },
            {
                "title": "Manual D setup",
                "rule": "Complete Manual D in Right-D using Midwest instructions.",
                "details": [
                    "Delete any extra supplies in each room.",
                    "Ensure there is only 1 supply per room.",
                    "Click Right-D toolbar icon.",
                    "Click Duct Preferences icon.",
                    "Change all duct material fields to ShtMetl.",
                    "Uncheck Use Variable Friction Rate box.",
                    "Click Static Pressure icon."
                ],
                "images": [
                    "screenshots/Cincinnati_Dayton/manual_d_right_d.png",
                    "screenshots/Cincinnati_Dayton/manual_d_duct_preferences.png",
                    "screenshots/Cincinnati_Dayton/manual_d_static_pressure.png"
                ]
            },
            {
                "title": "Manual D static pressure values",
                "rule": "Use .5 for air handlers and .7 for gas furnaces.",
                "details": [
                    "External Static Pressure: .5 for air handlers.",
                    "External Static Pressure: .7 for gas furnaces.",
                    "Supply diffusers: .03.",
                    "Return grilles: .03.",
                    "Filter: .1 for gas systems.",
                    "Balancing Damper: .03 if a zoning system and/or manual dampers are being used."
                ],
                "images": []
            },
            {
                "title": "Carrier / Bryant coil pressure drop",
                "rule": "For Carrier / Bryant gas furnaces, use the appropriate coil pressure drop value.",
                "details": [
                    "For Carrier / Bryant air handlers, leave coil blank.",
                    "For Carrier / Bryant gas furnaces, use the matching coil pressure drop."
                ],
                "tables": [
                    {
                        "columns": ["Coil Size", "Vertical", "Horizontal"],
                        "rows": [
                            ["1.5 Ton", "0.18", "n/a"],
                            ["2 Ton", "0.19", "0.19"],
                            ["2.5 Ton", "0.23", "0.23"],
                            ["3 Ton", "0.27", "0.27"],
                            ["3.5 Ton", "0.29", "0.29"],
                            ["4 Ton", "0.29", "0.29"],
                            ["5 Ton", "0.31", "0.31"]
                        ]
                    }
                ],
                "images": []
            }
        ]
    },

    "STEP 10 - Equipment Sizing": {
        "items": [
            {
                "title": "Equipment sizing range",
                "rule": "Equipment will vary based on LEED level. Use 100%-130%.",
                "details": [
                    "Select equipment based on project requirements.",
                    "Confirm Manual S compliance.",
                    "LEED level can affect equipment selection."
                ],
                "images": []
            }
        ]
    },

    "STEP 11 - Internal Gains": {
        "table": [
            ["Bedroom", "1 Person"],
            ["Owner's Suite", "2 People"],
            ["Great Room / Family Room", "900 BTU"],
            ["Kitchen", "1200 BTU"],
            ["Kitchen with Double Oven or Additional Appliances", "2000 BTU"],
            ["Utility / Laundry", "0 BTU"],
            ["Media / Theater", "900 BTU"],
            ["Loft / Game / Bonus Room", "0 BTU"],
            ["Study / Library", "None unless bedroom-qualified"],
            ["Room with Freezer / Fridge / Under-Counter Fridge", "Add 600 BTU"]
        ],
        "notes": [
            "Study / Library counts as bedroom only if it has a closet and egress window or is listed as optional bedroom.",
            "Any room with freezer, fridge, or under-counter fridge gets 600 BTU added."
        ]
    },

    "STEP 12 - Save & Handoff": {
        "items": [
            {
                "title": "Final paperwork",
                "rule": "When finished, load paperwork needs to include the required reports.",
                "details": [
                    "Loads: Short Room Summary.",
                    "Equipment: ACCA Manual S Compliance Report.",
                    "Upon request: Energy Star Form.",
                    "Upon request: 310 HVAC Design.",
                    "For LEED: Energy Star, ACCA 310, and Manual D."
                ],
                "images": []
            },
            {
                "title": "Manual D final print requirement",
                "rule": "Do not forget to select the Duct System Summary while printing.",
                "details": [
                    "You are not complete until the correct duct summary is selected.",
                    "There may be other Wrightsoft parts that need to be applied.",
                    "The tables below are quick references for common parts."
                ],
                "images": ["screenshots/Cincinnati_Dayton/duct_system_summary.png"]
            },
            {
                "title": "Manual D supply side quick reference",
                "rule": "Use the supply-side fitting reference for common Manual D parts.",
                "details": [
                    "Measured Length of Run-Out: length of longest supply run.",
                    "Measured Length of Trunk: length of duct to supply take-off."
                ],
                "tables": [
                    {
                        "columns": ["Category", "Code", "Description", "Manual D Description"],
                        "rows": [
                            ["Take-Offs", "1A", "Round Plenum Take-Off", "90 deg. Round take-off - No Transition"],
                            ["Take-Offs", "2J1", "Top Take-Off", "Round From Top with Round Transition, 1 Dstr. Br."],
                            ["Take-Offs", "2A1", "Side Take-Off", "Round Take-Off From Side, No Transition, 1 Dstr. Br."],
                            ["Boots", "4H", "End Boot", "Floor From Round Horiz - Parallel"],
                            ["Boots", "4I", "St. Boot", "Floor From Round Vert."],
                            ["Boots", "4J", "Ell Boot", "Floor Elbow From Round Horiz."],
                            ["Wyes", "9J2", "Wye", "Trunk El of Round Y Tee"],
                            ["Junction Box", "11D", "Dist. Box", "Junction Box, Velocity In Duct = 700"],
                            ["Elbow", "8AA", "90 Degree Ell", "4 or 5 Piece Elbow, R/D = 1.0"],
                            ["Flex Bends", "11J", "Flex 90 Deg. Bend", "90 Deg. Radius Bend, Velocity = 700"]
                        ]
                    }
                ],
                "images": []
            },
            {
                "title": "Manual D return side quick reference",
                "rule": "Use the return-side fitting reference for common Manual D parts.",
                "details": [
                    "Measured Length of Run-Out: length of longest return run.",
                    "Measured Length of Trunk: length of duct to junction box.",
                    "Leave trunk length blank if no junction box is used."
                ],
                "tables": [
                    {
                        "columns": ["Category", "Code", "Description", "Manual D Description"],
                        "rows": [
                            ["Return Drop", "5H2", "Rect. RA Drop", "Square Elbow, H/W = 2.0"],
                            ["Panning - Not For LEED", "7A", "Stud Cavity", "High Or Low Wall Stud Cavity"],
                            ["Panning - Not For LEED", "7B2", "Stud to Joist Cavity", "Stud Space to Joist Space, CFM = 150"],
                            ["Panning - Not For LEED", "7C2", "Joist to Trunk", "Joist to Main Turning, CFM = 200"],
                            ["Return Box", "6P", "Return Box", "Ceiling Return Boot Without Transition"],
                            ["Elbows / Offsets", "8AA", "90 Degree Ell", "4 or 5 Piece Elbow, R/D = 1.0"]
                        ]
                    }
                ],
                "images": []
            },
            {
                "title": "Hotlink warning",
                "rule": "If prompted that info is automatically generated from RightDraw, uncheck Hotlink Drawing only when ready.",
                "details": [
                    "Click Options.",
                    "Uncheck Hotlink Drawing.",
                    "If you need to make more load drawing changes after un-hotlinking, you will have to start over from the beginning."
                ],
                "warning": "Only uncheck Hotlink Drawing when the drawing is finalized.",
                "images": ["screenshots/Cincinnati_Dayton/hotlink_warning.png"]
            }
        ]
    }
}

# ---------------- NORTHERN KENTUCKY DATA ---------------- #

northern_kentucky_steps = {
    "STEP 1 - CAD Cleanup": {
        "items": [
            {
                "title": "Garage setup",
                "rule": "Draw the garage as a room, then remove it from the calculations.",
                "details": [
                    "Garage: Yes.",
                    "Heating: none.",
                    "Cooling: none.",
                    "Use this unless stated differently in the Builder Spec Sheet."
                ],
                "images": []
            },
            {
                "title": "Open to below setup",
                "rule": "Only make Open To Below if the opening has closed walls surrounding it.",
                "details": [
                    "If the Open To Below has open railing, do not make it Open To Below.",
                    "Use the actual construction condition shown on the plan."
                ],
                "images": []
            }
        ]
    },

    "STEP 2 - Project Setup & Notes": {
        "items": [
            {
                "title": "Structure setup",
                "rule": "Use Northern Kentucky structure defaults unless specs say otherwise.",
                "details": [
                    "Zone upon request only.",
                    "Knee Walls: Yes.",
                    "Open to below: only if the open to below has closed wall surrounding.",
                    "Outside Air: No by default.",
                    "Use outside air only for foam insulation, Energy Star, or if requested in specs.",
                    "Sloped Ceilings: No.",
                    "Blinds & Insect Screens: blinds on Bedroom, WIC, or Bathroom windows only.",
                    "Insect screens are left as they are on the template.",
                    "Garage: Yes, draw it as a room then remove it from calculations."
                ],
                "warning": "Builder Spec Sheet overrides these defaults if it states something different.",
                "images": []
            }
        ]
    },

    "STEP 3 - Weather, County & Ceiling Setup": {
        "items": [
            {
                "title": "Standard wall setup",
                "rule": "Do not forget to change the outside wall type if it is not vinyl.",
                "details": [
                    "If there are multiple wall types, you may need to use the wall tool.",
                    "Use 2x4 wall for R-13 and R-15.",
                    "Use 2x6 wall for R-19 and R-21."
                ],
                "images": ["screenshots/Northern_Kentucky/standard_walls.png"]
            },
            {
                "title": "Knee wall setup",
                "rule": "Knee walls are used when attic is on the opposing side.",
                "details": [
                    "Knee Walls: Yes.",
                    "Use the wall tool / knee wall tab as needed.",
                    "Do not draw attic as its own room unless specs specifically require it."
                ],
                "images": []
            },
            {
                "title": "Sloped ceiling rule",
                "rule": "Sloped Ceilings: No.",
                "details": [
                    "Use wall tool / knee wall logic instead of treating sloped ceilings as standard room geometry."
                ],
                "images": []
            }
        ]
    },

    "STEP 4 - Options & In-Lieu Rooms": {
        "items": [
            {
                "title": "Study / Library classification",
                "rule": "Study / Library gets no internal gain unless it qualifies as a bedroom.",
                "details": [
                    "Study / Library: None by default.",
                    "Count it as a bedroom if it has a closet and egress window.",
                    "Count it as a bedroom if it is listed as an optional bedroom."
                ],
                "images": []
            }
        ]
    },

    "STEP 5 - Room Load Rules": {
        "items": [
            {
                "title": "Blinds and insect screens",
                "rule": "Blinds only go on Bedroom, WIC, or Bathroom windows.",
                "details": [
                    "Do not apply blinds to all windows.",
                    "Insect screens are left as they are on the template."
                ],
                "images": []
            },
            {
                "title": "Freezer / fridge / under-counter fridge",
                "rule": "Any room with a freezer, fridge, or under-counter fridge gets 600 BTU added.",
                "details": [
                    "Apply 600 BTU to any applicable room.",
                    "This is added on top of the normal room internal gain."
                ],
                "images": []
            }
        ]
    },

    "STEP 6 - Open To Below": {
        "items": [
            {
                "title": "Closed wall OTB rule",
                "rule": "Only create Open To Below if the opening has closed walls surrounding it.",
                "details": [
                    "If the open to below has open railing, do not make it Open To Below.",
                    "Use the plan condition to decide."
                ],
                "images": []
            }
        ]
    },

    "STEP 7 - Blower Door Settings": {
        "items": [
            {
                "title": "Northern Kentucky blower door setup",
                "rule": "Use builder specs when blower door settings are required.",
                "details": [
                    "Add ACH, wind shielding, test pressure, and builder-specific settings when provided."
                ],
                "images": []
            }
        ]
    },

    "STEP 8 - Energy Star": {
        "items": [
            {
                "title": "Outside air rule",
                "rule": "Outside Air is No unless required.",
                "details": [
                    "Use outside air only for foam insulation.",
                    "Use outside air for Energy Star.",
                    "Use outside air if requested in specs."
                ],
                "images": []
            }
        ]
    },

    "STEP 9 - Equipment Matchups, Airflow & Special Conditions": {
        "items": [
            {
                "title": "Northern Kentucky equipment setup",
                "rule": "Use project specs and equipment requirements.",
                "details": [
                    "Add specific matchup, static pressure, or manufacturer rules when provided."
                ],
                "images": []
            }
        ]
    },

    "STEP 10 - Equipment Sizing": {
        "items": [
            {
                "title": "Northern Kentucky equipment sizing",
                "rule": "Use Manual S and project specs for final sizing.",
                "details": [
                    "Confirm equipment sizing before final reports."
                ],
                "images": []
            }
        ]
    },

    "STEP 11 - Internal Gains": {
        "table": [
            ["Bedroom", "1 Person"],
            ["Owner's Suite", "2 People"],
            ["Great Room / Family Room", "900 BTU"],
            ["Kitchen", "1200 BTU"],
            ["Kitchen with Double Oven or Additional Appliances", "2000 BTU"],
            ["Utility / Laundry", "0 BTU"],
            ["Media / Theater", "900 BTU"],
            ["Loft / Game / Bonus Room", "0 BTU"],
            ["Study / Library", "None unless bedroom-qualified"],
            ["Room with Freezer / Fridge / Under-Counter Fridge", "Add 600 BTU"]
        ],
        "notes": [
            "Study / Library counts as bedroom only if it has a closet and egress window or is listed as optional bedroom.",
            "Any room with freezer, fridge, or under-counter fridge gets 600 BTU added."
        ]
    },

    "STEP 12 - Save & Handoff": {
        "items": [
            {
                "title": "Final review",
                "rule": "Confirm structure, internal gains, walls, and reports before handoff.",
                "details": [
                    "Verify internal gains.",
                    "Verify standard wall type.",
                    "Verify OTB condition.",
                    "Verify garage is removed from heating/cooling calculations."
                ],
                "images": []
            }
        ]
    }
}

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
                "title": "Use one CAD file",
                "rule": "It should be one file with the right elevation and options all in one.",
                "details": [
                    "Do not create multiple disconnected files for the same load.",
                    "The CAD should include the correct elevation and needed options in one file.",
                    "This keeps future design work cleaner and more accurate."
                ],
                "warning": "DO NOT create scattered separate files.",
                "images": ["screenshots/Dallas/do_not_do_this.png"]
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
                "example": "Load completed using Elevation B with selected options shown on plan.",
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
                "images": ["screenshots/Dallas/weather_location.png"]
            },
            {
                "title": "Verify county using Energy Star",
                "rule": "Verify the county on the Energy Star website when needed.",
                "details": [
                    "Use the county to confirm the correct weather data.",
                    "Adjust the load’s annual cooling and heating dry bulb temperatures to match the specified county.",
                    "This helps ensure the load is tied to the correct county-specific design conditions."
                ],
                "images": ["screenshots/Dallas/energy_star_county.png"]
            },
            {
                "title": "Bin City Data weather station",
                "rule": "Under Bin City Data, select the correct weather station.",
                "details": [
                    "The weather station should match the county/weather location requirements.",
                    "Do not leave the wrong default weather station if the project specifies another county or location."
                ],
                "images": ["screenshots/Dallas/bin_city_data.png", "screenshots/Dallas/weather_station.png"]
            },
            {
                "title": "Foam ceiling insulation setup",
                "rule": "When using foam custom ceiling insulation, place the configuration under Roof/Ceiling.",
                "details": [
                    "Foam ceiling setup should not be treated the same as non-foam ceiling setup.",
                    "Use the custom roof/ceiling configuration when foam insulation is required."
                ],
                "images": ["screenshots/Dallas/foam_ceiling.png"]
            },
            {
                "title": "Non-foam ceiling setup",
                "rule": "If it is a non-foam ceiling, leave it as shown in the standard setup.",
                "details": [
                    "Do not change the ceiling configuration unless the specs require it.",
                    "Only use the foam configuration when foam is actually specified."
                ],
                "images": ["screenshots/Dallas/non_foam_ceiling.png"]
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
                "title": "Add option windows to the base load when needed",
                "rule": "If the in-lieu room has more or worse windows, put those windows in the base load unless the option will be separated.",
                "details": [
                    "Example: Flex has no windows, but Study option has windows.",
                    "Room name should be Flex(Study).",
                    "Add the Study windows and the 600 BTUH to that room if Study is the worst case."
                ],
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
                "images": ["screenshots/Dallas/energy_star_fin180p.png"]
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
                    "Gas static pressure: .70.",
                    "Heat pump static pressure: .50."
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

# ---------------- NASHVILLE DATA ---------------- #

nashville_steps = {
    "STEP 1 - CAD Cleanup": {
        "items": [
            {
                "title": "Garage setup",
                "rule": "Garage should be included.",
                "details": [
                    "Garage: Yes.",
                    "Follow the plan and builder specs when setting up the garage."
                ],
                "images": []
            }
        ]
    },

    "STEP 2 - Project Setup & Notes": {
        "items": [
            {
                "title": "Weather location",
                "rule": "Use Nashville, TN weather location.",
                "details": [
                    "City: Nashville, TN.",
                    "Design City: Nashville Intl.",
                    "Standard: ASHRAE 2021.",
                    "Cooling: 92.",
                    "Heating: 20.",
                    "Override: No."
                ],
                "images": []
            },
            {
                "title": "Structure setup",
                "rule": "Use Nashville structure defaults unless specs say otherwise.",
                "details": [
                    "Knee Walls: Yes.",
                    "Open to below: If 1 system serving 2 floors, Yes.",
                    "Open to below: If 2 systems serving 2 floors, No.",
                    "Outside Air: Yes. See Info Sheet for type. Default is ERV - Balanced.",
                    "Sloped Ceilings: No.",
                    "Blinds & Insect Screens: Yes / Yes.",
                    "Remove blinds/screens from glass doors, sliders, French doors, transom windows, and sidelights."
                ],
                "images": []
            }
        ]
    },

    "STEP 3 - Weather, County & Ceiling Setup": {
        "items": [
            {
                "title": "Duct loss and gain scenarios",
                "rule": "Use the correct duct loss and gain scenario based on SA and RA location.",
                "details": [
                    "Scenario 1: SA Attic / RA Attic.",
                    "Scenario 2: SA Crawl Space / RA Crawl Space.",
                    "Scenario 3: SA Attic / RA Conditioned Space.",
                    "Scenario 4: SA Conditioned Space / RA Conditioned Space.",
                    "Heat Loss %: Default, except conditioned/conditioned is Default 0%.",
                    "Sensible Gain %: Default, except conditioned/conditioned is Default 0%.",
                    "Sealing: Average.",
                    "Insulation: R-8.",
                    "Leakage: MJ8."
                ],
                "images": []
            },
            {
                "title": "Supply and return configuration",
                "rule": "Set supply and return configuration based on trunk type.",
                "details": [
                    "Supply Configuration should be set to Radial, perimeter outlets when not using rigid trunk line.",
                    "Supply Configuration should be set to Trunk and branch, perimeter outlets when using rigid trunk line.",
                    "Return Configuration should always be set to Radial."
                ],
                "images": []
            }
        ]
    },

    "STEP 4 - Options & In-Lieu Rooms": {
        "items": [
            {
                "title": "Nashville option room rules",
                "rule": "Add Nashville option and in-lieu room rules here.",
                "details": [
                    "Add any builder-specific option, elevation, or in-lieu room rules."
                ],
                "images": []
            }
        ]
    },

    "STEP 5 - Room Load Rules": {
        "items": [
            {
                "title": "Blinds and insect screens",
                "rule": "Blinds and insect screens are Yes / Yes with exclusions.",
                "details": [
                    "Use blinds and insect screens as default.",
                    "Remove from glass doors.",
                    "Remove from sliders.",
                    "Remove from French doors.",
                    "Remove from transom windows.",
                    "Remove from sidelights."
                ],
                "images": []
            }
        ]
    },

    "STEP 6 - Open To Below": {
        "items": [
            {
                "title": "Open to below system rule",
                "rule": "Use OTB based on how many systems serve the floors.",
                "details": [
                    "If 1 system serves 2 floors: Open to below = Yes.",
                    "If 2 systems serve 2 floors: Open to below = No."
                ],
                "images": []
            }
        ]
    },

    "STEP 7 - Blower Door Settings": {
        "items": [
            {
                "title": "Nashville blower door settings",
                "rule": "Use builder specs if blower door settings are required.",
                "details": [
                    "Add ACH, test pressure, and wind shielding values when provided."
                ],
                "images": []
            }
        ]
    },

    "STEP 8 - Energy Star": {
        "items": [
            {
                "title": "Outside air setup",
                "rule": "Outside Air is Yes.",
                "details": [
                    "See Info Sheet for type.",
                    "Default outside air type is ERV - Balanced."
                ],
                "images": []
            }
        ]
    },

    "STEP 9 - Equipment Matchups, Airflow & Special Conditions": {
        "items": [
            {
                "title": "Equipment selection",
                "rule": "Find equipment matchups before selecting equipment.",
                "details": [
                    "Select Outdoor Unit: AC or Heat Pump.",
                    "Select Furnace for AC system only.",
                    "Select Electric Heat Strip for HP system only."
                ],
                "images": []
            }
        ]
    },

    "STEP 10 - Equipment Sizing": {
        "items": [
            {
                "title": "Nashville equipment sizing",
                "rule": "Use selected equipment matchups and Manual S report.",
                "details": [
                    "Confirm equipment selection before final reports."
                ],
                "images": []
            }
        ]
    },

    "STEP 11 - Internal Gains": {
        "table": [
            ["Bedroom", "1p"],
            ["Primary / Owner's Suite", "2p + Min. 500 / Max. 1000"],
            ["Great Rm / Family Rm", "Min. 900 / Max. 1800"],
            ["Kitchen - ≤3 Large Appliances", "Min. 1200 / Max. 2400"],
            ["Kitchen - >3 Large Appliances", "Min. 2000 / Max. 4000"],
            ["Bar", "Min. 600 / Max. 1200"],
            ["Utility / Laundry", "Min. 500 / Max. 1000"],
            ["Media / Theater", "Min. 1200 / Max. 2400"],
            ["Loft / Game / Bonus Rm", "Min. 900 / Max. 1800"],
            ["Study / Library / Office", "Min. 600 / Max. 1200"],
            ["Exercise / Gym", "Min. 600 / Max. 1200"],
            ["Add for Room with Refrigerator / Freezer", "Min. 600 / Max. 1200"]
        ],
        "notes": [
            "Use Nashville internal gains table.",
            "Add refrigerator/freezer load when applicable."
        ]
    },

    "STEP 12 - Save & Handoff": {
        "items": [
            {
                "title": "Reports included",
                "rule": "Include required Nashville reports.",
                "details": [
                    "Loads > Short Room Summary.",
                    "Loads > Multiple Orientations.",
                    "Loads > Component Constructions: Entire House, not Room by Room, upon request only.",
                    "Equipment > ACCA Manual S Compliance Report.",
                    "Duct > System Summary: Manual D only."
                ],
                "images": []
            }
        ]
    }
}

# ---------------- AUSTIN DATA ---------------- #

austin_steps = {
    "STEP 1 - CAD Cleanup": {
        "items": [
            {
                "title": "Austin CAD notes",
                "rule": "Use Austin matchups and follow Austin-specific notes.",
                "details": [
                    "Austin Matchups.",
                    "Texas Internal Gains.",
                    "Only options that affect the tonnage.",
                    "No commercial projects.",
                    "Try not to add additional BTUs unless needed.",
                    "If BTUs are needed, spread them out in main areas.",
                    "Areas to add BTUs: Living, Game Room, Media, Study, Master, Kitchen."
                ],
                "images": []
            }
        ]
    },

    "STEP 2 - Project Setup & Notes": {
        "items": [
            {
                "title": "Lennox blower power",
                "rule": "When adding BTUs to Lennox loads, increase blower power first.",
                "details": [
                    "Increase blower power between 500-750.",
                    "If more BTUs are still needed, then add BTUs to the load."
                ],
                "images": []
            },
            {
                "title": "360 CFM per ton",
                "rule": "Use 360 CFM per ton.",
                "details": [
                    "Verify airflow before final equipment selection."
                ],
                "images": []
            },
            {
                "title": "Select correct template",
                "rule": "Select the correct Austin template.",
                "details": [
                    "Template selection affects the full load setup."
                ],
                "images": []
            }
        ]
    },

    "STEP 3 - Weather, County & Ceiling Setup": {
        "items": [
            {
                "title": "Austin Energy completion",
                "rule": "Use Austin Energy requirements when applicable.",
                "details": [
                    "Average house load should be between 1600-3000 per Austin Energy Standard, not including people.",
                    "Add SHGC value to window description line.",
                    "Window minimum spec should be .40 / .25 if unknown.",
                    "Provide Manual D.",
                    "Duct leakage must be set to notable.",
                    "Semi-tight for regular homes and tight for foam.",
                    "Set upper door infiltration 50 PA / ACH 3.",
                    "Temperature settings: Indoor Design 72 heating / 75 cooling. Outdoor 100 summer / 20 winter."
                ],
                "images": ["screenshots/Austin/blower_door_method.png"]
            }
        ]
    },

    "STEP 4 - Options & In-Lieu Rooms": {
        "items": [
            {
                "title": "Options that affect tonnage",
                "rule": "Only use options that affect the tonnage.",
                "details": [
                    "Do not overwork options that do not affect equipment sizing.",
                    "Verify if the option changes square footage, windows, exposure, or load enough to change tonnage."
                ],
                "images": []
            }
        ]
    },

    "STEP 5 - Room Load Rules": {
        "items": [
            {
                "title": "Austin internal gain room rules",
                "rule": "Use Austin room gain values.",
                "details": [
                    "Add in Family activity room or theater: 600.",
                    "Laundry: 600.",
                    "Kitchen: Standard.",
                    "Master Bedroom: 2 people + 400 BTUs.",
                    "Bedrooms: 1 person + 400 BTUs.",
                    "Add insect screens to operable windows."
                ],
                "images": []
            },
            {
                "title": "BTU adjustments",
                "rule": "If additional BTUs are needed, spread them out in main areas.",
                "details": [
                    "Living.",
                    "Game Room.",
                    "Media.",
                    "Study.",
                    "Master.",
                    "Kitchen."
                ],
                "images": []
            }
        ]
    },

    "STEP 6 - Open To Below": {
        "items": [
            {
                "title": "Austin OTB",
                "rule": "Use project-specific open-to-below setup.",
                "details": [
                    "Match the plan and verify square footage.",
                    "Do not over-adjust the load unless it affects tonnage."
                ],
                "images": []
            }
        ]
    },

    "STEP 7 - Blower Door Settings": {
        "items": [
            {
                "title": "Austin blower door method",
                "rule": "Set upper door infiltration to 50 PA / ACH 3.",
                "details": [
                    "Use blower door method when required.",
                    "Confirm infiltration setup before completing Austin Energy jobs."
                ],
                "images": ["screenshots/Austin/blower_door_method.png"]
            }
        ]
    },

    "STEP 8 - Energy Star": {
        "items": [
            {
                "title": "Energy Star settings",
                "rule": "Use county and fresh air settings.",
                "details": [
                    "Location by County for Temperature.",
                    "Fresh Air Settings: 40 min / 60 min cycle for 8145.",
                    "Fresh Air Setting for other models: 45 min / 60 min cycle."
                ],
                "images": []
            }
        ]
    },

    "STEP 9 - Equipment Matchups, Airflow & Special Conditions": {
        "items": [
            {
                "title": "Austin matchups",
                "rule": "Use Austin equipment matchups.",
                "details": [
                    "Select equipment from Austin matchups.",
                    "Verify system type and capacity.",
                    "If the next tonnage has better coverage but cannot pull it down with additional BTUs, reset BTUs to standard and place the home as perimeter in the duct loss screen, then spread BTUs using main areas."
                ],
                "images": []
            },
            {
                "title": "City of Pflugerville",
                "rule": "Follow City of Pflugerville notes when applicable.",
                "details": [
                    "Plans with over 200% furnace capacity: add note to explain or adjust furnace size.",
                    "Semi-tight on all Manual Js.",
                    "Verify specs and match square footage.",
                    "Make sure walls adjacent to garage have correct insulation.",
                    "Fireplace set at 0 unless wood burning.",
                    "Infiltration: Semi Tight.",
                    "Provide a Manual D.",
                    "Verify window material, usually vinyl.",
                    "Set location correct and temps."
                ],
                "images": []
            }
        ]
    },

    "STEP 10 - Equipment Sizing": {
        "items": [
            {
                "title": "Equipment sizing",
                "rule": "Automatic tonnage increase is based on 95% sensible.",
                "details": [
                    "97% sensible: analyze the home and see if the next tonnage is better without excessive BTU additions.",
                    "If additions cause cooling in main areas to be wrong, keep the original system.",
                    "98% sensible: verify the next tonnage. If it does not break 115% total without additional BTUs, leave the larger tonnage.",
                    "99% sensible: tonnage passes."
                ],
                "images": []
            },
            {
                "title": "Capacity goals",
                "rule": "Use Austin capacity goals by equipment type.",
                "details": [
                    "Total: 100%-115%.",
                    "Sensible: Cannot be below 90%. Goal is 97%-100% when able.",
                    "2 Stage Total: 100%-120%.",
                    "2 Stage Sensible: Cannot be below 90%. Goal is 97%-100% when able.",
                    "Variable Speed Total: 100%-130%.",
                    "Variable Speed Sensible: Cannot be below 90%. Goal is 97%-100% when able."
                ],
                "images": []
            }
        ]
    },

    "STEP 11 - Internal Gains": {
        "table": [
            ["Bedroom", "1p"],
            ["Owner Suite", "2p + Min 500 / Max 1000"],
            ["Great Room / Family", "Min. 900 / Max. 1800"],
            ["Kitchen < 3 Large Appliances", "Min. 1200 / Max. 2400"],
            ["Kitchen > 3 Large Appliances", "Min. 2000 / Max. 4000"],
            ["Bar", "Min. 600 / Max. 1200"],
            ["Utility / Laundry", "Min. 500 / Max. 1000"],
            ["Media / Theater", "Min. 1200 / Max. 2400"],
            ["Loft / Game / Bonus", "Min. 900 / Max. 1800"],
            ["Study / Library / Office", "Min. 600 / Max. 1200"],
            ["Exercise", "Min. 600 / Max. 1200"],
            ["Add for Room with Refrigerator / Freezer", "Min. 600 / Max. 1200"]
        ],
        "notes": [
            "Family activity room or theater: add 600.",
            "Laundry: 600.",
            "Master Bedroom: 2 people + 400 BTUs.",
            "Bedrooms: 1 person + 400 BTUs."
        ]
    },

    "STEP 12 - Save & Handoff": {
        "items": [
            {
                "title": "Reports and final checks",
                "rule": "Complete final checks before saving.",
                "details": [
                    "Manual D: follow cheat sheet.",
                    "Form Order: Short Form, Multiple Orientation, Building Analysis, Components Construction, Project Summary, AED Assessment, Right-J Worksheet, Manual S Compliance, Duct Summary, Static Pressure and Friction Rate, Draw Screen.",
                    "Res checks: match square footage.",
                    "Match address and other pertinent city information.",
                    "Adjust window material to match.",
                    "Face the home per orientation, if none then worst case.",
                    "Save the load. POC will complete the PDF portion."
                ],
                "images": []
            }
        ]
    }
}

# ---------------- COLUMBUS DATA ---------------- #

columbus_steps = {
    "STEP 1 - CAD Cleanup": {
        "items": [
            {
                "title": "Garage Setup",
                "rule": "Draw the garage as a room, then remove it from calculations.",
                "details": [
                    "Garage: Yes.",
                    "Heating: none.",
                    "Cooling: none.",
                    "Use this unless stated differently in the Builder Spec Sheet."
                ],
                "images": []
            }
        ]
    },
    "STEP 2 - Project Setup & Notes": {
        "items": [
            {
                "title": "Structure Defaults",
                "rule": "Use Columbus structure defaults unless specs override.",
                "details": [
                    "Zone upon request only.",
                    "Knee Walls: Yes.",
                    "Open To Below: only if surrounded by closed walls.",
                    "If open railing exists, do NOT create Open To Below.",
                    "Outside Air: No.",
                    "Only use Outside Air for foam insulation, Energy Star, or when requested in specs.",
                    "Sloped Ceilings: No.",
                    "Blinds & Insect Screens: blinds on Bedroom, WIC, or Bathroom windows only.",
                    "Insect screens are left as they are on template.",
                    "Garage: draw in the room and then remove it from calculations."
                ],
                "warning": "Builder Spec Sheet overrides these defaults if it states something different.",
                "images": []
            }
        ]
    },
    "STEP 3 - Weather, County & Ceiling Setup": {
        "items": [
            {
                "title": "Standard Walls",
                "rule": "Always verify wall construction.",
                "details": [
                    "Do not forget to change your outside wall type if not vinyl.",
                    "If you have multiple wall types, you may need to use the wall tool.",
                    "2x4 Wall: R-13 and R-15.",
                    "2x6 Walls: R-19 and R-21."
                ],
                "images": ["screenshots/Columbus/standard_walls.png"]
            },
            {
                "title": "Finished Basement",
                "rule": "Use proper finished basement setup.",
                "details": [
                    "Apply finished basement construction settings.",
                    "Verify insulation values match plan."
                ],
                "images": ["screenshots/Columbus/finished_basement.png"]
            },
            {
                "title": "Unfinished Basement",
                "rule": "Use unfinished basement settings.",
                "details": [
                    "Apply unfinished basement construction settings.",
                    "Verify wall and floor insulation."
                ],
                "images": ["screenshots/Columbus/unfinished_basement.png"]
            },
            {
                "title": "Walkout Basement",
                "rule": "Use wall tool to override walkout above-grade walls.",
                "details": [
                    "If you have a walkout basement, use the wall tool to override the walkout above-grade walls.",
                    "Walkout walls should not be treated as normal below-grade basement walls."
                ],
                "images": ["screenshots/Columbus/walkout_basement.png"]
            },
            {
                "title": "Slab",
                "rule": "Use slab construction when applicable.",
                "details": [
                    "Verify slab edge insulation.",
                    "Verify perimeter insulation."
                ],
                "images": ["screenshots/Columbus/slab.png"]
            },
            {
                "title": "Knee Walls",
                "rule": "Use the wall tool and Knee Wall tab.",
                "details": [
                    "Knee walls are areas with attic on the opposing side.",
                    "Do not draw the attic in as a room.",
                    "Take this into account with wall tool, Knee Wall tab.",
                    "Wrightsoft does not read sloped walls. It deals with 90-degree angles.",
                    "If you have a sloped roof in an 8 ft room and the knee wall is only 5 ft tall, put the wall tool in at 8 ft tall.",
                    "If you enter 5 ft, Wrightsoft reads 5 ft of knee wall and 3 ft of regular outside wall."
                ],
                "images": [
                    "screenshots/Columbus/knee_wall_setup.png",
                    "screenshots/Columbus/knee_wall_example.png"
                ]
            }
        ]
    },
    "STEP 4 - Options & In-Lieu Rooms": {
        "items": [
            {
                "title": "Study / Library",
                "rule": "Study / Library is none unless it qualifies as a bedroom.",
                "details": [
                    "Count as a bedroom if it has a closet and egress window.",
                    "Count as a bedroom if it is listed as optional bedroom."
                ],
                "images": []
            }
        ]
    },
    "STEP 5 - Room Load Rules": {
        "items": [
            {
                "title": "Internal Gain Rules",
                "rule": "Use Columbus internal gain values.",
                "details": [
                    "Bedroom: 1 person.",
                    "Owner's Suite: 2 people.",
                    "Great Room / Family Room: 900 BTU.",
                    "Kitchen: 1200 BTU.",
                    "Kitchen with double oven or additional appliances: 2000 BTU.",
                    "Utility / Laundry: 0 BTU.",
                    "Media / Theater: 900 BTU.",
                    "Loft / Game / Bonus Room: 0 BTU.",
                    "Study / Library: None unless bedroom-qualified."
                ],
                "images": []
            },
            {
                "title": "Refrigerator / Freezer Rule",
                "rule": "Any room with freezer, fridge, or under-counter fridge gets 600 BTU added.",
                "details": [
                    "Add 600 BTU to applicable rooms.",
                    "This is in addition to normal internal gains."
                ],
                "images": []
            },
            {
                "title": "Blinds and insect screens",
                "rule": "Blinds only go on Bedroom, WIC, or Bathroom windows.",
                "details": [
                    "Insect screens are left as they are on the template."
                ],
                "images": []
            }
        ]
    },
    "STEP 6 - Open To Below": {
        "items": [
            {
                "title": "Open To Below",
                "rule": "Only create Open To Below if it is surrounded by closed walls.",
                "details": [
                    "If open railing exists, do not create Open To Below."
                ],
                "images": []
            }
        ]
    },
    "STEP 7 - Blower Door Settings": {
        "items": [
            {
                "title": "Blower Door",
                "rule": "Follow builder requirements.",
                "details": [
                    "Use project-specific blower door values.",
                    "Confirm ACH requirements if provided."
                ],
                "images": []
            }
        ]
    },
    "STEP 8 - Energy Star": {
        "items": [
            {
                "title": "Energy Star",
                "rule": "Use Energy Star settings when required.",
                "details": [
                    "Use Energy Star form upon request.",
                    "Verify fresh air calculations.",
                    "Verify county weather data."
                ],
                "images": []
            }
        ]
    },
    "STEP 9 - Equipment Matchups, Airflow & Special Conditions": {
        "items": [
            {
                "title": "Equipment Selection",
                "rule": "Follow Manual S.",
                "details": [
                    "Select proper equipment matchups.",
                    "Verify heating and cooling capacities.",
                    "Confirm airflow."
                ],
                "images": []
            }
        ]
    },
    "STEP 10 - Equipment Sizing": {
        "items": [
            {
                "title": "Equipment Sizing",
                "rule": "Use Manual S sizing requirements.",
                "details": [
                    "Verify total capacity.",
                    "Verify sensible capacity.",
                    "Confirm selected tonnage."
                ],
                "images": []
            }
        ]
    },
    "STEP 11 - Internal Gains": {
        "table": [
            ["Bedroom", "1 Person"],
            ["Owner's Suite", "2 People"],
            ["Great Room / Family Room", "900 BTU"],
            ["Kitchen", "1200 BTU"],
            ["Kitchen with Double Oven or Additional Appliances", "2000 BTU"],
            ["Utility / Laundry", "0 BTU"],
            ["Media / Theater", "900 BTU"],
            ["Loft / Game / Bonus Room", "0 BTU"],
            ["Study / Library", "None unless bedroom-qualified"],
            ["Room with Freezer / Fridge / Under-Counter Fridge", "Add 600 BTU"]
        ],
        "notes": [
            "Study / Library counts as bedroom only if it has a closet and egress window or is listed as optional bedroom.",
            "Any room that has a freezer, fridge, or under-counter fridge gets 600 BTU added."
        ]
    },
    "STEP 12 - Save & Handoff": {
        "items": [
            {
                "title": "Reports Included",
                "rule": "Include required reports.",
                "details": [
                    "Loads: Short Room Summary.",
                    "Equipment: ACCA Manual S Compliance Report.",
                    "Upon Request: Energy Star Form.",
                    "Upon Request: 310 HVAC Design.",
                    "LEED requires Energy Star, ACCA 310, and Manual D."
                ],
                "images": []
            }
        ]
    }
}

# ---------------- OTHER DIVISION PLACEHOLDERS ---------------- #
indianapolis_steps = make_placeholder_steps("Indianapolis", "Indianapolis")
louisville_steps = make_placeholder_steps("Louisville", "Louisville")
viccarone_steps = make_placeholder_steps("Viccarone", "Viccarone")
raleigh_steps = make_placeholder_steps("Raleigh", "Raleigh")
charlotte_steps = make_placeholder_steps("Charlotte", "Charlotte")
mid_atlantic_steps = make_placeholder_steps("Mid Atlantic", "Mid_Atlantic")
# ---------------- HOUSTON DATA ---------------- #

houston_steps = {
    "STEP 1 - CAD Cleanup": {
        "items": [
            {
                "title": "File handling and save rules",
                "rule": "Follow Houston folder layout and do not archive files.",
                "details": [
                    "Do not archive files.",
                    "Follow the folders layout.",
                    "Save by plan number, not by subdivision.",
                    "Write the square footage from the plans on the job/file notes."
                ],
                "images": []
            },
            {
                "title": "Template and matchup source",
                "rule": "Select the correct Houston template and use Houston matchups.",
                "details": [
                    "Houston Matchups.",
                    "Select the correct template.",
                    "Get equipment selection from Teams > Texas CED > NRG365 general > Houston match-ups.",
                    "Alternate path: CED-General > Division Info > select city in Texas you are working in > Houston CED."
                ],
                "images": []
            }
        ]
    },

    "STEP 2 - Project Setup & Notes": {
        "items": [
            {
                "title": "Weather and airflow setup",
                "rule": "Use Houston Hooks weather and 400 CFM per ton.",
                "details": [
                    "Weather city: Houston Hooks ASHRAE 2021.",
                    "Outdoor Temp: 98.",
                    "Use 400 CFM per ton.",
                    "Write the square footage from the plans on the job/file notes."
                ],
                "images": []
            },
            {
                "title": "Lennox blower power before adding BTUs",
                "rule": "When adding BTUs to Lennox loads, increase blower power first.",
                "details": [
                    "Increase blower power between 500-750 first.",
                    "Then, if needed, add more BTUs to the load.",
                    "Try not to add extra BTUs. Place the unit that fits."
                ],
                "warning": "Do not add extra BTUs unless needed after blower adjustment.",
                "images": []
            }
        ]
    },

    "STEP 3 - Weather, County & Ceiling Setup": {
        "items": [
            {
                "title": "Attic barrier rule",
                "rule": "Remove attic barrier unless the info sheet says to add it.",
                "details": [
                    "Remove attic barrier from the ceiling setup unless the info sheet says to add it.",
                    "Also remove it from duct loss where you change R-6 to R-8.",
                    "Use R-8 when required in duct loss setup."
                ],
                "images": []
            },
            {
                "title": "Beazer construction specs",
                "rule": "Use Beazer-specific construction values when applicable.",
                "details": [
                    "Custom Ceiling: R-49 / 0.023.",
                    "Walls: R-19 + R-3.",
                    "Floors over garage: R-42.",
                    "Windows: .30 / .22.",
                    "Knee walls: R-19."
                ],
                "images": []
            }
        ]
    },

    "STEP 4 - Options & In-Lieu Rooms": {
        "items": [
            {
                "title": "Houston options rule",
                "rule": "Use options only when they affect the load or equipment sizing.",
                "details": [
                    "Do not overwork options that do not affect the selected equipment.",
                    "Verify square footage, exposure, windows, and tonnage impact before adding extra work."
                ],
                "images": []
            }
        ]
    },

    "STEP 5 - Room Load Rules": {
        "items": [
            {
                "title": "Texas internal gains",
                "rule": "Use Texas internal gains for Houston.",
                "details": [
                    "Use the Houston/Texas internal gain table in Step 11.",
                    "Add refrigerator/freezer room gain when applicable."
                ],
                "images": []
            }
        ]
    },

    "STEP 6 - Open To Below": {
        "items": [
            {
                "title": "Houston OTB setup",
                "rule": "Use project-specific open-to-below setup.",
                "details": [
                    "Match the plan condition.",
                    "Verify square footage before selecting equipment."
                ],
                "images": []
            }
        ]
    },

    "STEP 7 - Blower Door Settings": {
        "items": [
            {
                "title": "Beazer blower door",
                "rule": "Use Beazer blower door settings when applicable.",
                "details": [
                    "Blower Door: Option 3.",
                    "Test Pressure: 50 Pa.",
                    "ACH: 1.5."
                ],
                "images": []
            }
        ]
    },

    "STEP 8 - Energy Star": {
        "items": [
            {
                "title": "Energy Star setup",
                "rule": "Use county location and correct fresh air location.",
                "details": [
                    "Location by county.",
                    "For the fresh air location, be sure it is Attic or Hall, not Mech."
                ],
                "warning": "Fresh air location should be Attic or Hall, not Mech.",
                "images": []
            }
        ]
    },

    "STEP 9 - Equipment Matchups, Airflow & Special Conditions": {
        "items": [
            {
                "title": "Houston equipment matchups",
                "rule": "Use Houston matchups and choose equipment based on capacity and square footage per ton.",
                "details": [
                    "Use Houston matchups from Teams or CED-General Division Info.",
                    "Pick equipment that gets as close as possible to 600-700 sq ft per ton for non-foam homes.",
                    "Pick equipment that gets as close as possible to 700-800 sq ft per ton for foam homes.",
                    "Stay within the capacity percentage requirements.",
                    "Try not to add extra BTUs. Place the unit that fits.",
                    "If at 100%, try the next size up unless square footage is already at 600-700 sq ft per ton.",
                    "If you have to add BTUs to make the larger size fit, keep the smaller one."
                ],
                "images": []
            },
            {
                "title": "Beazer equipment",
                "rule": "For Beazer, pick variable speed equipment.",
                "details": [
                    "Side discharge is variable speed and allows 130% total capacity.",
                    "Beazer has new equipment."
                ],
                "images": []
            }
        ]
    },

    "STEP 10 - Equipment Sizing": {
        "items": [
            {
                "title": "Capacity goals",
                "rule": "Use Houston capacity goals by equipment type.",
                "details": [
                    "Total: 100%-115%.",
                    "Sensible: Cannot be below 90%. Goal is 97%-100% when able.",
                    "2 Stage Total: 100%-120%.",
                    "2 Stage Sensible: Cannot be below 90%. Goal is 97%-100% when able.",
                    "Variable Speed Total: 100%-130%.",
                    "Variable Speed Sensible: Cannot be below 90%. Goal is 97%-100% when able."
                ],
                "images": []
            },
            {
                "title": "Square footage per ton check",
                "rule": "Use square footage per ton as a secondary sizing check.",
                "details": [
                    "Non-foam: target as close as possible to 600-700 sq ft per ton.",
                    "Foam: target as close as possible to 700-800 sq ft per ton.",
                    "If at 100%, try the next size up unless the square footage per ton is already in range.",
                    "If the larger unit needs added BTUs to fit, keep the smaller unit."
                ],
                "images": []
            }
        ]
    },

    "STEP 11 - Internal Gains": {
        "table": [
            ["Bedroom", "1p"],
            ["Owners Suite", "2p + Min 500 / Max 1000"],
            ["Great Room / Family", "Min. 900 / Max. 1800"],
            ["Kitchen < 3 Large Appliances", "Min. 1200 / Max. 2400"],
            ["Kitchen > 3 Large Appliances", "Min. 2000 / Max. 4000"],
            ["Bar", "Min. 600 / Max. 1200"],
            ["Utility / Laundry", "Min. 500 / Max. 1000"],
            ["Media / Theater", "Min. 1200 / Max. 2400"],
            ["Loft / Game / Bonus", "Min. 900 / Max. 1800"],
            ["Study / Library / Office", "Min. 600 / Max. 1200"],
            ["Exercise", "Min. 600 / Max. 1200"],
            ["Add for Room with Refrigerator / Freezer", "Min. 600 / Max. 1200"]
        ],
        "notes": [
            "Use Houston/Texas internal gains.",
            "Add refrigerator/freezer load when applicable."
        ]
    },

    "STEP 12 - Save & Handoff": {
        "items": [
            {
                "title": "Save and handoff",
                "rule": "Save the load. POC will complete the PDF portion.",
                "details": [
                    "Save by plan number, not by subdivision.",
                    "Follow the folders layout.",
                    "Do not archive files.",
                    "POC will complete the PDF portion."
                ],
                "images": []
            }
        ]
    }
}

san_antonio_steps = make_placeholder_steps("San Antonio", "San_Antonio")

# ---------------- DIVISION GUIDE STORAGE ---------------- #

division_guides = {
    "Cincinnati / Dayton": cincinnati_dayton_steps,
    "Northern Kentucky": northern_kentucky_steps,
    "Columbus": columbus_steps,
    "Indianapolis": indianapolis_steps,
    "Louisville": louisville_steps,
    "Viccarone": viccarone_steps,
    "Raleigh": raleigh_steps,
    "Charlotte": charlotte_steps,
    "Mid Atlantic": mid_atlantic_steps,
    "Nashville": nashville_steps,
    "Houston": houston_steps,
    "Dallas": dallas_steps,
    "San Antonio": san_antonio_steps,
    "Austin": austin_steps
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

                if item.get("tables"):
                    for table_data in item["tables"]:
                        show_custom_table(table_data)

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
