"""
Adapted from the data preprocessing code of I. Teinemaa et al., 
"Outcome-Oriented Predictive Process Monitoring: Review and Benchmark".
"""
import os

case_id_col = {}
activity_col = {}
resource_col = {}
timestamp_col = {}
label_col = {}
pos_label = {}
neg_label = {}
dynamic_cat_cols = {}
static_cat_cols = {}
dynamic_num_cols = {}
static_num_cols = {}
control_flow_var = {}
control_flow_var_incremental = {}
control_flow_var_binary = {}
environmental_actions = {}
control_flow_var_attribute = {}
filename = {}

base_dir = os.path.dirname(os.path.abspath(__file__))  # folder where the script is
logs_dir = "C:/Users/alegi/Desktop/intoRDDL/src/input"

#### SimBank settings ####
"""dataset = "SimBank"
filename[dataset] = os.path.join(logs_dir, "SimBank.csv")
case_id_col[dataset] = "case_nr"
activity_col[dataset] = "activity"
resource_col[dataset] = ""
timestamp_col[dataset] = "timestamp"
label_col[dataset] = "label"
pos_label[dataset] = "deviant"
neg_label[dataset] = "regular"

dynamic_cat_cols[dataset] = ["activity"]
static_cat_cols[dataset] = []
dynamic_num_cols[dataset] = ["unc_quality", "est_quality", "cum_cost", "elapsed_time", "interest_rate", "discount_factor", "min_interest_rate"]
static_num_cols[dataset] = ["amount"]

environmental_actions[dataset] = ['receive_acceptance', 'receive_refusal']
control_flow_var_incremental[dataset] = []
control_flow_var_binary[dataset]= []
control_flow_var_attribute[dataset] = ["noc", "nor"]
control_flow_var[dataset] = environmental_actions[dataset] + control_flow_var_incremental[dataset] + control_flow_var_attribute[dataset] + control_flow_var_binary[dataset]"""


#### Traffic fines settings ####

for formula in range(1,3):
    dataset = "rtf_preprocessed" 
    
    filename[dataset] = os.path.join(logs_dir, "rtf_preprocessed.csv")
    
    case_id_col[dataset] = "Case ID"
    activity_col[dataset] = "Activity"
    resource_col[dataset] = "Resource"
    timestamp_col[dataset] = "Complete Timestamp"
    label_col[dataset] = "label"
    pos_label[dataset] = "deviant"
    neg_label[dataset] = "regular"

    # features for classifier
    dynamic_cat_cols[dataset] = ["Activity", 'Resource', "lastSent", "notificationType", "dismissal"]
    static_cat_cols[dataset] = ["article",  "vehicleClass"]
    dynamic_num_cols[dataset] = ["expense", "timesincelastevent", "timesincecasestart", "timesincemidnight", "event_nr", "month", "weekday", "hour", "open_cases", "execution_time_minutes"]
    static_num_cols[dataset] = ["amount", "points"]

    environmental_actions[dataset] = []
    control_flow_var_incremental[dataset] = []
    control_flow_var_binary[dataset]= []
    control_flow_var_attribute[dataset] = []
    control_flow_var[dataset] = environmental_actions[dataset] + control_flow_var_incremental[dataset] + control_flow_var_attribute[dataset] + control_flow_var_binary[dataset]
    
  
    

#### Sepsis Cases settings ####

datasets = ["sepsis_preprocessed"]

for dataset in datasets:

    filename[dataset] = os.path.join(
        logs_dir,
        "sepsis_preprocessed.csv"
    )

    # ========================================================
    # BASIC COLUMNS
    # ========================================================

    case_id_col[dataset] = "Case ID"
    activity_col[dataset] = "Activity"
    resource_col[dataset] = "org:group"
    timestamp_col[dataset] = "timestamp"

    # ========================================================
    # NO PREDICTIVE LABEL
    # ========================================================

    # Questo dataset è usato direttamente per la costruzione
    # del MDP, quindi non abbiamo una label deviant/regular.

    label_col[dataset] = None
    pos_label[dataset] = None
    neg_label[dataset] = None

    # ========================================================
    # CATEGORICAL FEATURES
    # ========================================================

    # Activity e org:group sono attributi dinamici dell'evento.

    dynamic_cat_cols[dataset] = [
        "Activity",
        "org:group"
    ]

    # Attributi clinici disponibili come attributi dello stato.
    #
    # Sono categorici/booleani e devono essere mantenuti come
    # tali. L'encoding RDDL potrà poi rappresentarli come bool
    # quando il loro dominio è True/False/missing.

    static_cat_cols[dataset] = [
        "Diagnose",
        "DiagnosticArtAstrup",
        "DiagnosticBlood",
        "DiagnosticECG",
        "DiagnosticIC",
        "DiagnosticLacticAcid",
        "DiagnosticLiquor",
        "DiagnosticOther",
        "DiagnosticSputum",
        "DiagnosticUrinaryCulture",
        "DiagnosticUrinarySediment",
        "DiagnosticXthorax",
        "DisfuncOrg",
        "Hypotensie",
        "Hypoxie",
        "InfectionSuspected",
        "Infusion",
        "Oligurie",
        "SIRSCritHeartRate",
        "SIRSCritLeucos",
        "SIRSCritTachypnea",
        "SIRSCritTemperature",
        "SIRSCriteria2OrMore"
    ]

    # ========================================================
    # NUMERICAL FEATURES
    # ========================================================

    dynamic_num_cols[dataset] = [
        "CRP",
        "LacticAcid",
        "Leucocytes",
        "hour",
        "weekday",
        "month",
        "timesincemidnight",
        "timesincelastevent",
        "timesincecasestart",
        "event_nr",
        "open_cases",
        "execution_time_minutes"
    ]

    static_num_cols[dataset] = [
        "Age"
    ]

    # ========================================================
    # ENVIRONMENTAL ACTIONS
    # ========================================================

    # NESSUNA attività ambientale.
    #
    # Tutte le attività del log devono rimanere azioni del MDP,
    # comprese:
    #
    #   Return ER
    #   Admission IC
    #   Release A
    #   Release B
    #   Release C
    #   Release D
    #   Release E
    #
    # In questo modo vengono mantenute nella sequenza delle
    # azioni e possono essere usate come transizioni del MDP.

    environmental_actions[dataset] = []

    # ========================================================
    # CONTROL-FLOW VARIABLES
    # ========================================================

    # Nessuna variabile di control flow derivata da
    # recent_release o da altri outcome predittivi.

    control_flow_var_attribute[dataset] = []

    control_flow_var_incremental[dataset] = []

    control_flow_var_binary[dataset] = []

    control_flow_var[dataset] = (
        environmental_actions[dataset]
        + control_flow_var_incremental[dataset]
        + control_flow_var_attribute[dataset]
        + control_flow_var_binary[dataset]
    )


#### BPIC2017 settings ####

bpic2017_dict = {"bpic2017_cancelled": "BPIC17_O_Cancelled.csv",
                 "bpic2017_accepted": "BPIC17_O_Accepted.csv",
                 "bpic2017_refused": "BPIC17_O_Refused.csv"
                }

for dataset, fname in bpic2017_dict.items():

    filename[dataset] = os.path.join(logs_dir, fname)

    case_id_col[dataset] = "Case ID"
    activity_col[dataset] = "Activity"
    resource_col[dataset] = 'org:resource'
    timestamp_col[dataset] = 'time:timestamp'
    label_col[dataset] = "label"
    neg_label[dataset] = "regular"
    pos_label[dataset] = "deviant"

    # features for classifier
    dynamic_cat_cols[dataset] = ["Activity", "Accepted", "Selected"] 
    static_cat_cols[dataset] = ['ApplicationType', 'LoanGoal']
    dynamic_num_cols[dataset] = ['FirstWithdrawalAmount', 'MonthlyCost', 'NumberOfTerms', 'OfferedAmount', 'CreditScore',  "timesincelastevent", "timesincecasestart", "timesincemidnight", "event_nr", "month", "weekday", "hour", "open_cases"]
    static_num_cols[dataset] = ['RequestedAmount']
    environmental_actions[dataset] = ['O_Accepted', 'O_Cancelled', 'O_Returned']
    control_flow_var_incremental[dataset] = ['O_Create Offer', 'W_Call after offers']
    control_flow_var_binary[dataset]= []
    control_flow_var_attribute[dataset] = []
    control_flow_var[dataset] = environmental_actions[dataset] + control_flow_var_incremental[dataset] + control_flow_var_attribute[dataset] + control_flow_var_binary[dataset]
    
  
    
#### Hospital billing settings ####
for i in range(1, 7):
    #for suffix in ["", "_sample10000", "_sample30000"]:
        dataset = "hospital_billing_%s" % (i)

        filename[dataset] = os.path.join(logs_dir, "hospital_billing_%s.csv" % (i))

        case_id_col[dataset] = "Case ID"
        activity_col[dataset] = "Activity"
        resource_col[dataset] = "Resource"
        timestamp_col[dataset] = "Complete Timestamp"
        label_col[dataset] = "label"
        neg_label[dataset] = "regular"
        pos_label[dataset] = "deviant"

        if i == 1:
            neg_label[dataset] = "deviant"
            pos_label[dataset] = "regular"

        # features for classifier
        dynamic_cat_cols[dataset] = ["Activity", 'Resource', 'actOrange', 'actRed', 'blocked', 'caseType', 'diagnosis', 'flagC', 'flagD', 'msgCode', 'msgType', 'state', 'version']#, 'isCancelled', 'isClosed', 'closeCode'] 
        static_cat_cols[dataset] = ['speciality']
        dynamic_num_cols[dataset] = ['msgCount', "timesincelastevent", "timesincecasestart", "timesincemidnight", "event_nr", "month", "weekday", "hour"]#, "open_cases"]
        static_num_cols[dataset] = []

        if i == 2: 
            environmental_actions[dataset] = []
            control_flow_var_incremental[dataset] = []
            control_flow_var_binary[dataset]= []
            control_flow_var_attribute[dataset] = ["isCancelled"]
            control_flow_var[dataset] = environmental_actions[dataset] + control_flow_var_incremental[dataset] + control_flow_var_attribute[dataset] + control_flow_var_binary[dataset]

        if i == 1: # label is created based on isCancelled attribute
            dynamic_cat_cols[dataset] = [col for col in dynamic_cat_cols[dataset] if col != "isCancelled"]
        elif i == 2:
            dynamic_cat_cols[dataset] = [col for col in dynamic_cat_cols[dataset] if col != "isClosed"]
    
            
#### BPIC2012 settings ####

bpic2012_dict = {
    "bpi12_preprocessed": "bpi12_preprocessed.csv"
}

for dataset, fname in bpic2012_dict.items():

    filename[dataset] = os.path.join(logs_dir, fname)

    case_id_col[dataset] = "case:concept:name"
    activity_col[dataset] = "concept:name"
    resource_col[dataset] = "org:resource"
    timestamp_col[dataset] = "time:timestamp"

    label_col[dataset] = None
    neg_label[dataset] = None
    pos_label[dataset] = None

    # State attributes
    dynamic_cat_cols[dataset] = [
        "concept:name",
        "org:resource"
    ]

    static_cat_cols[dataset] = []

    dynamic_num_cols[dataset] = [
        "hour",
        "weekday",
        "month",
        "timesincemidnight",
        "timesincelastevent",
        "timesincecasestart",
        "event_nr",
        "open_cases",
        "execution_time_minutes"
    ]

    static_num_cols[dataset] = [
        "AMOUNT_REQ"
    ]

    # ---------------------------------------------------------
    # Control-flow variables
    # ---------------------------------------------------------

    # Solo attività che vogliamo trasformare in variabili di stato
    control_flow_var_incremental[dataset] = [
        "O_CREATED-COMPLETE"
    ]

    control_flow_var_binary[dataset] = []

    control_flow_var_attribute[dataset] = []

    control_flow_var[dataset] = (
        control_flow_var_incremental[dataset]
        + control_flow_var_attribute[dataset]
        + control_flow_var_binary[dataset]
    )

    # Nessuna environmental action viene rimossa
    environmental_actions[dataset] = []    

#### BPI 2020 Permit settings ####

datasets = ["permit_preprocessed"]

for dataset in datasets:

    filename[dataset] = os.path.join(
        logs_dir,
        "Permit_preprocessed.csv"
    )

    # ========================================================
    # BASIC COLUMNS
    # ========================================================

    case_id_col[dataset] = "Case ID"
    activity_col[dataset] = "Activity"
    resource_col[dataset] = "Resource"
    timestamp_col[dataset] = "timestamp"

    # ========================================================
    # NO PREDICTIVE LABEL
    # ========================================================

    # Il dataset viene usato direttamente per la costruzione
    # del MDP. Non viene definita una label deviant/regular.

    label_col[dataset] = None
    pos_label[dataset] = None
    neg_label[dataset] = None

    # ========================================================
    # CATEGORICAL FEATURES
    # ========================================================

    # Attributi dinamici dell'evento.

    dynamic_cat_cols[dataset] = [
        "Activity",
        "Resource",
        "Role"
    ]

    # Attributi relativi al permit/case.

    static_cat_cols[dataset] = [
        "OrganizationalEntity",
        "ProjectNumber",
        "TaskNumber",
        "ActivityNumber",
        "travel permit number",
        "BudgetNumber",
        "Overspent",
        "DeclarationNumber_0",
        "RfpNumber_0",
        "Cost Type_0",
        "Task_0",
        "Project_0"
    ]

    # ========================================================
    # NUMERICAL FEATURES
    # ========================================================

    # Variabili che cambiano/sono osservabili nel corso
    # dell'esecuzione del processo.

    dynamic_num_cols[dataset] = [
        "timesincemidnight",
        "month",
        "weekday",
        "hour",
        "timesincelastevent",
        "timesincecasestart",
        "event_nr",
        "execution_time_minutes"
    ]

    # Attributi economici associati al permit/case.

    static_num_cols[dataset] = [
        "TotalDeclared",
        "RequestedAmount_0",
        "RequestedBudget",
        "OverspentAmount"
    ]

    # ========================================================
    # ENVIRONMENTAL ACTIONS
    # ========================================================

    # Per ora nessuna attività viene rimossa dal MDP.
    #
    # Tutte le attività del log rimangono azioni/transizioni
    # disponibili nella sequenza del processo.

    environmental_actions[dataset] = []

    # ========================================================
    # CONTROL-FLOW VARIABLES
    # ========================================================

    # Nessuna variabile di control flow aggiuntiva.

    control_flow_var_attribute[dataset] = []

    control_flow_var_incremental[dataset] = []

    control_flow_var_binary[dataset] = []

    control_flow_var[dataset] = (
        environmental_actions[dataset]
        + control_flow_var_incremental[dataset]
        + control_flow_var_attribute[dataset]
        + control_flow_var_binary[dataset]
    )

#### BPI 2020 International Declarations settings ####

datasets = ["intDecl_preprocessed"]

for dataset in datasets:

    filename[dataset] = os.path.join(
        logs_dir,
        "intDecl_preprocessed.csv"
    )

    # ========================================================
    # BASIC COLUMNS
    # ========================================================

    case_id_col[dataset] = "Case ID"
    activity_col[dataset] = "Activity"
    resource_col[dataset] = "Resource"
    timestamp_col[dataset] = "timestamp"

    # ========================================================
    # NO PREDICTIVE LABEL
    # ========================================================

    # Il dataset viene utilizzato direttamente per la
    # costruzione del MDP.
    # Non viene utilizzata una label deviant/regular.

    label_col[dataset] = None
    pos_label[dataset] = None
    neg_label[dataset] = None

    # ========================================================
    # CATEGORICAL FEATURES
    # ========================================================

    # Attributi dinamici dell'evento.

    dynamic_cat_cols[dataset] = [
        "Activity",
        "Resource",
        "Role"
    ]

    # Attributi statici relativi alla dichiarazione
    # e al permit associato.

    static_cat_cols[dataset] = [
        "DeclarationNumber",
        "Permit travel permit number",
        "travel permit number",
        "Permit TaskNumber",
        "Permit BudgetNumber",
        "Permit ProjectNumber",
        "Permit OrganizationalEntity",
        "Permit ID",
        "Permit id",
        "BudgetNumber"
    ]

    # ========================================================
    # NUMERICAL FEATURES
    # ========================================================

    # Variabili temporali/event-level.

    dynamic_num_cols[dataset] = [
        "timesincemidnight",
        "month",
        "weekday",
        "hour",
        "timesincelastevent",
        "timesincecasestart",
        "event_nr",
        "execution_time_minutes"
    ]

    # Attributi economici della dichiarazione/permit.

    static_num_cols[dataset] = [
        "Amount",
        "RequestedAmount",
        "OriginalAmount",
        "Permit RequestedBudget",
        "AdjustedAmount"
    ]

    # ========================================================
    # ENVIRONMENTAL ACTIONS
    # ========================================================

    # Per ora nessuna attività viene esclusa.
    #
    # Tutte le attività del log vengono mantenute come
    # azioni/transizioni del MDP.

    environmental_actions[dataset] = []

    # ========================================================
    # CONTROL-FLOW VARIABLES
    # ========================================================

    # Nessuna variabile di control flow aggiuntiva.

    control_flow_var_attribute[dataset] = []

    control_flow_var_incremental[dataset] = []

    control_flow_var_binary[dataset] = []

    control_flow_var[dataset] = (
        environmental_actions[dataset]
        + control_flow_var_incremental[dataset]
        + control_flow_var_attribute[dataset]
        + control_flow_var_binary[dataset]
    )