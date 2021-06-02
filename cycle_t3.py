students_scores = [
    {'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '4b', 'scores': [5,5,5,5,3,3,3]},
    {'school_class': '4c', 'scores': [3,2,2,1,2,5]}
]
school_sum = 0
school_all = 0
for x in students_scores:
    class_sum = 0
    for score in x["scores"]:
        class_sum += score
        #print(class_sum)
    scores_avg = class_sum/len(x["scores"])
    print(x["school_class"]+' '+str(round(scores_avg,2)))
    school_sum += class_sum
    school_all += len(x["scores"])
school_avg = school_sum/school_all
print(round(school_avg,2))


