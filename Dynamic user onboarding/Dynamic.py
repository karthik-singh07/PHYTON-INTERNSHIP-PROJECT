roles = {'1': 'admin', '2': 'employee', '3': 'regular', '4': 'fresher', '5': 'experience', '6': 'guest'}

class FeedbackSystem:
    onboarding_system = {
        'admin': {'welcoming': [], 'documentation': [], 'access': [], 'accounts': [], 'follow_up': []},
        'employee': {'welcoming': [], 'documentation': [], 'access': [], 'accounts': [], 'follow_up': []},
        'regular': {'welcoming': [], 'documentation': [], 'access': [], 'accounts': [], 'follow_up': []},
        'fresher': {'welcoming': [], 'documentation': [], 'access': [], 'accounts': [], 'follow_up': []},
        'experience': {'welcoming': [], 'documentation': [], 'access': [], 'accounts': [], 'follow_up': []},
        'guest': {'welcoming': [], 'documentation': [], 'access': [], 'accounts': [], 'follow_up': []},
    }


    def _init_(self):
        self.feedback_data = {}

    def design_onboarding_flow(self, category):
        print(f"Category : {category}")
        for index, step in enumerate(self.onboarding_system[category].keys(), 1):
            print(f'{index} - {step}')

    def collect_feedback_step(self, role):
        feedback_fields = input(f"Enter feedback fields for {roles[role]} ").split(',')
        role_feedback = self.feedback_data.get(role, {})

        for field in feedback_fields:
            feedback_value = input(f"Enter feedback for {field}: ")
            role_feedback[field] = feedback_value

        self.feedback_data[role] = role_feedback
        

    def update_feedback(self, role):
        feedback_fields = input(f"Enter feedback fields to update for {roles[role]} ").split(',')
        role_feedback = self.feedback_data.get(role, {})
        role_feedback = {field: input(f"Enter updated feedback for {field}: ") for field in feedback_fields}
        self.feedback_data[role] = role_feedback

    def delete_feedback(self, role):
        if role in self.feedback_data:
            del self.feedback_data[role] 
            print(f"Feedback for {roles[role]} deleted successfully.")
        else:
            print("No feedback found for the specified role.")

    def print_feedback(self):
        print("\n=== Feedback Summary ===")
        for role, feedback in self.feedback_data.items():
            print(f"{role} : {roles[role]}")
            for field, value in feedback.items():
                print(f"{field}: {value}")

    def print_onboarding_system_key(self, category_index):
        category = roles.get(str(category_index))
        if category:
            print(category.capitalize())
            return category
        else:
            print("Invalid category index.")
            return None

    
def main():
    feedback_system = FeedbackSystem()

    while True:
        print("\n=== Menu ===")
        print("1. Collect Feedback")
        print("2. Update Feedback")
        print("3. Delete Feedback")
        print("4. Print Feedback")
        print("5. To see onboarding steps")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '6':
            break
        
        match choice :
            case '1'|'2'|'3'|'4' : 
                category_index = input("Enter the onboarding category index (1-6): ")
                if not category_index.isdigit() or not (1 <= int(category_index) <= 6):
                    print("Invalid category index. Please enter a number between 1 and 6.")
                category = feedback_system.print_onboarding_system_key(category_index)
                if not category:
                    continue

        match choice : 
            case '1':
                feedback_system.collect_feedback_step(str(category_index))
            case '2':
                feedback_system.update_feedback(str(category_index))
            case '3':
                feedback_system.delete_feedback(str(category_index))
            case '4':
                feedback_system.print_feedback()
            case '5' :
                category = input("Enter the cateory to see the onboarding steps : ")
                feedback_system.design_onboarding_flow(category) 
            case _ : 
                print("Invalid choice. Please enter a number between 1 and 5.")

    print("Exiting the program.")


if __name__ == "_main_":
    main()