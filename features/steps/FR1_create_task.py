from behave import then, when
from behave.runner import Context


@when('I click the "Create New Task" button')
def when_i_click_the_create_new_task_button(context: Context) -> None:
    context.task_form_opened = True
    context.task = {}


@when('I enter "{title}" as the task title')
def when_i_enter_title_as_the_task_title(context: Context, title: str) -> None:
    context.task["title"] = title


@when('I add a description "{description}"')
def when_i_add_a_description_description(context: Context, description: str) -> None:
    context.task["description"] = description


@when('I associate the task with the project "{project}"')
def when_i_associate_the_task_with_the_project_project(
    context: Context, project: str
) -> None:
    context.task["project"] = project


@when('I assign the category "{category}"')
def when_i_assign_the_category_category(context: Context, category: str) -> None:
    context.task["category"] = category


@when('I add tags "{tag1}", "{tag2}"')
def when_i_add_tags_tag1_tag2(context: Context, tag1: str, tag2: str) -> None:
    context.task["tags"] = [tag1, tag2]


@when('I upload the file "{filename}"')
def when_i_upload_the_file_filename(context: Context, filename: str) -> None:
    context.task["attachment"] = filename


@when("I leave the title field empty")
def when_i_leave_the_title_field_empty(context: Context) -> None:
    context.task["title"] = ""


@when('I click the "Save" button')
def when_i_click_the_save_button(context: Context) -> None:
    title = context.task.get("title", "")
    if title == "":
        context.validation_error = "Title is required"
        context.task_created = False
        return

    if getattr(context, "simulate_storage_error", False):
        context.storage_error = True
        context.task_created = False
        return

    context.task_created = True
    if not hasattr(context, "task_list"):
        context.task_list = []
    context.task_list.append(context.task)


@when('I create a task titled "{title}"')
def when_i_create_a_task_titled_title(context: Context, title: str) -> None:
    context.task = {"title": title}
    if getattr(context, "simulate_storage_error", False):
        context.task_created = False
        context.storage_error = True
    else:
        context.task_created = True
        if not hasattr(context, "task_list"):
            context.task_list = []
        context.task_list.append(context.task)


@then("I should see a success message")
def then_i_should_see_a_success_message(context: Context) -> None:
    assert context.task_created, "Expected success message, but task was not created."


@then('the task "{title}" should appear in my task list')
def then_the_task_title_should_appear_in_my_task_list(
    context: Context, title: str
) -> None:
    task_list = getattr(context, "task_list", [])
    found = any(task.get("title") == title for task in task_list)
    assert found, f'Task "{title}" was not found in the task list.'


@then("I should see a validation error for the title field")
def then_i_should_see_a_validation_error_for_the_title_field(context: Context) -> None:
    assert hasattr(
        context, "validation_error"
    ), "Expected validation error, but none was raised."
    assert (
        context.validation_error == "Title is required"
    ), "Unexpected validation error message."


@then("the task should not be created")
def then_the_task_should_not_be_created(context: Context) -> None:
    assert not context.task_created, "Expected task to NOT be created."


@then("the task should not appear in my task list")
def then_the_task_should_not_appear_in_my_task_list(context: Context) -> None:
    title = context.task.get("title")
    task_list = getattr(context, "task_list", [])
    found = any(task.get("title") == title for task in task_list)
    assert not found, f'Task "{title}" should not appear in the task list.'
