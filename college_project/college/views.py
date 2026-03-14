from django.shortcuts import render

# Create your views here.


courses = {
"btech":[
"Computer Science Engineering",
"Electronics & Communication",
"Electrical Engineering",
"Mechanical Engineering",
"Civil Engineering",
"AI & Data Science"
],

"mba":[
"Finance",
"Marketing",
"Human Resource",
"Business Analytics"
],

"diploma":[
"Mechanical",
"Civil",
"Electrical",
"Computer Engineering"
],

"pharmacy":[
"B.Pharmacy",
"D.Pharmacy",
"M.Pharmacy"
]
}

course_names={
"btech":"B.Tech",
"mba":"MBA",
"diploma":"Diploma",
"pharmacy":"Pharmacy"
}

def index(request):
    return render(request,"index.html",{"course_names":course_names})

def branches(request,course):

    branch_list = courses.get(course)
    title = course_names.get(course)

    other_courses={
        key:value for key,value in course_names.items() if key!=course
    }

    return render(request,"branches.html",{
        "branches":branch_list,
        "title":title,
        "course":course,
        "other_courses":other_courses
    })