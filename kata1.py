# Scanner Health Checks
# A Medline branch checks its handheld scanners every 15 minutes. Print the first 10 check times.
# Expected: Check 1: 15 minutes after shift start … Check 10: 150 minutes after shift start
for check in range(10):
    check_time = (check * 60 + 1) * 15
    print(check_time // 60, ":", check_time % 60)
# check in range 10