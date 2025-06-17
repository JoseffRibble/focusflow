from behave import given, then, when
from behave.runner import Context


@given('a task titled "Submit report" exists and is accessible')
def given_a_task_titled_submit_report_exists_and_is_accessible(
    context: Context,
) -> None:
    context.task = {"title": "Submit report", "status": "To Do", "history": []}


@when('I select the task "Submit report"')
def when_i_select_the_task_submit_report(context: Context) -> None:
    context.selected_task = context.task


@when('I change the status to "{new_status}"')
def when_i_change_the_status_to_new_status(context: Context, new_status: str) -> None:
    valid_statuses = ["To Do", "In Progress", "Done"]
    if getattr(context, "simulate_update_error", False):
        context.update_error = True
        context.confirmation = False
    elif new_status not in valid_statuses:
        context.invalid_status = True
        context.confirmation = False
    else:
        context.selected_task["status"] = new_status
        context.confirmation = True
        context.confirmation_message = True
        context.status_comment = None
        context.selected_task["history"].append(f"Status changed to {new_status}")


@when('I attempt to change the status to "Archived"')
def when_i_attempt_to_change_the_status_to_archived(context: Context) -> None:
    context.invalid_status = True
    context.confirmation = False


@when('I enter the comment "{comment}"')
def when_i_enter_the_comment_comment(context: Context, comment: str) -> None:
    context.status_comment = comment
    context.selected_task["history"].append(f"Comment: {comment}")


@then('the status of task "Submit report" should be "{expected_status}"')
def then_the_status_of_task_submit_report_should_be_expected_status(
    context: Context, expected_status: str
) -> None:
    assert (
        context.selected_task["status"] == expected_status
    ), f"Expected status '{expected_status}', got '{context.selected_task['status']}'"


@then("the status change should be recorded in task history")
def then_the_status_change_should_be_recorded_in_task_history(context: Context) -> None:
    history = context.selected_task.get("history", [])
    assert any(
        "Status changed to" in entry for entry in history
    ), "Status change not recorded in history."


@then('the comment "{comment}" should be saved with the status change')
def then_the_comment_comment_should_be_saved_with_the_status_change(
    context: Context, comment: str
) -> None:
    assert (
        f"Comment: {comment}" in context.selected_task["history"]
    ), "Comment not recorded."


@then("I should see an error message about invalid status")
def then_i_should_see_an_error_message_about_invalid_status(context: Context) -> None:
    assert context.invalid_status, "Expected invalid status error, but none occurred."


@then('the status of task "Submit report" should remain unchanged')
def then_the_status_of_task_submit_report_should_remain_unchanged(
    context: Context,
) -> None:
    assert context.task["status"] == "To Do", "Task status was changed unexpectedly."
