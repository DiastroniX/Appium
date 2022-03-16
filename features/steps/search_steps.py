from behave import given, when, then

@given("Tap on search field")
def tap_search(context):
    context.app.main_screen.click_search()

@when("Enter {search_phrase} to search field")
def input_search(context, search_phrase):
    context.app.search_screen.input_search(search_phrase)

@then ("Top Result for {search_phrase} is shown")
def verify_search_result(context, search_phrase):
    context.app.search_screen.verify_search_result(search_phrase)
