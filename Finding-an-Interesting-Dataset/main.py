import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

student_performance_data = pandas.read_csv("student_data.csv")

print(student_performance_data)