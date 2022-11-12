import pandas as pd
import matplotlib.pyplot as pt

#load csv

students_data_df = pd.read_csv("the-hello-dataset-fa22.csv")
print(f"The head of dataset is: {students_data_df.head()}")

#correcting colors
students_data_df['FavoriteColor'] = students_data_df['FavoriteColor'].str.lower()

#load the students who name starts with H

students_with_h = students_data_df[students_data_df.Name.str.startswith('H')]
print(students_with_h)

#print the total number of students who have a three words name (first-middle-surname).
student_names = students_data_df['Name'].tolist()
logic_list = [name.strip() for name in student_names if len(name.strip().replace("  "," ").split(" ")) == 3]
student_len_w_three_words = len(logic_list)
print(logic_list)
print(f"The length of students with three words is : {student_len_w_three_words}")

#print the percentage of students who have a CGPA of 3.0 or above.

students_with_cgpa_gt_3 = students_data_df[students_data_df.CGPA > 3.0]
print(students_with_cgpa_gt_3)

#plot a pie chart to show the ratio of male and female students.
male_female_ratio_df = students_data_df['Gender'].tolist()
ratio_list = [male_female_ratio_df.count("Male"), male_female_ratio_df.count("Female")]
pt.pie(ratio_list,labels=["Male","Female"],autopct="%1.1f%%")
pt.show()

# # Plot the CGPA of all male students on a histogram with intervals 2.0-2.5, 2.6-3.0, 3.1-3.5, 3.6-4.0
male_students_df = students_data_df[students_data_df.Gender.str.startswith('M')]
male_students_cgpa_df = male_students_df["CGPA"].tolist()
pt.hist(male_students_cgpa_df, bins=[2.0,2.5,3.0,3.5,4.0])
pt.show()

# plot the HSSC-1 marks of all male vs female students on a scatter plot.
pt.scatter(students_data_df['HSSC-1'],students_data_df["Gender"],color="red")
pt.show()

# plot the favorite colors of male vs female students on a bar chart.

pt.bar(male_students_df["FavoriteColor"].unique(),male_students_df["FavoriteColor"].value_counts())
pt.show()

female_students_df = students_data_df[students_data_df.Gender.str.startswith('F')]
pt.bar(female_students_df["FavoriteColor"].unique(),female_students_df["FavoriteColor"].value_counts())
pt.show()

#plot line chart of students and their birth months
pt.plot(students_data_df["BirthMonth"].unique(),students_data_df["BirthMonth"].value_counts())
pt.show()

#create a correlation matrix between HSSC-1 and HSSC-2 marks and then plot on a heatmap.
corr_bw_hssc1_hssc2 = students_data_df[["HSSC-1","HSSC-2"]].corr()
pt.imshow(corr_bw_hssc1_hssc2,cmap="YlGnBu",interpolation="nearest")
pt.show()