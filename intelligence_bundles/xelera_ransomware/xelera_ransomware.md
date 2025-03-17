
# Xelera ransomware

Seqrite - 2025/02/12, Report, [Reference Link](https://www.seqrite.com/blog/xelera-ransomware-fake-fci-job-offers/)

A collection of rules that aim to detect xelera ransomware which act as a RAT, uses discord as C2 and encrypt files.

## Related Rules

1. [initial_access/executable_file_create_from_office](https://github.com/Inovasys-CS/EDI/tree/main/emulation_and_detection/initial_access/executable_file_create_from_office)
2. [defense_evasion/executable_downloaded_from_github](https://github.com/Inovasys-CS/EDI/tree/main/emulation_and_detection/defense_evasion/executable_downloaded_from_github)
3. [execution/office_application_spawning_another_process](https://github.com/Inovasys-CS/EDI/tree/main/emulation_and_detection/execution/office_application_spawning_another_process)
4. [command_and_control/discord_as_legitimate_c2](https://github.com/Inovasys-CS/EDI/tree/main/emulation_and_detection/command_and_control/discord_as_legitimate_c2)
5. [command_and_control/discord_cdn_connection](https://github.com/Inovasys-CS/EDI/tree/main/emulation_and_detection/command_and_control/discord_cdn_connection)
6. [persistence/file_event_win_startup_folder_file_write](https://github.com/Inovasys-CS/EDI/tree/main/emulation_and_detection/persistence/file_event_win_startup_folder_file_write)

