
#Find a average of 3 sections and tell which section is winner and highest average .


section1 =[12,31,45,67,89,54]
section2 = [45,34,25,78,54,89]
section3 = [56,54,34,65,43,57]

def calculate_avg_section(section1,section2,section3):

    section1_avg = sum(section1)/len(section1)
    print(section1_avg)


    section2_avg = sum(section2)/len(section2)
    print(section2_avg)

    section3_avg = sum(section3)/len(section3)
    print(section3_avg)

    if section1_avg >= section2_avg  and section1_avg >=section3_avg:
        print("section1 is greatest average")
        print("Highest average is section1 ",section1_avg)
    elif section2_avg >= section1_avg and section2_avg >= section3_avg:
        print("section2 is greatest average")
        print("Highest average is section2 ",section2_avg)
    else:
        print("section3 is greatest average")
        print("Highest average is section3 ",section3_avg)


calculate_avg_section(section1,section2,section3)



