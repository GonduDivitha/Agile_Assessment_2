class Crop:
    def __init__(self, name, area, water_required, fertilizer_required, expected_yield):
        self.name = name
        self.area = area  # in acres
        self.water_required = water_required  # liters per acre
        self.fertilizer_required = fertilizer_required  # kg per acre
        self.expected_yield = expected_yield  # quintals per acre

    def total_water(self):
        return self.area * self.water_required

    def total_fertilizer(self):
        return self.area * self.fertilizer_required

    def total_yield(self):
        return self.area * self.expected_yield


class Farm:
    def __init__(self):
        self.crops = []

    def add_crop(self):
        name = input("Enter crop name: ")
        area = float(input("Enter area (in acres): "))
        water = float(input("Enter water required per acre (liters): "))
        fertilizer = float(input("Enter fertilizer required per acre (kg): "))
        yield_per_acre = float(input("Enter expected yield per acre (quintals): "))

        crop = Crop(name, area, water, fertilizer, yield_per_acre)
        self.crops.append(crop)
        print("Crop added successfully!\n")

    def view_crops(self):
        if not self.crops:
            print("No crops added yet.\n")
            return

        for crop in self.crops:
            print(f"\nCrop: {crop.name}")
            print(f"Area: {crop.area} acres")
            print(f"Total Water Needed: {crop.total_water()} liters")
            print(f"Total Fertilizer Needed: {crop.total_fertilizer()} kg")
            print(f"Expected Total Yield: {crop.total_yield()} quintals")

    def calculate_profit(self):
        if not self.crops:
            print("No crops available.\n")
            return

        total_profit = 0
        for crop in self.crops:
            price = float(input(f"Enter market price per quintal for {crop.name}: "))
            cost = float(input(f"Enter total production cost for {crop.name}: "))
            revenue = crop.total_yield() * price
            profit = revenue - cost
            total_profit += profit
            print(f"Profit for {crop.name}: ₹{profit}")

        print(f"\nTotal Farm Profit: ₹{total_profit}\n")


def main():
    farm = Farm()

    while True:
        print("\n--- Agriculture Management System ---")
        print("1. Add Crop")
        print("2. View Crops")
        print("3. Calculate Profit")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            farm.add_crop()
        elif choice == "2":
            farm.view_crops()
        elif choice == "3":
            farm.calculate_profit()
        elif choice == "4":
            print("Exiting system...")
            break
        else:
            print("Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()