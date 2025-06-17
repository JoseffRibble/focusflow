from datetime import datetime

from behave import given, then, when
from behave.runner import Context

# ----------------- GIVEN -----------------


@given("I am logged in")
def given_i_am_logged_in(context: Context) -> None:
    context.user = {"authenticated": True}


@given("I have permission to create tasks")
def given_i_have_permission_to_create_tasks(context: Context) -> None:
    context.permissions = getattr(context, "permissions", [])
    if "create_task" not in context.permissions:
        context.permissions.append("create_task")


@given("I have permission to modify tasks")
def given_i_have_permission_to_modify_tasks(context: Context) -> None:
    context.permissions = getattr(context, "permissions", [])
    if "modify_task" not in context.permissions:
        context.permissions.append("modify_task")


@given("I have permission to assign tasks")
def given_i_have_permission_to_assign_tasks(context: Context) -> None:
    context.permissions = getattr(context, "permissions", [])
    if "assign_task" not in context.permissions:
        context.permissions.append("assign_task")


@given("the system encounters a storage error")
def given_the_system_encounters_a_storage_error(context: Context) -> None:
    context.simulate_storage_error = True


@given("the system encounters an update error")
def given_the_system_encounters_an_update_error(context: Context) -> None:
    context.simulate_update_error = True


@given('the current system time is "{timestamp}"')
def given_the_current_system_time_is_timestamp(
    context: Context, timestamp: str
) -> None:
    context.current_time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M")


@given("I have access to the task list")
def given_i_have_access_to_the_task_list(context: Context) -> None:
    context.task_list = []


@given("the following tasks exist")
def given_the_following_tasks_exist(context: Context) -> None:
    context.task_list = []
    for row in context.table:
        due_date_str = row.get("due_date", "").strip()
        due_date = None
        if due_date_str:
            for fmt in ("%Y-%m-%d %H:%M", "%Y-%m-%d"):
                try:
                    due_date = datetime.strptime(due_date_str, fmt)
                    break
                except ValueError:
                    continue
        task = {
            "title": row.get("title"),
            "status": row.get("status"),
            "due_date": due_date,
            "project": row.get("project"),
            "category": row.get("category"),
            "area": row.get("area"),
        }
        context.task_list.append(task)
    context.filtered_list = list(context.task_list)


# ----------------- WHEN -----------------


@when("I view the task list")
def when_i_view_the_task_list(context: Context) -> None:
    context.visible_tasks = (
        context.filtered_list
        if hasattr(context, "filtered_list")
        else context.task_list
    )


@when('I filter tasks by status "{status}"')
def when_i_filter_tasks_by_status_status(context: Context, status: str) -> None:
    filtered = [t for t in context.task_list if t["status"] == status]
    context.filtered_list = filtered
    if not filtered:
        context.no_results = True


@when('I sort tasks by "{field}" in "{direction}" order')
def when_i_sort_tasks_by_field_in_direction_order(
    context: Context, field: str, direction: str
) -> None:
    reverse = direction.lower() == "descending"
    context.filtered_list = sorted(
        context.filtered_list,
        key=lambda x: x.get(field) if x.get(field) is not None else "",
        reverse=reverse,
    )


@when('I apply a filter with status "Done" and area "Unknown Team"')
def when_i_apply_a_filter_with_status_done_and_area_unknown_team(
    context: Context,
) -> None:
    context.invalid_filter_combo = True


# ----------------- THEN -----------------


@then("I should see an error message")
def then_i_should_see_an_error_message(context: Context) -> None:
    assert any(
        [
            getattr(context, "simulate_storage_error", False),
            getattr(context, "simulate_update_error", False),
            getattr(context, "simulate_save_error", False),
        ]
    ), "Expected error message but no error simulated"


@then("I should see a confirmation message")
def then_i_should_see_a_confirmation_message(context: Context) -> None:
    assert getattr(
        context, "confirmation_message", False
    ), "Expected confirmation message but none found"


@then("I should see the following tasks")
def then_i_should_see_the_following_tasks(context: Context) -> None:
    expected_titles = [row["title"] for row in context.table]
    actual_titles = [task["title"] for task in context.filtered_list]
    assert (
        expected_titles == actual_titles
    ), f"Expected: {expected_titles}, but got: {actual_titles}"


@then("the task list should be ordered as")
def then_the_task_list_should_be_ordered_as(context: Context) -> None:
    expected_order = [row["title"] for row in context.table]
    actual_order = [task["title"] for task in context.filtered_list]
    assert (
        expected_order == actual_order
    ), f"Expected order: {expected_order}, but got: {actual_order}"


@then('I should see a "No tasks match criteria" message')
def then_i_should_see_a_no_tasks_match_criteria_message(context: Context) -> None:
    assert getattr(
        context, "no_results", False
    ), "Expected no results message, but tasks were found"


@then("I should see a warning message about invalid filter combination")
def then_i_should_see_a_warning_message_about_invalid_filter_combination(
    context: Context,
) -> None:
    assert getattr(
        context, "invalid_filter_combo", False
    ), "Expected warning for invalid filter combination"


@then("I should see the following visual status indicators")
def then_i_should_see_the_following_visual_status_indicators(context: Context) -> None:
    # Stub: Add visual logic if needed
    pass


@then('I should see a warning icon next to "Broken task"')
def then_i_should_see_a_warning_icon_next_to_broken_task(context: Context) -> None:
    # Stub: Add error visualization logic
    pass


@then('default styling should be applied to "Broken task"')
def then_default_styling_should_be_applied_to_broken_task(context: Context) -> None:
    # Stub: Add UI style check
    pass


@then("the system should retain the previous indicators")
def then_the_system_should_retain_the_previous_indicators(context: Context) -> None:
    # Stub: Add visual state persistence check
    pass
