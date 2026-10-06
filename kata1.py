# Scanner Health Checks
# A Medline branch checks its handheld scanners every 15 minutes. Print the first 10 check times.
# Expected: Check 1: 15 minutes after shift start … Check 10: 150 minutes after shift start
for check in range(1, 11):
    check_time = check * 15
    print(f"Check {check}: {check_time} minutes after shift start") 
    