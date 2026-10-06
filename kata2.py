# Warehouse Audit Calendar
# For days 1–30, apply these rules:

# Every 3rd day → Cycle count
# Every 5th day → Scanner audit
# Days that are both → FULL AUDIT
# Any other day → Normal operations

# Expected: Day 3: Cycle count, Day 5: Scanner audit, Day 15: FULL AUDIT, Day 30: FULL AUDIT
DAYS_IN_MONTH = 31
#DAYS_IN_MONTH = 31 DAYS IN THE MONTH 
for day in range(1, DAYS_IN_MONTH + 1):
    is_cycle_count_day = day % 3 == 0
    is_scanner_audit_day = day % 5 == 0
    if is_cycle_count_day and is_scanner_audit_day:
        print(f"Day {day}: FULL AUDIT")
    elif is_cycle_count_day:
        print(f"Day {day}: Cycle count")
    elif is_scanner_audit_day:
        print(f"Day {day}: Scanner audit")
    else:
        print(f"Day {day}: Normal operations")