# welcome guys
import sys
full_name = sys.argv[1]

email = full_name.lower().replace(".", ".")+ "@company.com"

print("---your profile---")
print("full name:", full_name)
print("Generated email:", email)