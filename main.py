from excludemeta import *


# working on primary energy
exclude_meta("Table_1.1_Primary_Energy_Overview.xlsx", "Monthly Data", "Primary_Energy_Overview_excluding_meta.xlsx")
exclude_meta("Table_1.1_Primary_Energy_Overview.xlsx", "Annual Data", "Primary_Energy_Overview_excluding_meta.xlsx")

# primary energy imports by source
exclude_meta("Table_1.4a_Primary_Energy_Imports_by_Source.xlsx", "Monthly Data",
             "Primary_Energy_Imports_by_Source_excluding_meta.xlsx")
exclude_meta("Table_1.4a_Primary_Energy_Imports_by_Source.xlsx", "Annual Data",
             "Primary_Energy_Imports_by_Source_excluding_meta.xlsx")

# primary energy net imports by source
exclude_meta("Table_1.4c_Primary_Energy_Net_Imports_by_Source.xlsx", "Monthly Data",
             "Primary_Energy_Net_Imports_by_Source_excluding_meta.xlsx")
exclude_meta("Table_1.4c_Primary_Energy_Net_Imports_by_Source.xlsx", "Annual Data",
             "Primary_Energy_Net_Imports_by_Source_excluding_meta.xlsx")
