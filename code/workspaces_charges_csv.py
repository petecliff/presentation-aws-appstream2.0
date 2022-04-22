import csv
from matplotlib.pyplot import plt

days = 30

# Standard = 80GB root, 10GB user
# by_hour_month_charge = 8
# by_hour_hour_charge = 0.32
# always_on_month_charge = 34
# type = "standard_80_10"


# Performance = 80GB root, 10GB user
# by_hour_month_charge = 8
# by_hour_hour_charge = 0.53
# always_on_month_charge = 48
# type = "performance_80_10"

# Performance = 80GB root, 10GB user
by_hour_month_charge = 23
by_hour_hour_charge = 1.97
always_on_month_charge = 735
type = "graphics_100_100"

costs = []

for hours_on_per_day in range(1,25):
    by_hour_total_charge = (days * (by_hour_hour_charge * hours_on_per_day)) + by_hour_month_charge
    cmp = "-"
    if always_on_month_charge < by_hour_total_charge:
        cmp = "+"
    elif always_on_month_charge == by_hour_total_charge:
        cmp = "="
    costs.append([hours_on_per_day, always_on_month_charge, "%.2f" % by_hour_total_charge, cmp])

with open("workspaces_costs_{type}.csv".format(type = type), "w", newline="") as fpo:
    writer = csv.writer(fpo)
    writer.writerows(costs)

