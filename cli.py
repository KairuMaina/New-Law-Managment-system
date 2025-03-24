from database import session
from models.case import Case
from models.lawyer import Lawyer

def add_case():
    title = input("Enter case title: ")
    description = input("Enter case description: ")
    case = Case(title=title, description=description)
    session.add(case)
    session.commit()
    print("Case added successfully!")

def view_cases():
    cases = session.query(Case).all()
    for case in cases:
        print(f"{case.id}: {case.title} - Status: {case.status}")

def assign_lawyer():
    case_id = int(input("Enter case ID: "))
    lawyer_id = int(input("Enter lawyer ID: "))
    case = session.query(Case).get(case_id)
    case.lawyer_id = lawyer_id
    session.commit()
    print("Lawyer assigned!")

def main():
    while True:
        print("\nLaw Case Management System")
        print("1. Add Case")
        print("2. View Cases")
        print("3. Assign Lawyer")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_case()
        elif choice == "2":
            view_cases()
        elif choice == "3":
            assign_lawyer()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
