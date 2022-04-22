import csv

days = 30

rds_sal_fee_day = 0.14 # $4.19/30

on_demand_stopped_cost_hour = 0.026
running_instance_cost_hour = 0.11

on_demand = 0
always_on = 0

costs = []

for hours_on in range(1,25):
    for day in range(1,days+1):
        always_on = always_on + (24 * running_instance_cost_hour) + rds_sal_fee_day
        on_demand = on_demand + (hours_on * running_instance_cost_hour) + rds_sal_fee_day
        day_cost = [hours_on, day, "%.2f" % always_on, "%.2f" % on_demand]
        costs.append(day_cost)
    on_demand = 0
    always_on = 0

with open("appstream2_costs.csv", "w", newline="") as fpo:
    writer = csv.writer(fpo)
    writer.writerows(costs)

