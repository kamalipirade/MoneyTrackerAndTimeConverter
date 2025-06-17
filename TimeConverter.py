# Print Welcome Banner
print("\n>>==============================================<<\n"
        "||                                              ||\n"
        "||             WELCOME TO DEPE's TIME           ||\n"
        "||                 CONVERTER APP                ||\n"
        "||                                              ||\n"
        ">>==============================================<<\n")

# Ask for time in seconds
waktu_pengiriman = int(input("Masukkan waktu pengiriman dalam sekon: "))

# Calculate weeks, days, hours, minutes, and seconds
weeks = waktu_pengiriman // (7 * 24 * 60 * 60)
sisa_weeks =  waktu_pengiriman % (7 * 24 * 60 * 60)
days = sisa_weeks // (24 * 60 * 60)
sisa_days = sisa_weeks % (24 * 60 * 60)
hours = sisa_days // (60 * 60)
sisa_hours = sisa_days % (60 * 60)
minutes = sisa_hours // 60
seconds = sisa_hours % 60

# Print the result
print("Uang Dekdepe akan ditransfer dalam waktu:")
print(f"{weeks} minggu {days} hari {hours} jam {minutes} menit {seconds} detik")
print("Makasih mamah!")

# Print Output Banner
print("\n>>==============================================<<\n"
        "||                                              ||\n"
        "||           THANK YOU FOR USING DEPE'S         ||\n"
        "||              TIME CONVERTER APP              ||\n"
        "||                                              ||\n"
        ">>==============================================<<\n")