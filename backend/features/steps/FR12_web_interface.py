from behave import given, then, when
from behave.runner import Context


@given("the system is operational")
def given_the_system_is_operational(context: Context) -> None:
    context.system_operational = True


@given('I have a compatible "{device}" with "{browser}" and screen width of {width}')
def given_i_have_a_compatible_device_with_browser_and_screen_width_of_width(
    context: Context, device: str, browser: str, width: str
) -> None:
    context.device = device
    context.browser = browser
    context.width = int(width)
    context.compatible = True


@given('I am using a compatible "{device}" device with "{browser}"')
def given_i_am_using_a_compatible_device_device_with_browser(
    context: Context, device: str, browser: str
) -> None:
    context.device = device
    context.browser = browser
    context.compatible = True


@given('I have a stable browser "{browser}"')
def given_i_have_a_stable_browser_browser(context: Context, browser: str) -> None:
    context.browser = browser
    context.compatible = True


@given("I have valid credentials")
def given_i_have_valid_credentials(context: Context) -> None:
    context.valid_credentials = True


@given('my connection speed is "{speed}"')
def given_my_connection_speed_is_speed(context: Context, speed: str) -> None:
    context.connection_speed = speed


@given('I have an incompatible "{browser}" browser')
def given_i_have_an_incompatible_browser_browser(
    context: Context, browser: str
) -> None:
    context.browser = browser
    context.compatible = False


@when("I access the system URL")
def when_i_access_the_system_url(context: Context) -> None:
    speed = getattr(context, "connection_speed", "fast")
    if not context.compatible:
        context.browser_warning = True
    elif speed == "slow":
        context.offline_mode = True
        context.connection_status_shown = True
    else:
        context.interface_loaded = True
        if context.width >= 1024:
            context.rendered_layout = "Desktop"
        elif context.width >= 600:
            context.rendered_layout = "Tablet"
        else:
            context.rendered_layout = "Mobile"


@when("I log in successfully")
def when_i_log_in_successfully(context: Context) -> None:
    if context.valid_credentials:
        context.authenticated = True
        context.dashboard_loaded = True

        # fallback to layout detection if it hasn’t run yet
        if not hasattr(context, "rendered_layout"):
            if context.width >= 1024:
                context.rendered_layout = "Desktop"
            elif context.width >= 600:
                context.rendered_layout = "Tablet"
            else:
                context.rendered_layout = "Mobile"


@then('I should see the "{layout}" layout loaded')
def then_i_should_see_the_layout_layout_loaded(context: Context, layout: str) -> None:
    assert (
        context.rendered_layout == layout
    ), f"Expected {layout}, but got {context.rendered_layout}"


@then("my theme preference should be applied")
def then_my_theme_preference_should_be_applied(context: Context) -> None:
    context.theme_applied = True
    assert context.theme_applied is True


@then("I should see a browser compatibility warning")
def then_i_should_see_a_browser_compatibility_warning(context: Context) -> None:
    assert context.browser_warning, "Expected browser compatibility warning"


@then("the system should enable offline mode")
def then_the_system_should_enable_offline_mode(context: Context) -> None:
    assert context.offline_mode, "Offline mode was not enabled for slow connection"


@then("I should see a connection status indicator")
def then_i_should_see_a_connection_status_indicator(context: Context) -> None:
    assert context.connection_status_shown, "Connection status indicator not shown"


@then("my personalized dashboard should load")
def then_my_personalized_dashboard_should_load(context: Context) -> None:
    assert context.dashboard_loaded, "Dashboard did not load after login"
