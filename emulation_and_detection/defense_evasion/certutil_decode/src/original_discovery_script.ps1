$machine_guid = New-Guid
$output_file = "C:\Users\Public\$machine_guid.txt"

whoami >> $output_file
wmic sysaccount list /format:list >> $output_file
wmic ntdomain list /format:list >> $output_file