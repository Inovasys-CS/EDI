
# BumbleBee → AdaptixC2 → Akira

The DFIR Report - 2026/06/29, [From Bing Search to Ransomware: BumbleBee and AdaptixC2 Deliver Akira](https://thedfirreport.com/2026/06/29/from-bing-search-to-ransomware-bumblebee-and-adaptixc2-deliver-akira-3/)

A collection of rules created by inovasys team that aim to detect behaviors and artifacts observed in the BumbleBee → AdaptixC2 → Akira attack chain.

## Related Rules

1. [System_File_Execution_Location_Anomaly](https://github.com/Inovasys-CS/EDI/tree/main/emulation_and_detection/defense_evasion/System_File_Execution_Location_Anomaly)
2. [Advanced_IP_Scanner](https://github.com/Inovasys-CS/EDI/tree/main/emulation_and_detection/discovery/Advanced_IP_Scanner)
3. [Wab_Execution_From_Non_Default_Location](https://github.com/Inovasys-CS/EDI/tree/main/emulation_and_detection/defense_evasion/Wab_Execution_From_Non_Default_Location)
4. [wab_unusual_parent_or_child_processes](https://github.com/Inovasys-CS/EDI/tree/main/emulation_and_detection/defense_evasion/wab_unusual_parent_or_child_processes)
5. [password_provided_in_command_line_of_net_exe](https://github.com/Inovasys-CS/EDI/tree/main/emulation_and_detection/discovery/password_provided_in_command_line_of_net_exe)
6. [new_user_created_via_net_exe_never_expire](https://github.com/Inovasys-CS/EDI/tree/main/emulation_and_detection/persistence/new_user_created_via_net_exe_never_expire)
7. [new_user_created_via_net_exe](https://github.com/Inovasys-CS/EDI/tree/main/emulation_and_detection/persistence/new_user_created_via_net_exe)
8. [user_added_to_local_administrators_group](https://github.com/Inovasys-CS/EDI/tree/main/emulation_and_detection/persistence/user_added_to_local_administrators_group)
9. [user_added_to_highly_privileged_group](https://github.com/Inovasys-CS/EDI/tree/main/emulation_and_detection/persistence/user_added_to_highly_privileged_group)
10. [network_connection_to_cloudflared_tunnels_domains](https://github.com/Inovasys-CS/EDI/tree/main/emulation_and_detection/command_and_control/net_conn_cloudflared_tunnels_domains)
11. [cloudflared_portable_execution](https://github.com/Inovasys-CS/EDI/tree/main/emulation_and_detection/command_and_control/cloudflared_portable_execution)
12. [cloudflared_quick_tunnel_execution](https://github.com/Inovasys-CS/EDI/tree/main/emulation_and_detection/command_and_control/cloudflared_quick_tunnel_exe)
13. [cloudflared_tunnel_execution](https://github.com/Inovasys-CS/EDI/tree/main/emulation_and_detection/command_and_control/cloudflared_tunnel_exe)
14. [hacktool_crackmapexec_process_patterns](https://github.com/Inovasys-CS/EDI/tree/main/emulation_and_detection/credential_access/crackmapexec_process_patterns)
15. [recon_command_output_piped_to_findstr_exe](https://github.com/Inovasys-CS/EDI/tree/main/emulation_and_detection/discovery/recon_output_piped_to_findstr_exe)
16. [process_memory_dump_via_comsvcs_dll](https://github.com/Inovasys-CS/EDI/tree/main/emulation_and_detection/credential_access/pro_dump_via_comsvcs_dll)
17. [comsvcs_lsass_dump_via_rundll32](https://github.com/Inovasys-CS/EDI/tree/main/emulation_and_detection/credential_access/comsvcs_lsass_dump_via_rundll32)
18. [shadow_copies_deletion_using_os_utilities](https://github.com/Inovasys-CS/EDI/tree/main/emulation_and_detection/defense_evasion/shadow_copies_deletion_using_os_utilities)
19. [sensitive_file_dump_via_wbadmin_exe](https://github.com/Inovasys-CS/EDI/tree/main/emulation_and_detection/credential_access/sensitive_file_dump_via_wbadmin_exe)
20. [filezilla_installer_execution_from_uncommon_directory](https://github.com/Inovasys-CS/EDI/tree/main/emulation_and_detection/exfiltration/filezilla_exe_from_uncommon_directory)
21. [veeambackup_database_credentials_dump_via_psql_exe](https://github.com/Inovasys-CS/EDI/tree/main/emulation_and_detection/collection/veeambackup_dump_via_psql_exe)
22. [remote_access_tool_rustdesk_execution](https://github.com/Inovasys-CS/EDI/tree/main/emulation_and_detection/command_and_control/rustdesk_execution)
23. [potential_dll_side_loading_of_msimg32_dll](https://github.com/Inovasys-CS/EDI/tree/main/emulation_and_detection/defense_evasion/potential_dll_side_loading_of_msimg32_dll)
