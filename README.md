# Intelligent Placer

## Постановка задачи
Intelligent Placer - это программа для размещения обьектов внутри многоугольника.
- На вход программа получает путь к фотографии, на которой изображено произвольное количество объектов (от нуля до десяти) и многоугольник, нарисованный на белом листе бумаги (все объекты и многоугольник находятся на одной фотографии).
- Программа должна понять, поместятся ли объекты внутри многоугольника и закончить работу в течении 5 минут. Если программе удалось разместить объекты внутри многоугольника за отведенное время, то возвращать "true", в противном случае вернуть "false".
- Вывод ответа в стандартный поток вывода (консоль) 

### Требования к входным данным
#### К фотографиям:
- Фотографии в формате .jpg 
- Сняты при одинаковом освещении
- Сняты на одно устройство 
- Сняты на широкоугольную камеру не менее 10 мп
- Сьемка проводится на одной высоте и не должна привышать 50 см
- На фотографии не должно присутсвовать фильтров
- На фотографии должны отсутствовать блики и шумы 
- Фотографии должны быть цветные
- Фотографии не должны быть размытые 
- Устройство для сьемки должно распологаться перпендикулярно нормали к фотографируемой поверхности 

#### К объектам: 
- Объекты находятся в фокусе 
- Объекты полностью попадают в кадр
- Объекты не должны повторяться
- Объекты не должны накладываться друг на друга 
- Объекты не должны попадать на лист с многоугольником 
- Между объектами должно быть расстояние в 2 пикселя 

#### К поверхности:
- Светлая 
- Горизонтальная 
- Прямая 
- Однотонная. 
- Не должна совпадать с цветом листа.
- Поверхность на всех изображениях должна быть одна и та же.
- Поверхность должна быть достаточного размера, чтобы разместить лист и объекты.

#### К листу:
- Должен быть ровным.
- Должен быть белым.
- Должен быть квадратный или прямоугольный. 

### Требования к выходным данным: 
- Должен возвращать "true" или "false".
- Ответ должен быть получен в консоли.

### Требования к задаче
- Многоугольник должен быть закрытым.
- Многоугольник должен быть выпуклым.
- Многоугольник должен быть нарисован темным маркером. 
- Линии многоугольника должны иметь одинаковую толщину. 
- Количество граней многоугольника не должно превышать 7. 
- На фотографии должен находиться один многоугольник. 
- Если в жизни форму обьекта можно изменить, во время работы программы считать его статичным. 
Например:
  - цепочка
  - веревка 
  - ножницы
- Если какой-то объект внутри себя имеет отверстие, то это отверстие считается частью объекта и внутри него нельзя размещать другие объекты. 
- Объекты не должны касаться стенок многоугольника.
- Если многоугольник нарисован от руки, то программа должна считать его. 

### Данные 
- Набор данных и выбранную поверхность можно можно посмотреть в [data](https://github.com/Fourroubles/Intelligent-Placer/tree/develop/data)
- Набор данных с проверенными ответами, комментариями и необычными случаями можно посмотреть в [test](https://github.com/Fourroubles/Intelligent-Placer/blob/develop/test/description.md)

## План работы
Весь план разбит на несколько частей, каждый из которых будет выполняться друг за другом.

### Первая часть:
- Из цветного изображения сделать черно-белое.
- Бинаризация: Найти на изображении объекты и лист с многоугольником. 
- Применить морфологические операции для удаления патян с изображения. 
- С помощью детектора Канни найти границы изображения. 
- Научиться отличать лист от предметов. 


### Вторая часть 
Вторая часть будет направлена на работу с листом. 

- Проверить, является лист прямоугольным/квадратным, если нет, то вернуть false.
- Проверить, присутсвует ли на листе многоугольник, если нет, то вернуть false.
- Проверить, что на листе изображен только один многоугольник. 
- Определить количество граний многоугольника. Если количество граний меньше 3 и больше 8, то вернуть false. 
- Проверить, является многоугольник выпуклым, если нет то вернуть false. 
- Проверить, является ли многоугольник закрытым, если нет, то вернуть false
- Проверить, находится ли врнутри многоугольника какие-то ли или другие нарисованные обьекты, если да, то вернуть false.
- Определить кол-во пикселей в многоугольнике. 

### Третья часть часть 
Третья часть будет направлена на работу с объектами. 

- Научиться находить каждый объект.
- Определить количество обьектов на изображении. 
- Определить количество пикселей каждого изображения.
- Определить количество пикселей на границе каждого объекта. Сумму пикслей на границе умножить на 3. Это нужно для того, чтобы расстояние между объектами были 2 пикселя. 
- Посчитать сумму пикселей объкта с суммой полученной в предыдущем пункте. В дальнейшем такая сумма будет называться "Общая сумма пикселей обьекта".
- Сложить все общие суммы пикселей обьектов.
- Научиться, поворачивать объекты. 

### Четвертая часть часть 
- Отсортировать все объекты по общей суммы пикселей обьектов. Для того, чтобы разместить сначала самы большой объект. 
- Сравнить количества суммы пикселей объектов с количеством пикселей многоугольника. Если количество пикселей объектов превышает или равно количеству пикселей многоугольника, то вернуть false. 
- Поочередно начинаем перетаскивать объекты в многоугольник. 
  - Выставляем первый объект. 
  - Выставлем следующий объект из отсортируемого списка. 
  - Если обьект не помешается то поворачиваем его на 1 градус вправо. 
    - Если объект не поместился, то возвращаемся на шаг назад. 
    - Если объект поместился то переходим ко 2 пункту.
    - Если объект не поместился после проделанных предыдущих операций, то возвращаемся на один объект назад и поворачиваем его на 1 градус и переходим к пункту 2. 
  - Если получилось разместить все объекты то возвращем true, если нет, то возвращаем false. 
