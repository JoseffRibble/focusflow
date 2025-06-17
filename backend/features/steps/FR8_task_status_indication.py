from behave import given, then, when
from behave.runner import Context


@given("the following tasks exist with status indicators")
def given_the_following_tasks_exist_with_status_indicators(context: Context) -> None:
    context.task_list = []
    for row in context.table:
        task = {}
        for heading in row.headings:
            task[heading] = row[heading]
        context.task_list.append(task)


@when("I check the task status indicators")
def when_i_check_the_task_status_indicators(context: Context) -> None:
    # This is where the logic for checking task status indicators would be placed
    pass


@then(
    "I should see visual status indicators for overdue, upcoming, and completed tasks"
)
def step_impl(context: Context) -> None:
    # This is where the logic for validating the visual indicators would be placed
    pass
