<!-- Generated with Claude 3.5 Sonnet -->

# Use Case: Filter and Sort Tasks

### Name: 
Filter and Sort Task List

### Summary: 
This use case describes the process of filtering and sorting tasks based on various criteria including status, due date, and organizational attributes. This functionality enables users to efficiently organize and find relevant tasks.

### Actor:
System User

### Triggering Event:
User initiates filtering or sorting of task list

### Inputs:
- Filter criteria:
  - Task status
  - Due date range
  - Project
  - Category
  - Area of responsibility
- Sort criteria:
  - Sort field
  - Sort direction (ascending/descending)

### Pre-Conditions:
- User is authenticated in the system
- User has access to task list
- Tasks exist in the system

### Process Description:
1. User navigates to task list view
2. System displays default task list
3. User selects filter criteria and/or sort options
4. System validates filter/sort combination
5. System applies selected filters
6. System sorts filtered results
7. System displays filtered and sorted task list
8. User can modify or clear filters
9. System updates view in real-time

### Exceptions:
1. Invalid Filter Combination:
   - System displays warning message
   - User adjusts filter criteria
   - Process continues from step 4

2. No Results Found:
   - System displays "No tasks match criteria" message
   - User can modify filters
   - Process returns to step 3

### Outputs and Post-Conditions:
- Task list is filtered according to criteria
- Tasks are sorted as specified
- Filter/sort preferences may be saved
- Task count reflects filtered results
- Original task list remains unchanged