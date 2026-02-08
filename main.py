from gui.app import PandaSpaApp

def main():
    app = PandaSpaApp()
    app.run()

if __name__ == "__main__":
    main()


#def show_menu():
#    print("\n🐼 Panda Bamboo Spa Menu")
#    print("1 - Create Spa Service")
#    print("2 - Create Customer")
#    print("3 - Show Services")
#    print("4 - Show Customers")
#    print("5 - Create Booking")
#    print("6 - Show Bookings")
#    print("7 - Show Total Income")
#    print("8 - Add Expense")
#    print("9 - Show Profit")
#    print("10 - Show Most Popular Service")
#    print("0 - Exit")
#
#
#def create_service():
#    name = input("Service name: ")
#    price = float(input("Price (€): "))
#    duration = int(input("Duration (minutes): "))
#
#    service = SpaService(name, price, duration)
#    services.append(service)
#
#    print("✅ Spa service created!")
#
#
#def create_customer():
#    name = input("Customer name: ")
#    species = input("Species: ")
#
#    customer = Customer(name, species)
#    customers.append(customer)
#
#    print("✅ Customer created!")
#
#
#def show_services():
#    if not services:
#        print("No services available.")
#        return
#
#    print("\nAvailable Spa Services:")
#    for service in services:
#        print(f"- {service.name}: {service.price}€ ({service.duration_minutes} min)")
#
#
#def show_customers():
#    if not customers:
#        print("No customers available.")
#        return
#
#    print("\nCustomers:")
#    for customer in customers:
#        print(f"- {customer.species} named {customer.name}")
#
#
#def create_booking():
#    if not customers or not services:
#        print("❌ Please create at least one customer and one service first.")
#        return
#
#    print("\nSelect Customer:")
#    for index, customer in enumerate(customers):
#        print(f"{index} - {customer.species} named {customer.name}")
#
#    customer_index = int(input("Customer number: "))
#    customer = customers[customer_index]
#
#    print("\nSelect Service:")
#    for index, service in enumerate(services):
#        print(f"{index} - {service.name} ({service.price}€)")
#
#    service_index = int(input("Service number: "))
#    service = services[service_index]
#
#    date_time = input("Date and time (e.g. 2026-02-10 14:00): ")
#
#    booking = Booking(customer, service, date_time)
#    bookings.append(booking)
#
#    print("✅ Booking created!")
#
#
#def show_bookings():
#    if not bookings:
#        print("No bookings available.")
#        return
#
#    print("\nBookings:")
#    for booking in bookings:
#        print(
#            f"- {booking.date_time}: "
#            f"{booking.customer.species} {booking.customer.name} "
#            f"-> {booking.service.name}"
#        )
#
#
#def calculate_total_income():
#    total_income = 0.0
#
#    for booking in bookings:
#        total_income += booking.service.price
#
#    return total_income
#
#
#def show_total_income():
#    income = calculate_total_income()
#    print(f"\n💰 Total income: {income:.2f} €")
#
#
#def add_expense():
#    description = input("Expense description: ")
#    amount = float(input("Amount (€): "))
#
#    expenses.append((description, amount))
#    print("✅ Expense added!")
#
#
#def calculate_total_expenses():
#    total = 0.0
#    for expense in expenses:
#        total += expense[1]
#    return total
#
#
#def calculate_profit():
#    income = calculate_total_income()
#    expenses_total = calculate_total_expenses()
#    return income - expenses_total
#
#
#def show_profit():
#    profit = calculate_profit()
#    print(f"\n📊 Current profit: {profit:.2f} €")
#
#
#def get_most_popular_service():
#    if not bookings:
#        return None, 0
#
#    service_count = {}
#
#    for booking in bookings:
#        service_name = booking.service.name
#        service_count[service_name] = service_count.get(service_name, 0) + 1
#
#    most_popular = max(service_count, key=service_count.get)
#    return most_popular, service_count[most_popular]
#
#
#def show_most_popular_service():
#    service_name, count = get_most_popular_service()
#
#    if not service_name:
#        print("No bookings available for statistics.")
#        return
#
#    print(
#        f"\n📊 Most popular service: {service_name} "
#        f"({count} bookings)"
#    )
#
#
#def main():
#    while True:
#        show_menu()
#        choice = input("Choose an option: ")
#
#        if choice == "1":
#            create_service()
#        elif choice == "2":
#            create_customer()
#        elif choice == "3":
#            show_services()
#        elif choice == "4":
#            show_customers()
#        elif choice == "5":
#            create_booking()
#        elif choice == "6":
#            show_bookings()
#        elif choice == "7":
#            show_total_income()
#        elif choice == "8":
#            add_expense()
#        elif choice == "9":
#            show_profit()
#        elif choice == "10":
#            show_most_popular_service()
#        elif choice == "0":
#            save_data(services, customers, bookings, expenses)
#            print("💾 Data saved. Goodbye from Panda Bamboo Spa!")
#            break
#        else:
#            print("❌ Invalid option. Please try again.")
#
#
#if __name__ == "__main__":
#    main()