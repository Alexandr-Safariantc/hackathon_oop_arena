<a name="readme-top"></a>
<!-- PROJECT LOGO -->
<div align='center'>
  <a href="https://www.python.org/" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/python-colored.svg" height="95" alt="Python">
  </a>
  <a>
    <img src="https://cdn.pixabay.com/photo/2014/04/03/10/01/coliseum-309629_1280.png" height="100" alt="Arena" hspace="10">
  </a>
  </a>
  <a>
    <img src="https://cdn.pixabay.com/photo/2016/10/26/14/29/gladiator-1771625_1280.png" height="120" alt="Gladiator" hspace="0">
  </a>

<h3 align="center">Игра Арена</h3>

  <p align="center">
    Консольная игра о гладиаторах, выполненная в рамках хакатона
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Оглавление</summary>
  <ol>
    <li>
      <a href="#Общее-об-игре">Общее об игре</a>
    </li>
    <li>
      <a href="#Технологии">Технологии</a>
    </li>
    <li>
      <a href="#Описание-игры">Описание игры</a>
      <ul>
        <li><a href="#Игровые-объекты">Игровые объекты</a></li>
        <li><a href="#Алгоритм-проведения-боя">Алгоритм проведения боя</a></li>
        <li><a href="#ВАЖНО">ВАЖНО!!!</a></li>
      </ul>
    </li>
    <li><a href="#Контакты">Контакты</a></li>
  </ol>
</details>


## Общее об игре

> *время на выполнение задания - 2 часа*

Мини-игра арена, на которую добавляются персонажи и сражаются между собой. Игра определяет победителя в консоли.

Для запуска вам потребуется только среда разработки, через которую можно запускать код для выполнения.

## Технологии

![](https://img.shields.io/badge/python-3.9.19-blue)

## Описание игры

### *Игровые объекты*

- **Вещи**: `class Thing`
Класс содержит в себе следующие параметры - **название, процент защиты, атаку и жизнь**. Параметры защиты, атаки и очков жизни принимают значения **не более 0,1** и явлюятся множителями к базовым характеристикам персонажей;

- **Персонажи**: `class Person` 
Класс, содержащий в себе:

    - **базовые значения** параметров защиты, атаки и очков жизни;

    - метод `set_things`, присваивающий каждому персонажу случайное количество (от 1 до 4) магических вещей;

    - метод `set_final_characteristics`, рассчитывающий характеристики персонажа с учетом множителей от присвоенных магических вещей;

    - метод `get_recieving_damage`, рассчитывающий урон от входной атаки;

    - метод `decrease_hit_points` вычитания жизни на основе входной атаки, а также методы для выполнения алгоритма, представленного ниже;

    - классы персонажей:

        - **Паладин** (наследник класса Person): `class Paladin`
        Базовые значения **жизни и процента защиты умножается на 2**;

        - **Воин** (наследник класса Person): `class Warrior`
        Базовое значение **атаки умножается на 2**.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### *Алгоритм проведения боя*

> *Скучные подробности (куда интереснее просто запустить игру)*

1. Создание необходимого количества вещей;

2. Создание 10 персонажей (среди них воины и паладины) с именами из созданного списка;

3. Отправление персонажей на арену *(добавление в список)*;

4. Распределение магических вещей персонажам;

5. Расчет характеристик персонажей с учетом полученных вещей;

6. Случайный выбор *(извлечение из списка)* пары Нападающий и Защищающийся;

    - У Защищающегося вызывается метод вычитания жизни на основе атаки Нападающего.

7. Вывод информации о результате атаки в консоль;

8. Возврат атакующего в список персонажей;

9. Проверка на то был ли удар *летальным* для защищающегося. В случае, если у защищающегося количество жизни меньше 0, выводится сообщение о его кончине, иначе он возвращается в список персонажей;

10. Игра заканчивается, когда остается лишь один персонаж в списке персонажей.

### **ВАЖНО!!!**

> Не забывайте о веселье

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Контакты

**Александр Сафарьянц** Backend developer

[![Gmail Badge](https://img.shields.io/badge/-safariantc.aa@gmail.com-c14438?style=flat&logo=Gmail&logoColor=white&link=mailto:safariantc.aa@gmail.com)](mailto:safariantc.aa@gmail.com)<p align='left'>

<p align="right">(<a href="#readme-top">back to top</a>)</p>