Feature: Tests for Wiki search

    Scenario: User can search and correct result is shown
        Given Tap on search field
        When Enter Python to search field
        Then Top Result for Python is shown