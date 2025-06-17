from datetime import datetime

from behave import given, then, when
from behave.runner import Context


@given('a task titled "Design homepage" exists and is accessible')
def given_a_task_titled_design_homepage_exists_and_is_accessible(
    context: Context,
) -> None:
    context.task = {"title": "Design homepage", "due_date": None, "history": []}


@when('I select the task "Design homepage"')
def when_i_select_the_task_design_homepage(context: Context) -> None:
    context.selected_task = context.task


@when('I set the due date to "{due_date}"')
def when_i_set_the_due_date_to_due_date(context: Context, due_date: str) -> None:
    try:
        parsed_date = datetime.strptime(due_date, "%Y-%m-%d %H:%M")
        now = datetime.now()

        if getattr(context, "simulate_update_error", False):
            context.update_error = True
            context.confirmation = False
            return

        if parsed_date < now:
            context.invalid_due_date = True
            context.confirmation = False
        else:
            context.selected_task["due_date"] = due_date
            context.confirmation = True
            context.confirmation_message = True
            context.selected_task["history"].append(f"Due date set to {due_date}")
    except ValueError:
        context.invalid_due_date = True
        context.confirmation = False


@then('the due date of task "Design homepage" should be "{expected_date}"')
def then_the_due_date_of_task_design_homepage_should_be_expected_date(
    context: Context, expected_date: str
) -> None:
    assert (
        context.selected_task["due_date"] == expected_date
    ), f'Expected due date "{expected_date}", got "{context.selected_task["due_date"]}"'


@then("the due date change should be recorded in task history")
def then_the_due_date_change_should_be_recorded_in_task_history(
    context: Context,
) -> None:
    history = context.selected_task.get("history", [])
    assert any(
        "Due date set to" in entry for entry in history
    ), "Due date change not recorded."


@then("I should see a validation error for invalid date")
def then_i_should_see_a_validation_error_for_invalid_date(context: Context) -> None:
    assert (
        context.invalid_due_date
    ), "Expected validation error for past date, but none occurred."


@then("the task due date should not be updated")
def then_the_task_due_date_should_not_be_updated(context: Context) -> None:
    assert (
        context.selected_task["due_date"] is None
    ), "Task due date was incorrectly updated."


@then("the task due date should remain unchanged")
def then_the_task_due_date_should_remain_unchanged(context: Context) -> None:
    assert (
        context.task["due_date"] is None
    ), "Due date should remain unchanged after system error."
