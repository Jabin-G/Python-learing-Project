first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

full_name = f"{first_name} {last_name}"
email = f"{first_name.lower()}.{last_name.lower()}@company.com"

print("\n--- Your Profile ---")
print("Full Name:", full_name)
print("Generated Email:", email)