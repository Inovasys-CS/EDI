# Cavalry Werewolf APT

Picus Security – 2025/10/20, Report  [Reference Link](https://www.picussecurity.com/resource/blog/cavalry-werewolf-apt)

Cavalry Werewolf APT deploys custom malware to steal credentials, moves laterally using built-in Windows tools, maintains stealthy persistence, and exfiltrates sensitive data over encrypted channels.

---
## Related Rules
## Related Rules

1. [initial_access/email_attachments_with_fake_official/email_attachments_with_fake_official_or_urgent_lures.yml](../initial_access/email_attachments_with_fake_official/email_attachments_with_fake_official_or_urgent_lures.yml)

2. [initial_access/suspicious_attachment_in_outlook_cache/suspicious_files_in_outlook_cache_directory.yml](../initial_access/suspicious_attachment_in_outlook_cache/suspicious_files_in_outlook_cache_directory.yml)

3. [defense_evasion/proc_creation_win_powershell_base64_invoke/proc_creation_win_powershell_base64_invoke.yml](../defense_evasion/proc_creation_win_powershell_base64_invoke/proc_creation_win_powershell_base64_invoke.yml)

4. [discovery/proc_creation_win_susp_network_command/proc_creation_win_susp_network_command.yml](../discovery/proc_creation_win_susp_network_command/proc_creation_win_susp_network_command.yml)

5. [execution/proc_creation_win_powershell_download_iex/proc_creation_win_powershell_download_iex.yml](../execution/proc_creation_win_powershell_download_iex/proc_creation_win_powershell_download_iex.yml)

6. [exfiltration/file_creation_from_telegram/suspicious_file_downloads_from_telegram.yml](../exfiltration/file_creation_from_telegram/suspicious_file_downloads_from_telegram.yml)

7. [command_and_control/non_browser_communication_with_telegram_api/net_connection_win_domain_telegram_api_non_browser_access.yml](../command_and_control/non_browser_communication_with_telegram_api/net_connection_win_domain_telegram_api_non_browser_access.yml)

8. [command_and_control/proc_creation_win_pua_chisel/pua_chisel_tunneling_tool_execution.yml](../command_and_control/proc_creation_win_pua_chisel/pua_chisel_tunneling_tool_execution.yml)
