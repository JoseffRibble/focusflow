<!-- Generated with Claude 3.5 Sonnet -->

# Use Case: Task Notifications

### Name: 
Send Task Assignment Notifications

### Summary: 
This use case describes how the system notifies users about new task assignments and task updates. This functionality ensures users stay informed about their task responsibilities and changes to existing tasks.

### Actor:
System User, System Notification Service

### Triggering Event:
- New task assignment
- Task update (status, due date, details)
- Task deletion or archival

### Inputs:
- Task identifier
- Task details
- Change type
- User notification preferences
- User contact information

### Pre-Conditions:
- User is registered in the system
- User has valid notification settings
- User has opted in to notifications
- System notification service is operational

### Process Description:
1. System detects task-related event
2. System checks user notification preferences
3. System prepares notification content:
   - Task title and description
   - Type of change
   - Relevant details
   - Action links
4. System selects notification channel(s):
   - In-app notification
   - Email
   - Browser notification
5. System sends notification
6. System tracks notification delivery
7. System logs notification event

### Exceptions:
1. Notification Delivery Failure:
   - System logs delivery error
   - System attempts retry (up to 3 times)
   - System marks notification as failed
   - User can view pending notifications in-app

2. Invalid User Contact Info:
   - System logs validation error
   - System uses fallback notification method
   - System prompts user to update contact info

### Outputs and Post-Conditions:
- User receives notification
- Notification is marked as sent
- Notification appears in user's history
- System logs notification status
- User can interact with notification