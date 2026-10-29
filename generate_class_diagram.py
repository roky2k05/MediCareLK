import html
import os
import xml.etree.ElementTree as ET

# Define output path
output_file = r"c:\Users\Rasindu\AndroidStudioProjects\MedicareLk\MedicareLk_Class_Diagram.drawio"

def build_drawio_xml():
    # Colors matching reference diagram
    COLOR_MODEL_HEADER = "#107C41"
    COLOR_MODEL_STROKE = "#0D5E31"
    COLOR_ADAPTER_HEADER = "#1A5276"
    COLOR_ADAPTER_STROKE = "#154360"
    COLOR_SCREEN_HEADER = "#6E2D91"
    COLOR_SCREEN_STROKE = "#51226B"
    COLOR_AUTH_HEADER = "#B45309"
    COLOR_AUTH_STROKE = "#92400E"
    COLOR_UTIL_HEADER = "#66101F"
    COLOR_UTIL_STROKE = "#4A0B16"

    def class_card_html(stereotype, title, header_bg, fields, methods):
        fields_str = "<br/>".join(html.escape(f) for f in fields)
        methods_str = "<br/>".join(html.escape(m) for m in methods)
        
        return (
            f'<div style="background-color: {header_bg}; color: #FFFFFF; padding: 6px; text-align: center; font-family: Helvetica, Arial, sans-serif; border-bottom: 2px solid rgba(0,0,0,0.15);">'
            f'<div style="font-size: 10px; font-style: italic; opacity: 0.9;">&laquo;{html.escape(stereotype)}&raquo;</div>'
            f'<div style="font-size: 13px; font-weight: bold; margin-top: 1px;">{html.escape(title)}</div>'
            f'</div>'
            f'<div style="padding: 7px 9px; font-size: 10.5px; font-family: Consolas, \'Courier New\', monospace; color: #1E293B; line-height: 1.35; text-align: left;">'
            f'{fields_str}'
            f'</div>'
            f'<hr style="border: 0; border-top: 1px solid {header_bg}; margin: 2px 0; opacity: 0.6;"/>'
            f'<div style="padding: 7px 9px; font-size: 10.5px; font-family: Consolas, \'Courier New\', monospace; color: #1E293B; line-height: 1.35; text-align: left;">'
            f'{methods_str}'
            f'</div>'
        )

    # Class definitions
    classes = [
        # ================= ROW 1: MODELS =================
        {
            "id": "model_doctor",
            "x": 60, "y": 90, "w": 310, "h": 350,
            "stereotype": "models", "title": "Doctor",
            "header_color": COLOR_MODEL_HEADER, "stroke_color": COLOR_MODEL_STROKE,
            "fields": [
                "- id : int",
                "- name : String",
                "- specialization : String",
                "- qualification : String",
                "- experienceYears : int",
                "- fee : double",
                "- hospital : String",
                "- city : String",
                "- rating : double",
                "- availableDays : String",
                "- availableTimes : String",
                "- about : String",
                "- phone : String",
                "- email : String"
            ],
            "methods": [
                "+ Doctor()",
                "+ Doctor(id, name, spec, qual, exp, ...)",
                "+ getters / setters (all fields)"
            ]
        },
        {
            "id": "model_appointment",
            "x": 420, "y": 90, "w": 310, "h": 350,
            "stereotype": "models", "title": "Appointment",
            "header_color": COLOR_MODEL_HEADER, "stroke_color": COLOR_MODEL_STROKE,
            "fields": [
                "- id : int",
                "- referenceNo : String",
                "- firebaseUid : String",
                "- userEmail : String",
                "- userId : int",
                "- doctorId : int",
                "- doctorName : String",
                "- specialization : String",
                "- hospital : String",
                "- appointmentDate : String",
                "- timeSlot : String",
                "- consultationType : String",
                "- patientName : String",
                "- patientPhone : String",
                "- notes : String",
                "- fee : double",
                "- status : String",
                "- cancellationReason : String",
                "- createdAt : String"
            ],
            "methods": [
                "+ Appointment()",
                "+ Appointment(id, ref, uid, docId, ...)",
                "+ getters / setters (all fields)"
            ]
        },
        {
            "id": "model_service",
            "x": 780, "y": 90, "w": 310, "h": 350,
            "stereotype": "models", "title": "ServiceItem",
            "header_color": COLOR_MODEL_HEADER, "stroke_color": COLOR_MODEL_STROKE,
            "fields": [
                "- id : int",
                "- title : String",
                "- category : String",
                "- price : double",
                "- description : String",
                "- features : String",
                "- hospital : String",
                "- preparation : String",
                "--- NotificationItem ---",
                "- notifId : int",
                "- notifTitle : String",
                "- notifMessage : String",
                "- notifType : String",
                "- isRead : int"
            ],
            "methods": [
                "+ ServiceItem()",
                "+ ServiceItem(id, title, cat, price, ...)",
                "+ getters / setters (all fields)"
            ]
        },
        {
            "id": "model_user",
            "x": 1140, "y": 90, "w": 310, "h": 350,
            "stereotype": "models", "title": "User",
            "header_color": COLOR_MODEL_HEADER, "stroke_color": COLOR_MODEL_STROKE,
            "fields": [
                "- id : int",
                "- firebaseUid : String",
                "- name : String",
                "- email : String",
                "- phone : String",
                "- password : String",
                "- nic : String",
                "- dob : String",
                "- gender : String",
                "- bloodGroup : String",
                "- address : String",
                "- emergencyContactName : String",
                "- emergencyContactPhone : String",
                "- allergies : String",
                "- chronicConditions : String",
                "- medications : String",
                "- createdAt : String"
            ],
            "methods": [
                "+ User()",
                "+ User(id, name, email, phone, pwd)",
                "+ getters / setters (all fields)"
            ]
        },

        # ================= ROW 2: ADAPTERS =================
        {
            "id": "adapter_doctor",
            "x": 60, "y": 480, "w": 310, "h": 200,
            "stereotype": "adapters", "title": "DoctorAdapter",
            "header_color": COLOR_ADAPTER_HEADER, "stroke_color": COLOR_ADAPTER_STROKE,
            "fields": [
                "- context : Context",
                "- doctorList : List<Doctor>",
                "- listener : OnDoctorClickListener"
            ],
            "methods": [
                "+ onCreateViewHolder(p, vt) : ViewHolder",
                "+ onBindViewHolder(h, pos) : void",
                "+ getItemCount() : int",
                "+ updateList(newList: List<Doctor>) : void"
            ]
        },
        {
            "id": "adapter_appointment",
            "x": 420, "y": 480, "w": 310, "h": 200,
            "stereotype": "adapters", "title": "AppointmentAdapter",
            "header_color": COLOR_ADAPTER_HEADER, "stroke_color": COLOR_ADAPTER_STROKE,
            "fields": [
                "- context : Context",
                "- appointmentList : List<Appointment>",
                "- listener : OnAppointmentActionListener"
            ],
            "methods": [
                "+ onCreateViewHolder(p, vt) : ViewHolder",
                "+ onBindViewHolder(h, pos) : void",
                "+ getItemCount() : int",
                "+ updateList(newList: List<Appointment>) : void",
                "- openDetails(appt: Appointment) : void"
            ]
        },
        {
            "id": "adapter_service",
            "x": 780, "y": 480, "w": 310, "h": 200,
            "stereotype": "adapters", "title": "ServiceAdapter",
            "header_color": COLOR_ADAPTER_HEADER, "stroke_color": COLOR_ADAPTER_STROKE,
            "fields": [
                "- context : Context",
                "- serviceList : List<ServiceItem>",
                "- listener : OnServiceClickListener"
            ],
            "methods": [
                "+ onCreateViewHolder(p, vt) : ViewHolder",
                "+ onBindViewHolder(h, pos) : void",
                "+ getItemCount() : int",
                "+ updateList(newList: List<ServiceItem>) : void"
            ]
        },
        {
            "id": "adapter_notification",
            "x": 1140, "y": 480, "w": 310, "h": 200,
            "stereotype": "adapters", "title": "NotificationAdapter",
            "header_color": COLOR_ADAPTER_HEADER, "stroke_color": COLOR_ADAPTER_STROKE,
            "fields": [
                "- context : Context",
                "- notificationList : List<NotificationItem>",
                "- listener : OnNotificationClickListener"
            ],
            "methods": [
                "+ onCreateViewHolder(p, vt) : ViewHolder",
                "+ onBindViewHolder(h, pos) : void",
                "+ getItemCount() : int",
                "+ updateList(newList: List<NotificationItem>) : void"
            ]
        },

        # ================= ROW 3: FEATURE SCREENS (PURPLE) =================
        {
            "id": "screen_doctor_list",
            "x": 60, "y": 740, "w": 310, "h": 220,
            "stereotype": "activities", "title": "DoctorListActivity",
            "header_color": COLOR_SCREEN_HEADER, "stroke_color": COLOR_SCREEN_STROKE,
            "fields": [
                "- databaseHelper : DatabaseHelper",
                "- doctorAdapter : DoctorAdapter",
                "- doctorList : List<Doctor>",
                "- rvDoctors : RecyclerView",
                "- etSearch : TextInputEditText",
                "- spinnerSpecialization : Spinner"
            ],
            "methods": [
                "+ onCreate(savedInstanceState: Bundle) : void",
                "+ loadDoctors() : void",
                "+ filterDoctors(query: String, spec: String) : void",
                "+ onBookClick(doctor: Doctor) : void",
                "+ onViewProfileClick(doctor: Doctor) : void"
            ]
        },
        {
            "id": "screen_book_appointment",
            "x": 420, "y": 740, "w": 310, "h": 220,
            "stereotype": "activities", "title": "BookAppointmentActivity",
            "header_color": COLOR_SCREEN_HEADER, "stroke_color": COLOR_SCREEN_STROKE,
            "fields": [
                "- databaseHelper : DatabaseHelper",
                "- sessionManager : SessionManager",
                "- firebaseHelper : FirebaseHelper",
                "- doctor : Doctor",
                "- selectedDate : String",
                "- selectedTimeSlot : String",
                "- etPatientName, etPatientPhone : EditText"
            ],
            "methods": [
                "+ onCreate(savedInstanceState: Bundle) : void",
                "+ showDatePicker() : void",
                "+ setupTimeSlots() : void",
                "+ confirmBooking() : void",
                "+ validateInput() : boolean"
            ]
        },
        {
            "id": "screen_appointments",
            "x": 780, "y": 740, "w": 310, "h": 220,
            "stereotype": "activities", "title": "AppointmentsActivity",
            "header_color": COLOR_SCREEN_HEADER, "stroke_color": COLOR_SCREEN_STROKE,
            "fields": [
                "- databaseHelper : DatabaseHelper",
                "- sessionManager : SessionManager",
                "- firebaseHelper : FirebaseHelper",
                "- appointmentAdapter : AppointmentAdapter",
                "- appointmentList : List<Appointment>",
                "- tabLayoutAppointments : TabLayout",
                "- currentStatus : String"
            ],
            "methods": [
                "+ onCreate(savedInstanceState: Bundle) : void",
                "+ loadAppointments() : void",
                "+ listenToFirebaseAppointments() : void",
                "+ onReschedule(appt: Appointment) : void",
                "+ onCancel(appt: Appointment) : void"
            ]
        },
        {
            "id": "screen_profile",
            "x": 1140, "y": 740, "w": 310, "h": 220,
            "stereotype": "activities", "title": "ProfileActivity",
            "header_color": COLOR_SCREEN_HEADER, "stroke_color": COLOR_SCREEN_STROKE,
            "fields": [
                "- databaseHelper : DatabaseHelper",
                "- sessionManager : SessionManager",
                "- firebaseHelper : FirebaseHelper",
                "- currentUser : User",
                "- etProfileName, etProfilePhone : EditText",
                "- spinnerBloodGroup, spinnerGender : Spinner"
            ],
            "methods": [
                "+ onCreate(savedInstanceState: Bundle) : void",
                "+ loadUserProfile() : void",
                "+ saveProfileChanges() : void",
                "+ logoutUser() : void"
            ]
        },

        # ================= ROW 4: AUTH & DASHBOARD (ORANGE/BROWN) =================
        {
            "id": "act_login",
            "x": 60, "y": 1020, "w": 310, "h": 220,
            "stereotype": "activities", "title": "LoginActivity",
            "header_color": COLOR_AUTH_HEADER, "stroke_color": COLOR_AUTH_STROKE,
            "fields": [
                "- databaseHelper : DatabaseHelper",
                "- sessionManager : SessionManager",
                "- firebaseHelper : FirebaseHelper",
                "- tilEmailPhone, tilPassword : TextInputLayout",
                "- etEmailPhone, etPassword : TextInputEditText",
                "- btnLogin : MaterialButton"
            ],
            "methods": [
                "+ onCreate(savedInstanceState: Bundle) : void",
                "+ loginUser() : void",
                "+ showForgotPasswordDialog() : void",
                "+ syncUserFromFirebase(uid: String) : void"
            ]
        },
        {
            "id": "act_register",
            "x": 420, "y": 1020, "w": 310, "h": 220,
            "stereotype": "activities", "title": "RegisterActivity",
            "header_color": COLOR_AUTH_HEADER, "stroke_color": COLOR_AUTH_STROKE,
            "fields": [
                "- databaseHelper : DatabaseHelper",
                "- sessionManager : SessionManager",
                "- firebaseHelper : FirebaseHelper",
                "- etFullName, etEmail, etPhone : EditText",
                "- etRegPassword, etConfirmPassword : EditText",
                "- cbTerms : CheckBox"
            ],
            "methods": [
                "+ onCreate(savedInstanceState: Bundle) : void",
                "+ registerUser() : void",
                "+ validateForm() : boolean",
                "+ createFirebaseAccount() : void"
            ]
        },
        {
            "id": "act_main",
            "x": 780, "y": 1020, "w": 310, "h": 220,
            "stereotype": "activities", "title": "MainActivity",
            "header_color": COLOR_AUTH_HEADER, "stroke_color": COLOR_AUTH_STROKE,
            "fields": [
                "- databaseHelper : DatabaseHelper",
                "- sessionManager : SessionManager",
                "- firebaseHelper : FirebaseHelper",
                "- doctorAdapter : DoctorAdapter",
                "- upcomingAppointment : Appointment",
                "- rvTopDoctors : RecyclerView",
                "- bottomNavigationView : BottomNavigationView"
            ],
            "methods": [
                "+ onCreate(savedInstanceState: Bundle) : void",
                "+ initViews() : void",
                "+ setupNavigation() : void",
                "+ loadUpcomingAppointment() : void",
                "+ listenToNotificationsRealtime() : void"
            ]
        },
        {
            "id": "act_appointment_detail",
            "x": 1140, "y": 1020, "w": 310, "h": 220,
            "stereotype": "activities", "title": "AppointmentDetailActivity",
            "header_color": COLOR_AUTH_HEADER, "stroke_color": COLOR_AUTH_STROKE,
            "fields": [
                "- databaseHelper : DatabaseHelper",
                "- firebaseHelper : FirebaseHelper",
                "- sessionManager : SessionManager",
                "- appointment : Appointment",
                "- tvRefNo, tvDoctorName, tvStatus : TextView",
                "- btnReschedule, btnCancel : MaterialButton"
            ],
            "methods": [
                "+ onCreate(savedInstanceState: Bundle) : void",
                "+ loadAppointmentDetails() : void",
                "+ promptCancelAppointment() : void",
                "+ promptRescheduleAppointment() : void"
            ]
        },

        # ================= ROW 5: UTILITIES & DATABASE (MAROON) =================
        {
            "id": "util_db",
            "x": 60, "y": 1300, "w": 310, "h": 250,
            "stereotype": "database", "title": "DatabaseHelper",
            "header_color": COLOR_UTIL_HEADER, "stroke_color": COLOR_UTIL_STROKE,
            "fields": [
                "- DATABASE_NAME : String = \"medicare_lk.db\"",
                "- DATABASE_VERSION : int = 2",
                "+ TABLE_USERS, TABLE_DOCTORS : String",
                "+ TABLE_APPOINTMENTS, TABLE_SERVICES : String",
                "+ TABLE_NOTIFICATIONS, TABLE_HEALTH_TIPS : String"
            ],
            "methods": [
                "+ onCreate(db: SQLiteDatabase) : void",
                "+ registerUser(user: User) : long",
                "+ loginUser(emailOrPhone, pwd) : User",
                "+ getAllDoctors() : List<Doctor>",
                "+ bookAppointment(appt: Appointment) : long",
                "+ getAppointmentsByUser(uid, stat) : List<Appointment>",
                "+ rescheduleAppointment(id, dt, slot) : boolean",
                "+ cancelAppointment(id, reason) : boolean"
            ]
        },
        {
            "id": "util_firebase",
            "x": 420, "y": 1300, "w": 310, "h": 250,
            "stereotype": "database", "title": "FirebaseHelper",
            "header_color": COLOR_UTIL_HEADER, "stroke_color": COLOR_UTIL_STROKE,
            "fields": [
                "- instance : FirebaseHelper",
                "- auth : FirebaseAuth",
                "- databaseRef : DatabaseReference",
                "- database : FirebaseDatabase"
            ],
            "methods": [
                "+ getInstance() : FirebaseHelper",
                "+ getCurrentUid() : String",
                "+ isUserLoggedIn() : boolean",
                "+ saveUserProfile(user, listener) : void",
                "+ saveAppointment(appt, listener) : void",
                "+ updateAppointmentStatus(...) : void",
                "+ rescheduleAppointment(...) : void",
                "+ listenToUserAppointments(uid, listener) : void",
                "+ seedCatalogIfEmpty(docs, serv, tips) : void"
            ]
        },
        {
            "id": "util_notification",
            "x": 780, "y": 1300, "w": 310, "h": 250,
            "stereotype": "utility", "title": "NotificationHelper",
            "header_color": COLOR_UTIL_HEADER, "stroke_color": COLOR_UTIL_STROKE,
            "fields": [
                "+ CHANNEL_ID : String = \"medicare_channel\"",
                "+ CHANNEL_NAME : String",
                "+ CHANNEL_DESC : String",
                "- TAG : String = \"NotificationHelper\""
            ],
            "methods": [
                "+ createNotificationChannel(ctx: Context) : void",
                "+ showNotification(ctx, title, msg, id, intent) : void",
                "+ showAppointmentNotification(ctx, appt) : void"
            ]
        },
        {
            "id": "util_session",
            "x": 1140, "y": 1300, "w": 310, "h": 250,
            "stereotype": "utility", "title": "SessionManager",
            "header_color": COLOR_UTIL_HEADER, "stroke_color": COLOR_UTIL_STROKE,
            "fields": [
                "- PREF_NAME : String = \"MedicareLkSession\"",
                "- pref : SharedPreferences",
                "- editor : SharedPreferences.Editor",
                "- context : Context"
            ],
            "methods": [
                "+ createLoginSession(uid, id, name, email, phone) : void",
                "+ isLoggedIn() : boolean",
                "+ getFirebaseUid() : String",
                "+ getUserId() : int",
                "+ getUserName() : String",
                "+ getUserEmail() : String",
                "+ updateUserInfo(name, phone) : void",
                "+ logoutUser() : void"
            ]
        }
    ]

    # Section Headers
    section_headers = [
        {"id": "sec_models", "text": "Models", "color": "#107C41", "x": 60, "y": 62, "w": 1390},
        {"id": "sec_adapters", "text": "Adapters", "color": "#1A5276", "x": 60, "y": 454, "w": 1390},
        {"id": "sec_screens", "text": "Feature Screens", "color": "#6E2D91", "x": 60, "y": 712, "w": 1390},
        {"id": "sec_auth", "text": "Activities (Auth & Dashboard)", "color": "#B45309", "x": 60, "y": 992, "w": 1390},
        {"id": "sec_utilities", "text": "Database & Utilities", "color": "#66101F", "x": 60, "y": 1272, "w": 1390}
    ]

    # Connections / Relationships
    edges = [
        # Solid Associations (Adapters -> Models)
        {
            "id": "edge_doc_adapt",
            "source": "adapter_doctor", "target": "model_doctor",
            "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#1A5276;strokeWidth=1.8;endArrow=none;endFill=0;",
            "label": "uses"
        },
        {
            "id": "edge_appt_adapt",
            "source": "adapter_appointment", "target": "model_appointment",
            "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#1A5276;strokeWidth=1.8;endArrow=none;endFill=0;",
            "label": "uses"
        },
        {
            "id": "edge_serv_adapt",
            "source": "adapter_service", "target": "model_service",
            "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#1A5276;strokeWidth=1.8;endArrow=none;endFill=0;",
            "label": "uses"
        },
        # Screen -> Adapter dependencies (dashed)
        {
            "id": "edge_doclist_adapt",
            "source": "screen_doctor_list", "target": "adapter_doctor",
            "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#6E2D91;strokeWidth=1.5;dashed=1;dashPattern=5 5;endArrow=open;endFill=0;",
            "label": "uses"
        },
        {
            "id": "edge_apptlist_adapt",
            "source": "screen_appointments", "target": "adapter_appointment",
            "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#6E2D91;strokeWidth=1.5;dashed=1;dashPattern=5 5;endArrow=open;endFill=0;",
            "label": "uses"
        },
        {
            "id": "edge_profile_user",
            "source": "screen_profile", "target": "model_user",
            "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#6E2D91;strokeWidth=1.5;dashed=1;dashPattern=5 5;endArrow=open;endFill=0;",
            "label": "uses"
        },
        {
            "id": "edge_book_doc",
            "source": "screen_book_appointment", "target": "model_doctor",
            "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#6E2D91;strokeWidth=1.5;dashed=1;dashPattern=5 5;endArrow=open;endFill=0;exitX=0.2;exitY=0;entryX=0.5;entryY=1;",
            "label": "uses"
        },
        {
            "id": "edge_book_appt",
            "source": "screen_book_appointment", "target": "model_appointment",
            "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#6E2D91;strokeWidth=1.5;dashed=1;dashPattern=5 5;endArrow=open;endFill=0;",
            "label": "creates"
        },
        # Activity -> Activity flow
        {
            "id": "edge_login_register",
            "source": "act_login", "target": "act_register",
            "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#B45309;strokeWidth=1.5;dashed=1;dashPattern=4 4;endArrow=open;endFill=0;",
            "label": "navigates"
        },
        {
            "id": "edge_login_main",
            "source": "act_login", "target": "act_main",
            "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#B45309;strokeWidth=1.5;dashed=1;dashPattern=4 4;endArrow=open;endFill=0;exitX=1;exitY=0.8;entryX=0;entryY=0.8;",
            "label": "onSuccess"
        },
        {
            "id": "edge_main_doclist",
            "source": "act_main", "target": "screen_doctor_list",
            "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#B45309;strokeWidth=1.5;dashed=1;dashPattern=4 4;endArrow=open;endFill=0;exitX=0.2;exitY=0;entryX=0.5;entryY=1;",
            "label": "navigates"
        },
        {
            "id": "edge_main_appointments",
            "source": "act_main", "target": "screen_appointments",
            "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#B45309;strokeWidth=1.5;dashed=1;dashPattern=4 4;endArrow=open;endFill=0;",
            "label": "navigates"
        },
        {
            "id": "edge_main_profile",
            "source": "act_main", "target": "screen_profile",
            "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#B45309;strokeWidth=1.5;dashed=1;dashPattern=4 4;endArrow=open;endFill=0;exitX=0.8;exitY=0;entryX=0.5;entryY=1;",
            "label": "navigates"
        },
        {
            "id": "edge_appt_detail",
            "source": "screen_appointments", "target": "act_appointment_detail",
            "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#6E2D91;strokeWidth=1.5;dashed=1;dashPattern=4 4;endArrow=open;endFill=0;exitX=0.8;exitY=1;entryX=0.5;entryY=0;",
            "label": "viewDetails"
        },
        # Database & Utility dependencies
        {
            "id": "edge_doclist_db",
            "source": "act_login", "target": "util_db",
            "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#66101F;strokeWidth=1.5;dashed=1;dashPattern=4 4;endArrow=open;endFill=0;",
            "label": "uses"
        },
        {
            "id": "edge_register_firebase",
            "source": "act_register", "target": "util_firebase",
            "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#66101F;strokeWidth=1.5;dashed=1;dashPattern=4 4;endArrow=open;endFill=0;",
            "label": "uses"
        },
        {
            "id": "edge_main_session",
            "source": "act_main", "target": "util_session",
            "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#66101F;strokeWidth=1.5;dashed=1;dashPattern=4 4;endArrow=open;endFill=0;exitX=0.8;exitY=1;entryX=0.2;entryY=0;",
            "label": "uses"
        },
        {
            "id": "edge_main_notif",
            "source": "act_main", "target": "util_notification",
            "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#66101F;strokeWidth=1.5;dashed=1;dashPattern=4 4;endArrow=open;endFill=0;",
            "label": "uses"
        },
        {
            "id": "edge_profile_session",
            "source": "screen_profile", "target": "util_session",
            "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#66101F;strokeWidth=1.5;dashed=1;dashPattern=4 4;endArrow=open;endFill=0;exitX=0.5;exitY=1;entryX=0.8;entryY=0;",
            "label": "uses"
        }
    ]

    # Title Banner
    title_html = (
        '<div style="text-align: center; font-family: Helvetica, Arial, sans-serif;">'
        '<div style="font-size: 20px; font-weight: bold; color: #0F172A; letter-spacing: 0.5px;">MedicareLk &ndash; Class Diagram</div>'
        '<div style="font-size: 11px; color: #64748B; margin-top: 3px;">Full Architectural &amp; Object Model with Model-View-Adapter-Database Layers</div>'
        '</div>'
    )

    # Legend HTML
    legend_html = (
        '<div style="display: flex; align-items: center; justify-content: center; gap: 20px; font-family: Helvetica, Arial, sans-serif; font-size: 11px; color: #334155; height: 100%;">'
        '<b style="font-size: 11.5px; color: #0F172A; margin-right: 8px;">Legend:</b>'
        '<span style="display: inline-flex; align-items: center;"><span style="display:inline-block; width:13px; height:13px; background:#107C41; border-radius:2px; margin-right:5px;"></span>Model</span>'
        '<span style="display: inline-flex; align-items: center;"><span style="display:inline-block; width:13px; height:13px; background:#1A5276; border-radius:2px; margin-right:5px;"></span>Adapter</span>'
        '<span style="display: inline-flex; align-items: center;"><span style="display:inline-block; width:13px; height:13px; background:#6E2D91; border-radius:2px; margin-right:5px;"></span>Activity (Feature)</span>'
        '<span style="display: inline-flex; align-items: center;"><span style="display:inline-block; width:13px; height:13px; background:#B45309; border-radius:2px; margin-right:5px;"></span>Activity (Auth/Core)</span>'
        '<span style="display: inline-flex; align-items: center;"><span style="display:inline-block; width:13px; height:13px; background:#66101F; border-radius:2px; margin-right:5px;"></span>Database / Utility</span>'
        '<span style="margin-left: 15px; color: #64748B;">&mdash;&mdash; association</span>'
        '<span style="margin-left: 10px; color: #64748B;">- - - - &gt; dependency (uses)</span>'
        '</div>'
    )

    # Construct XML Tree
    mxfile = ET.Element("mxfile", host="app.diagrams.net", agent="Antigravity", version="21.0.0", type="device")
    diagram = ET.SubElement(mxfile, "diagram", id="medicarelk_class_diagram", name="MedicareLk - Class Diagram")
    mxGraphModel = ET.SubElement(diagram, "mxGraphModel", dx="1600", dy="1200", grid="1", gridSize="10", guides="1", tooltips="1", connect="1", arrows="1", fold="1", page="1", pageScale="1", pageWidth="1520", pageHeight="1720", math="0", shadow="0")
    root = ET.SubElement(mxGraphModel, "root")

    ET.SubElement(root, "mxCell", id="0")
    ET.SubElement(root, "mxCell", id="1", parent="0")

    # Title cell
    title_cell = ET.SubElement(root, "mxCell", id="main_title", value=title_html, style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;", vertex="1", parent="1")
    ET.SubElement(title_cell, "mxGeometry", attrib={"x": "60", "y": "15", "width": "1390", "height": "40", "as": "geometry"})

    # Section Headers
    for sec in section_headers:
        sec_value = f'<div style="font-family: Helvetica, Arial, sans-serif; font-size: 11px; font-weight: bold; color: {sec["color"]}; text-transform: uppercase; letter-spacing: 1px; text-align: center;">&bull;&nbsp;&nbsp;{html.escape(sec["text"])}&nbsp;&nbsp;&bull;</div>'
        sec_cell = ET.SubElement(root, "mxCell", id=sec["id"], value=sec_value, style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;", vertex="1", parent="1")
        ET.SubElement(sec_cell, "mxGeometry", attrib={"x": str(sec["x"]), "y": str(sec["y"]), "width": str(sec["w"]), "height": "20", "as": "geometry"})

    # Class Cards
    for c in classes:
        card_val = class_card_html(c["stereotype"], c["title"], c["header_color"], c["fields"], c["methods"])
        style = f"rounded=1;arcSize=3;whiteSpace=wrap;html=1;overflow=hidden;fillColor=#FFFFFF;strokeColor={c['stroke_color']};strokeWidth=1.8;shadow=1;align=left;verticalAlign=top;spacing=0;spacingTop=0;spacingBottom=0;spacingLeft=0;spacingRight=0;"
        cell = ET.SubElement(root, "mxCell", id=c["id"], value=card_val, style=style, vertex="1", parent="1")
        ET.SubElement(cell, "mxGeometry", attrib={"x": str(c["x"]), "y": str(c["y"]), "width": str(c["w"]), "height": str(c["h"]), "as": "geometry"})

    # Legend Card
    legend_cell = ET.SubElement(root, "mxCell", id="legend_box", value=legend_html, style="rounded=1;arcSize=6;whiteSpace=wrap;html=1;overflow=hidden;fillColor=#F8FAFC;strokeColor=#CBD5E1;strokeWidth=1.5;shadow=1;align=center;verticalAlign=middle;spacing=0;", vertex="1", parent="1")
    ET.SubElement(legend_cell, "mxGeometry", attrib={"x": "60", "y": "1590", "width": "1390", "height": "55", "as": "geometry"})

    # Edges
    for edge in edges:
        edge_cell = ET.SubElement(root, "mxCell", id=edge["id"], value=edge.get("label", ""), style=edge["style"], edge="1", parent="1", source=edge["source"], target=edge["target"])
        mxGeo = ET.SubElement(edge_cell, "mxGeometry", attrib={"relative": "1", "as": "geometry"})
        if edge.get("label"):
            ET.SubElement(mxGeo, "mxPoint", attrib={"as": "offset"})

    # Save to file with proper XML declaration and formatting
    xml_str = ET.tostring(mxfile, encoding="utf-8", xml_declaration=True)
    with open(output_file, "wb") as f:
        f.write(xml_str)

    print(f"Successfully generated {output_file} (size: {os.path.getsize(output_file)} bytes)")

if __name__ == "__main__":
    build_drawio_xml()
