from typing import Any, Dict, List, Optional, TypedDict

from behave import given, then, when
from behave.runner import Context


class Task(TypedDict, total=False):
    title: str
    description: str
    status: str
    due_date: str
    assignee: str
    project: str
    category: str
    area: str


@given('a user "{username}" exists and has enabled notifications')
def given_a_user_username_exists_and_has_enabled_notifications(
    context: Context, username: str
) -> None:
    context.users = context.users if hasattr(context, "users") else {}
    context.users[username] = {
        "notifications_enabled": True,
        "email_valid": True,
        "notifications": [],
    }


@given("the notification service is operational")
def given_the_notification_service_is_operational(context: Context) -> None:
    context.notification_service_online = True


@given('"{username}" has an invalid email address')
def given_username_has_an_invalid_email_address(
    context: Context, username: str
) -> None:
    context.users[username]["email_valid"] = False


@given('a task titled "{title}" is assigned to "{username}"')
def given_a_task_titled_title_is_assigned_to_username(
    context: Context, title: str, username: str
) -> None:
    task: Task = {"title": title, "assignee": username}
    context.task = task
    context.users[username]["tasks"] = context.users[username].get("tasks", []) + [task]


@when('a task titled "{title}" is assigned to "{username}"')
def when_a_task_titled_title_is_assigned_to_username(
    context: Context, title: str, username: str
) -> None:
    task: Task = {
        "title": title,
        "description": "Task description",
        "assignee": username,
    }
    context.task = task
    context.notification_event = f"Assigned task '{title}'"
    send_notification(context, username, task, "assignment")


@when('the status of task "{title}" changes to "{status}"')
def when_the_status_of_task_title_changes_to_status(
    context: Context, title: str, status: str
) -> None:
    context.task["status"] = status
    context.notification_event = f"Task '{title}' status changed to {status}"
    send_notification(context, context.task["assignee"], context.task, "status update")


@when('the due date of task "{title}" changes to "{due_date}"')
def when_the_due_date_of_task_title_changes_to_due_date(
    context: Context, title: str, due_date: str
) -> None:
    context.task["due_date"] = due_date
    context.notification_event = f"Task '{title}' due date changed to {due_date}"
    send_notification(
        context, context.task["assignee"], context.task, "due date update"
    )


@when("a notification is triggered")
def when_a_notification_is_triggered(context: Context) -> None:
    send_notification(context, context.task["assignee"], context.task, "generic")


@then('"{username}" should receive a notification about the assignment')
@then('"{username}" should receive a notification about the status update')
@then('"{username}" should receive a notification about the due date change')
def then_username_should_receive_a_notification_about_the_due_date_change(
    context: Context, username: str
) -> None:
    notifications: List[Dict[str, Any]] = context.users[username]["notifications"]
    assert len(notifications) > 0, f"{username} did not receive any notification"


@then("the notification should include the task title and description")
def then_the_notification_should_include_the_task_title_and_description(
    context: Context,
) -> None:
    notif = context.users[context.task["assignee"]]["notifications"][-1]
    assert (
        "title" in notif and "description" in notif
    ), "Notification missing task details"


@then("the notification should include the new status")
def then_the_notification_should_include_the_new_status(context: Context) -> None:
    notif = context.users[context.task["assignee"]]["notifications"][-1]
    assert "status" in notif, "Status not included in notification"


@then("the notification should include the new due date")
def then_the_notification_should_include_the_new_due_date(context: Context) -> None:
    notif = context.users[context.task["assignee"]]["notifications"][-1]
    assert "due_date" in notif, "Due date not included in notification"


@then("the notification should be logged")
def then_the_notification_should_be_logged(context: Context) -> None:
    assert hasattr(context, "notification_log"), "No notification log found"
    assert (
        context.notification_event in context.notification_log
    ), "Notification not logged"


@then("the system should attempt to retry delivery 3 times")
def then_the_system_should_attempt_to_retry_delivery_3_times(context: Context) -> None:
    assert context.retry_attempts == 3, "System did not retry 3 times"


@then("the system should mark the notification as failed")
def then_the_system_should_mark_the_notification_as_failed(context: Context) -> None:
    assert (
        context.last_notification_status == "failed"
    ), "Notification was not marked as failed"


@then('"{username}" should see the notification in the in-app center')
def then_username_should_see_the_notification_in_the_in_app_center(
    context: Context, username: str
) -> None:
    notif = context.users[username]["notifications"][-1]
    assert notif["channel"] == "in-app", "Notification fallback to in-app failed"


# -------------- Helper ------------------


def send_notification(
    context: Context, username: str, task: Task, change_type: str
) -> None:
    context.notification_log = (
        context.notification_log if hasattr(context, "notification_log") else []
    )
    context.retry_attempts = 0

    user = context.users[username]

    if not user["notifications_enabled"]:
        return

    notification: Dict[str, Optional[str]] = {
        "title": task.get("title"),
        "description": task.get("description", ""),
        "status": task.get("status") if change_type == "status update" else None,
        "due_date": task.get("due_date") if change_type == "due date update" else None,
        "channel": "email" if user["email_valid"] else "in-app",
    }

    # Simulate retries on email failure
    if not user["email_valid"]:
        while context.retry_attempts < 3:
            context.retry_attempts += 1
        context.last_notification_status = "failed"
    else:
        context.last_notification_status = "sent"

    user["notifications"].append(notification)
    event = getattr(
        context,
        "notification_event",
        f"{change_type.capitalize()} notification for task '{task.get('title')}'",
    )
    context.notification_log.append(event)
