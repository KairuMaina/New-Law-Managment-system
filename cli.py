from database import session
from models.case import Case
from models.lawyer import Lawyer

def add_case():
    title = input("Enter case title: ")
    description = input("Enter case description: ")

    case = Case(title=title, description=description)
    session.add(case)
    session.commit()

    print("✅ Case added successfully!")

def view_cases():
    cases = session.query(Case).all()
    if not cases:
        print("⚠️ No cases found.")
        return

    for case in cases:
        lawyer_assigned = f"- Lawyer ID: {case.lawyer_id}" if case.lawyer_id else "- No lawyer assigned"
        print(f"📌 {case.id}: {case.title} - Status: {case.status} {lawyer_assigned}")

def assign_lawyer():
    try:
        case_id = int(input("Enter case ID: "))  # Convert input to integer
        lawyer_id = int(input("Enter lawyer ID: "))  # Convert input to integer

        # Validate case exists
        case = session.query(Case).filter_by(id=case_id).first()
        if not case:
            print("⚠️ Case not found!")
            return

        # Validate lawyer exists
        lawyer = session.query(Lawyer).filter_by(id=lawyer_id).first()
        if not lawyer:
            print("⚠️ Lawyer not found!")
            return

        case.lawyer_id = lawyer.id
        session.commit()
        print(f"✅ Lawyer {lawyer_id} assigned to Case {case_id} successfully!")

    except ValueError:
        print("❌ Invalid input! Please enter numeric Case ID and Lawyer ID.")

def main():
    while True:
        print("\n📜 Law Case Management System")
        print("1️⃣ Add Case")
        print("2️⃣ View Cases")
        print("3️⃣ Assign Lawyer")
        print("4️⃣ Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_case()
        elif choice == "2":
            view_cases()
        elif choice == "3":
            assign_lawyer()
        elif choice == "4":
            print("🚪 Exiting program... Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
