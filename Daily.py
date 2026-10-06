print("DAILY TASK MANAGER")

# ---------- PART 1: homework time ----------
homework = int(input("Enter the number of homeworks you have."))
min = homework * 20

# ---------- PART 2: choose a plan ----------
if min >= 60:
    print("START NOW.")
else:
    print("ALSO START NOW.")

# ---------- PART 3: free time ----------
if min >= 120:
    print("NO FREE TIME.")
else:
    print("Ok, free time.")
# ---------- PART 4: summary ----------
print("===== DAILY PLAN =====")
if homework == 3:
    print("Lots of hw.")
else:
    print("Not lots of hw, have some fun.")
