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
        "teacher_name": "楊千萱",
        "teacher_email": "qooqlecpt@gmail.com"
    }
    response = requests.post("http://127.0.0.1:5000/teachers", json=new_teacher)
    assert response.status_code == 201
    
def test_update_course():
    updated_course = {
    "courseId": 1,
    "course_title": "投資學",
    "location": "大仁樓 101",
    "start_time": "0900",
    "end_time": "1100",
    "syllabus": "學習如何投資",
    "teacher_name": "楊千萱",
    "teacher_email": "qooqlecpt@gmail.com"
    }
    response = requests.put("http://127.0.0.1:5000/courses/1", json=updated_course)
    assert response.status_code == 200