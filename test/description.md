# Тестовые данные

## Набор тестов 
Тестовые данные были подобраны такие, чтобы показать корректность работы программы.

### Первый тест 
Проверяет присутсвуеют ли объекты на фотографии и изображен ли многоугольник. 
![test 1](https://github.com/Fourroubles/Intelligent-Placer/blob/develop/test/images/1.jpg)

Ответ: false

### Второй тест 
Пытаемся размести объект в несуществующий многоугольник. 
![test 2](https://github.com/Fourroubles/Intelligent-Placer/blob/develop/test/images/2.jpg)

Ответ: false

### Третий тест 
На фотографии отсутствуют обьекты, но присутсвует многоугольник. Так как нет обьектов для размещения, то программа работает корректно. 
![test 3](https://github.com/Fourroubles/Intelligent-Placer/blob/develop/test/images/3.jpg)

Ответ: true

### Четвертый тест 
На фотографии изображен мноугольник с 8 гранями. По условию задания количество граней не должно привышать 7. 
![test 4](https://github.com/Fourroubles/Intelligent-Placer/blob/develop/test/images/4.jpg)

Ответ: false

### Пятый тест 
На фотографии изображено два мноугольника. По условию задания должен быть изображен только один многоугольник.
![test 5](https://github.com/Fourroubles/Intelligent-Placer/blob/develop/test/images/5.jpg)

Ответ: false

### Шестой тест 
На фотографии изображен не выпуклый многоугольник. По условию задания он должен быть выпуклым. 
![test 6](https://github.com/Fourroubles/Intelligent-Placer/blob/develop/test/images/6.jpg)

Ответ: false

### Седьмой тест 
На фотографии изображен незакрытый многоугольник. По условию задания он должен быть закрытым.  
![test 7](https://github.com/Fourroubles/Intelligent-Placer/blob/develop/test/images/7.jpg)

Ответ: false

### Восьмой тест 
Внутри многоугольника присутсвуют лишнии линии. По условию задания внутри мноугольника ничего не должно быть изображенно.   
![test 8](https://github.com/Fourroubles/Intelligent-Placer/blob/develop/test/images/8.jpg)

Ответ: false

### Девятый тест 
Многоульник нарисован от руки. Программа должна корректно считывать такие многоугольники.   
![test 9](https://github.com/Fourroubles/Intelligent-Placer/blob/develop/test/images/9.jpg)

Ответ: true

### Десятый тест
Объект небольшого размера должен разместиться внутри большого многоугоьника. 
![test 10](https://github.com/Fourroubles/Intelligent-Placer/blob/develop/test/images/10.jpg)

Ответ: true

### Одинадцатый тест
Объект помещается под одним углом и однозначно. 
![test 11](https://github.com/Fourroubles/Intelligent-Placer/blob/develop/test/images/11.jpg)

Ответ: true

### Двенадцатый тест
Объект большого размера не может поместиться внутри маленького многоугольника. 
![test 12](https://github.com/Fourroubles/Intelligent-Placer/blob/develop/test/images/12.jpg)

Ответ: false

### Тринадцатый тест
Для того, чтобы обьект разместился его надо повернуть.  
![test 13](https://github.com/Fourroubles/Intelligent-Placer/blob/develop/test/images/13.jpg)

Ответ: true

### Четырнадцатый тест
Объект помещается в многоугольник. 
![test 14](https://github.com/Fourroubles/Intelligent-Placer/blob/develop/test/images/14.jpg)

Ответ: true

### Пятнадцатый тест
Данный тест проводится после теста номер 15. Тот же самый объект не может поместиться в немного меньший многоугольник, который визуально похож на многоугольник из 15 теста.   
![test 15](https://github.com/Fourroubles/Intelligent-Placer/blob/develop/test/images/15.jpg)

Ответ: false

### Шестнадцатый тест
Маленький объект размешается внутри маленького многоугольника.  
![test 16](https://github.com/Fourroubles/Intelligent-Placer/blob/develop/test/images/16.jpg)

Ответ: true

### Семнадцатый тест
Два обьекта не могут поместиться внутри мальенького многоуугольника. 
![test 17](https://github.com/Fourroubles/Intelligent-Placer/blob/develop/test/images/17.jpg)

Ответ: false

### Восемнадцатый тест
Два выпуклых обьекта помешаются внутри многоугольника. 
![test 18](https://github.com/Fourroubles/Intelligent-Placer/blob/develop/test/images/18.jpg)

Ответ: true

### Девятнадцатый тест
На первый взгляд, кажется, что обьекты не помещаются, но на самом деле их можно разместить.  
![test 19](https://github.com/Fourroubles/Intelligent-Placer/blob/develop/test/images/19.jpg)

Ответ: true

### Двадцатый тест
Три обьекта помещаются внутри многоугольника.   
![test 20](https://github.com/Fourroubles/Intelligent-Placer/blob/develop/test/images/20.jpg)

Ответ: true

### Двадцать первый тест
Объект задевает границы многоугольника снизу и сверху. По условию задания объект не должен касаться границ.   
![test 21](https://github.com/Fourroubles/Intelligent-Placer/blob/develop/test/images/21.jpg)

Ответ: false

### Двадцать второй тест
Все обьекты размещены внутри многоугольника.   
![test 22](https://github.com/Fourroubles/Intelligent-Placer/blob/develop/test/images/22.jpg)

Ответ: true

### Двадцать третий тест
Все обьекты размещены внутри многоугольника меньшего размера.   
![test 23](https://github.com/Fourroubles/Intelligent-Placer/blob/develop/test/images/23.jpg)

Ответ: true
