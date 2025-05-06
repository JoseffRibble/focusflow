from copy import deepcopy

from behave import given, then, when
from behave.runner import Context


@given("the notification system is operational")
def given_the_notification_system_is_operational(context: Context) -> None:
    context.notification_system_online = True


@given("my current notification settings are:")
def given_my_current_notification_settings_are(context: Context) -> None:
    context.notification_settings = {}
    for row in context.table:
        context.notification_settings[row["type"]] = {
            "enabled": row["enabled"].lower() == "true",
            "channel": row["channel"],
        }
    context.original_settings = deepcopy(context.notification_settings)


@given("the system encounters a save error")
def given_the_system_encounters_a_save_error(context: Context) -> None:
    context.simulate_save_error = True


@given("my current notification settings are")
def given_my_current_notification_settings_are_1(context: Context) -> None:
    context.notification_settings = {}
    for row in context.table:
        context.notification_settings[row["type"]] = {
            "enabled": row["enabled"].lower() == "true",
            "channel": row["channel"],
        }
    context.original_settings = context.notification_settings.copy()


@when("I update my notification preferences to")
def when_i_update_my_notification_preferences_to(context: Context) -> None:
    new_settings = {}
    for row in context.table:
        new_settings[row["type"]] = {
            "enabled": row["enabled"].lower() == "true",
            "channel": row["channel"],
        }

    # Simulate validation
    for setting in new_settings.values():
        if setting["enabled"] and setting["channel"] == "none":
            context.invalid_config = True
            context.updated = False
            return

    # Simulate save error
    if getattr(context, "simulate_save_error", False):
        context.updated = False
        context.save_error = True
        return

    context.notification_settings = new_settings
    context.updated = True


@then("my updated preferences should be")
def then_my_updated_preferences_should_be(context: Context) -> None:
    for row in context.table:
        expected_enabled = row["enabled"].lower() == "true"
        expected_channel = row["channel"]
        actual = context.notification_settings[row["type"]]
        assert (
            actual["enabled"] == expected_enabled
        ), f"Enabled mismatch for {row['type']}"
        assert (
            actual["channel"] == expected_channel
        ), f"Channel mismatch for {row['type']}"


@then("I should see a confirmation of saved changes")
def then_i_should_see_a_confirmation_of_saved_changes(context: Context) -> None:
    assert context.updated is True, "Expected confirmation, but changes were not saved"


@then("I should see an error about invalid channel selection")
def then_i_should_see_an_error_about_invalid_channel_selection(
    context: Context,
) -> None:
    assert getattr(
        context, "invalid_config", False
    ), "Expected validation error but none occurred"


@then("my preferences should remain unchanged")
def then_my_preferences_should_remain_unchanged(context: Context) -> None:
    assert (
        context.notification_settings == context.original_settings
    ), "Preferences were unexpectedly modified"
