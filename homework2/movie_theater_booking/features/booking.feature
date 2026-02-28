Feature: Booking pages
  As a User
  I want to be able to visit each page properly
  So I can view all the pages

  Scenario: User views movies page
    Given I am on the movies page
    Then I should see "The Batman"
  
  Scenario: User views home page
    Given I am on the home page
    Then I should see "Movies"

  Scenario: User views showings page for showing 1
    Given I am on the showings page
    Then I should see "Mountain Time"

  Scenario: User views seats page for showing 3
    Given I am on the seats page
    Then I should see "B3"
  
  Scenario: Logged out user redirected from booking history
    Given I am not logged in
    When I visit my booking history page
    Then I should be redirected to the login page

  Scenario: Logged out user redirected when booking a seat
    Given there is an available seat for the behave movie
    And I am not logged in
    When I try to book that seat
    Then I should be redirected to the login page

  Scenario: Logged in user can book a seat
    Given there is an available seat for the behave movie
    And I am logged in as a user
    When I try to book that seat
    Then the seat should be marked booked
    And a booking should exist for that user and seat