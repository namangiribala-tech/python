a=int(input("enter your units consumed"))
# --- Bill calculation ---
if a <= 100:
    total = 0
elif a <= 200:
    total = (a - 100) * 5
else:
    total = (100 * 5) + (a - 200) * 10

# --- Discount calculation ---
if a>=200:
    d=total*0.1
else:
    d=0
print("discounted amount =",d)
print("total amount is",total-d)

# --- Recommendations ---
print("\nEnergy Saving Recommendations:")
if a <= 150:
    print("- Great job! Keep using energy-efficient appliances.")
elif a <= 200:
    print("- Replace incandescent bulbs with LEDs.")
    print("- Use smart plugs or timers to save electricity.")
else:
    print("- Schedule an energy audit.")
    print("- Shift high-power usage to off-peak hours.")