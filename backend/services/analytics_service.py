from services.sql_service import get_connection


def get_dashboard_metrics():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) AS total FROM employees")
    employees = cursor.fetchone()["total"]

    cursor.execute("SELECT AVG(salary) AS avg_salary FROM employees")
    avg_salary = cursor.fetchone()["avg_salary"]

    cursor.execute("SELECT MAX(salary) AS max_salary FROM employees")
    max_salary = cursor.fetchone()["max_salary"]

    cursor.execute(
        """
        SELECT COUNT(DISTINCT department) AS departments
        FROM employees
        """
    )

    departments = cursor.fetchone()["departments"]

    cursor.close()
    conn.close()

    return {

        "employees": employees,

        "avg_salary": round(float(avg_salary), 2),

        "max_salary": float(max_salary),

        "departments": departments

    }


def employees_by_department():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT

            department,

            COUNT(*) AS total

        FROM employees

        GROUP BY department

        ORDER BY total DESC
        """
    )

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows


def salary_distribution():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT salary
        FROM employees
        ORDER BY salary
        """
    )

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows


def hiring_trend():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT

            YEAR(hire_date) AS year,

            COUNT(*) AS total

        FROM employees

        GROUP BY YEAR(hire_date)

        ORDER BY year
        """
    )

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows

# -------------------------------------------------
# AI Dashboard Insights
# -------------------------------------------------

def get_dashboard_insights():

    conn = get_connection()
    cursor = conn.cursor()

    # Highest Paid Department
    cursor.execute("""
        SELECT
            department,
            ROUND(AVG(salary),2) AS avg_salary
        FROM employees
        GROUP BY department
        ORDER BY avg_salary DESC
        LIMIT 1
    """)

    highest_paid = cursor.fetchone()

    # Lowest Paid Department
    cursor.execute("""
        SELECT
            department,
            ROUND(AVG(salary),2) AS avg_salary
        FROM employees
        GROUP BY department
        ORDER BY avg_salary ASC
        LIMIT 1
    """)

    lowest_paid = cursor.fetchone()

    # Average Salary
    cursor.execute("""
        SELECT ROUND(AVG(salary),2) AS salary
        FROM employees
    """)

    avg_salary = cursor.fetchone()["salary"]

    # Latest Hiring Year
    cursor.execute("""
        SELECT
            MAX(YEAR(hire_date)) AS latest_year
        FROM employees
    """)

    latest_year = cursor.fetchone()["latest_year"]

    # Employee Count
    cursor.execute("""
        SELECT COUNT(*) AS total
        FROM employees
    """)

    total = cursor.fetchone()["total"]

    cursor.close()
    conn.close()

    return {

        "highest_paid_department":
            highest_paid,

        "lowest_paid_department":
            lowest_paid,

        "average_salary":
            avg_salary,

        "latest_hiring_year":
            latest_year,

        "total_employees":
            total

    }