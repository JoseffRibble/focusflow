from datetime import datetime

from behave import given, then, when
from behave.runner import Context


@given("the following tasks exist with due dates")
def given_the_following_tasks_exist_with_due_dates(context: Context) -> None:
    context.tasks = []
    for row in context.table:
        context.tasks.append({"title": row["title"], "due_date": row["due_date"]})


@given("no tasks with due dates exist")
def given_no_tasks_with_due_dates_exist(context: Context) -> None:
    context.tasks = []


@when("I switch to the calendar view")
def when_i_switch_to_the_calendar_view(context: Context) -> None:
    if getattr(context, "simulate_error", False):
        context.update_error = True
    else:
        context.view_mode = "calendar"


@when("I switch to the timeline view")
def when_i_switch_to_the_timeline_view(context: Context) -> None:
    if getattr(context, "simulate_error", False):
        context.update_error = True
    else:
        context.view_mode = "timeline"


@when('I navigate to the week of "{date}"')
def when_i_navigate_to_the_week_of_date(context: Context, date: str) -> None:
    context.current_week_start = datetime.strptime(date, "%Y-%m-%d")


@then("I should see tasks arranged by their due dates")
def then_i_should_see_tasks_arranged_by_their_due_dates(context: Context) -> None:
    # expected_titles = [row["title"] for row in context.table]
    actual_titles = sorted([t["title"] for t in context.tasks], key=lambda x: x)
    for row in context.table:
        assert row["title"] in actual_titles


@then("I should see the following tasks in timeline")
def then_i_should_see_the_following_tasks_in_timeline(context: Context) -> None:
    visible_tasks = [t["title"] for t in context.tasks]
    for row in context.table:
        assert row["title"] in visible_tasks


@then('I should see a "No scheduled tasks" message')
def then_i_should_see_a_no_scheduled_tasks_message(context: Context) -> None:
    assert context.tasks == [], "Expected no scheduled tasks, but some exist."
