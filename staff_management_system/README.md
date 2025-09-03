This application manages the staff of a company, where the HR can check existing staff, create new staff, delete staff, and update staff records.

The goal is to create a web application for businesses to efficiently manage their employees. The system will provide a centralized platform for storing employee information, tracking their roles, and managing their status within the company.



Requirements:

1\.	CRUD Operations for Staff, Grade, and Departments.

2\.	Endpoint for searching staff records.

3\.	Use Django ORM for database interactions.

4\.	Deploy the API on Heroku or PythonAnywhere.

Features of the Software:

1\.	Managed by the HR with different Permissions levels : 

a.	Admin - Can perform all tasks, including administrative,

b.	HR Staff - Can simply view records only (ReadOnly), but can not create or delete a record.

c.	Customized - Can view records and can create new staff, but can not delete, or access can be customized to taste.

2\.	Secured Authentication: Authentication is secured using a token and email for security.

3\.	Employee Profiles: A page to view detailed information for each employee, including their name, ID, contact information, role, and the department they belong to.

4\.	Department Management: The ability to add, edit, and view all departments within the company.

5\.	Add/Edit Employees: A form to add new employees and the ability to assign them to an existing department. You can also update the details of an existing employee.

6\.	Search Functionality: A search bar to quickly find employees by name or employee ID. You can also implement a search to filter employees by department.

7\.	View All Employees and Departments: A dashboard or list view to see all employees and departments at a glance.

API Usage (Optional):

For this project, I don't need to rely on any external APIs. All the necessary data and functionality will be handled internally by my Django application. This keeps the project focused on core backend development concepts.



Models and Endpoints:

It uses two core models: Employee and Department. This Employee model will represent an employee/staff in my database, while the Department will represent the Unit / Department the employee belongs to.

The Employee model will have a relationship with the Department model.

Models

●	Department Model:

○	name (CharField, unique=True)

○	description (TextField, optional)

○	created\_at (DateTimeField)

●	Employee Model:

○	first\_name (CharField)

○	last\_name (CharField)

○	employee\_id (IntegerField, unique=True)

○	email (EmailField, unique=True)

○	phone\_number (CharField, optional)

○	role (CharField)

○	hire\_date (DateField)

○	is\_active (BooleanField, default=True)

○	department (ForeignKey to Department, on\_delete=models.CASCADE)



API Endpoints

I have separate endpoints for both models to handle CRUD (Create, Read, Update, Delete) operations.

●	Department Endpoints:

○	GET /api/departments/: Get a list of all departments.

○	POST /api/departments/: Add a new department.

○	GET /api/departments/<int:pk>/: Get a single department's details.

○	PUT /api/departments/<int:pk>/: Update an existing department.

○	DELETE /api/departments/<int:pk>/: Delete a department.

●	Employee Endpoints:

○	GET /api/employees/: Get a list of all employees.

○	POST /api/employees/: Add a new employee, and assign them to a department.

○	GET /api/employees/<int:pk>/: Get a single employee's details, including their department's information.

○	PUT /api/employees/<int:pk>/: Update an existing employee.

○	DELETE /api/employees/<int:pk>/: Delete an employee.



