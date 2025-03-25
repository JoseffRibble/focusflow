# **Exercise 2 – FocusFlow Requirements and Use Cases**

# **Note**

- We use ChatGpt to confirm grammatical correctness.

# **2.1 Requirements**

## **1\. Core Task Management**

| ID | Requirement Description |
| :---: | ----- |
| FR1 | The system shall allow users to create new tasks with a title, relevant details, and contextual information. |
| FR2 | The system shall allow users to assign a status to each task (e.g., "To Do", "In Progress", "Done") to track workflow. |
| FR3 | The system shall allow users to assign specific due dates to tasks. |
| FR4 | The system shall allow users to assign one or more organizational attributes to each task, such as project, category, or area of responsibility. |
| FR5 | The system shall allow users to assign tasks to any user, including themselves. |

## **2\. Task Visualization & Prioritization**

| ID | Requirement Description |
| :---: | ----- |
| FR6 | The system shall allow users to filter or sort tasks based on status, due date, or organizational attributes (e.g. project, category, or area of responsibility). |
| FR7 | The system shall enable users to view tasks organized by their due dates (e.g., timeline or calendar view). |
| FR8 | The system shall visually indicate overdue tasks, upcoming tasks, and completed tasks. |

## 

## **3\. Notifications & Reminders**

| ID | Requirement Description |
| :---: | ----- |
| FR9 | The system could send notifications to users when they are assigned new tasks or when tasks are updated. |
| FR10 | The system could send reminder notifications to users for tasks with due dates, including: a) an upcoming reminder before the due date (e.g., 1 day in advance), b) a reminder on the due date, c) and an overdue notification if the due date has passed and the task is not completed. |
| FR11 | The system shall allow users to configure or limit the frequency and type of notifications they receive. |

## **4\. User Interface & Accessibility**

| ID | Requirement Description |
| :---: | ----- |
| FR12 | The system shall provide an intuitive and clean web-based user interface accessible from multiple devices. |

# **2.2 Quality Model**

## **Selected ISO 25010 Quality Aspects**

### **1\. Functional Suitability**

- **Reason**: Users depend on the system to fulfill their organizational needs, so the application's feature set must be complete, correct, and relevant to their workflows.  
- **Quality Model**:  
  - Percentage of implemented functional requirements (requirement coverage).  
  - Success rate of functional test cases.  
  - User feedback from acceptance testing.  
- **Testability**:  
  - Use a traceability matrix to map each requirement to corresponding test cases.  
  - Implement automated unit tests for individual component validation.  
  - Run integration tests to verify interactions between modules.  
  - Conduct acceptance tests to ensure workflows align with user expectations.

### **2\. Performance Efficiency**

- **Reason**: FocusFlow should perform efficiently, ensuring quick task retrieval, minimal delay in updating statuses, and optimal resource utilization. Slow response times may reduce productivity and frustrate users.  
- **Quality Mode**l:  
  - Measure response times for task creation, filtering, and reminders.  
  - Monitor memory and CPU consumption under typical loads.  
  - Verify the system can support a reasonable number of concurrent users without performance degradation.

### **3\. Reliability**

- **Reason**: FocusFlow requires high reliability, ensuring data persistence, accurate reminders, and continuous availability. If reminders fail or the system crashes, users may miss critical deadlines.  
- **Quality Mode**l:  
  - Monitor system uptime to ensure high availability.  
  - Ensure system continues to function despite minor failures.  
  - Ensure data persistence and accurate delivery of reminders.  
- **Testability**:   
  - Perform failure injection tests to evaluate fault tolerance.  
  - Use uptime monitoring tools to track availability and detect downtimes.

### **4\. Maintainability**

- **Reason**: The system should be easy to modify, update, and debug to accommodate future improvements, bug fixes, and performance enhancements.  
- **Quality Mode**l:  
  - Ensure the codebase is well-structured, allowing independent updates to components.  
  - Develop reusable components to minimize redundant coding.  
- **Testability**:   
  - Perform regression testing after updates to ensure existing features remain intact.  
  - Use static code analysis tools to detect code complexity and highlight maintainability concerns.