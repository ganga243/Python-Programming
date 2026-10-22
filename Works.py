# 1.college Event Registration
# --------------------------------------------

# age = int(input("Enter your age: "))
# student = input("Are you a student? (yes/no): ")

# if age >= 18 and age <= 25 and student == "yes":
#     print("Eligible for registration")
# else:
#     print("Not eligible for registration")
# -------------------------------------------------------

# 2.Online Shopping Discount
# -----------------------------------------

# amount = int(input("Enter order amount: "))
# premium = input("Are you a premium member? (yes/no): ")

# if amount >= 3000 or premium == "yes":
#     print("Customer qualifies for discount")
# else:
#     print("Customer does not qualify for discount")

# 3.Airport Check-in
# --------------------------------------------

# ticket = input("Is your ticket confirmed? (yes/no): ")
# passport = input("Is your passport valid? (yes/no): ")
# hours = float(input("How many hours until departure? "))

# if ticket == "yes" and passport == "yes" and hours > 2:
#     print("Online check-in is available")
# else:
#     print("Online check-in is not available")

# 4.Movie Ticket Booking
# -------------------------------------------------

# age = int(input("Enter your age: "))

# if age < 12 or age >= 60:
#     print("Eligible for special ticket price")
# else:
#     print("Not eligible for special ticket price")

# 5.Bank Loan Pre-Eligibility
# --------------------------------------------------------

# income = int(input("Enter your monthly income: "))
# credit_score = int(input("Enter your credit score: "))
# default = input("Do you have an existing loan default? (yes/no): ")

# if income >= 40000 and credit_score >= 700 and default == "no":
#     print("Eligible for loan")
# else:
#     print("Not eligible for loan")

# 6.Food Delivery-Free Shipping
# -----------------------------------------

# amount = 600
# premium = False
# delivery_enabled = True

# if (amount >= 500 or premium) and delivery_enabled:
#     print("Free delivery available")
# else:
#     print("Free delivery not available")

# 7.Employee Work-From-Home Eligibility
# ---------------------------------------------------

# experience = 8
# remote_work = True

# if experience >= 6 and remote_work:
#     print("Work from home allowed")
# else:
#     print("Work from home not allowed")

# 8. Hotel Room Booking
# ----------------------------------------

# room_available = True
# valid_payment = True
# reservations_open = True

# if room_available and valid_payment and reservations_open:
#     print("Booking can proceed")
# else:
#     print("Booking cannot proceed")

# 10. Gym Membership Plan
# ---------------------------------------------

# years = 2
# membership_active = True
# yearly_plan = False

# if (years >= 1 and membership_active) or yearly_plan:
#     print("Premium upgrade available")
# else:
#     print("Premium upgrade not available")

# 11. Ride Booking Application
# ----------------------------------------

# service_area = True
# driver_available = True
# scheduled_rides = False

# if (service_area and driver_available) or scheduled_rides:
#     print("Ride booking available")
# else:
#     print("Ride booking not available")

# 12. E-commerce Product Return
# ------------------------------------------

# days = 8
# unused = True
# return_eligible = True

# if days <= 7 and unused and return_eligible:
#     print("Return request accepted")
# else:
#     print("Return request rejected")

# 13. Library Book Borrowing
# ---------------------------------------

# no_overdue = False
# membership_active = True
# book_available = True

# if no_overdue and membership_active and book_available:
#     print("Book can be borrowed")
# else:
#     print("Book cannot be borrowed")

# 14. Job Application Screening
# ---------------------------------------
# experience = -1
# django = True
# fastapi = False

# if (experience >= 1 and (django or fastapi)) or experience >= 3:
#     print("Candidate qualifies for next stage")
# else:
#     print("Candidate does not qualify")

# 15. Mobile Data Usage Alert
# -----------------------------------------

# usage = 80
# remaining_data = 2
# unlimited = False

# if (usage >= 90 or remaining_data < 1) and not unlimited:
#     print("Warning: Data usage is high")
# else:
#     print("No warning")

# 16. Parking Lot Entry
# ----------------------------------------

# parking_pass = False
# visitor_payment = False
# parking_full = False

# if (parking_pass or visitor_payment) and not parking_full:
#     print("Vehicle can enter")
# else:
#     print("Vehicle cannot enter")

# 17. Scholarship Eligibility
# ---------------------------------------

# score = 90
# attendance = 80

# if (score >= 85 and attendance >= 75) or score >= 95:
#     print("Student is eligible for scholarship")
# else:
#     print("Student is not eligible for scholarship")

# 18. Food Ordering – Restaurant Availability
# ------------------------------------------------------------

# restaurant_open = False
# delivers_location = True
# online_orders = True

# if restaurant_open and delivers_location and online_orders:
#     print("Order can be placed")
# else:
#     print("Order cannot be placed")

# 19. Smart Home Security
# ------------------------------------------

# motion_detected = False
# system_armed = True
# door_opened = False

# if (motion_detected and system_armed) or (door_opened and system_armed):
#     print("Security alert triggered")
# else:
#     print("Security alert not triggered")

# 20. Travel Insurance Eligibility
# -------------------------------------------------

age = 35   #25
trip_days = 40   #20
country_covered = True
destination_excluded = False

if 18 <= age <= 65 and trip_days <= 30 and country_covered and not destination_excluded:
    print("Eligible for travel insurance")
else:
    print("Not eligible for travel insurance")