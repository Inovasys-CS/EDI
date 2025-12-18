# MuddyWater Espionage APT

**Threat Date:** October 22, 2025  
**Threat Actor Name:** MuddyWater (Espionage)

---

## Overview

MuddyWater is an advanced persistent threat group conducting long-term espionage campaigns using spear-phishing as the primary initial access vector. 
The actor leverages PowerShell-based malware, credential harvesting techniques, COM object hijacking, and registry-based persistence to maintain stealthy access. 
MuddyWater establishes resilient command-and-control channels to execute commands, exfiltrate sensitive data, and sustain control over compromised systems, primarily targeting government, telecom, and energy sectors.

---

## Related Rules

1. [credential_access/file_access_win_browser_credential_access](https://github.com/Inovasys-CS/EDI/blob/main/emulation_and_detection/credential_access/file_access_win_browser_credential_access/file_access_win_browser_credential_access.yml)
2. [credential_access/file_access_win_dpapi_master_key_access](https://github.com/Inovasys-CS/EDI/blob/main/emulation_and_detection/credential_access/file_access_win_dpapi_master_key_access/file_access_win_dpapi_master_key_access.yml)
3. [privilege_escalation/COM_object_hijacking_via_CLSID_default_value](https://github.com/Inovasys-CS/EDI/blob/main/emulation_and_detection/privilege_escalation/CLSID_Default_Value_Hijacking/COM_Object_Hijacking_via_CLSID_Default_Value_Modification.yml)
4. [execution/proc_creation_win_pdqdeploy_execution](https://github.com/Inovasys-CS/EDI/blob/main/emulation_and_detection/execution/proc_creation_win_pdqdeploy_execution/proc_creation_win_pdqdeploy_execution.yml)
5. [persistence/registry_set_com_hijacking_susp_locations](https://github.com/Inovasys-CS/EDI/blob/main/emulation_and_detection/persistence/reg_set_com_hijacking_susp_locations/registry_set_persistence_com_hijacking_susp_locations.yml)
