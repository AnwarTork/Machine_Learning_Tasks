from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# قائمة الطلاب (مع id)
students = [
    {"id": 1, "name": "أحمد", "age": 22, "major": "علوم حاسوب"},
    {"id": 2, "name": "سارة", "age": 20, "major": "هندسة كهربائية"},
    {"id": 3, "name": "محمد", "age": 23, "major": "إدارة أعمال"},
    {"id": 4, "name": "ليلى", "age": 21, "major": "تصميم داخلي"},
    {"id": 5, "name": "خالد", "age": 24, "major": "طب بشري"}
]

# مولد ال id
next_id = 6

# -------------------------------
# READ: عرض جميع الطلاب
# -------------------------------
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# -------------------------------
# READ: عرض طالب واحد حسب ID
# -------------------------------
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if student is None:
        abort(404)  # إذا لم يوجد الطالب
    return jsonify(student)

# -------------------------------
# CREATE: إضافة طالب جديد
# -------------------------------
@app.route('/students', methods=['POST'])
def add_student():
    global next_id
    new_student = request.get_json()
    
    # تأكد من أن المدخلات صحيحة
    required_fields = ['name', 'age', 'major']
    if not all(field in new_student for field in required_fields):
        abort(400)  # Bad Request
    
    new_student['id'] = next_id
    next_id += 1
    students.append(new_student)
    return jsonify(new_student), 201  # Created

# -------------------------------
# UPDATE: تعديل بيانات طالب
# -------------------------------
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if student is None:
        abort(404)

    data = request.get_json()
    required_fields = ['name', 'age', 'major']
    if not all(field in data for field in required_fields):
        abort(400)

    student.update(data)
    return jsonify(student)

# -------------------------------
# DELETE: حذف طالب
# -------------------------------
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    student = next((s for s in students if s['id'] == student_id), None)
    if student is None:
        abort(404)

    students = [s for s in students if s['id'] != student_id]
    return jsonify({"message": "Student deleted successfully"})

# تشغيل السيرفر
if __name__ == '__main__':
    app.run(debug=True)