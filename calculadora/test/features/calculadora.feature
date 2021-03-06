Feature: Compute factorial
	In order to play with Lettuce As beginners We’ll implement factorial

Scenario: Calculator of sum
	Given I have the number 3 and 5
	When I compute its plus
	Then I see the number 8
Scenario: Calculator of sum
	Given I have the number 10 and 15
	When I compute its plus
	Then I see the number 25
Scenario: Calculator of sum
	Given I have the number 39 and 25
	When I compute its plus
	Then I see the number 64

Scenario: Calculator of subtraction
	Given I have the number "-10" and "25"
	When I compute its subtraction
	Then I see the number "-35"
Scenario: Calculator of subtraction
	Given I have the number 15 and 67
	When I compute its subtraction
	Then I see the number "-52"
Scenario: Calculator of subtraction
	Given I have the number 100 and 34
	When I compute its subtraction
	Then I see the number 66

Scenario: Calculator of multiplication
	Given I have the number "3.5" and "9"
	When I compute its multiplication
	Then I see the number "31.5"
Scenario: Calculator of multiplication
	Given I have the number 100 and 34
	When I compute its multiplication
	Then I see the number 3400
Scenario: Calculator of multiplication
	Given I have the number 13 and 3
	When I compute its multiplication
	Then I see the number 39

Scenario: Calculator of division
	Given I have the number 100 and 5
	When I compute its division
	Then I see the number "20"
Scenario: Calculator of division
	Given I have the number 10 and 10
	When I compute its division
	Then I see the number 1
Scenario: Calculator of division
	Given I have the number "-34" and "2"
	When I compute its division
	Then I see the number "-17"
