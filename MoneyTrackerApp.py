# Print Welcome Banner
print(">>==============================================<<\n"
        "||                      $$$$                    ||\n"
        "||            WELCOME TO DEPE's MONEY           ||\n"
        "||                   TRACKER APP                ||\n"
        "||                      $$$$                    ||\n"
        ">>==============================================<<\n")

# Ask for full name
name = input("\nMasukkan nama lengkap: ")

# Ask for this month's housing expense
housing_expense = int(input("Masukkan pengeluaran kos bulan ini: "))

# Print barrier
print("\n--------------------------------------------------\n")

# Ask for food expenses (Week 1-4) (Dilarang pake loop)
food_expense_1 = int(input("Masukkan pengeluaran makan minggu ke-1: "))
food_expense_2 = int(input("Masukkan pengeluaran makan minggu ke-2: "))
food_expense_3 = int(input("Masukkan pengeluaran makan minggu ke-3: "))
food_expense_4 = int(input("Masukkan pengeluaran makan minggu ke-4: "))
total_food_expense = food_expense_1 + food_expense_2 + food_expense_3 + food_expense_4

# Print barrier
print("\n--------------------------------------------------\n")

# Ask for entertainment expenses (Week 1-4)
entertainment_expense_1 = int(input("Masukkan pengeluaran hiburan minggu ke-1: "))
entertainment_expense_2 = int(input("Masukkan pengeluaran hiburan minggu ke-2: "))
entertainment_expense_3 = int(input("Masukkan pengeluaran hiburan minggu ke-3: "))
entertainment_expense_4 = int(input("Masukkan pengeluaran hiburan minggu ke-4: "))
total_entertainment_expense = entertainment_expense_1 + entertainment_expense_2 + entertainment_expense_3 + entertainment_expense_4

# Print barrier
print("\n--------------------------------------------------\n")

# Ask for transportation expenses (Week 1-4)
transportation_expense_1 = int(input("Masukkan pengeluaran transportasi minggu ke-1: "))
transportation_expense_2 = int(input("Masukkan pengeluaran transportasi minggu ke-2: "))
transportation_expense_3 = int(input("Masukkan pengeluaran transportasi minggu ke-3: "))
transportation_expense_4 = int(input("Masukkan pengeluaran transportasi minggu ke-4: "))
total_transportation_expense = transportation_expense_1 + transportation_expense_2 + transportation_expense_3 + transportation_expense_4

# Print barrier
print("\n--------------------------------------------------\n")

# Ask for other expenses
other_expenses = int(input("Masukkan pengeluaran lainnya: "))

# Print barrier
print("\n--------------------------------------------------\n")

# Count total expenses
total = total_food_expense + total_entertainment_expense + total_transportation_expense + other_expenses + housing_expense

# Print output
print("Halo, " + name + "!")
print("Total pengeluaranmu bulan ini adalah Rp" + str(total*1000))
print("Rata-rata pengeluaranmu bulan ini adalah Rp" + str(int((total/5)*1000)))
print("Rata-rata pengeluaran tiap kategori:")
print("- Kos          : Rp" + str(housing_expense*1000))
print("- Makan        : Rp" + str((int((total_food_expense/4)*1000))))
print("- Hiburan      : Rp" + str((int((total_entertainment_expense/4)*1000))))
print("- Transportasi : Rp" + str((int((total_transportation_expense/4)*1000))))
print("- Lainnya      : Rp" + str(other_expenses*1000))

# Print Thank You Banner
print("\n>>==============================================<<\n"
        "||                     $$$$                     ||\n"
        "||           THANK YOU TO DEPE's MONEY          ||\n"
        "||                  TRACKER APP                 ||\n"
        "||                     $$$$                     ||\n"
        ">>==============================================<<\n")