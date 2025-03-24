from database import session
from models.case import Case
from models.lawyer import Lawyer

def add_case():
    """Adds a new case to the database."""
    try:
        case_id = int(input(" Enter case ID (numeric): "))
        title = input(" Enter case title: ").strip()
        description = input(" Enter case description: ").strip()

        # Check if case ID already exists
        existing_case = session.query(Case).filter_by(id=case_id).first()
        if existing_case:
            print(" Case ID already exists! Please enter a unique ID.")
            return

        # Add new case
        case = Case(id=case_id, title=title, description=description)
        session.add(case)
        session.commit()

        print(f" Case '{title}' added successfully with ID {case_id}!")

    except ValueError:
        print(" Invalid input! Please enter a numeric Case ID.")

def view_cases():
    """Displays all cases in the system."""
    cases = session.query(Case).all()
    if not cases:
        print(" No cases found in the system.")
        return

    print("\n All Cases:")
    for case in cases:
        lawyer_assigned = f" Lawyer ID: {case.lawyer_id}" if case.lawyer_id else " No lawyer assigned"
        print(f" {case.id}: {case.title} - Status: {case.status} | {lawyer_assigned}")

def assign_lawyer():
    """Assigns a lawyer to an existing case."""
    try:
        case_id = int(input(" Enter case ID (numeric): ").strip())
        lawyer_id = int(input(" Enter lawyer ID (numeric): ").strip())

        # Validate case existence
        case = session.query(Case).filter_by(id=case_id).first()
        if not case:
            print(f" Case with ID {case_id} not found! Please enter a valid Case ID.")
            return

        # Validate lawyer existence
        lawyer = session.query(Lawyer).filter_by(id=lawyer_id).first()
        if not lawyer:
            print(f" Lawyer with ID {lawyer_id} not found! Please enter a valid Lawyer ID.")
            return

        # Assign lawyer
        case.lawyer_id = lawyer.id
        session.commit()
        print(f" Lawyer {lawyer_id} assigned to Case {case_id} successfully!")

    except ValueError:
        print(" Invalid input! Please enter numeric Case ID and Lawyer ID.")

def add_lawyer():
    """Adds a new lawyer to the database."""
    name = input(" Enter lawyer's name: ").strip()
    
    if not name:
        print(" Lawyer name cannot be empty!")
        return

    lawyer = Lawyer(name=name)
    session.add(lawyer)
    session.commit()
    print(f" Lawyer '{name}' added successfully with ID {lawyer.id}!")

def view_lawyers():
    """Displays all registered lawyers."""
    lawyers = session.query(Lawyer).all()
    if not lawyers:
        print(" No lawyers found in the system. Add a lawyer first.")
        return

    print("\n Registered Lawyers:")
    for lawyer in lawyers:
        print(f" {lawyer.id}: {lawyer.name}")

def main():
    """Main menu loop for the Law Case Management System."""
    while True:
        print("\n Law Case Management System")
        print("1 Add Case")
        print("2 View Cases")
        print("3 Assign Lawyer")
        print("4 Add Lawyer")
        print("5 View Lawyers")
        print("6 Exit")

        choice = input("🔹 Enter choice: ")

        if choice == "1":
            add_case()
        elif choice == "2":
            view_cases()
        elif choice == "3":
            assign_lawyer()
        elif choice == "4":
            add_lawyer()
        elif choice == "5":
            view_lawyers()
        elif choice == "6":
            print(" Exiting program... Goodbye!")
            break
        else:
            print(" Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
