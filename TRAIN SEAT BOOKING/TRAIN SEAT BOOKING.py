
# Project 33: Train Seat Booking

import array


# Integers
# Example seat bookings per coach
coach_bookings = [45, 38, 50, 29, 60]

total_bookings = sum(coach_bookings)
average_bookings = total_bookings / len(coach_bookings)
min_bookings = min(coach_bookings)
max_bookings = max(coach_bookings)

# Strings with f-strings
report = f"""
Train Seat Booking Report
Total Bookings   : {total_bookings}
Average Bookings : {average_bookings:.2f}
Minimum Bookings : {min_bookings}
Maximum Bookings : {max_bookings}
"""
print(report)

# Booleans with threshold + compound condition
threshold = 40
if average_bookings > threshold and max_bookings > 50:
    print("Status: Above Standard\n")
else:
    print("Status: Below Standard\n")
# Lists

print("=== LIST OPERATIONS ===")
seat_list = ["Coach-A", "Coach-B", "Coach-C", "Coach-D"]

print("Original List:", seat_list)

# Add new element
seat_list.append("Coach-E")

# Remove one based on a condition (remove Coach-B if it exists)
if "Coach-B" in seat_list:
    seat_list.remove("Coach-B")

# Sort list
seat_list.sort()

print("Modified & Sorted List:", seat_list, "\n")
# Arrays
print("=== ARRAY OPERATIONS ===")
# Store a fixed subset of bookings in an array
booking_array = array.array("i", [45, 38, 50])

# Compute sum
array_sum = sum(booking_array)
list_sum = sum(coach_bookings)

print("Array Elements:", booking_array.tolist())
print("Array Sum:", array_sum)
print("List Sum (All Coaches):", list_sum, "\n")
# Dictionaries
print("=== DICTIONARY OPERATIONS ===")
records = [
    {"id": 1, "name": "Coach-A", "value": 45},
    {"id": 2, "name": "Coach-B", "value": 38},
    {"id": 3, "name": "Coach-C", "value": 50},
]

# Update one record (Coach-B new value 42)
for record in records:
    if record["name"] == "Coach-B":
        record["value"] = 42

# Delete one record (remove Coach-C)
records = [r for r in records if r["name"] != "Coach-C"]

# Compute total of 'value' field
total_value = sum(r["value"] for r in records)

print("Updated Records:", records)
print("Total Value After Update:", total_value)
