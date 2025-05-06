from behave import given, then, when
from behave.runner import Context


@given('a task titled "Write quarterly summary" exists and is accessible')
def given_a_task_titled_write_quarterly_summary_exists_and_is_accessible(
    context: Context,
) -> None:
    context.task = {
        "title": "Write quarterly summary",
        "project": None,
        "category": None,
        "area": None,
        "history": [],
    }
    context.original_task_state = context.task.copy()
    context.pending_attributes = {}


@when('I select the task "Write quarterly summary"')
def when_i_select_the_task_write_quarterly_summary(context: Context) -> None:
    context.selected_task = context.task


@when('I assign the project "{project}"')
def when_i_assign_the_project_project(context: Context, project: str) -> None:
    context.pending_attributes["project"] = project


@when('I select the category "{category}"')
def when_i_select_the_category_category(context: Context, category: str) -> None:
    context.pending_attributes["category"] = category


@when('I set the area of responsibility to "{area}"')
def when_i_set_the_area_of_responsibility_to_area(context: Context, area: str) -> None:
    context.pending_attributes["area"] = area


@when("I click confirm to save attributes")
def when_i_click_confirm_to_save_attributes(context: Context) -> None:
    project = context.pending_attributes.get("project")
    category = context.pending_attributes.get("category")
    area = context.pending_attributes.get("area")

    if project == "Finance" and category == "Engineering":
        context.invalid_attribute_combo = True
        context.confirmation = False
        return

    if getattr(context, "simulate_update_error", False):
        context.update_error = True
        context.confirmation = False
        return

    # Save the attributes to the task
    context.selected_task["project"] = project
    context.selected_task["category"] = category
    context.selected_task["area"] = area
    context.selected_task["history"].append(f"Project set to {project}")
    context.selected_task["history"].append(f"Category set to {category}")
    context.selected_task["history"].append(f"Area set to {area}")
    context.confirmation = True
    context.confirmation_message = True


@then('the task "Write quarterly summary" should have the project "{project}"')
def then_the_task_write_quarterly_summary_should_have_the_project_project(
    context: Context, project: str
) -> None:
    assert context.selected_task["project"] == project, "Project assignment mismatch."


@then('the task should be categorized under "{category}"')
def then_the_task_should_be_categorized_under_category(
    context: Context, category: str
) -> None:
    assert (
        context.selected_task["category"] == category
    ), "Category assignment mismatch."


@then('the task should be assigned to area "{area}"')
def then_the_task_should_be_assigned_to_area_area(context: Context, area: str) -> None:
    assert context.selected_task["area"] == area, "Area assignment mismatch."


@then("the attribute changes should be recorded in task history")
def then_the_attribute_changes_should_be_recorded_in_task_history(
    context: Context,
) -> None:
    history = context.selected_task.get("history", [])
    assert any(
        "Project set to" in entry for entry in history
    ), "Project change not recorded."
    assert any(
        "Category set to" in entry for entry in history
    ), "Category change not recorded."
    assert any("Area set to" in entry for entry in history), "Area change not recorded."


@then("I should see a validation error for invalid attribute combination")
def then_i_should_see_a_validation_error_for_invalid_attribute_combination(
    context: Context,
) -> None:
    assert (
        context.invalid_attribute_combo
    ), "Expected attribute validation error, but none occurred."


@then("the task attributes should remain unchanged")
def then_the_task_attributes_should_remain_unchanged(context: Context) -> None:
    assert (
        context.selected_task["project"] == context.original_task_state["project"]
    ), "Project was unexpectedly changed."
    assert (
        context.selected_task["category"] == context.original_task_state["category"]
    ), "Category was unexpectedly changed."
    assert (
        context.selected_task["area"] == context.original_task_state["area"]
    ), "Area was unexpectedly changed."
