import requests

def test_get_courses():
    response = requests.get("http://127.0.0.1:5000/courses")
    assert response.status_code == 200
    courses = response.json()
    assert isinstance(courses, list)
    for course in courses:
        assert 'courseId' in course
        assert 'course_title' in course
        assert 'location' in course
        assert 'start_time' in course
        assert 'end_time' in course
        assert 'syllabus' in course
        assert 'teacher_name' in course
        assert 'teacher_email' in course


def test_create_teacher():
    new_teacher = {
        "teacher_id": 1,
        "teacher_name": "Chris Yang",
        "teacher_email": "qooqlecp@gmail.com"
    }
    response = requests.post("http://127.0.0.1:5000/teachers", json=new_teacher)
    assert response.status_code == 201
    data = response.json()
    
    assert 'teacher' in data
    teacher_data = data['teacher']
    assert 'teacher_id' in teacher_data and isinstance(teacher_data['teacher_id'], int), 'teacher_id must be an int'
    assert 'teacher_name' in teacher_data and isinstance(teacher_data['teacher_name'], str), 'teacher_name must be an str'
    assert 'teacher_email' in teacher_data and isinstance(teacher_data['teacher_email'], str), 'teacher_email must be an str'
    
def test_update_course():
    updated_course = {
    "courseId": 1,
    "course_title": "投資學",
    "location": "大仁樓 101",
    "start_time": "0900",
    "end_time": "1100",
    "syllabus": "學習如何投資",
    "teacher_name": "Chris Yang",
    "teacher_email": "qooqlecp@gmail.com"
    }
    response = requests.put("http://127.0.0.1:5000/courses/1", json=updated_course)
    assert response.status_code == 200
    data = response.json()
    assert 'course' in data
    course_data = data['course']
    assert 'courseId' in course_data and isinstance(course_data['courseId'], int), 'courseId must be an int'
    assert 'course_title' in course_data and isinstance(course_data['course_title'], str), 'course_title must be an str'
    assert 'location' in course_data and isinstance(course_data['location'], str), 'location must be an str'
    assert 'start_time' in course_data and isinstance(course_data['start_time'], str), 'start_time must be an str'
    assert 'end_time' in course_data and isinstance(course_data['end_time'], str), 'end_time must be an str'
    assert 'syllabus' in course_data and isinstance(course_data['syllabus'], str), 'syllabus must be an str'
    assert 'teacher_name' in course_data and isinstance(course_data['teacher_name'], str), 'teacher_name must be an str'
    assert 'teacher_email' in course_data and isinstance(course_data['teacher_email'], str), 'teacher_email must be an str'