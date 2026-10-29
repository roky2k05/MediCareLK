"""
generate_medicare_diagrams.py
Generates draw.io (.drawio) XML diagram files for MediCare LK:
1. Activity Diagram (MedicareLk_Activity_Diagram.drawio)
2. Entity-Relationship Diagram (MedicareLk_ER_Diagram.drawio)
3. Normalized Relational Schemas (MedicareLk_Normalized_Schemas.drawio)
4. Multi-page draw.io file containing all 3 (MedicareLk_System_Design_All.drawio)
5. Interactive HTML Preview (MedicareLk_Diagrams_Preview.html)
"""

import os
import html
import xml.etree.ElementTree as ET

WORKSPACE_DIR = r"c:\Users\Rasindu\AndroidStudioProjects\MedicareLk"

def escape_xml(s):
    return html.escape(str(s))

# ==============================================================================
# 1. GENERATE ACTIVITY DIAGRAM (.drawio)
# ==============================================================================
def generate_activity_diagram_xml():
    """
    Builds the Activity Diagram matching the visual layout of Image 1:
    - Lanes: AUTH, MAIN APP, BACKGROUND, EXIT
    - Nodes with precise colors matching Image 1:
      * Soft Blue: #D9E8FB (border #6C8EBF)
      * Soft Yellow/Gold: #FFF2CC (border #D6B656) for decisions
      * Soft Orange: #FFE6CC (border #D79B00)
      * Soft Green: #D5E8D4 (border #82B366)
      * Soft Purple: #E1D5E7 (border #9673A6)
      * Soft Red/Pink: #F8CECC (border #B85450)
    """
    root = ET.Element("mxGraphModel", {
        "dx": "1600", "dy": "2200", "grid": "1", "gridSize": "10",
        "guides": "1", "tooltips": "1", "connect": "1", "arrows": "1",
        "fold": "1", "page": "1", "pageScale": "1", "pageWidth": "1200", "pageHeight": "1950",
        "math": "0", "shadow": "0"
    })
    mx_root = ET.SubElement(root, "root")
    ET.SubElement(mx_root, "mxCell", {"id": "0"})
    ET.SubElement(mx_root, "mxCell", {"id": "1", "parent": "0"})

    # Title
    t_cell = ET.SubElement(mx_root, "mxCell", {
        "id": "title",
        "value": '<div style="font-family: \'Times New Roman\', serif; font-size: 26px; font-weight: bold; color: #1E293B;">Activity Diagram</div><div style="font-family: Arial, sans-serif; font-size: 11px; color: #64748B; margin-top: 3px;">MediCare LK - Doctor Channeling &amp; Patient Telemedicine System</div>',
        "style": "text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;",
        "vertex": "1", "parent": "1"
    })
    ET.SubElement(t_cell, "mxGeometry", {"x": "60", "y": "25", "width": "500", "height": "45", "as": "geometry"})

    # Partition lines (Dashed lines across the page)
    # AUTH line
    p1 = ET.SubElement(mx_root, "mxCell", {
        "id": "line_auth", "value": "",
        "style": "endArrow=none;dashed=1;html=1;dashPattern=6 6;strokeColor=#CBD5E1;strokeWidth=1.5;",
        "edge": "1", "parent": "1"
    })
    g_p1 = ET.SubElement(p1, "mxGeometry", {"width": "50", "height": "50", "relative": "1", "as": "geometry"})
    ET.SubElement(g_p1, "mxPoint", {"x": "40", "y": "220", "as": "sourcePoint"})
    ET.SubElement(g_p1, "mxPoint", {"x": "1160", "y": "220", "as": "targetPoint"})

    lbl_auth = ET.SubElement(mx_root, "mxCell", {
        "id": "lbl_auth", "value": "<b>AUTH</b>",
        "style": "text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=11;fontColor=#475569;fontFamily=Arial;",
        "vertex": "1", "parent": "1"
    })
    ET.SubElement(lbl_auth, "mxGeometry", {"x": "45", "y": "195", "width": "80", "height": "20", "as": "geometry"})

    # MAIN APP line
    p2 = ET.SubElement(mx_root, "mxCell", {
        "id": "line_main", "value": "",
        "style": "endArrow=none;dashed=1;html=1;dashPattern=6 6;strokeColor=#CBD5E1;strokeWidth=1.5;",
        "edge": "1", "parent": "1"
    })
    g_p2 = ET.SubElement(p2, "mxGeometry", {"width": "50", "height": "50", "relative": "1", "as": "geometry"})
    ET.SubElement(g_p2, "mxPoint", {"x": "40", "y": "620", "as": "sourcePoint"})
    ET.SubElement(g_p2, "mxPoint", {"x": "1160", "y": "620", "as": "targetPoint"})

    lbl_main = ET.SubElement(mx_root, "mxCell", {
        "id": "lbl_main", "value": "<b>MAIN APP</b>",
        "style": "text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=11;fontColor=#475569;fontFamily=Arial;",
        "vertex": "1", "parent": "1"
    })
    ET.SubElement(lbl_main, "mxGeometry", {"x": "45", "y": "595", "width": "90", "height": "20", "as": "geometry"})

    # BACKGROUND line
    p3 = ET.SubElement(mx_root, "mxCell", {
        "id": "line_bg", "value": "",
        "style": "endArrow=none;dashed=1;html=1;dashPattern=6 6;strokeColor=#CBD5E1;strokeWidth=1.5;",
        "edge": "1", "parent": "1"
    })
    g_p3 = ET.SubElement(p3, "mxGeometry", {"width": "50", "height": "50", "relative": "1", "as": "geometry"})
    ET.SubElement(g_p3, "mxPoint", {"x": "40", "y": "1640", "as": "sourcePoint"})
    ET.SubElement(g_p3, "mxPoint", {"x": "1160", "y": "1640", "as": "targetPoint"})

    lbl_bg = ET.SubElement(mx_root, "mxCell", {
        "id": "lbl_bg", "value": "<b>BACKGROUND</b>",
        "style": "text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=11;fontColor=#475569;fontFamily=Arial;",
        "vertex": "1", "parent": "1"
    })
    ET.SubElement(lbl_bg, "mxGeometry", {"x": "45", "y": "1615", "width": "110", "height": "20", "as": "geometry"})

    # EXIT line
    p4 = ET.SubElement(mx_root, "mxCell", {
        "id": "line_exit", "value": "",
        "style": "endArrow=none;dashed=1;html=1;dashPattern=6 6;strokeColor=#CBD5E1;strokeWidth=1.5;",
        "edge": "1", "parent": "1"
    })
    g_p4 = ET.SubElement(p4, "mxGeometry", {"width": "50", "height": "50", "relative": "1", "as": "geometry"})
    ET.SubElement(g_p4, "mxPoint", {"x": "40", "y": "1770", "as": "sourcePoint"})
    ET.SubElement(g_p4, "mxPoint", {"x": "1160", "y": "1770", "as": "targetPoint"})

    # ---------- NODES DEFINITION ----------
    # Style presets
    STYLE_START = "ellipse;fillColor=#1E293B;strokeColor=none;"
    STYLE_BLUE = "rounded=1;arcSize=10;whiteSpace=wrap;html=1;fillColor=#D9E8FB;strokeColor=#6C8EBF;strokeWidth=1.2;fontFamily=Arial;fontSize=11;fontColor=#0F172A;"
    STYLE_DECISION = "rhombus;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;strokeWidth=1.2;fontFamily=Arial;fontSize=10.5;fontColor=#0F172A;"
    STYLE_ORANGE = "rounded=1;arcSize=10;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;strokeWidth=1.2;fontFamily=Arial;fontSize=11;fontColor=#0F172A;"
    STYLE_GREEN = "rounded=1;arcSize=10;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;strokeWidth=1.2;fontFamily=Arial;fontSize=11;fontColor=#0F172A;"
    STYLE_PURPLE = "rounded=1;arcSize=10;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;strokeWidth=1.2;fontFamily=Arial;fontSize=11;fontColor=#0F172A;"
    STYLE_RED = "rounded=1;arcSize=10;whiteSpace=wrap;html=1;fillColor=#F8CECC;strokeColor=#B85450;strokeWidth=1.2;fontFamily=Arial;fontSize=11;fontColor=#0F172A;"
    STYLE_GRAY = "rounded=1;arcSize=10;whiteSpace=wrap;html=1;fillColor=#F5F5F5;strokeColor=#666666;strokeWidth=1.2;fontFamily=Arial;fontSize=11;fontColor=#0F172A;fontStyle=1;"
    STYLE_FINAL = "ellipse;html=1;shape=endState;fillColor=#1E293B;strokeColor=#1E293B;strokeWidth=2;"

    nodes = [
        # Start & Splash
        {"id": "node_start", "val": "", "style": STYLE_START, "x": 338, "y": 80, "w": 24, "h": 24},
        {"id": "act_splash", "val": "<b>Splash screen</b>", "style": STYLE_BLUE, "x": 270, "y": 120, "w": 160, "h": 36},
        {"id": "dec_logged_in", "val": "Logged in?", "style": STYLE_DECISION, "x": 305, "y": 170, "w": 90, "h": 40},

        # Auth section
        {"id": "act_enter_creds", "val": "Enter email &amp; password", "style": STYLE_BLUE, "x": 255, "y": 245, "w": 190, "h": 36},
        {"id": "act_validate_inputs", "val": "Validate inputs", "style": STYLE_ORANGE, "x": 270, "y": 300, "w": 160, "h": 34},
        {"id": "dec_valid", "val": "Valid?", "style": STYLE_DECISION, "x": 315, "y": 350, "w": 70, "h": 36},
        {"id": "act_show_field_err", "val": "Show field error", "style": STYLE_RED, "x": 110, "y": 350, "w": 130, "h": 34},
        {"id": "act_firebase_auth", "val": "<b>Firebase signInWithEmail</b>", "style": STYLE_GREEN, "x": 255, "y": 410, "w": 190, "h": 38},
        {"id": "dec_auth_success", "val": "Auth success?", "style": STYLE_DECISION, "x": 305, "y": 470, "w": 90, "h": 40},
        {"id": "act_toast_fail", "val": "Toast: auth failed", "style": STYLE_RED, "x": 110, "y": 473, "w": 130, "h": 34},

        # Register branch
        {"id": "act_register", "val": "<b>Register screen</b><br/>(name, email, phone, pwd)", "style": STYLE_PURPLE, "x": 510, "y": 265, "w": 180, "h": 44},
        {"id": "act_create_user", "val": "Create Firebase user<br/>+ save to Realtime DB &amp; SQLite", "style": STYLE_GREEN, "x": 510, "y": 330, "w": 180, "h": 46},

        # Main App Section
        {"id": "act_home", "val": "<b>Home screen</b><br/>(featured doctors + lab tests + stats)", "style": STYLE_BLUE, "x": 250, "y": 645, "w": 200, "h": 42},
        {"id": "act_bottom_nav", "val": "Bottom Nav: Home(Doctors) &bull; Book &bull; Bookings &bull; Profile", "style": STYLE_GRAY, "x": 170, "y": 715, "w": 360, "h": 32},

        # --- Column 1: BROWSE DOCTORS (Purple) ---
        {"id": "lbl_col_browse", "val": "<b style='color:#6E2D91;'>BROWSE</b>", "style": "text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;", "x": 60, "y": 765, "w": 90, "h": 18},
        {"id": "act_doc_directory", "val": "Doctor directory screen", "style": STYLE_PURPLE, "x": 30, "y": 788, "w": 150, "h": 34},
        {"id": "dec_search_query", "val": "Search / Filter?", "style": STYLE_DECISION, "x": 65, "y": 840, "w": 80, "h": 36},
        {"id": "act_load_all_docs", "val": "Load all doctors", "style": STYLE_PURPLE, "x": 15, "y": 895, "w": 85, "h": 32},
        {"id": "act_filter_results", "val": "Filter / search results", "style": STYLE_PURPLE, "x": 110, "y": 895, "w": 105, "h": 32},
        {"id": "act_select_doc", "val": "Select doctor", "style": STYLE_PURPLE, "x": 55, "y": 948, "w": 100, "h": 32},
        {"id": "act_doc_detail", "val": "Doctor detail<br/>(fee, hospital, rating)", "style": STYLE_PURPLE, "x": 40, "y": 1000, "w": 130, "h": 40},
        {"id": "act_goto_book", "val": "&rarr; Book consultation", "style": STYLE_ORANGE, "x": 45, "y": 1060, "w": 120, "h": 30},

        # --- Column 2: BOOKING FLOW (Orange/Print) ---
        {"id": "lbl_col_book", "val": "<b style='color:#D79B00;'>BOOKING</b>", "style": "text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;", "x": 350, "y": 765, "w": 90, "h": 18},
        {"id": "act_book_form", "val": "<b>Book appointment form</b>", "style": STYLE_ORANGE, "x": 320, "y": 788, "w": 150, "h": 34},
        {"id": "act_config_order", "val": "Configure booking<br/>(patient info, symptoms/notes)", "style": STYLE_ORANGE, "x": 315, "y": 840, "w": 160, "h": 38},
        {"id": "dec_consult_mode", "val": "Consultation type?", "style": STYLE_DECISION, "x": 345, "y": 898, "w": 100, "h": 38},
        {"id": "act_mode_clinic", "val": "In-Person Clinic selected", "style": STYLE_ORANGE, "x": 260, "y": 955, "w": 125, "h": 34},
        {"id": "act_mode_video", "val": "Video Telemedicine selected", "style": STYLE_ORANGE, "x": 410, "y": 955, "w": 135, "h": 34},
        {"id": "act_pick_date_slot", "val": "Pick calendar date &amp;<br/>available time slot chip", "style": STYLE_ORANGE, "x": 315, "y": 1010, "w": 160, "h": 40},
        {"id": "act_calc_fee", "val": "Calculate total fee<br/>(Doc fee + LKR 250 platform)", "style": STYLE_ORANGE, "x": 315, "y": 1070, "w": 160, "h": 38},
        {"id": "act_submit_db", "val": "<b>Submit appointment to<br/>SQLite &amp; Firebase RTDB</b>", "style": STYLE_GREEN, "x": 310, "y": 1130, "w": 170, "h": 44},
        {"id": "dec_saved", "val": "Saved?", "style": STYLE_DECISION, "x": 360, "y": 1195, "w": 70, "h": 36},
        {"id": "act_booking_err", "val": "Show error / retry", "style": STYLE_RED, "x": 450, "y": 1196, "w": 105, "h": 34},
        {"id": "act_push_notif", "val": "Push notification: order / booking placed", "style": STYLE_GREEN, "x": 290, "y": 1255, "w": 210, "h": 34},
        {"id": "act_show_receipt", "val": "Booking confirmation receipt<br/>(Unique Ref: MC-2026-XXXXX)", "style": STYLE_BLUE, "x": 295, "y": 1310, "w": 200, "h": 38},

        # --- Column 3: ORDERS / BOOKINGS (Green) ---
        {"id": "lbl_col_orders", "val": "<b style='color:#27AE60;'>BOOKINGS</b>", "style": "text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;", "x": 625, "y": 765, "w": 90, "h": 18},
        {"id": "act_orders_list", "val": "<b>My bookings list</b><br/>(Upcoming, Completed, Cancelled)", "style": STYLE_GREEN, "x": 585, "y": 788, "w": 170, "h": 38},
        {"id": "act_tap_order", "val": "Tap an appointment card", "style": STYLE_GREEN, "x": 600, "y": 846, "w": 140, "h": 32},
        {"id": "act_order_detail", "val": "Appointment detail<br/>(status, specs, total)", "style": STYLE_GREEN, "x": 595, "y": 898, "w": 150, "h": 38},
        {"id": "dec_can_manage", "val": "Upcoming &amp;<br/>active?", "style": STYLE_DECISION, "x": 630, "y": 955, "w": 80, "h": 40},
        {"id": "act_manage_choice", "val": "Reschedule / Cancel booking", "style": STYLE_ORANGE, "x": 595, "y": 1015, "w": 150, "h": 34},
        {"id": "act_track_order", "val": "View consultation record<br/>(Confirmed &rarr; Completed)", "style": STYLE_GREEN, "x": 600, "y": 1075, "w": 140, "h": 38},
        {"id": "act_notif_status", "val": "Notify on status change", "style": STYLE_GREEN, "x": 605, "y": 1133, "w": 130, "h": 30},

        # --- Column 4: PROFILE (Red/Pink) ---
        {"id": "lbl_col_profile", "val": "<b style='color:#C0392B;'>PROFILE</b>", "style": "text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=10;", "x": 860, "y": 765, "w": 90, "h": 18},
        {"id": "act_profile_screen", "val": "<b>Profile screen</b>", "style": STYLE_RED, "x": 830, "y": 788, "w": 150, "h": 34},
        {"id": "act_edit_profile", "val": "Edit profile<br/>(name, phone, photo)", "style": STYLE_RED, "x": 760, "y": 850, "w": 115, "h": 38},
        {"id": "act_logout", "val": "<b>Logout</b>", "style": STYLE_RED, "x": 890, "y": 852, "w": 70, "h": 32},
        {"id": "act_edit_address", "val": "Edit medical info<br/>(allergies, conditions)", "style": STYLE_RED, "x": 975, "y": 850, "w": 125, "h": 38},
        {"id": "act_save_prof_db", "val": "Save to Firebase", "style": STYLE_GREEN, "x": 765, "y": 908, "w": 105, "h": 28},
        {"id": "act_firebase_signout", "val": "Firebase signOut<br/>&rarr; Back to Login", "style": STYLE_GREEN, "x": 880, "y": 904, "w": 90, "h": 36},
        {"id": "act_save_med_db", "val": "Save to Firebase", "style": STYLE_GREEN, "x": 985, "y": 908, "w": 105, "h": 28},

        # Background Section
        {"id": "act_workmanager", "val": "<b>WorkManager: ReminderWorker</b><br/>(periodic sync / upcoming alert every 24h)", "style": STYLE_GREEN, "x": 260, "y": 1670, "w": 220, "h": 44},
        {"id": "act_bg_push", "val": "Push: appointment reminder / wellness notification", "style": STYLE_GREEN, "x": 510, "y": 1675, "w": 220, "h": 34},

        # Final State
        {"id": "act_session_exit", "val": "Session active / exit", "style": "rounded=1;arcSize=10;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#94A3B8;strokeWidth=1;fontFamily=Arial;fontSize=10;fontColor=#475569;", "x": 300, "y": 1805, "w": 120, "h": 28},
        {"id": "node_final", "val": "", "style": STYLE_FINAL, "x": 348, "y": 1855, "w": 24, "h": 24}
    ]

    for n in nodes:
        c = ET.SubElement(mx_root, "mxCell", {
            "id": n["id"], "value": n["val"], "style": n["style"],
            "vertex": "1", "parent": "1"
        })
        ET.SubElement(c, "mxGeometry", {
            "x": str(n["x"]), "y": str(n["y"]),
            "width": str(n["w"]), "height": str(n["h"]),
            "as": "geometry"
        })

    # ---------- EDGES / TRANSITIONS ----------
    STYLE_EDGE = "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#334155;strokeWidth=1.2;fontFamily=Arial;fontSize=10;fontColor=#1E293B;"

    edges = [
        # Start -> Splash -> Logged In?
        {"id": "e_start_splash", "src": "node_start", "tgt": "act_splash", "lbl": ""},
        {"id": "e_splash_dec", "src": "act_splash", "tgt": "dec_logged_in", "lbl": ""},
        {"id": "e_logged_no", "src": "dec_logged_in", "tgt": "act_enter_creds", "lbl": "No"},
        {"id": "e_logged_yes", "src": "dec_logged_in", "tgt": "act_home", "lbl": "Yes", "exitX": "1", "exitY": "0.5", "entryX": "0.8", "entryY": "0"},

        # Login flow
        {"id": "e_creds_val", "src": "act_enter_creds", "tgt": "act_validate_inputs", "lbl": ""},
        {"id": "e_val_dec", "src": "act_validate_inputs", "tgt": "dec_valid", "lbl": ""},
        {"id": "e_valid_no", "src": "dec_valid", "tgt": "act_show_field_err", "lbl": "No"},
        {"id": "e_err_loop", "src": "act_show_field_err", "tgt": "act_enter_creds", "lbl": "", "exitX": "0.5", "exitY": "0", "entryX": "0", "entryY": "0.5"},
        {"id": "e_valid_yes", "src": "dec_valid", "tgt": "act_firebase_auth", "lbl": "Yes"},
        {"id": "e_auth_dec", "src": "act_firebase_auth", "tgt": "dec_auth_success", "lbl": ""},
        {"id": "e_auth_fail", "src": "dec_auth_success", "tgt": "act_toast_fail", "lbl": "Fail"},
        {"id": "e_fail_loop", "src": "act_toast_fail", "tgt": "act_enter_creds", "lbl": "", "exitX": "0.5", "exitY": "0", "entryX": "0", "entryY": "0.5"},
        {"id": "e_auth_ok", "src": "dec_auth_success", "tgt": "act_home", "lbl": "OK"},

        # Register branch
        {"id": "e_no_account", "src": "act_enter_creds", "tgt": "act_register", "lbl": "No account?"},
        {"id": "e_reg_create", "src": "act_register", "tgt": "act_create_user", "lbl": ""},
        {"id": "e_create_home", "src": "act_create_user", "tgt": "act_home", "lbl": "", "exitX": "0.5", "exitY": "1", "entryX": "0.9", "entryY": "0"},

        # Home & Bottom Nav
        {"id": "e_home_nav", "src": "act_home", "tgt": "act_bottom_nav", "lbl": ""},

        # Branches from Bottom Nav
        {"id": "e_nav_browse", "src": "act_bottom_nav", "tgt": "act_doc_directory", "lbl": "", "exitX": "0.1", "exitY": "1", "entryX": "0.5", "entryY": "0"},
        {"id": "e_nav_book", "src": "act_bottom_nav", "tgt": "act_book_form", "lbl": "", "exitX": "0.4", "exitY": "1", "entryX": "0.5", "entryY": "0"},
        {"id": "e_nav_orders", "src": "act_bottom_nav", "tgt": "act_orders_list", "lbl": "", "exitX": "0.7", "exitY": "1", "entryX": "0.5", "entryY": "0"},
        {"id": "e_nav_profile", "src": "act_bottom_nav", "tgt": "act_profile_screen", "lbl": "", "exitX": "0.95", "exitY": "1", "entryX": "0.5", "entryY": "0"},

        # Column 1: Browse
        {"id": "e_dir_dec", "src": "act_doc_directory", "tgt": "dec_search_query", "lbl": ""},
        {"id": "e_search_no", "src": "dec_search_query", "tgt": "act_load_all_docs", "lbl": "No"},
        {"id": "e_search_yes", "src": "dec_search_query", "tgt": "act_filter_results", "lbl": "Yes"},
        {"id": "e_load_select", "src": "act_load_all_docs", "tgt": "act_select_doc", "lbl": ""},
        {"id": "e_filter_select", "src": "act_filter_results", "tgt": "act_select_doc", "lbl": ""},
        {"id": "e_select_detail", "src": "act_select_doc", "tgt": "act_doc_detail", "lbl": ""},
        {"id": "e_detail_bookbtn", "src": "act_doc_detail", "tgt": "act_goto_book", "lbl": ""},
        {"id": "e_bookbtn_form", "src": "act_goto_book", "tgt": "act_book_form", "lbl": "", "exitX": "1", "exitY": "0.5", "entryX": "0", "entryY": "0.5"},

        # Column 2: Booking Form
        {"id": "e_form_config", "src": "act_book_form", "tgt": "act_config_order", "lbl": ""},
        {"id": "e_config_mode", "src": "act_config_order", "tgt": "dec_consult_mode", "lbl": ""},
        {"id": "e_mode_clinic", "src": "dec_consult_mode", "tgt": "act_mode_clinic", "lbl": "In-Person"},
        {"id": "e_mode_video", "src": "dec_consult_mode", "tgt": "act_mode_video", "lbl": "Telemedicine"},
        {"id": "e_clinic_slot", "src": "act_mode_clinic", "tgt": "act_pick_date_slot", "lbl": ""},
        {"id": "e_video_slot", "src": "act_mode_video", "tgt": "act_pick_date_slot", "lbl": ""},
        {"id": "e_slot_fee", "src": "act_pick_date_slot", "tgt": "act_calc_fee", "lbl": ""},
        {"id": "e_fee_submit", "src": "act_calc_fee", "tgt": "act_submit_db", "lbl": ""},
        {"id": "e_submit_saved", "src": "act_submit_db", "tgt": "dec_saved", "lbl": ""},
        {"id": "e_saved_fail", "src": "dec_saved", "tgt": "act_booking_err", "lbl": "Fail"},
        {"id": "e_saved_ok", "src": "dec_saved", "tgt": "act_push_notif", "lbl": "OK"},
        {"id": "e_notif_receipt", "src": "act_push_notif", "tgt": "act_show_receipt", "lbl": ""},

        # Column 3: Bookings
        {"id": "e_orders_tap", "src": "act_orders_list", "tgt": "act_tap_order", "lbl": ""},
        {"id": "e_tap_detail", "src": "act_tap_order", "tgt": "act_order_detail", "lbl": ""},
        {"id": "e_detail_can", "src": "act_order_detail", "tgt": "dec_can_manage", "lbl": ""},
        {"id": "e_can_yes", "src": "dec_can_manage", "tgt": "act_manage_choice", "lbl": "Yes"},
        {"id": "e_can_no", "src": "dec_can_manage", "tgt": "act_track_order", "lbl": "No", "exitX": "1", "exitY": "0.5", "entryX": "1", "entryY": "0.5"},
        {"id": "e_manage_loop", "src": "act_manage_choice", "tgt": "act_book_form", "lbl": "Edit &rarr;", "exitX": "0", "exitY": "0.5", "entryX": "1", "entryY": "0.5"},
        {"id": "e_track_notif", "src": "act_track_order", "tgt": "act_notif_status", "lbl": ""},

        # Column 4: Profile
        {"id": "e_prof_edit", "src": "act_profile_screen", "tgt": "act_edit_profile", "lbl": ""},
        {"id": "e_prof_logout", "src": "act_profile_screen", "tgt": "act_logout", "lbl": ""},
        {"id": "e_prof_addr", "src": "act_profile_screen", "tgt": "act_edit_address", "lbl": ""},
        {"id": "e_save_prof", "src": "act_edit_profile", "tgt": "act_save_prof_db", "lbl": ""},
        {"id": "e_logout_so", "src": "act_logout", "tgt": "act_firebase_signout", "lbl": ""},
        {"id": "e_so_login", "src": "act_firebase_signout", "tgt": "act_enter_creds", "lbl": "Back to login", "exitX": "0.5", "exitY": "1", "entryX": "1", "entryY": "0.5"},
        {"id": "e_save_med", "src": "act_edit_address", "tgt": "act_save_med_db", "lbl": ""},

        # Background
        {"id": "e_worker_push", "src": "act_workmanager", "tgt": "act_bg_push", "lbl": ""},

        # Exit
        {"id": "e_exit_final", "src": "act_session_exit", "tgt": "node_final", "lbl": ""}
    ]

    for e in edges:
        edge_style = STYLE_EDGE
        if "exitX" in e:
            edge_style += f"exitX={e['exitX']};exitY={e['exitY']};"
        if "entryX" in e:
            edge_style += f"entryX={e['entryX']};entryY={e['entryY']};"
        c = ET.SubElement(mx_root, "mxCell", {
            "id": e["id"], "value": e["lbl"], "style": edge_style,
            "edge": "1", "parent": "1", "source": e["src"], "target": e["tgt"]
        })
        ET.SubElement(c, "mxGeometry", {"relative": "1", "as": "geometry"})

    xml_str = ET.tostring(root, encoding="utf-8").decode("utf-8")
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net" agent="Antigravity" version="21.0.0" type="device">
  <diagram id="medicare_activity" name="Activity Diagram">
    {xml_str}
  </diagram>
</mxfile>"""

# ==============================================================================
# 2. GENERATE ER DIAGRAM (.drawio)
# ==============================================================================
def generate_er_diagram_xml():
    """
    Builds the Entity-Relationship (ER) Diagram matching the visual layout of Image 2:
    - Dark Navy rectangular Entity boxes: #1B365D (white text, bold, rounded=0)
    - Dark Navy diamond Relationship boxes: #1B365D (white text, bold, rhombus)
    - Dark Navy oval Attribute bubbles: #1B365D (white text, ellipse)
      with (PK) and (FK) indicators.
    - Cardinality labels ('1', 'N', 'M') on the lines.
    - Background: clean ivory #FFFDF9 / sterile white.
    """
    root = ET.Element("mxGraphModel", {
        "dx": "1600", "dy": "1800", "grid": "1", "gridSize": "10",
        "guides": "1", "tooltips": "1", "connect": "1", "arrows": "1",
        "fold": "1", "page": "1", "pageScale": "1", "pageWidth": "1400", "pageHeight": "1200",
        "math": "0", "shadow": "0"
    })
    mx_root = ET.SubElement(root, "root")
    ET.SubElement(mx_root, "mxCell", {"id": "0"})
    ET.SubElement(mx_root, "mxCell", {"id": "1", "parent": "0"})

    # Title
    t_cell = ET.SubElement(mx_root, "mxCell", {
        "id": "er_title",
        "value": '<div style="font-family: \'Times New Roman\', serif; font-size: 26px; font-weight: bold; color: #1E293B;">ER Diagram</div><div style="font-family: Arial, sans-serif; font-size: 11px; color: #64748B; margin-top: 3px;">MediCare LK - Entity-Relationship Conceptual Model (Chen / Crow\'s Foot Hybrid)</div>',
        "style": "text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;",
        "vertex": "1", "parent": "1"
    })
    ET.SubElement(t_cell, "mxGeometry", {"x": "60", "y": "25", "width": "600", "height": "45", "as": "geometry"})

    # Styles matching Image 2
    STYLE_ENTITY = "rounded=0;whiteSpace=wrap;html=1;fillColor=#1B365D;strokeColor=#0F2038;fontColor=#FFFFFF;fontFamily=Arial;fontSize=13;fontStyle=1;"
    STYLE_REL = "rhombus;whiteSpace=wrap;html=1;fillColor=#1B365D;strokeColor=#0F2038;fontColor=#FFFFFF;fontFamily=Arial;fontSize=10;fontStyle=1;"
    STYLE_ATTR = "ellipse;whiteSpace=wrap;html=1;fillColor=#1B365D;strokeColor=#0F2038;fontColor=#FFFFFF;fontFamily=Arial;fontSize=9.5;align=center;"
    STYLE_CARD = "edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=11;fontColor=#1E293B;fontStyle=1;fontFamily=Arial;"
    STYLE_LINE = "endArrow=none;html=1;strokeColor=#475569;strokeWidth=1.2;"

    # ENTITIES
    entities = [
        {"id": "ent_user", "val": "User", "x": 190, "y": 300, "w": 140, "h": 44},
        {"id": "ent_doctor", "val": "Doctor", "x": 680, "y": 270, "w": 140, "h": 44},
        {"id": "ent_category", "val": "Specialization", "x": 980, "y": 370, "w": 140, "h": 44},
        {"id": "ent_sizes", "val": "Doctor_Availability", "x": 570, "y": 145, "w": 150, "h": 40},
        {"id": "ent_materials", "val": "Hospital_Branch", "x": 790, "y": 145, "w": 150, "h": 40},
        {"id": "ent_order", "val": "Appointment", "x": 680, "y": 560, "w": 140, "h": 44},
        {"id": "ent_notif", "val": "Notification", "x": 190, "y": 520, "w": 140, "h": 44},
        {"id": "ent_status", "val": "AppointmentStatus", "x": 190, "y": 740, "w": 150, "h": 44},
        {"id": "ent_delivery", "val": "ConsultationType", "x": 680, "y": 780, "w": 150, "h": 44},
    ]

    for e in entities:
        c = ET.SubElement(mx_root, "mxCell", {
            "id": e["id"], "value": e["val"], "style": STYLE_ENTITY,
            "vertex": "1", "parent": "1"
        })
        ET.SubElement(c, "mxGeometry", {
            "x": str(e["x"]), "y": str(e["y"]), "width": str(e["w"]), "height": str(e["h"]), "as": "geometry"
        })

    # RELATIONSHIPS (Diamonds)
    relationships = [
        {"id": "rel_receives", "val": "RECEIVES", "x": 225, "y": 420, "w": 70, "h": 50},
        {"id": "rel_places", "val": "PLACES", "x": 465, "y": 435, "w": 75, "h": 55},
        {"id": "rel_triggers", "val": "TRIGGERS", "x": 425, "y": 535, "w": 75, "h": 55},
        {"id": "rel_contains", "val": "SCHEDULED<br/>FOR", "x": 710, "y": 415, "w": 80, "h": 55},
        {"id": "rel_belongs", "val": "BELONGS<br/>TO", "x": 880, "y": 290, "w": 75, "h": 55},
        {"id": "rel_status", "val": "HAS<br/>STATUS", "x": 440, "y": 660, "w": 75, "h": 55},
        {"id": "rel_delivery", "val": "HAS<br/>MODE", "x": 715, "y": 680, "w": 70, "h": 50},
    ]

    for r in relationships:
        c = ET.SubElement(mx_root, "mxCell", {
            "id": r["id"], "value": r["val"], "style": STYLE_REL,
            "vertex": "1", "parent": "1"
        })
        ET.SubElement(c, "mxGeometry", {
            "x": str(r["x"]), "y": str(r["y"]), "width": str(r["w"]), "height": str(r["h"]), "as": "geometry"
        })

    # ATTRIBUTES (Ovals)
    # User attributes
    user_attrs = [
        ("u_id", "id (PK)", 235, 195, 75, 30),
        ("u_name", "name", 85, 260, 75, 30),
        ("u_email", "email", 85, 300, 75, 30),
        ("u_phone", "phone", 95, 345, 75, 30),
        ("u_addr", "address", 235, 375, 80, 30),
        ("u_nic", "nic", 115, 220, 75, 30),
        ("u_allergies", "allergies", 355, 230, 80, 30),
        ("u_blood", "blood_group", 350, 340, 85, 30),
    ]

    # Doctor attributes
    doc_attrs = [
        ("d_id", "id (PK)", 505, 195, 75, 30),
        ("d_name", "name", 535, 240, 75, 30),
        ("d_desc", "about", 530, 285, 75, 30),
        ("d_price", "fee", 595, 310, 75, 30),
        ("d_hosp", "hospital", 715, 220, 80, 30),
        ("d_spec", "specialization", 830, 220, 95, 30),
    ]

    # Category attributes
    cat_attrs = [
        ("c_id", "id (PK)", 1070, 430, 75, 30),
        ("c_name", "name", 915, 430, 75, 30),
        ("c_icon", "icon", 995, 460, 75, 30),
    ]

    # Sizes / Availability attributes
    size_attrs = [
        ("s_id", "id (PK)", 470, 115, 75, 30),
        ("s_pid", "doctor_id (FK)", 555, 95, 95, 30),
        ("s_size", "time_slot", 670, 105, 80, 30),
    ]

    # Materials / Hospital Branch attributes
    mat_attrs = [
        ("m_pid", "doctor_id (FK)", 805, 95, 95, 30),
        ("m_id", "id (PK)", 920, 115, 75, 30),
        ("m_mat", "hospital_name", 945, 175, 95, 30),
    ]

    # Appointment attributes (Central Order Entity)
    appt_attrs = [
        ("a_id", "id (PK)", 540, 505, 75, 30),
        ("a_ref", "reference_no", 515, 570, 90, 30),
        ("a_uid", "user_id (FK)", 520, 615, 85, 30),
        ("a_did", "doctor_id (FK)", 560, 655, 95, 30),
        ("a_date", "appointment_date", 615, 475, 110, 30),
        ("a_slot", "time_slot", 745, 475, 85, 30),
        ("a_mode", "consultation_type", 830, 505, 110, 30),
        ("a_pname", "patient_name", 850, 545, 95, 30),
        ("a_fee", "total_fee", 845, 590, 80, 30),
        ("a_stat", "status", 805, 635, 80, 30),
        ("a_created", "created_at", 715, 640, 80, 30),
    ]

    # Notification attributes
    notif_attrs = [
        ("n_id", "id (PK)", 85, 450, 75, 30),
        ("n_uid", "user_id (FK)", 25, 485, 85, 30),
        ("n_aid", "appointment_id (FK)", 15, 530, 120, 30),
        ("n_date", "date", 65, 580, 70, 30),
        ("n_msg", "message", 140, 600, 75, 30),
        ("n_title", "title", 220, 595, 75, 30),
    ]

    # Status attributes
    stat_attrs = [
        ("st_id", "id (PK)", 65, 705, 75, 30),
        ("st_name", "name", 50, 765, 75, 30),
        ("st_up", "Upcoming", 85, 810, 85, 30),
        ("st_can", "Cancelled", 190, 815, 80, 30),
        ("st_comp", "Completed", 280, 810, 85, 30),
    ]

    # Delivery / Mode attributes
    deliv_attrs = [
        ("dl_id", "id (PK)", 565, 795, 75, 30),
        ("dl_name", "name", 630, 860, 75, 30),
        ("dl_clinic", "In-Person Clinic", 725, 860, 105, 30),
        ("dl_video", "Telemedicine", 845, 850, 95, 30),
    ]

    all_attr_groups = [
        (user_attrs, "ent_user"),
        (doc_attrs, "ent_doctor"),
        (cat_attrs, "ent_category"),
        (size_attrs, "ent_sizes"),
        (mat_attrs, "ent_materials"),
        (appt_attrs, "ent_order"),
        (notif_attrs, "ent_notif"),
        (stat_attrs, "ent_status"),
        (deliv_attrs, "ent_delivery"),
    ]

    for attrs, parent_ent in all_attr_groups:
        for a_id, a_val, ax, ay, aw, ah in attrs:
            c = ET.SubElement(mx_root, "mxCell", {
                "id": a_id, "value": a_val, "style": STYLE_ATTR,
                "vertex": "1", "parent": "1"
            })
            ET.SubElement(c, "mxGeometry", {
                "x": str(ax), "y": str(ay), "width": str(aw), "height": str(ah), "as": "geometry"
            })

            # Line to parent entity
            line = ET.SubElement(mx_root, "mxCell", {
                "id": f"l_{a_id}", "value": "", "style": STYLE_LINE,
                "edge": "1", "parent": "1", "source": parent_ent, "target": a_id
            })
            ET.SubElement(line, "mxGeometry", {"relative": "1", "as": "geometry"})

    # CONNECTIONS BETWEEN ENTITIES AND RELATIONSHIPS
    entity_rel_edges = [
        # User -> RECEIVES -> Notification
        {"id": "e_u_rec", "src": "ent_user", "tgt": "rel_receives", "card": "1"},
        {"id": "e_rec_n", "src": "rel_receives", "tgt": "ent_notif", "card": "N"},

        # User -> PLACES -> Appointment
        {"id": "e_u_pla", "src": "ent_user", "tgt": "rel_places", "card": "1"},
        {"id": "e_pla_a", "src": "rel_places", "tgt": "ent_order", "card": "N"},

        # Appointment -> TRIGGERS -> Notification
        {"id": "e_a_trig", "src": "ent_order", "tgt": "rel_triggers", "card": "1"},
        {"id": "e_trig_n", "src": "rel_triggers", "tgt": "ent_notif", "card": "N"},

        # Doctor -> SCHEDULED FOR -> Appointment
        {"id": "e_d_cont", "src": "ent_doctor", "tgt": "rel_contains", "card": "1"},
        {"id": "e_cont_a", "src": "rel_contains", "tgt": "ent_order", "card": "N"},

        # Doctor -> BELONGS TO -> Category (Specialization)
        {"id": "e_d_bel", "src": "ent_doctor", "tgt": "rel_belongs", "card": "N"},
        {"id": "e_bel_c", "src": "rel_belongs", "tgt": "ent_category", "card": "1"},

        # Doctor -> Availability (Sizes)
        {"id": "e_d_sizes", "src": "ent_doctor", "tgt": "ent_sizes", "card": "1 : N"},

        # Doctor -> Hospital Branch (Materials)
        {"id": "e_d_mat", "src": "ent_doctor", "tgt": "ent_materials", "card": "1 : N"},

        # Appointment -> HAS STATUS -> AppointmentStatus
        {"id": "e_a_stat", "src": "ent_order", "tgt": "rel_status", "card": "N"},
        {"id": "e_stat_st", "src": "rel_status", "tgt": "ent_status", "card": "1"},

        # Appointment -> HAS MODE -> ConsultationType
        {"id": "e_a_del", "src": "ent_order", "tgt": "rel_delivery", "card": "N"},
        {"id": "e_del_dl", "src": "rel_delivery", "tgt": "ent_delivery", "card": "1"},
    ]

    for er in entity_rel_edges:
        edge = ET.SubElement(mx_root, "mxCell", {
            "id": er["id"], "value": "", "style": STYLE_LINE,
            "edge": "1", "parent": "1", "source": er["src"], "target": er["tgt"]
        })
        ET.SubElement(edge, "mxGeometry", {"relative": "1", "as": "geometry"})

        if er.get("card"):
            card = ET.SubElement(mx_root, "mxCell", {
                "id": f"card_{er['id']}", "value": er["card"], "style": STYLE_CARD,
                "vertex": "1", "connectable": "0", "parent": er["id"]
            })
            ET.SubElement(card, "mxGeometry", {"x": "0.1", "y": "0", "relative": "1", "as": "geometry"})

    xml_str = ET.tostring(root, encoding="utf-8").decode("utf-8")
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net" agent="Antigravity" version="21.0.0" type="device">
  <diagram id="medicare_er" name="ER Diagram">
    {xml_str}
  </diagram>
</mxfile>"""

# ==============================================================================
# 3. GENERATE NORMALIZED RELATIONAL SCHEMAS (.drawio)
# ==============================================================================
def generate_normalized_schemas_xml():
    """
    Builds the Normalized Relational Schemas diagram matching Image 3:
    - Tables represented as horizontal rectangular rows of cells
    - Title above each table (e.g., 'User', 'Specialization', 'Doctor', 'Doctor_Time_Slot', 'Order/Appointment')
    - Primary keys underlined (<u>PK</u>)
    - Foreign keys dashed underlined (<span style="border-bottom: 1px dashed black;">FK</span>)
    - Orthogonal connector arrows with arrowheads pointing from Foreign Keys up to Primary Keys of parent tables!
    """
    root = ET.Element("mxGraphModel", {
        "dx": "1600", "dy": "1800", "grid": "1", "gridSize": "10",
        "guides": "1", "tooltips": "1", "connect": "1", "arrows": "1",
        "fold": "1", "page": "1", "pageScale": "1", "pageWidth": "1400", "pageHeight": "1100",
        "math": "0", "shadow": "0"
    })
    mx_root = ET.SubElement(root, "root")
    ET.SubElement(mx_root, "mxCell", {"id": "0"})
    ET.SubElement(mx_root, "mxCell", {"id": "1", "parent": "0"})

    # Title
    t_cell = ET.SubElement(mx_root, "mxCell", {
        "id": "schema_title",
        "value": '<div style="font-family: \'Times New Roman\', serif; font-size: 26px; font-weight: bold; color: #1E293B;">Normalized Relational Schemas</div><div style="font-family: Arial, sans-serif; font-size: 11px; color: #64748B; margin-top: 3px;">MediCare LK - Third Normal Form (3NF) Relational Database Schema &amp; Referential Integrity</div>',
        "style": "text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;",
        "vertex": "1", "parent": "1"
    })
    ET.SubElement(t_cell, "mxGeometry", {"x": "60", "y": "25", "width": "750", "height": "45", "as": "geometry"})

    STYLE_TBL_NAME = "text;html=1;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontFamily=Arial;fontSize=12;fontStyle=1;fontColor=#0F172A;"
    STYLE_CELL = "rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#475569;strokeWidth=1;fontFamily=Arial;fontSize=11;fontColor=#0F172A;align=center;"
    STYLE_REF_EDGE = "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#475569;strokeWidth=1.2;endArrow=classic;endFill=1;"

    # Schema definition
    # 1. User
    # 2. Specialization (Category in sample)
    # 3. Doctor (Product in sample)
    # 4. Doctor_Time_Slot (Product_Material in sample)
    # 5. Doctor_Hospital (Product_Size in sample)
    # 6. Appointment (Order in sample)
    # 7. Notification (Notification in sample)

    tables = [
        {
            "name": "User", "table_id": "tbl_user",
            "x": 60, "y": 100,
            "columns": [
                {"id": "u_pk", "name": "<u>User_ID</u>", "w": 90, "is_pk": True},
                {"id": "u_name", "name": "Name", "w": 90},
                {"id": "u_email", "name": "Email", "w": 110},
                {"id": "u_phone", "name": "Phone", "w": 90},
                {"id": "u_nic", "name": "NIC", "w": 85},
                {"id": "u_blood", "name": "Blood_Group", "w": 95},
                {"id": "u_addr", "name": "Address", "w": 110},
            ]
        },
        {
            "name": "Specialization", "table_id": "tbl_spec",
            "x": 60, "y": 200,
            "columns": [
                {"id": "s_pk", "name": "<u>Specialization_ID</u>", "w": 130, "is_pk": True},
                {"id": "s_name", "name": "Name", "w": 100},
                {"id": "s_icon", "name": "Icon_URL", "w": 100},
                {"id": "s_desc", "name": "Description", "w": 120},
            ]
        },
        {
            "name": "Doctor", "table_id": "tbl_doc",
            "x": 60, "y": 300,
            "columns": [
                {"id": "d_pk", "name": "<u>Doctor_ID</u>", "w": 90, "is_pk": True},
                {"id": "d_fk_spec", "name": "<span style='border-bottom: 1px dashed black;'>Specialization_ID</span>", "w": 130, "is_fk": True},
                {"id": "d_name", "name": "Name", "w": 90},
                {"id": "d_qual", "name": "Qualification", "w": 95},
                {"id": "d_exp", "name": "Experience", "w": 85},
                {"id": "d_fee", "name": "Fee", "w": 75},
                {"id": "d_hosp", "name": "Hospital", "w": 95},
                {"id": "d_city", "name": "City", "w": 75},
            ]
        },
        {
            "name": "Doctor_Time_Slot", "table_id": "tbl_slot",
            "x": 60, "y": 420,
            "columns": [
                {"id": "sl_fk_doc", "name": "<span style='border-bottom: 1px dashed black;'>Doctor_ID</span>", "w": 90, "is_fk": True},
                {"id": "sl_day", "name": "<u>Day_Of_Week</u>", "w": 100, "is_pk": True},
                {"id": "sl_time", "name": "<u>Time_Slot</u>", "w": 100, "is_pk": True},
            ]
        },
        {
            "name": "Doctor_Hospital_Branch", "table_id": "tbl_hosp_branch",
            "x": 60, "y": 540,
            "columns": [
                {"id": "hb_fk_doc", "name": "<span style='border-bottom: 1px dashed black;'>Doctor_ID</span>", "w": 90, "is_fk": True},
                {"id": "hb_name", "name": "<u>Branch_Name</u>", "w": 110, "is_pk": True},
                {"id": "hb_city", "name": "City", "w": 85},
            ]
        },
        {
            "name": "Appointment", "table_id": "tbl_appt",
            "x": 60, "y": 660,
            "columns": [
                {"id": "a_pk", "name": "<u>Appointment_ID</u>", "w": 115, "is_pk": True},
                {"id": "a_ref", "name": "Reference_No", "w": 105},
                {"id": "a_fk_u", "name": "<span style='border-bottom: 1px dashed black;'>User_ID</span>", "w": 85, "is_fk": True},
                {"id": "a_fk_d", "name": "<span style='border-bottom: 1px dashed black;'>Doctor_ID</span>", "w": 85, "is_fk": True},
                {"id": "a_date", "name": "Appointment_Date", "w": 115},
                {"id": "a_slot", "name": "Time_Slot", "w": 85},
                {"id": "a_mode", "name": "Consultation_Type", "w": 115},
                {"id": "a_fee", "name": "Total_Fee", "w": 85},
                {"id": "a_status", "name": "Status", "w": 75},
                {"id": "a_pname", "name": "Patient_Name", "w": 95},
                {"id": "a_created", "name": "Created_At", "w": 85},
            ]
        },
        {
            "name": "Notification", "table_id": "tbl_notif",
            "x": 60, "y": 780,
            "columns": [
                {"id": "n_pk", "name": "<u>Notification_ID</u>", "w": 110, "is_pk": True},
                {"id": "n_fk_u", "name": "<span style='border-bottom: 1px dashed black;'>User_ID</span>", "w": 85, "is_fk": True},
                {"id": "n_fk_a", "name": "<span style='border-bottom: 1px dashed black;'>Appointment_ID</span>", "w": 115, "is_fk": True},
                {"id": "n_title", "name": "Title", "w": 85},
                {"id": "n_message", "name": "Message", "w": 100},
                {"id": "n_date", "name": "Date", "w": 75},
                {"id": "n_read", "name": "Is_Read", "w": 70},
            ]
        }
    ]

    for t in tables:
        # Table Title
        lbl = ET.SubElement(mx_root, "mxCell", {
            "id": f"lbl_{t['table_id']}", "value": f"<b>{t['name']}</b>",
            "style": STYLE_TBL_NAME, "vertex": "1", "parent": "1"
        })
        ET.SubElement(lbl, "mxGeometry", {"x": str(t["x"]), "y": str(t["y"] - 22), "width": "200", "height": "20", "as": "geometry"})

        # Cells
        curr_x = t["x"]
        for col in t["columns"]:
            c = ET.SubElement(mx_root, "mxCell", {
                "id": col["id"], "value": col["name"], "style": STYLE_CELL,
                "vertex": "1", "parent": "1"
            })
            ET.SubElement(c, "mxGeometry", {
                "x": str(curr_x), "y": str(t["y"]), "width": str(col["w"]), "height": "34", "as": "geometry"
            })
            curr_x += col["w"]

    # Referential Integrity Arrows (Foreign Key -> Primary Key)
    # Exactly as in Image 3
    ref_edges = [
        # Doctor.Specialization_ID -> Specialization.Specialization_ID
        {"id": "ref_doc_spec", "src": "d_fk_spec", "tgt": "s_pk",
         "exitX": "0.5", "exitY": "0", "entryX": "0.5", "entryY": "1"},

        # Doctor_Time_Slot.Doctor_ID -> Doctor.Doctor_ID
        {"id": "ref_slot_doc", "src": "sl_fk_doc", "tgt": "d_pk",
         "exitX": "0.2", "exitY": "0", "entryX": "0.2", "entryY": "1"},

        # Doctor_Hospital_Branch.Doctor_ID -> Doctor.Doctor_ID
        {"id": "ref_branch_doc", "src": "hb_fk_doc", "tgt": "d_pk",
         "exitX": "0.5", "exitY": "0", "entryX": "0.5", "entryY": "1"},

        # Appointment.User_ID -> User.User_ID
        {"id": "ref_appt_user", "src": "a_fk_u", "tgt": "u_pk",
         "exitX": "0", "exitY": "0.5", "entryX": "0", "entryY": "0.5"},

        # Appointment.Doctor_ID -> Doctor.Doctor_ID
        {"id": "ref_appt_doc", "src": "a_fk_d", "tgt": "d_pk",
         "exitX": "0.8", "exitY": "0", "entryX": "0.8", "entryY": "1"},

        # Notification.User_ID -> User.User_ID
        {"id": "ref_notif_user", "src": "n_fk_u", "tgt": "u_pk",
         "exitX": "0", "exitY": "0.5", "entryX": "0", "entryY": "0.5"},

        # Notification.Appointment_ID -> Appointment.Appointment_ID
        {"id": "ref_notif_appt", "src": "n_fk_a", "tgt": "a_pk",
         "exitX": "0.5", "exitY": "0", "entryX": "0.5", "entryY": "1"},
    ]

    for re in ref_edges:
        style = f"{STYLE_REF_EDGE}exitX={re['exitX']};exitY={re['exitY']};entryX={re['entryX']};entryY={re['entryY']};"
        edge = ET.SubElement(mx_root, "mxCell", {
            "id": re["id"], "value": "", "style": style,
            "edge": "1", "parent": "1", "source": re["src"], "target": re["tgt"]
        })
        ET.SubElement(edge, "mxGeometry", {"relative": "1", "as": "geometry"})

    xml_str = ET.tostring(root, encoding="utf-8").decode("utf-8")
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net" agent="Antigravity" version="21.0.0" type="device">
  <diagram id="medicare_schemas" name="Normalized Relational Schemas">
    {xml_str}
  </diagram>
</mxfile>"""

# ==============================================================================
# 4. MULTI-PAGE ALL-IN-ONE DRAW.IO FILE
# ==============================================================================
def generate_all_in_one_drawio():
    """Combines all 3 diagrams into a single 3-page draw.io file."""
    # Build models
    act_xml = generate_activity_diagram_xml()
    er_xml = generate_er_diagram_xml()
    sch_xml = generate_normalized_schemas_xml()

    # Extract the <mxGraphModel> from each
    act_root = ET.fromstring(act_xml).find("diagram").find("mxGraphModel")
    er_root = ET.fromstring(er_xml).find("diagram").find("mxGraphModel")
    sch_root = ET.fromstring(sch_xml).find("diagram").find("mxGraphModel")

    act_graph_str = ET.tostring(act_root, encoding="utf-8").decode("utf-8")
    er_graph_str = ET.tostring(er_root, encoding="utf-8").decode("utf-8")
    sch_graph_str = ET.tostring(sch_root, encoding="utf-8").decode("utf-8")

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net" agent="Antigravity" version="21.0.0" type="device">
  <diagram id="tab_activity" name="1. Activity Diagram">
    {act_graph_str}
  </diagram>
  <diagram id="tab_er" name="2. ER Diagram">
    {er_graph_str}
  </diagram>
  <diagram id="tab_schemas" name="3. Normalized Relational Schemas">
    {sch_graph_str}
  </diagram>
</mxfile>"""

def main():
    print("Generating draw.io diagrams for MediCare LK...")

    # 1. Activity Diagram
    act_path = os.path.join(WORKSPACE_DIR, "MedicareLk_Activity_Diagram.drawio")
    with open(act_path, "w", encoding="utf-8") as f:
        f.write(generate_activity_diagram_xml())
    print(f"Generated: {act_path}")

    # 2. ER Diagram
    er_path = os.path.join(WORKSPACE_DIR, "MedicareLk_ER_Diagram.drawio")
    with open(er_path, "w", encoding="utf-8") as f:
        f.write(generate_er_diagram_xml())
    print(f"Generated: {er_path}")

    # 3. Normalized Schemas
    sch_path = os.path.join(WORKSPACE_DIR, "MedicareLk_Normalized_Schemas.drawio")
    with open(sch_path, "w", encoding="utf-8") as f:
        f.write(generate_normalized_schemas_xml())
    print(f"Generated: {sch_path}")

    # 4. Multi-page all-in-one file
    all_path = os.path.join(WORKSPACE_DIR, "MedicareLk_System_Design_All.drawio")
    with open(all_path, "w", encoding="utf-8") as f:
        f.write(generate_all_in_one_drawio())
    print(f"Generated: {all_path}")

    print("All draw.io diagram files successfully generated!")

if __name__ == "__main__":
    main()
