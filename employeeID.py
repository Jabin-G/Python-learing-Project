import sys
import random

first_name = sys.argv[1]
last_name = sys.argv[2]

full_name = f"{first_name} {last_name}"
email = f"{first_name.lower()}.{last_name.lower()}@company.com"

# Generate reference code
reference_code = (
    first_name[:2].upper() +
    last_name[:2].upper() +
    str(random.randint(1000, 9999))
)

print("--- Your Profile ---")
print("Full Name:", full_name)
print("Generated Email:", email)
print("Reference Code:", reference_code)