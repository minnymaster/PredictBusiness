document.getElementById('analysisForm').addEventListener('submit', function(e) {
    e.preventDefault(); // Предотвращаем отправку формы

    // Собираем данные из формы
    let gpa = document.getElementById('gpa').value;
    let universityGPA = document.getElementById('universityGPA').value;
    let satisfaction = document.getElementById('satisfaction').value;
    let internships = document.getElementById('internships').value;
    let projects = document.getElementById('projects').value;
    let skills = document.getElementById('skills').value;
    let networking = document.getElementById('networking').value;

    // Валидация данных перед отправкой
    let errorMessages = [];

    if (gpa === '' || gpa < 0 || gpa > 5) errorMessages.push('Средний балл в старшей школе (GPA) должен быть от 0 до 5.');
    if (universityGPA === '' || universityGPA < 0 || universityGPA > 5) errorMessages.push('Средний балл в университете (University GPA) должен быть от 0 до 5.');
    if (satisfaction === '') errorMessages.push('Пожалуйста, выберите удовлетворенность карьерой.');
    if (internships === '' || internships < 0) errorMessages.push('Количество завершенных стажировок не может быть отрицательным.');
    if (projects === '' || projects < 0) errorMessages.push('Количество завершенных проектов не может быть отрицательным.');
    if (skills === '' || skills < 0 || skills > 10) errorMessages.push('Оценка мягких навыков должна быть от 0 до 10.');
    if (networking === '' || networking < 0 || networking > 10) errorMessages.push('Оценка сетевого взаимодействия должна быть от 0 до 10.');

    // Если есть ошибки, показываем их и не отправляем форму
    if (errorMessages.length > 0) {
        alert(errorMessages.join('\n'));
        return;
    }

    // Подготовка данных для отправки на сервер
    let data = {
        gpa: gpa,
        universityGPA: universityGPA,
        satisfaction: satisfaction,
        internships: internships,
        projects: projects,
        skills: skills,
        networking: networking
    };

    // Отправка данных через AJAX
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "your_backend_endpoint", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onload = function() {
        if (xhr.status == 200) {
            // Выводим результат
            let response = JSON.parse(xhr.responseText);
            document.getElementById('resultText').innerText = `Предпринимательский потенциал: ${response.result}`;
        } else {
            alert('Ошибка при отправке данных.');
        }
    };
    xhr.send(JSON.stringify(data));
});
