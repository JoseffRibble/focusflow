<!-- Generated with Claude 3.5 Sonnet -->

# Use Case: Manage Task Status

### Name: 
Update Task Status

### Summary: 
This use case describes the process of managing and updating task statuses in the system. Users can change the status of tasks between predefined states ("To Do", "In Progress", "Done") to reflect the current state of work. This functionality enables effective workflow tracking and task progression visualization.

### Actor:
System User

### Triggering Event:
User initiates status change for a task

### Inputs:
- Task identifier
- New status selection ("To Do", "In Progress", "Done")
- Optional status change comment

### Pre-Conditions:
- User is authenticated in the system
- User has permissions to modify tasks
- Task exists in the system
- Task is accessible to the user

### Process Description:
1. User selects a task from the task list
2. System displays the task details and current status
3. User clicks on status change control
4. System displays available status options
5. User selects the new status
6. User optionally enters a status change comment
7. System validates the status change
8. System updates the task status in the database
9. System records the status change in task history
10. System displays confirmation of successful status update

### Exceptions:
1. Invalid Status Transition:
   - System displays error message explaining invalid transition
   - User selects different status or cancels operation
   - Process returns to step 4

2. System Update Error:
   - System displays error message
   - System logs the error
   - User can retry the operation
   - Process returns to step 5

### Outputs and Post-Conditions:
- Task status is updated in the system
- Task appears in appropriate status view/filter
- Status change is logged in task history
- Task maintains all other attributes and associations
- Status change timestamp is recorded