from pathlib import Path
import random
from datetime import date, timedelta
from faker import Faker

fake = Faker()

# -------------------------------------
# Helper Function
# -------------------------------------

def write_insert_file(file_path, table_name, columns, rows):

    with open(file_path, "w", encoding="utf-8") as f:

        f.write("-- ======================================\n")
        f.write(f"-- {table_name} Seed Data\n")
        f.write("-- Generated Automatically\n")
        f.write("-- ======================================\n\n")

        f.write(
            f"INSERT INTO {table_name} "
            f"({', '.join(columns)})\nVALUES\n"
        )

        f.write(",\n".join(rows))

        f.write(";\n")
# -------------------------------------
# Paths
# -------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_DIR = BASE_DIR / "database"

DATABASE_DIR.mkdir(exist_ok=True)

# -------------------------------------
# Configuration
# -------------------------------------

EMPLOYEE_COUNT = 20
PROJECT_COUNT = 15

ATTENDANCE_DAYS = 30

LEAVE_REQUEST_COUNT = 40

PERFORMANCE_REVIEW_COUNT = 20

SALARY_HISTORY_COUNT = 40

ASSET_COUNT = 30

TRAINING_COUNT = 40

DEPARTMENTS = [
    ("IT", "John Smith", "Hyderabad", 500000),
    ("HR", "Sarah Johnson", "Bangalore", 200000),
    ("Finance", "David Wilson", "Mumbai", 350000),
    ("Sales", "Emily Davis", "Pune", 400000),
    ("Marketing", "Robert Brown", "Chennai", 300000),
    ("Operations", "Michael Scott", "Delhi", 450000),
    ("Research", "Sophia Miller", "Hyderabad", 600000),
    ("Customer Support", "James Anderson", "Kolkata", 180000),
    ("Legal", "Olivia Thomas", "Mumbai", 250000),
    ("Administration", "William Harris", "Bangalore", 220000)
]

DESIGNATIONS = [
    "Software Engineer",
    "Senior Software Engineer",
    "Backend Developer",
    "Frontend Developer",
    "Full Stack Developer",
    "AI Engineer",
    "ML Engineer",
    "Data Scientist",
    "HR Executive",
    "HR Manager",
    "Financial Analyst",
    "Accountant",
    "Sales Executive",
    "Sales Manager",
    "Marketing Executive",
    "Marketing Manager",
    "Operations Executive",
    "Project Manager",
    "Legal Advisor",
    "Support Engineer"
]

PROJECT_NAMES = [
    "AI Recruitment Assistant",
    "Employee Management System",
    "Payroll Automation",
    "Customer Analytics Dashboard",
    "Inventory Management",
    "Healthcare Portal",
    "Banking CRM",
    "Retail Sales Dashboard",
    "Smart Attendance System",
    "Document AI Platform",
    "Fraud Detection System",
    "AI SQL Assistant",
    "Cloud Migration",
    "HR Analytics",
    "E-Commerce Platform",
    "Supply Chain Optimizer",
    "Financial Dashboard",
    "Customer Support Bot",
    "Sales Forecasting",
    "LLM Observability Platform",
    "Project Tracking System",
    "Marketing Analytics",
    "Hospital Management",
    "Student Portal",
    "IoT Monitoring",
    "Expense Tracker",
    "Warehouse Automation",
    "Insurance Claims System",
    "Business Intelligence",
    "AI Chatbot"
]


# -------------------------------------
# Department Generator
# -------------------------------------

def generate_departments():

    output_file = DATABASE_DIR / "02_seed_departments.sql"

    rows = []

    for dept in DEPARTMENTS:

        rows.append(
            f"('{dept[0]}','{dept[1]}','{dept[2]}',{dept[3]})"
        )

    write_insert_file(
        output_file,
        "departments",
        [
            "department_name",
            "manager",
            "location",
            "budget"
        ],
        rows
    )

    print("Departments Generated Successfully")

# -------------------------------------
# Employee Generator
# -------------------------------------

def generate_employees():

    output_file = DATABASE_DIR / "03_seed_employees.sql"

    rows = []

    for _ in range(EMPLOYEE_COUNT):

        first_name = fake.first_name().replace("'", "''")
        last_name = fake.last_name().replace("'", "''")

        email = f"{first_name.lower()}.{last_name.lower()}@company.com"

        department = random.choice(DEPARTMENTS)[0]

        designation = random.choice(DESIGNATIONS)

        salary = random.randint(35000, 120000)

        hire_date = fake.date_between(
            start_date="-5y",
            end_date="today"
        )

        rows.append(
            f"('{first_name}',"
            f"'{last_name}',"
            f"'{email}',"
            f"'{department}',"
            f"'{designation}',"
            f"{salary},"
            f"'{hire_date}')"
        )

    write_insert_file(
        output_file,
        "employees",
        [
            "first_name",
            "last_name",
            "email",
            "department",
            "designation",
            "salary",
            "hire_date"
        ],
        rows
    )

    print("Employees Generated Successfully")

# -------------------------------------
# Project Generator
# -------------------------------------

def generate_projects():

    output_file = DATABASE_DIR / "04_seed_projects.sql"

    clients = [
        "Microsoft",
        "Google",
        "Amazon",
        "Infosys",
        "TCS",
        "Wipro",
        "Accenture",
        "Deloitte",
        "Capgemini",
        "IBM"
    ]

    statuses = [
        "Completed",
        "In Progress",
        "On Hold"
    ]

    rows = []

    for i in range(PROJECT_COUNT):

        project_name = PROJECT_NAMES[i]

        client = random.choice(clients)

        budget = random.randint(100000, 1000000)

        start_date = fake.date_between(
            start_date="-3y",
            end_date="-1y"
        )

        end_date = fake.date_between(
            start_date="today",
            end_date="+1y"
        )

        status = random.choice(statuses)

        rows.append(
            f"('{project_name}',"
            f"'{client}',"
            f"{budget},"
            f"'{start_date}',"
            f"'{end_date}',"
            f"'{status}')"
        )

    write_insert_file(
        output_file,
        "projects",
        [
            "project_name",
            "client_name",
            "budget",
            "start_date",
            "end_date",
            "status"
        ],
        rows
    )

    print("Projects Generated Successfully")


# -------------------------------------
# Employee Project Generator
# -------------------------------------

def generate_employee_projects():

    output_file = DATABASE_DIR / "05_seed_employee_projects.sql"

    roles = [
        "Project Manager",
        "Team Lead",
        "Backend Developer",
        "Frontend Developer",
        "Full Stack Developer",
        "AI Engineer",
        "ML Engineer",
        "Data Scientist",
        "QA Engineer",
        "DevOps Engineer",
        "Business Analyst",
        "UI/UX Designer",
        "Database Administrator",
        "Support Engineer"
    ]

    rows = []
    assigned = set()

    # Each employee will be assigned to 1–3 unique projects
    for employee_id in range(1, EMPLOYEE_COUNT + 1):

        project_count = random.randint(1, 3)

        available_projects = random.sample(
            range(1, PROJECT_COUNT + 1),
            project_count
        )

        for project_id in available_projects:

            key = (employee_id, project_id)

            if key not in assigned:

                assigned.add(key)

                role = random.choice(roles)

                rows.append(
                    f"({employee_id}, {project_id}, '{role}')"
                )

    write_insert_file(
        output_file,
        "employee_projects",
        [
            "employee_id",
            "project_id",
            "role"
        ],
        rows
    )

    print("Employee Projects Generated Successfully")

# -------------------------------------
# Attendance Generator
# -------------------------------------

def generate_attendance():

    output_file = DATABASE_DIR / "06_seed_attendance.sql"

    start_date = date(2026, 6, 1)

    statuses = [
        "Present",
        "Present",
        "Present",
        "Present",
        "WFH",
        "Absent"
    ]

    rows = []

    for employee_id in range(1, EMPLOYEE_COUNT + 1):

        for day in range(ATTENDANCE_DAYS):

            attendance_date = start_date + timedelta(days=day)

            status = random.choice(statuses)

            rows.append(
                f"({employee_id}, '{attendance_date}', '{status}')"
            )

    with open(output_file, "w", encoding="utf-8") as f:

        f.write("-- ======================================\n")
        f.write("-- Attendance Seed Data\n")
        f.write("-- Generated Automatically\n")
        f.write("-- ======================================\n\n")

        f.write(
            "INSERT INTO attendance "
            "(employee_id, attendance_date, status)\nVALUES\n"
        )

        f.write(",\n".join(rows))

        f.write(";\n")

    print("Attendance Generated Successfully")

# -------------------------------------
# Leave Request Generator
# -------------------------------------

def generate_leave_requests():

    output_file = DATABASE_DIR / "07_seed_leave_requests.sql"

    leave_types = [
        "Sick Leave",
        "Casual Leave",
        "Vacation",
        "Work From Home"
    ]

    statuses = [
        "Approved",
        "Approved",
        "Pending",
        "Rejected"
    ]

    rows = []

    for _ in range(1, LEAVE_REQUEST_COUNT):

        employee_id = random.randint(1, EMPLOYEE_COUNT)

        start_day = random.randint(1, 25)

        duration = random.randint(1, 5)

        start_date = date(2026, 6, start_day)
        end_date = start_date + timedelta(days=duration)

        rows.append(
            f"({employee_id}, "
            f"'{random.choice(leave_types)}', "
            f"'{start_date}', "
            f"'{end_date}', "
            f"'{random.choice(statuses)}')"
        )

    write_insert_file(
        output_file,
        "leave_requests",
        [
            "employee_id",
            "leave_type",
            "start_date",
            "end_date",
            "status"
        ],
        rows
    )

    print("Leave Requests Generated Successfully")


# -------------------------------------
# Performance Review Generator
# -------------------------------------

def generate_performance_reviews():

    output_file = DATABASE_DIR / "08_seed_performance.sql"

    remarks = [
        "Outstanding Performance",
        "Excellent Team Player",
        "Exceeds Expectations",
        "Good Performance",
        "Needs Improvement"
    ]

    rows = []

    for _ in range(PERFORMANCE_REVIEW_COUNT):

        employee_id = random.randint(1, EMPLOYEE_COUNT)

        review_year = random.choice([2024, 2025, 2026])

        rating = round(random.uniform(3.0, 5.0), 1)

        remark = random.choice(remarks).replace("'", "''")

        rows.append(
            f"({employee_id}, {review_year}, {rating}, '{remark}')"
        )

    write_insert_file(
        output_file,
        "performance_reviews",
        [
            "employee_id",
            "review_year",
            "rating",
            "remarks"
        ],
        rows
    )

    print("Performance Reviews Generated Successfully")


# -------------------------------------
# Salary History Generator
# -------------------------------------

def generate_salary_history():

    output_file = DATABASE_DIR / "09_seed_salary_history.sql"

    rows = []

    for _ in range(SALARY_HISTORY_COUNT):

        employee_id = random.randint(1, EMPLOYEE_COUNT)

        previous_salary = random.randint(35000, 90000)

        increment = random.randint(3000, 15000)

        new_salary = previous_salary + increment

        effective_date = date(
            random.choice([2024, 2025, 2026]),
            random.randint(1, 12),
            random.randint(1, 28)
        )

        rows.append(
            f"({employee_id}, "
            f"{previous_salary}, "
            f"{new_salary}, "
            f"'{effective_date}')"
        )

    write_insert_file(
        output_file,
        "salary_history",
        [
            "employee_id",
            "previous_salary",
            "new_salary",
            "effective_date"
        ],
        rows
    )

    print("Salary History Generated Successfully")


# -------------------------------------
# Asset Generator
# -------------------------------------

def generate_assets():

    output_file = DATABASE_DIR / "10_seed_assets.sql"

    asset_names = [
        "Dell Laptop",
        "MacBook Pro",
        "Lenovo ThinkPad",
        "HP EliteBook",
        "Monitor",
        "Keyboard",
        "Mouse",
        "Docking Station",
        "iPhone",
        "Android Phone"
    ]

    rows = []

    for i in range(ASSET_COUNT):

        employee_id = random.randint(1, EMPLOYEE_COUNT)

        asset_name = random.choice(asset_names)

        serial_number = f"AST-{1000+i}"

        assigned_date = date(
            random.choice([2024, 2025, 2026]),
            random.randint(1, 12),
            random.randint(1, 28)
        )

        rows.append(
            f"({employee_id}, "
            f"'{asset_name}', "
            f"'{serial_number}', "
            f"'{assigned_date}')"
        )

    write_insert_file(
        output_file,
        "assets",
        [
            "employee_id",
            "asset_name",
            "serial_number",
            "assigned_date"
        ],
        rows
    )

    print("Assets Generated Successfully")


# -------------------------------------
# Training Records Generator
# -------------------------------------

def generate_training_records():

    output_file = DATABASE_DIR / "11_seed_training.sql"

    courses = [
        "Python",
        "Advanced SQL",
        "FastAPI",
        "Docker",
        "Kubernetes",
        "AWS Cloud",
        "Azure Fundamentals",
        "Machine Learning",
        "Deep Learning",
        "Generative AI",
        "LangChain",
        "Power BI",
        "Leadership",
        "Project Management"
    ]

    certifications = [
        "Completed",
        "Completed",
        "Completed",
        "In Progress"
    ]

    rows = []

    for _ in range(TRAINING_COUNT):

        employee_id = random.randint(1, EMPLOYEE_COUNT)

        course = random.choice(courses)

        completion_date = date(
            random.choice([2024, 2025, 2026]),
            random.randint(1, 12),
            random.randint(1, 28)
        )

        certification = random.choice(certifications)

        rows.append(
            f"({employee_id}, "
            f"'{course}', "
            f"'{completion_date}', "
            f"'{certification}')"
        )

    write_insert_file(
        output_file,
        "training_records",
        [
            "employee_id",
            "course_name",
            "completion_date",
            "certification"
        ],
        rows
    )

    print("Training Records Generated Successfully")


# -------------------------------------
# Master SQL Generator
# -------------------------------------

def generate_master_seed():

    output_file = DATABASE_DIR / "enterprise_hr_seed.sql"

    files = [
        "01_schema.sql",
        "02_seed_departments.sql",
        "03_seed_employees.sql",
        "04_seed_projects.sql",
        "05_seed_employee_projects.sql",
        "06_seed_attendance.sql",
        "07_seed_leave_requests.sql",
        "08_seed_performance.sql",
        "09_seed_salary_history.sql",
        "10_seed_assets.sql",
        "11_seed_training.sql"
    ]

    with open(output_file, "w", encoding="utf-8") as master:

        master.write("-- ==========================================\n")
        master.write("-- Enterprise HR Database\n")
        master.write("-- Auto Generated Master SQL\n")
        master.write("-- ==========================================\n\n")

        for file_name in files:

            file_path = DATABASE_DIR / file_name

            if file_path.exists():

                master.write(f"\n-- {file_name}\n\n")

                with open(file_path, "r", encoding="utf-8") as f:

                    master.write(f.read())

                    master.write("\n\n")

    print("Master SQL Generated Successfully")


# -------------------------------------
# Main
# -------------------------------------

if __name__ == "__main__":

    print("=" * 50)
    print("Enterprise HR Seed Generator")
    print("=" * 50)
    
    generate_departments()
    generate_employees()
    generate_projects()
    generate_employee_projects()
    generate_attendance()
    generate_leave_requests()
    generate_performance_reviews()
    generate_salary_history()
    generate_assets()
    generate_training_records()
    generate_master_seed()

    print("\nDone.")