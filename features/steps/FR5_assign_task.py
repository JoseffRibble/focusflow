from behave import given, then, when
from behave.runner import Context


@given('a task titled "Prepare Q3 presentation" exists and is assignable')
def given_a_task_titled_prepare_q3_presentation_exists_and_is_assignable(
    context: Context,
) -> None:
    context.task = {
        "title": "Prepare Q3 presentation",
        "assignee": None,
        "history": [],
        "locked": False,
    }


@given('a user "alice" has an active account')
def given_a_user_alice_has_an_active_account(context: Context) -> None:
    context.available_users = {"alice": {"active": True, "notified": False}}


@given("I do not have permission to assign tasks")
def given_i_do_not_have_permission_to_assign_tasks(context: Context) -> None:
    context.permissions = []


@when('I select the task "Prepare Q3 presentation"')
def when_i_select_the_task_prepare_q3_presentation(context: Context) -> None:
    context.selected_task = context.task


@when('I assign the task to "alice"')
def when_i_assign_the_task_to_alice(context: Context) -> None:
    if "assign_task" not in context.permissions:
        context.invalid_assignment = True
        context.simulate_update_error = True
        context.confirmation = False
        return
    context.pending_assignee = "alice"


@when('I enter the assignment comment "Please complete by Friday"')
def when_i_enter_the_assignment_comment_please_complete_by_friday(
    context: Context,
) -> None:
    context.assignment_comment = "Please complete by Friday"


@when("I confirm the assignment")
def when_i_confirm_the_assignment(context: Context) -> None:
    if getattr(context, "invalid_assignment", False):
        context.confirmation = False
        return

    if getattr(context, "simulate_update_error", False):
        context.update_error = True
        context.confirmation = False
        return

    context.selected_task["assignee"] = context.pending_assignee
    context.selected_task["history"].append(f"Assigned to {context.pending_assignee}")
    if hasattr(context, "assignment_comment"):
        context.selected_task["history"].append(
            f"Comment: {context.assignment_comment}"
        )
    context.available_users[context.pending_assignee]["notified"] = True
    context.confirmation = True
    context.confirmation_message = True


@then('the task should be assigned to "alice"')
def then_the_task_should_be_assigned_to_alice(context: Context) -> None:
    assert context.selected_task["assignee"] == "alice", "Assignee mismatch"


@then("the assignment should be recorded in task history")
def then_the_assignment_should_be_recorded_in_task_history(context: Context) -> None:
    history = context.selected_task["history"]
    assert any("Assigned to alice" in h for h in history), "Assignment not logged"


@then('"alice" should be notified')
def then_alice_should_be_notified(context: Context) -> None:
    assert context.available_users["alice"]["notified"], "Notification not sent"


@then("the task should remain unassigned")
def then_the_task_should_remain_unassigned(context: Context) -> None:
    assert context.task["assignee"] is None, "Task was incorrectly assigned"
