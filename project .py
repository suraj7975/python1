class TrafficSignal:
    def _init_(self, signal_id, duration_green, duration_yellow, duration_red):
        self.signal_id = signal_id
        self.duration_green = duration_green
        self.duration_yellow = duration_yellow
        self.duration_red = duration_red

class TrafficSignalController:
    def _init_(self):
        self.signals = {}

    def create_signal(self, signal_id, duration_green, duration_yellow, duration_red):
        signal = TrafficSignal(signal_id, duration_green, duration_yellow, duration_red)
        self.signals[signal_id] = signal

    def update_signal(self, signal_id, duration_green, duration_yellow, duration_red):
        if signal_id in self.signals:
            self.signals[signal_id].duration_green = duration_green
            self.signals[signal_id].duration_yellow = duration_yellow
            self.signals[signal_id].duration_red = duration_red
        else:
            print("Signal ID not found.")

    def delete_signal(self, signal_id):
        if signal_id in self.signals:
            del self.signals[signal_id]
        else:
            print("Signal ID not found.")

    def optimize_traffic_signals(self, signal_id):
        # Algorithm to optimize traffic signals
        pass

    def analyze_traffic_impact(self, impact_id):
        # Analyze the impact of timing changes on traffic
        pass

def menu():
    print("\n1. Create Traffic Signal")
    print("2. Update Traffic Signal")
    print("3. Delete Traffic Signal")
    print("4. Optimize Traffic Signals")
    print("5. Analyze Traffic Impact")
    print("6. Exit")

def main():
    controller = TrafficSignalController()

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            signal_id = input("Enter signal ID: ")
            duration_green = int(input("Enter duration of green light: "))
            duration_yellow = int(input("Enter duration of yellow light: "))
            duration_red = int(input("Enter duration of red light: "))
            controller.create_signal(signal_id, duration_green, duration_yellow, duration_red)
            print("Traffic Signal created successfully.")

        elif choice == '2':
            signal_id = input("Enter signal ID to update: ")
            duration_green = int(input("Enter new duration of green light: "))
            duration_yellow = int(input("Enter new duration of yellow light: "))
            duration_red = int(input("Enter new duration of red light: "))
            controller.update_signal(signal_id, duration_green, duration_yellow, duration_red)
            print("Traffic Signal updated successfully.")

        elif choice == '3':
            signal_id = input("Enter signal ID to delete: ")
            controller.delete_signal(signal_id)
            print("Traffic Signal deleted successfully.")

        elif choice == '4':
            signal_id = input("Enter signal ID to optimize: ")
            controller.optimize_traffic_signals(signal_id)
            print("Traffic Signals optimized successfully.")

        elif choice == '5':
            impact_id = input("Enter impact ID to analyze: ")
            controller.analyze_traffic_impact(impact_id)

        elif choice == '6':
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if _name_ == "_main_":
    main()
