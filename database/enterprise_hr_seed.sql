-- ==========================================
-- Enterprise HR Database
-- Auto Generated Master SQL
-- ==========================================


-- 01_schema.sql

-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: hayabusa.proxy.rlwy.net    Database: railway
-- ------------------------------------------------------
-- Server version	9.4.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `assets`
--

DROP TABLE IF EXISTS `assets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `assets` (
  `asset_id` int NOT NULL AUTO_INCREMENT,
  `employee_id` int DEFAULT NULL,
  `asset_name` varchar(100) DEFAULT NULL,
  `serial_number` varchar(100) DEFAULT NULL,
  `assigned_date` date DEFAULT NULL,
  PRIMARY KEY (`asset_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `attendance`
--

DROP TABLE IF EXISTS `attendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attendance` (
  `attendance_id` int NOT NULL AUTO_INCREMENT,
  `employee_id` int DEFAULT NULL,
  `attendance_date` date DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`attendance_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `departments`
--

DROP TABLE IF EXISTS `departments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `departments` (
  `department_id` int NOT NULL AUTO_INCREMENT,
  `department_name` varchar(100) NOT NULL,
  `manager` varchar(100) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `budget` decimal(12,2) DEFAULT NULL,
  PRIMARY KEY (`department_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `employee_projects`
--

DROP TABLE IF EXISTS `employee_projects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_projects` (
  `employee_id` int NOT NULL,
  `project_id` int NOT NULL,
  `role` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`employee_id`,`project_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `employee_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `email` varchar(150) NOT NULL,
  `department` varchar(100) NOT NULL,
  `designation` varchar(100) NOT NULL,
  `salary` decimal(10,2) NOT NULL,
  `hire_date` date NOT NULL,
  PRIMARY KEY (`employee_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `leave_requests`
--

DROP TABLE IF EXISTS `leave_requests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `leave_requests` (
  `leave_id` int NOT NULL AUTO_INCREMENT,
  `employee_id` int DEFAULT NULL,
  `leave_type` varchar(50) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`leave_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `performance_reviews`
--

DROP TABLE IF EXISTS `performance_reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `performance_reviews` (
  `review_id` int NOT NULL AUTO_INCREMENT,
  `employee_id` int DEFAULT NULL,
  `review_year` int DEFAULT NULL,
  `rating` decimal(2,1) DEFAULT NULL,
  `remarks` text,
  PRIMARY KEY (`review_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `projects`
--

DROP TABLE IF EXISTS `projects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects` (
  `project_id` int NOT NULL AUTO_INCREMENT,
  `project_name` varchar(150) NOT NULL,
  `client_name` varchar(150) DEFAULT NULL,
  `budget` decimal(12,2) DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `status` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`project_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `salary_history`
--

DROP TABLE IF EXISTS `salary_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salary_history` (
  `salary_id` int NOT NULL AUTO_INCREMENT,
  `employee_id` int DEFAULT NULL,
  `previous_salary` decimal(10,2) DEFAULT NULL,
  `new_salary` decimal(10,2) DEFAULT NULL,
  `effective_date` date DEFAULT NULL,
  PRIMARY KEY (`salary_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `training_records`
--

DROP TABLE IF EXISTS `training_records`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `training_records` (
  `training_id` int NOT NULL AUTO_INCREMENT,
  `employee_id` int DEFAULT NULL,
  `course_name` varchar(150) DEFAULT NULL,
  `completion_date` date DEFAULT NULL,
  `certification` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`training_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-07-09  9:29:06



-- 02_seed_departments.sql

-- ======================================
-- departments Seed Data
-- Generated Automatically
-- ======================================

INSERT INTO departments (department_name, manager, location, budget)
VALUES
('IT','John Smith','Hyderabad',500000),
('HR','Sarah Johnson','Bangalore',200000),
('Finance','David Wilson','Mumbai',350000),
('Sales','Emily Davis','Pune',400000),
('Marketing','Robert Brown','Chennai',300000),
('Operations','Michael Scott','Delhi',450000),
('Research','Sophia Miller','Hyderabad',600000),
('Customer Support','James Anderson','Kolkata',180000),
('Legal','Olivia Thomas','Mumbai',250000),
('Administration','William Harris','Bangalore',220000);



-- 03_seed_employees.sql

-- ======================================
-- employees Seed Data
-- Generated Automatically
-- ======================================

INSERT INTO employees (first_name, last_name, email, department, designation, salary, hire_date)
VALUES
('Benjamin','King','benjamin.king@company.com','Customer Support','Data Scientist',118717,'2024-01-17'),
('Michele','Powers','michele.powers@company.com','Legal','Marketing Manager',104956,'2025-02-08'),
('Rachel','Kelley','rachel.kelley@company.com','Research','Senior Software Engineer',64595,'2025-09-08'),
('Ryan','Bradford','ryan.bradford@company.com','Administration','Software Engineer',54621,'2024-06-24'),
('Dennis','Garcia','dennis.garcia@company.com','Administration','HR Manager',80101,'2023-03-16'),
('Caitlin','Wright','caitlin.wright@company.com','Operations','Software Engineer',95514,'2025-06-17'),
('Mitchell','Velazquez','mitchell.velazquez@company.com','Finance','Sales Manager',67441,'2025-06-20'),
('William','Brown','william.brown@company.com','Operations','Operations Executive',71200,'2025-10-02'),
('Robert','Moore','robert.moore@company.com','Customer Support','Support Engineer',105284,'2023-01-05'),
('Roger','Stokes','roger.stokes@company.com','Customer Support','Backend Developer',103929,'2021-07-21'),
('Michael','Boyd','michael.boyd@company.com','HR','Marketing Manager',73589,'2026-01-20'),
('Joshua','Robertson','joshua.robertson@company.com','Legal','Sales Executive',115201,'2023-05-19'),
('Donald','Walter','donald.walter@company.com','Legal','Marketing Executive',83070,'2023-03-14'),
('Alyssa','Velez','alyssa.velez@company.com','HR','AI Engineer',59544,'2024-07-07'),
('Nicholas','Reynolds','nicholas.reynolds@company.com','Customer Support','ML Engineer',80071,'2023-03-21'),
('Nicole','Reed','nicole.reed@company.com','Marketing','HR Manager',49607,'2023-03-09'),
('Nathan','Martin','nathan.martin@company.com','Research','Accountant',97440,'2022-01-14'),
('Shannon','Barnes','shannon.barnes@company.com','Research','Sales Executive',57871,'2026-03-12'),
('Joshua','Martin','joshua.martin@company.com','Legal','Full Stack Developer',68667,'2024-03-23'),
('Kevin','Smith','kevin.smith@company.com','Sales','HR Manager',60638,'2023-12-12');



-- 04_seed_projects.sql

-- ======================================
-- projects Seed Data
-- Generated Automatically
-- ======================================

INSERT INTO projects (project_name, client_name, budget, start_date, end_date, status)
VALUES
('AI Recruitment Assistant','Wipro',554612,'2023-09-09','2026-10-18','Completed'),
('Employee Management System','TCS',374833,'2024-04-09','2027-07-08','On Hold'),
('Payroll Automation','Google',611919,'2023-09-10','2027-04-14','In Progress'),
('Customer Analytics Dashboard','TCS',544385,'2024-03-02','2026-10-28','In Progress'),
('Inventory Management','TCS',565851,'2024-10-05','2026-08-20','Completed'),
('Healthcare Portal','Amazon',475826,'2024-02-12','2026-11-18','On Hold'),
('Banking CRM','Microsoft',197625,'2023-12-31','2026-07-21','In Progress'),
('Retail Sales Dashboard','Google',729942,'2024-03-20','2027-06-01','On Hold'),
('Smart Attendance System','TCS',175439,'2024-05-08','2027-02-21','In Progress'),
('Document AI Platform','Amazon',848394,'2024-07-21','2027-02-22','In Progress'),
('Fraud Detection System','Microsoft',643496,'2023-10-01','2027-01-25','In Progress'),
('AI SQL Assistant','Deloitte',309444,'2024-05-19','2026-08-16','On Hold'),
('Cloud Migration','Microsoft',952962,'2025-01-10','2027-07-06','On Hold'),
('HR Analytics','Capgemini',709148,'2025-03-06','2026-11-01','Completed'),
('E-Commerce Platform','Deloitte',117385,'2025-06-05','2026-07-25','On Hold');



-- 05_seed_employee_projects.sql

-- ======================================
-- employee_projects Seed Data
-- Generated Automatically
-- ======================================

INSERT INTO employee_projects (employee_id, project_id, role)
VALUES
(1, 12, 'UI/UX Designer'),
(1, 8, 'UI/UX Designer'),
(2, 6, 'Project Manager'),
(2, 13, 'Project Manager'),
(3, 15, 'Data Scientist'),
(3, 8, 'Team Lead'),
(4, 4, 'Team Lead'),
(4, 1, 'Database Administrator'),
(4, 7, 'Full Stack Developer'),
(5, 3, 'UI/UX Designer'),
(5, 9, 'Frontend Developer'),
(6, 10, 'DevOps Engineer'),
(7, 3, 'Team Lead'),
(7, 2, 'ML Engineer'),
(8, 15, 'Project Manager'),
(9, 2, 'QA Engineer'),
(9, 13, 'Team Lead'),
(10, 4, 'Business Analyst'),
(10, 10, 'Data Scientist'),
(10, 14, 'Frontend Developer'),
(11, 6, 'Support Engineer'),
(11, 15, 'UI/UX Designer'),
(12, 11, 'Database Administrator'),
(12, 15, 'QA Engineer'),
(13, 13, 'Team Lead'),
(13, 3, 'Project Manager'),
(13, 10, 'ML Engineer'),
(14, 15, 'Database Administrator'),
(14, 12, 'Business Analyst'),
(14, 14, 'Full Stack Developer'),
(15, 14, 'UI/UX Designer'),
(15, 1, 'Team Lead'),
(16, 15, 'Project Manager'),
(16, 12, 'Frontend Developer'),
(17, 9, 'Backend Developer'),
(18, 9, 'Full Stack Developer'),
(18, 11, 'UI/UX Designer'),
(19, 4, 'Project Manager'),
(19, 15, 'ML Engineer'),
(19, 14, 'Business Analyst'),
(20, 3, 'Team Lead');



-- 06_seed_attendance.sql

-- ======================================
-- Attendance Seed Data
-- Generated Automatically
-- ======================================

INSERT INTO attendance (employee_id, attendance_date, status)
VALUES
(1, '2026-06-01', 'Present'),
(1, '2026-06-02', 'WFH'),
(1, '2026-06-03', 'Absent'),
(1, '2026-06-04', 'Present'),
(1, '2026-06-05', 'WFH'),
(1, '2026-06-06', 'Present'),
(1, '2026-06-07', 'WFH'),
(1, '2026-06-08', 'Present'),
(1, '2026-06-09', 'Absent'),
(1, '2026-06-10', 'WFH'),
(1, '2026-06-11', 'WFH'),
(1, '2026-06-12', 'WFH'),
(1, '2026-06-13', 'Present'),
(1, '2026-06-14', 'Present'),
(1, '2026-06-15', 'WFH'),
(1, '2026-06-16', 'Present'),
(1, '2026-06-17', 'Absent'),
(1, '2026-06-18', 'WFH'),
(1, '2026-06-19', 'Absent'),
(1, '2026-06-20', 'WFH'),
(1, '2026-06-21', 'Present'),
(1, '2026-06-22', 'Present'),
(1, '2026-06-23', 'Absent'),
(1, '2026-06-24', 'Absent'),
(1, '2026-06-25', 'Present'),
(1, '2026-06-26', 'Present'),
(1, '2026-06-27', 'WFH'),
(1, '2026-06-28', 'Present'),
(1, '2026-06-29', 'Present'),
(1, '2026-06-30', 'Present'),
(2, '2026-06-01', 'Present'),
(2, '2026-06-02', 'Present'),
(2, '2026-06-03', 'Present'),
(2, '2026-06-04', 'Present'),
(2, '2026-06-05', 'Present'),
(2, '2026-06-06', 'Present'),
(2, '2026-06-07', 'Present'),
(2, '2026-06-08', 'Present'),
(2, '2026-06-09', 'Present'),
(2, '2026-06-10', 'Present'),
(2, '2026-06-11', 'Present'),
(2, '2026-06-12', 'Present'),
(2, '2026-06-13', 'Absent'),
(2, '2026-06-14', 'Present'),
(2, '2026-06-15', 'Absent'),
(2, '2026-06-16', 'Absent'),
(2, '2026-06-17', 'Present'),
(2, '2026-06-18', 'Present'),
(2, '2026-06-19', 'Present'),
(2, '2026-06-20', 'Present'),
(2, '2026-06-21', 'Absent'),
(2, '2026-06-22', 'Present'),
(2, '2026-06-23', 'Present'),
(2, '2026-06-24', 'Present'),
(2, '2026-06-25', 'Present'),
(2, '2026-06-26', 'Present'),
(2, '2026-06-27', 'WFH'),
(2, '2026-06-28', 'Absent'),
(2, '2026-06-29', 'Present'),
(2, '2026-06-30', 'Present'),
(3, '2026-06-01', 'Present'),
(3, '2026-06-02', 'WFH'),
(3, '2026-06-03', 'Present'),
(3, '2026-06-04', 'Present'),
(3, '2026-06-05', 'Present'),
(3, '2026-06-06', 'WFH'),
(3, '2026-06-07', 'Present'),
(3, '2026-06-08', 'Present'),
(3, '2026-06-09', 'Present'),
(3, '2026-06-10', 'Present'),
(3, '2026-06-11', 'WFH'),
(3, '2026-06-12', 'WFH'),
(3, '2026-06-13', 'Present'),
(3, '2026-06-14', 'Present'),
(3, '2026-06-15', 'WFH'),
(3, '2026-06-16', 'Present'),
(3, '2026-06-17', 'WFH'),
(3, '2026-06-18', 'Present'),
(3, '2026-06-19', 'Present'),
(3, '2026-06-20', 'Present'),
(3, '2026-06-21', 'WFH'),
(3, '2026-06-22', 'Absent'),
(3, '2026-06-23', 'WFH'),
(3, '2026-06-24', 'Present'),
(3, '2026-06-25', 'Present'),
(3, '2026-06-26', 'Present'),
(3, '2026-06-27', 'WFH'),
(3, '2026-06-28', 'Present'),
(3, '2026-06-29', 'Absent'),
(3, '2026-06-30', 'WFH'),
(4, '2026-06-01', 'WFH'),
(4, '2026-06-02', 'Present'),
(4, '2026-06-03', 'Absent'),
(4, '2026-06-04', 'Absent'),
(4, '2026-06-05', 'Present'),
(4, '2026-06-06', 'WFH'),
(4, '2026-06-07', 'WFH'),
(4, '2026-06-08', 'Present'),
(4, '2026-06-09', 'Present'),
(4, '2026-06-10', 'Absent'),
(4, '2026-06-11', 'Present'),
(4, '2026-06-12', 'Present'),
(4, '2026-06-13', 'WFH'),
(4, '2026-06-14', 'Present'),
(4, '2026-06-15', 'Present'),
(4, '2026-06-16', 'WFH'),
(4, '2026-06-17', 'Absent'),
(4, '2026-06-18', 'Absent'),
(4, '2026-06-19', 'Present'),
(4, '2026-06-20', 'Present'),
(4, '2026-06-21', 'Absent'),
(4, '2026-06-22', 'Present'),
(4, '2026-06-23', 'WFH'),
(4, '2026-06-24', 'Present'),
(4, '2026-06-25', 'Present'),
(4, '2026-06-26', 'Present'),
(4, '2026-06-27', 'WFH'),
(4, '2026-06-28', 'Present'),
(4, '2026-06-29', 'Present'),
(4, '2026-06-30', 'Present'),
(5, '2026-06-01', 'Present'),
(5, '2026-06-02', 'WFH'),
(5, '2026-06-03', 'WFH'),
(5, '2026-06-04', 'Present'),
(5, '2026-06-05', 'Present'),
(5, '2026-06-06', 'Absent'),
(5, '2026-06-07', 'Present'),
(5, '2026-06-08', 'Present'),
(5, '2026-06-09', 'WFH'),
(5, '2026-06-10', 'WFH'),
(5, '2026-06-11', 'Present'),
(5, '2026-06-12', 'Present'),
(5, '2026-06-13', 'Present'),
(5, '2026-06-14', 'Present'),
(5, '2026-06-15', 'Present'),
(5, '2026-06-16', 'Absent'),
(5, '2026-06-17', 'Present'),
(5, '2026-06-18', 'Present'),
(5, '2026-06-19', 'Absent'),
(5, '2026-06-20', 'Present'),
(5, '2026-06-21', 'Present'),
(5, '2026-06-22', 'Present'),
(5, '2026-06-23', 'Present'),
(5, '2026-06-24', 'WFH'),
(5, '2026-06-25', 'Present'),
(5, '2026-06-26', 'Absent'),
(5, '2026-06-27', 'Present'),
(5, '2026-06-28', 'Present'),
(5, '2026-06-29', 'Present'),
(5, '2026-06-30', 'Present'),
(6, '2026-06-01', 'Present'),
(6, '2026-06-02', 'Present'),
(6, '2026-06-03', 'Present'),
(6, '2026-06-04', 'Present'),
(6, '2026-06-05', 'WFH'),
(6, '2026-06-06', 'Absent'),
(6, '2026-06-07', 'Present'),
(6, '2026-06-08', 'Present'),
(6, '2026-06-09', 'Present'),
(6, '2026-06-10', 'Present'),
(6, '2026-06-11', 'Present'),
(6, '2026-06-12', 'Absent'),
(6, '2026-06-13', 'Present'),
(6, '2026-06-14', 'Present'),
(6, '2026-06-15', 'Present'),
(6, '2026-06-16', 'WFH'),
(6, '2026-06-17', 'WFH'),
(6, '2026-06-18', 'Present'),
(6, '2026-06-19', 'WFH'),
(6, '2026-06-20', 'Present'),
(6, '2026-06-21', 'Present'),
(6, '2026-06-22', 'Absent'),
(6, '2026-06-23', 'Present'),
(6, '2026-06-24', 'Absent'),
(6, '2026-06-25', 'WFH'),
(6, '2026-06-26', 'Present'),
(6, '2026-06-27', 'Absent'),
(6, '2026-06-28', 'Present'),
(6, '2026-06-29', 'Present'),
(6, '2026-06-30', 'Present'),
(7, '2026-06-01', 'Present'),
(7, '2026-06-02', 'Present'),
(7, '2026-06-03', 'Present'),
(7, '2026-06-04', 'Present'),
(7, '2026-06-05', 'Present'),
(7, '2026-06-06', 'Present'),
(7, '2026-06-07', 'Present'),
(7, '2026-06-08', 'Absent'),
(7, '2026-06-09', 'Present'),
(7, '2026-06-10', 'Present'),
(7, '2026-06-11', 'Present'),
(7, '2026-06-12', 'Present'),
(7, '2026-06-13', 'WFH'),
(7, '2026-06-14', 'Present'),
(7, '2026-06-15', 'Present'),
(7, '2026-06-16', 'Present'),
(7, '2026-06-17', 'Present'),
(7, '2026-06-18', 'Present'),
(7, '2026-06-19', 'Present'),
(7, '2026-06-20', 'WFH'),
(7, '2026-06-21', 'WFH'),
(7, '2026-06-22', 'Absent'),
(7, '2026-06-23', 'Present'),
(7, '2026-06-24', 'Present'),
(7, '2026-06-25', 'Present'),
(7, '2026-06-26', 'WFH'),
(7, '2026-06-27', 'Present'),
(7, '2026-06-28', 'Present'),
(7, '2026-06-29', 'WFH'),
(7, '2026-06-30', 'Present'),
(8, '2026-06-01', 'Present'),
(8, '2026-06-02', 'Present'),
(8, '2026-06-03', 'Present'),
(8, '2026-06-04', 'WFH'),
(8, '2026-06-05', 'Present'),
(8, '2026-06-06', 'Present'),
(8, '2026-06-07', 'Present'),
(8, '2026-06-08', 'Present'),
(8, '2026-06-09', 'Present'),
(8, '2026-06-10', 'Present'),
(8, '2026-06-11', 'Present'),
(8, '2026-06-12', 'Present'),
(8, '2026-06-13', 'Absent'),
(8, '2026-06-14', 'Present'),
(8, '2026-06-15', 'Present'),
(8, '2026-06-16', 'Present'),
(8, '2026-06-17', 'Present'),
(8, '2026-06-18', 'Present'),
(8, '2026-06-19', 'Present'),
(8, '2026-06-20', 'WFH'),
(8, '2026-06-21', 'WFH'),
(8, '2026-06-22', 'Present'),
(8, '2026-06-23', 'Absent'),
(8, '2026-06-24', 'Present'),
(8, '2026-06-25', 'Absent'),
(8, '2026-06-26', 'WFH'),
(8, '2026-06-27', 'WFH'),
(8, '2026-06-28', 'Present'),
(8, '2026-06-29', 'Present'),
(8, '2026-06-30', 'Absent'),
(9, '2026-06-01', 'Present'),
(9, '2026-06-02', 'Absent'),
(9, '2026-06-03', 'Absent'),
(9, '2026-06-04', 'Present'),
(9, '2026-06-05', 'Present'),
(9, '2026-06-06', 'Present'),
(9, '2026-06-07', 'Present'),
(9, '2026-06-08', 'Present'),
(9, '2026-06-09', 'WFH'),
(9, '2026-06-10', 'WFH'),
(9, '2026-06-11', 'WFH'),
(9, '2026-06-12', 'WFH'),
(9, '2026-06-13', 'WFH'),
(9, '2026-06-14', 'Present'),
(9, '2026-06-15', 'Present'),
(9, '2026-06-16', 'Present'),
(9, '2026-06-17', 'Present'),
(9, '2026-06-18', 'Present'),
(9, '2026-06-19', 'Present'),
(9, '2026-06-20', 'WFH'),
(9, '2026-06-21', 'Present'),
(9, '2026-06-22', 'Present'),
(9, '2026-06-23', 'Present'),
(9, '2026-06-24', 'Present'),
(9, '2026-06-25', 'Present'),
(9, '2026-06-26', 'Present'),
(9, '2026-06-27', 'Absent'),
(9, '2026-06-28', 'Present'),
(9, '2026-06-29', 'Absent'),
(9, '2026-06-30', 'WFH'),
(10, '2026-06-01', 'Absent'),
(10, '2026-06-02', 'Present'),
(10, '2026-06-03', 'WFH'),
(10, '2026-06-04', 'Present'),
(10, '2026-06-05', 'Present'),
(10, '2026-06-06', 'Present'),
(10, '2026-06-07', 'Absent'),
(10, '2026-06-08', 'Present'),
(10, '2026-06-09', 'Present'),
(10, '2026-06-10', 'Present'),
(10, '2026-06-11', 'Present'),
(10, '2026-06-12', 'Present'),
(10, '2026-06-13', 'Present'),
(10, '2026-06-14', 'WFH'),
(10, '2026-06-15', 'WFH'),
(10, '2026-06-16', 'WFH'),
(10, '2026-06-17', 'Absent'),
(10, '2026-06-18', 'Absent'),
(10, '2026-06-19', 'WFH'),
(10, '2026-06-20', 'Present'),
(10, '2026-06-21', 'WFH'),
(10, '2026-06-22', 'Present'),
(10, '2026-06-23', 'Present'),
(10, '2026-06-24', 'Absent'),
(10, '2026-06-25', 'Absent'),
(10, '2026-06-26', 'Present'),
(10, '2026-06-27', 'Absent'),
(10, '2026-06-28', 'Absent'),
(10, '2026-06-29', 'Present'),
(10, '2026-06-30', 'Present'),
(11, '2026-06-01', 'Present'),
(11, '2026-06-02', 'Present'),
(11, '2026-06-03', 'Present'),
(11, '2026-06-04', 'WFH'),
(11, '2026-06-05', 'Present'),
(11, '2026-06-06', 'Present'),
(11, '2026-06-07', 'Absent'),
(11, '2026-06-08', 'Present'),
(11, '2026-06-09', 'WFH'),
(11, '2026-06-10', 'WFH'),
(11, '2026-06-11', 'Present'),
(11, '2026-06-12', 'Absent'),
(11, '2026-06-13', 'Present'),
(11, '2026-06-14', 'WFH'),
(11, '2026-06-15', 'Present'),
(11, '2026-06-16', 'WFH'),
(11, '2026-06-17', 'Present'),
(11, '2026-06-18', 'Present'),
(11, '2026-06-19', 'Present'),
(11, '2026-06-20', 'Present'),
(11, '2026-06-21', 'Present'),
(11, '2026-06-22', 'Present'),
(11, '2026-06-23', 'WFH'),
(11, '2026-06-24', 'Present'),
(11, '2026-06-25', 'Present'),
(11, '2026-06-26', 'WFH'),
(11, '2026-06-27', 'Absent'),
(11, '2026-06-28', 'Present'),
(11, '2026-06-29', 'Present'),
(11, '2026-06-30', 'WFH'),
(12, '2026-06-01', 'Present'),
(12, '2026-06-02', 'Absent'),
(12, '2026-06-03', 'Present'),
(12, '2026-06-04', 'Present'),
(12, '2026-06-05', 'Present'),
(12, '2026-06-06', 'Present'),
(12, '2026-06-07', 'Present'),
(12, '2026-06-08', 'Absent'),
(12, '2026-06-09', 'WFH'),
(12, '2026-06-10', 'Present'),
(12, '2026-06-11', 'WFH'),
(12, '2026-06-12', 'Present'),
(12, '2026-06-13', 'WFH'),
(12, '2026-06-14', 'Present'),
(12, '2026-06-15', 'Present'),
(12, '2026-06-16', 'Absent'),
(12, '2026-06-17', 'Present'),
(12, '2026-06-18', 'Present'),
(12, '2026-06-19', 'WFH'),
(12, '2026-06-20', 'Present'),
(12, '2026-06-21', 'Present'),
(12, '2026-06-22', 'Present'),
(12, '2026-06-23', 'Present'),
(12, '2026-06-24', 'Present'),
(12, '2026-06-25', 'Present'),
(12, '2026-06-26', 'Absent'),
(12, '2026-06-27', 'Absent'),
(12, '2026-06-28', 'Present'),
(12, '2026-06-29', 'WFH'),
(12, '2026-06-30', 'Present'),
(13, '2026-06-01', 'Present'),
(13, '2026-06-02', 'WFH'),
(13, '2026-06-03', 'Present'),
(13, '2026-06-04', 'Present'),
(13, '2026-06-05', 'Present'),
(13, '2026-06-06', 'Absent'),
(13, '2026-06-07', 'Present'),
(13, '2026-06-08', 'Present'),
(13, '2026-06-09', 'Present'),
(13, '2026-06-10', 'Absent'),
(13, '2026-06-11', 'WFH'),
(13, '2026-06-12', 'Present'),
(13, '2026-06-13', 'Present'),
(13, '2026-06-14', 'Present'),
(13, '2026-06-15', 'WFH'),
(13, '2026-06-16', 'Present'),
(13, '2026-06-17', 'Present'),
(13, '2026-06-18', 'Present'),
(13, '2026-06-19', 'Absent'),
(13, '2026-06-20', 'Present'),
(13, '2026-06-21', 'Present'),
(13, '2026-06-22', 'Present'),
(13, '2026-06-23', 'WFH'),
(13, '2026-06-24', 'Present'),
(13, '2026-06-25', 'Present'),
(13, '2026-06-26', 'Present'),
(13, '2026-06-27', 'Present'),
(13, '2026-06-28', 'Absent'),
(13, '2026-06-29', 'Present'),
(13, '2026-06-30', 'Present'),
(14, '2026-06-01', 'Present'),
(14, '2026-06-02', 'Present'),
(14, '2026-06-03', 'WFH'),
(14, '2026-06-04', 'Present'),
(14, '2026-06-05', 'WFH'),
(14, '2026-06-06', 'Present'),
(14, '2026-06-07', 'Present'),
(14, '2026-06-08', 'WFH'),
(14, '2026-06-09', 'Present'),
(14, '2026-06-10', 'Present'),
(14, '2026-06-11', 'Present'),
(14, '2026-06-12', 'Absent'),
(14, '2026-06-13', 'Present'),
(14, '2026-06-14', 'Present'),
(14, '2026-06-15', 'Absent'),
(14, '2026-06-16', 'Present'),
(14, '2026-06-17', 'Absent'),
(14, '2026-06-18', 'WFH'),
(14, '2026-06-19', 'WFH'),
(14, '2026-06-20', 'Present'),
(14, '2026-06-21', 'WFH'),
(14, '2026-06-22', 'Present'),
(14, '2026-06-23', 'Present'),
(14, '2026-06-24', 'Absent'),
(14, '2026-06-25', 'WFH'),
(14, '2026-06-26', 'Present'),
(14, '2026-06-27', 'Present'),
(14, '2026-06-28', 'Present'),
(14, '2026-06-29', 'Present'),
(14, '2026-06-30', 'Present'),
(15, '2026-06-01', 'Present'),
(15, '2026-06-02', 'Absent'),
(15, '2026-06-03', 'Present'),
(15, '2026-06-04', 'Present'),
(15, '2026-06-05', 'Present'),
(15, '2026-06-06', 'Present'),
(15, '2026-06-07', 'Present'),
(15, '2026-06-08', 'Present'),
(15, '2026-06-09', 'Present'),
(15, '2026-06-10', 'Present'),
(15, '2026-06-11', 'Present'),
(15, '2026-06-12', 'Absent'),
(15, '2026-06-13', 'Present'),
(15, '2026-06-14', 'WFH'),
(15, '2026-06-15', 'Present'),
(15, '2026-06-16', 'Absent'),
(15, '2026-06-17', 'Present'),
(15, '2026-06-18', 'Present'),
(15, '2026-06-19', 'Present'),
(15, '2026-06-20', 'Present'),
(15, '2026-06-21', 'Present'),
(15, '2026-06-22', 'Absent'),
(15, '2026-06-23', 'Present'),
(15, '2026-06-24', 'Present'),
(15, '2026-06-25', 'WFH'),
(15, '2026-06-26', 'Present'),
(15, '2026-06-27', 'WFH'),
(15, '2026-06-28', 'Present'),
(15, '2026-06-29', 'Present'),
(15, '2026-06-30', 'Present'),
(16, '2026-06-01', 'Absent'),
(16, '2026-06-02', 'Present'),
(16, '2026-06-03', 'Present'),
(16, '2026-06-04', 'Present'),
(16, '2026-06-05', 'Absent'),
(16, '2026-06-06', 'Present'),
(16, '2026-06-07', 'Present'),
(16, '2026-06-08', 'Present'),
(16, '2026-06-09', 'Absent'),
(16, '2026-06-10', 'Present'),
(16, '2026-06-11', 'Absent'),
(16, '2026-06-12', 'Absent'),
(16, '2026-06-13', 'Absent'),
(16, '2026-06-14', 'Present'),
(16, '2026-06-15', 'Present'),
(16, '2026-06-16', 'WFH'),
(16, '2026-06-17', 'Present'),
(16, '2026-06-18', 'WFH'),
(16, '2026-06-19', 'Present'),
(16, '2026-06-20', 'Present'),
(16, '2026-06-21', 'Present'),
(16, '2026-06-22', 'Present'),
(16, '2026-06-23', 'Absent'),
(16, '2026-06-24', 'Present'),
(16, '2026-06-25', 'Present'),
(16, '2026-06-26', 'Present'),
(16, '2026-06-27', 'WFH'),
(16, '2026-06-28', 'Present'),
(16, '2026-06-29', 'Present'),
(16, '2026-06-30', 'Present'),
(17, '2026-06-01', 'Present'),
(17, '2026-06-02', 'Present'),
(17, '2026-06-03', 'Absent'),
(17, '2026-06-04', 'Absent'),
(17, '2026-06-05', 'Present'),
(17, '2026-06-06', 'Present'),
(17, '2026-06-07', 'Present'),
(17, '2026-06-08', 'Absent'),
(17, '2026-06-09', 'Present'),
(17, '2026-06-10', 'Present'),
(17, '2026-06-11', 'Present'),
(17, '2026-06-12', 'Present'),
(17, '2026-06-13', 'Present'),
(17, '2026-06-14', 'Present'),
(17, '2026-06-15', 'Present'),
(17, '2026-06-16', 'Present'),
(17, '2026-06-17', 'Present'),
(17, '2026-06-18', 'Present'),
(17, '2026-06-19', 'Absent'),
(17, '2026-06-20', 'Present'),
(17, '2026-06-21', 'WFH'),
(17, '2026-06-22', 'Present'),
(17, '2026-06-23', 'Present'),
(17, '2026-06-24', 'Present'),
(17, '2026-06-25', 'Absent'),
(17, '2026-06-26', 'Absent'),
(17, '2026-06-27', 'Present'),
(17, '2026-06-28', 'Present'),
(17, '2026-06-29', 'Present'),
(17, '2026-06-30', 'Present'),
(18, '2026-06-01', 'Present'),
(18, '2026-06-02', 'Present'),
(18, '2026-06-03', 'Absent'),
(18, '2026-06-04', 'Present'),
(18, '2026-06-05', 'Present'),
(18, '2026-06-06', 'Present'),
(18, '2026-06-07', 'Absent'),
(18, '2026-06-08', 'Absent'),
(18, '2026-06-09', 'WFH'),
(18, '2026-06-10', 'Present'),
(18, '2026-06-11', 'Present'),
(18, '2026-06-12', 'Present'),
(18, '2026-06-13', 'Present'),
(18, '2026-06-14', 'Absent'),
(18, '2026-06-15', 'Present'),
(18, '2026-06-16', 'Present'),
(18, '2026-06-17', 'Present'),
(18, '2026-06-18', 'Absent'),
(18, '2026-06-19', 'Present'),
(18, '2026-06-20', 'Present'),
(18, '2026-06-21', 'Present'),
(18, '2026-06-22', 'Present'),
(18, '2026-06-23', 'Present'),
(18, '2026-06-24', 'WFH'),
(18, '2026-06-25', 'Present'),
(18, '2026-06-26', 'Absent'),
(18, '2026-06-27', 'WFH'),
(18, '2026-06-28', 'Present'),
(18, '2026-06-29', 'Absent'),
(18, '2026-06-30', 'WFH'),
(19, '2026-06-01', 'Present'),
(19, '2026-06-02', 'WFH'),
(19, '2026-06-03', 'Present'),
(19, '2026-06-04', 'WFH'),
(19, '2026-06-05', 'WFH'),
(19, '2026-06-06', 'Present'),
(19, '2026-06-07', 'Present'),
(19, '2026-06-08', 'Present'),
(19, '2026-06-09', 'Present'),
(19, '2026-06-10', 'Absent'),
(19, '2026-06-11', 'Present'),
(19, '2026-06-12', 'Present'),
(19, '2026-06-13', 'Present'),
(19, '2026-06-14', 'Present'),
(19, '2026-06-15', 'Present'),
(19, '2026-06-16', 'Absent'),
(19, '2026-06-17', 'WFH'),
(19, '2026-06-18', 'Present'),
(19, '2026-06-19', 'Present'),
(19, '2026-06-20', 'Present'),
(19, '2026-06-21', 'Present'),
(19, '2026-06-22', 'Present'),
(19, '2026-06-23', 'Present'),
(19, '2026-06-24', 'Present'),
(19, '2026-06-25', 'Present'),
(19, '2026-06-26', 'Present'),
(19, '2026-06-27', 'WFH'),
(19, '2026-06-28', 'WFH'),
(19, '2026-06-29', 'Present'),
(19, '2026-06-30', 'Present'),
(20, '2026-06-01', 'Present'),
(20, '2026-06-02', 'Absent'),
(20, '2026-06-03', 'Present'),
(20, '2026-06-04', 'Present'),
(20, '2026-06-05', 'Present'),
(20, '2026-06-06', 'Present'),
(20, '2026-06-07', 'Present'),
(20, '2026-06-08', 'Present'),
(20, '2026-06-09', 'Present'),
(20, '2026-06-10', 'Present'),
(20, '2026-06-11', 'Absent'),
(20, '2026-06-12', 'Present'),
(20, '2026-06-13', 'Absent'),
(20, '2026-06-14', 'WFH'),
(20, '2026-06-15', 'Present'),
(20, '2026-06-16', 'Present'),
(20, '2026-06-17', 'Present'),
(20, '2026-06-18', 'Present'),
(20, '2026-06-19', 'Present'),
(20, '2026-06-20', 'Present'),
(20, '2026-06-21', 'Present'),
(20, '2026-06-22', 'Present'),
(20, '2026-06-23', 'Present'),
(20, '2026-06-24', 'Present'),
(20, '2026-06-25', 'WFH'),
(20, '2026-06-26', 'Absent'),
(20, '2026-06-27', 'WFH'),
(20, '2026-06-28', 'Present'),
(20, '2026-06-29', 'WFH'),
(20, '2026-06-30', 'Present');



-- 07_seed_leave_requests.sql

-- ======================================
-- leave_requests Seed Data
-- Generated Automatically
-- ======================================

INSERT INTO leave_requests (employee_id, leave_type, start_date, end_date, status)
VALUES
(13, 'Work From Home', '2026-06-21', '2026-06-22', 'Approved'),
(14, 'Work From Home', '2026-06-11', '2026-06-16', 'Rejected'),
(11, 'Casual Leave', '2026-06-02', '2026-06-04', 'Approved'),
(18, 'Sick Leave', '2026-06-02', '2026-06-07', 'Approved'),
(13, 'Vacation', '2026-06-05', '2026-06-09', 'Approved'),
(14, 'Vacation', '2026-06-05', '2026-06-10', 'Pending'),
(15, 'Work From Home', '2026-06-01', '2026-06-05', 'Rejected'),
(8, 'Sick Leave', '2026-06-07', '2026-06-09', 'Approved'),
(20, 'Sick Leave', '2026-06-19', '2026-06-23', 'Approved'),
(12, 'Casual Leave', '2026-06-17', '2026-06-19', 'Pending'),
(13, 'Casual Leave', '2026-06-22', '2026-06-24', 'Approved'),
(11, 'Sick Leave', '2026-06-06', '2026-06-10', 'Approved'),
(20, 'Sick Leave', '2026-06-12', '2026-06-14', 'Approved'),
(10, 'Work From Home', '2026-06-20', '2026-06-25', 'Approved'),
(2, 'Work From Home', '2026-06-08', '2026-06-09', 'Approved'),
(4, 'Vacation', '2026-06-14', '2026-06-15', 'Pending'),
(6, 'Sick Leave', '2026-06-05', '2026-06-09', 'Rejected'),
(17, 'Sick Leave', '2026-06-14', '2026-06-18', 'Approved'),
(4, 'Vacation', '2026-06-01', '2026-06-05', 'Pending'),
(4, 'Vacation', '2026-06-22', '2026-06-26', 'Rejected'),
(10, 'Work From Home', '2026-06-07', '2026-06-11', 'Rejected'),
(11, 'Work From Home', '2026-06-24', '2026-06-29', 'Pending'),
(2, 'Casual Leave', '2026-06-14', '2026-06-17', 'Rejected'),
(4, 'Sick Leave', '2026-06-05', '2026-06-07', 'Rejected'),
(10, 'Casual Leave', '2026-06-15', '2026-06-17', 'Rejected'),
(15, 'Casual Leave', '2026-06-10', '2026-06-15', 'Rejected'),
(5, 'Sick Leave', '2026-06-02', '2026-06-04', 'Approved'),
(5, 'Casual Leave', '2026-06-04', '2026-06-06', 'Approved'),
(19, 'Vacation', '2026-06-05', '2026-06-08', 'Approved'),
(12, 'Vacation', '2026-06-09', '2026-06-10', 'Pending'),
(2, 'Vacation', '2026-06-12', '2026-06-15', 'Approved'),
(19, 'Vacation', '2026-06-04', '2026-06-05', 'Approved'),
(3, 'Sick Leave', '2026-06-07', '2026-06-08', 'Approved'),
(18, 'Work From Home', '2026-06-16', '2026-06-21', 'Approved'),
(9, 'Work From Home', '2026-06-11', '2026-06-14', 'Approved'),
(13, 'Casual Leave', '2026-06-19', '2026-06-24', 'Approved'),
(4, 'Sick Leave', '2026-06-17', '2026-06-21', 'Approved'),
(12, 'Sick Leave', '2026-06-21', '2026-06-26', 'Approved'),
(5, 'Casual Leave', '2026-06-10', '2026-06-15', 'Rejected');



-- 08_seed_performance.sql

-- ======================================
-- performance_reviews Seed Data
-- Generated Automatically
-- ======================================

INSERT INTO performance_reviews (employee_id, review_year, rating, remarks)
VALUES
(11, 2025, 3.1, 'Needs Improvement'),
(13, 2024, 4.2, 'Outstanding Performance'),
(8, 2024, 3.8, 'Excellent Team Player'),
(19, 2025, 3.3, 'Excellent Team Player'),
(13, 2026, 4.6, 'Outstanding Performance'),
(13, 2025, 4.8, 'Outstanding Performance'),
(5, 2024, 4.9, 'Good Performance'),
(8, 2024, 3.8, 'Good Performance'),
(19, 2025, 4.2, 'Exceeds Expectations'),
(4, 2025, 3.2, 'Excellent Team Player'),
(14, 2025, 4.5, 'Exceeds Expectations'),
(5, 2026, 3.1, 'Outstanding Performance'),
(4, 2025, 4.3, 'Excellent Team Player'),
(1, 2024, 4.0, 'Outstanding Performance'),
(8, 2024, 4.3, 'Exceeds Expectations'),
(9, 2026, 4.0, 'Good Performance'),
(2, 2025, 4.9, 'Excellent Team Player'),
(9, 2024, 4.9, 'Good Performance'),
(4, 2024, 3.6, 'Outstanding Performance'),
(6, 2025, 4.2, 'Outstanding Performance');



-- 09_seed_salary_history.sql

-- ======================================
-- salary_history Seed Data
-- Generated Automatically
-- ======================================

INSERT INTO salary_history (employee_id, previous_salary, new_salary, effective_date)
VALUES
(10, 70178, 74824, '2025-03-10'),
(20, 42188, 54445, '2024-04-22'),
(10, 37469, 41756, '2026-01-11'),
(10, 46174, 51286, '2025-04-02'),
(11, 36895, 43139, '2026-11-06'),
(3, 54845, 62714, '2026-07-15'),
(19, 39129, 47682, '2024-11-22'),
(16, 89029, 98664, '2025-05-06'),
(11, 77799, 88369, '2026-10-22'),
(3, 64027, 67934, '2024-11-20'),
(2, 35755, 41404, '2025-03-19'),
(16, 67102, 71468, '2026-01-28'),
(17, 82840, 90561, '2024-05-12'),
(2, 88612, 95022, '2025-12-12'),
(2, 51371, 61642, '2024-10-26'),
(10, 61776, 73320, '2025-05-06'),
(1, 70394, 75813, '2024-04-27'),
(20, 76776, 84570, '2025-03-21'),
(10, 84900, 94056, '2024-02-21'),
(17, 59668, 62765, '2025-09-15'),
(6, 80756, 94100, '2026-10-19'),
(19, 81504, 96402, '2026-03-24'),
(11, 69084, 73248, '2026-03-27'),
(13, 46899, 50449, '2024-09-28'),
(2, 80556, 94604, '2024-02-16'),
(19, 52385, 57877, '2024-06-03'),
(6, 78922, 88104, '2026-10-18'),
(19, 55172, 63183, '2024-02-12'),
(5, 43178, 53357, '2026-08-10'),
(2, 65427, 75745, '2024-07-13'),
(6, 77605, 85744, '2025-08-07'),
(3, 78016, 89286, '2025-04-08'),
(19, 51473, 57442, '2025-04-15'),
(1, 57539, 62925, '2025-06-22'),
(14, 47772, 61152, '2025-11-09'),
(18, 54032, 60849, '2026-01-17'),
(16, 89456, 99098, '2026-10-27'),
(20, 42409, 52617, '2026-05-05'),
(18, 44675, 59367, '2025-11-12'),
(18, 79389, 92035, '2024-05-13');



-- 10_seed_assets.sql

-- ======================================
-- assets Seed Data
-- Generated Automatically
-- ======================================

INSERT INTO assets (employee_id, asset_name, serial_number, assigned_date)
VALUES
(8, 'Monitor', 'AST-1000', '2025-07-10'),
(9, 'Docking Station', 'AST-1001', '2025-08-17'),
(3, 'Monitor', 'AST-1002', '2026-10-04'),
(13, 'MacBook Pro', 'AST-1003', '2026-02-16'),
(20, 'Dell Laptop', 'AST-1004', '2025-08-06'),
(7, 'Docking Station', 'AST-1005', '2025-12-12'),
(18, 'Keyboard', 'AST-1006', '2025-05-08'),
(8, 'iPhone', 'AST-1007', '2024-06-17'),
(10, 'Keyboard', 'AST-1008', '2026-07-10'),
(9, 'Docking Station', 'AST-1009', '2025-10-13'),
(13, 'MacBook Pro', 'AST-1010', '2024-06-19'),
(11, 'Android Phone', 'AST-1011', '2025-06-16'),
(10, 'Android Phone', 'AST-1012', '2026-07-02'),
(11, 'Mouse', 'AST-1013', '2025-04-03'),
(12, 'Lenovo ThinkPad', 'AST-1014', '2024-07-13'),
(18, 'HP EliteBook', 'AST-1015', '2025-04-11'),
(3, 'MacBook Pro', 'AST-1016', '2024-06-04'),
(15, 'Docking Station', 'AST-1017', '2026-01-25'),
(17, 'Android Phone', 'AST-1018', '2024-10-23'),
(2, 'MacBook Pro', 'AST-1019', '2026-10-17'),
(15, 'Mouse', 'AST-1020', '2026-01-15'),
(15, 'iPhone', 'AST-1021', '2024-07-22'),
(20, 'MacBook Pro', 'AST-1022', '2026-04-13'),
(17, 'iPhone', 'AST-1023', '2026-08-27'),
(11, 'Lenovo ThinkPad', 'AST-1024', '2024-07-13'),
(5, 'Dell Laptop', 'AST-1025', '2024-02-13'),
(11, 'HP EliteBook', 'AST-1026', '2026-04-03'),
(16, 'iPhone', 'AST-1027', '2025-05-24'),
(13, 'Monitor', 'AST-1028', '2025-04-27'),
(13, 'Android Phone', 'AST-1029', '2025-02-20');



-- 11_seed_training.sql

-- ======================================
-- training_records Seed Data
-- Generated Automatically
-- ======================================

INSERT INTO training_records (employee_id, course_name, completion_date, certification)
VALUES
(15, 'LangChain', '2026-01-26', 'Completed'),
(16, 'Deep Learning', '2025-08-11', 'Completed'),
(4, 'Advanced SQL', '2026-03-23', 'Completed'),
(17, 'FastAPI', '2025-12-18', 'In Progress'),
(7, 'FastAPI', '2026-02-10', 'Completed'),
(16, 'Machine Learning', '2024-02-19', 'Completed'),
(13, 'AWS Cloud', '2025-05-21', 'Completed'),
(10, 'Leadership', '2024-06-15', 'Completed'),
(2, 'Power BI', '2026-08-26', 'Completed'),
(9, 'LangChain', '2025-10-08', 'Completed'),
(14, 'Azure Fundamentals', '2026-09-13', 'Completed'),
(15, 'Machine Learning', '2025-02-02', 'Completed'),
(13, 'Machine Learning', '2026-09-13', 'Completed'),
(16, 'Leadership', '2025-05-12', 'Completed'),
(12, 'Leadership', '2026-04-14', 'Completed'),
(12, 'Python', '2024-01-27', 'Completed'),
(5, 'FastAPI', '2026-06-15', 'Completed'),
(17, 'Machine Learning', '2025-03-15', 'Completed'),
(9, 'Deep Learning', '2024-01-22', 'Completed'),
(6, 'Docker', '2026-11-24', 'Completed'),
(7, 'Power BI', '2025-01-21', 'Completed'),
(15, 'Kubernetes', '2024-05-08', 'Completed'),
(4, 'LangChain', '2024-06-18', 'In Progress'),
(16, 'Deep Learning', '2026-09-16', 'Completed'),
(9, 'Generative AI', '2024-11-16', 'Completed'),
(6, 'Docker', '2024-06-25', 'Completed'),
(12, 'Leadership', '2025-06-07', 'Completed'),
(15, 'Azure Fundamentals', '2024-03-24', 'Completed'),
(20, 'Project Management', '2025-03-22', 'Completed'),
(14, 'Kubernetes', '2026-11-03', 'In Progress'),
(6, 'Leadership', '2024-04-28', 'Completed'),
(7, 'Azure Fundamentals', '2026-07-28', 'Completed'),
(1, 'Kubernetes', '2024-06-19', 'Completed'),
(6, 'Deep Learning', '2026-12-20', 'Completed'),
(17, 'LangChain', '2024-10-12', 'In Progress'),
(7, 'Project Management', '2026-07-07', 'In Progress'),
(16, 'Azure Fundamentals', '2025-09-07', 'Completed'),
(6, 'Advanced SQL', '2024-01-14', 'Completed'),
(3, 'Advanced SQL', '2025-02-07', 'Completed'),
(6, 'Deep Learning', '2025-03-19', 'In Progress');


