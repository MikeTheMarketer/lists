my_list = [34, 56, 76, 45, 2, 12, 67, 98, 37, 54, 66]

sorted_list = my_list.copy()

sorted_list.sort()
print(sorted_list, "\n")

sum_lowest = sorted_list[0] + sorted_list[1]
sum_highest = sorted_list[9] + sorted_list[10]

print(sum_lowest)
print(sum_highest, "\n")

names = ["David", "Michael", "John", "James", "Greg", "Mark", "William", "Richard", "Thomas", "Steven", "Mary", "Susan", "Maria", "Karen", "Lisa", "Linda", "Donna", "Patricia", "Debra"]

scores = [99, 87, 78, 86, 68, 94, 76, 97, 56, 98, 76, 87, 79, 90, 73, 93, 82, 69, 97, 98]

test_example = input("Please enter student first name: ")
example_index = names.index(test_example)

grade_check = scores[example_index]
print("Your score is: ", grade_check, "\n")

one = []
for score in scores:
  one.append(score)
  
print("The maximum score is: ", max(one))
print(scores.count(99), "student scored", max(one), "\n")


month_and_years = [['January', 31], ['February', 28], ['March', 31], ['April', 30], ['May', 31], ['June', 30], ['July', 31], ['August', 31], ['September', 30], ['October', 31], ['November', 30], ['December', 31]]
spring = month_and_years[0:3]
fall = month_and_years[9:12]
summer = month_and_years[5:8]
winter = month_and_years[11 + 0:3]

summer_season_length = summer[0][1] + summer[1][1] + summer[2][1]
print(summer_season_length, "\n")