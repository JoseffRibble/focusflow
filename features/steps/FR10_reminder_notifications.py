from datetime import datetime, timedelta

from behave import given, then, when
from behave.runner import Context


@given("the system reminder service is operational")
def given_the_system_reminder_service_is_operational(context: Context) -> None:
    context.reminder_service_online = True


@given('a task titled "{title}" is due on "{due_date}"')
def given_a_task_titled_title_is_due_on_due_date(
    context: Context, title: str, due_date: str
) -> None:
    context.task = {
        "title": title,
        "due_date": datetime.strptime(due_date, "%Y-%m-%d %H:%M"),
        "completed": False,
    }


@given('a task titled "{title}" has an invalid due date')
def given_a_task_titled_title_has_an_invalid_due_date(
    context: Context, title: str
) -> None:
    context.task = {"title": title, "due_date": "INVALID", "completed": False}


@given("the task is completed")
def given_the_task_is_completed(context: Context) -> None:
    context.task["completed"] = True


@given("the task is not completed")
def given_the_task_is_not_completed(context: Context) -> None:
    if "task" not in context:
        context.task = {}
    context.task["completed"] = False


@given('"{user}" is assigned to the task and has enabled reminders')
def given_user_is_assigned_to_the_task_and_has_enabled_reminders(
    context: Context, user: str
) -> None:
    context.assignee = user
    context.user_settings = {
        user: {"reminders_enabled": True, "reminder_received": None}
    }


@when("the system checks for due reminders")
def when_the_system_checks_for_due_reminders(context: Context) -> None:
    task = context.task
    user = context.assignee
    reminders = context.user_settings[user]

    if not context.reminder_service_online or not reminders["reminders_enabled"]:
        return

    due = task.get("due_date")
    if isinstance(due, str) or due is None:
        context.task_flagged = True
        return

    if task.get("completed"):
        return

    delta = due - context.current_time
    if timedelta(hours=23, minutes=59) <= delta <= timedelta(days=1, minutes=1):
        reminders["reminder_received"] = "upcoming"
    elif due.date() == context.current_time.date():
        reminders["reminder_received"] = "due today"
    elif due < context.current_time:
        reminders["reminder_received"] = "overdue"

    context.last_reminder = {
        "type": reminders["reminder_received"],
        "title": task["title"],
    }


@then('"{user}" should receive a "{reminder_type}" reminder')
def then_user_should_receive_a_reminder_type_reminder(
    context: Context, user: str, reminder_type: str
) -> None:
    actual = context.user_settings[user]["reminder_received"]
    assert actual == reminder_type, f'Expected "{reminder_type}", but got "{actual}"'


@then('the reminder should include task title "{title}"')
def then_the_reminder_should_include_task_title_title(
    context: Context, title: str
) -> None:
    assert (
        context.last_reminder["title"] == title
    ), "Reminder does not contain correct task title"


@then('"{user}" should not receive a reminder')
def then_user_should_not_receive_a_reminder(context: Context, user: str) -> None:
    assert (
        context.user_settings[user]["reminder_received"] is None
    ), "Unexpected reminder sent"


@then("the system should flag the task for due date review")
def then_the_system_should_flag_the_task_for_due_date_review(context: Context) -> None:
    assert context.task_flagged, "Task with invalid due date was not flagged"
