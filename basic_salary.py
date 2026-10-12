total_slips = 0
net_pay = 0
total_net_pay = 0.0
highest_net_pay = -1.0
highest_paid_name = "none"
tax_rate = 0.0
pension_rate = 0.0

print("-------payroll processing system")
while True:
    employee_name = input("enter employee name: ").strip()
    if not employee_name:
        print("employee name cannot be empty.")
        continue

    try:
        hours = float(input("enter hours worked: "))
        rate = float(input("enetr hourly rate: "))
        tax_rate = float(input("enter tax rate: "))
        pension_rate = float(input("enter pension rate: "))
    except ValueError:
        print("invalid numeric input. skipping this employee.")
        continue

    if hours < 0 or hours > 300 or rate <= 0:
        print("invalid entry")
        continue

    regular_hours = min(hours, 160)
    overtime_hours = max(hours - 160, 0)
    regular_pay = regular_hours * rate
    overtime_pay = overtime_hours * rate * 1.5
    gross_pay = regular_pay + overtime_pay

    tax_amount = gross_pay * tax_rate
    pension_amount = gross_pay * pension_rate
    net_pay = gross_pay - tax_amount - pension_amount

    print(f"employee name: {employee_name}")
    print(f"gross pay: {gross_pay:.2f}")
    print(f"tax: {tax_amount:.2f}")
    print(f"pension: {pension_amount:.2f}")
    print(f"net pay: {net_pay:.2f}")

    total_slips += 1
    total_net_pay += net_pay

    if net_pay > highest_net_pay:
        highest_net_pay = net_pay
        highest_paid_name = employee_name

    another = input("do you wish to add another employee? (yes/no): ").strip().lower()
    if another != "yes":
        break
print("\n" + "= " * 15 +"\n")
print("\npayroll summary report")
print(f"total payslips processed: {total_slips}")
print(f"total net pay: {total_net_pay:.2f}")
print(f"highest net pay: {highest_net_pay:.2f}")
print(f"employee with highest pay: {highest_paid_name}")
print("\n" + "= " * 15 +"\n")


  
   
 