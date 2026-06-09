#!/usr/bin/env python3
"""
Генератор трёх UML-диаграмм в формате PlantUML.
Запуск: python3 generate_plantuml.py
Результат: uml_entities.puml, uml_data.puml, uml_gui.puml

Как получить PNG:
  1. Открыть https://www.plantuml.com/plantuml/uml/
  2. Скопировать содержимое .puml файла в текстовое поле
  3. Нажать Submit → скачать PNG
Или командой (если установлен plantuml):
  plantuml uml_entities.puml uml_data.puml uml_gui.puml
"""

# ============================================================
# Диаграмма 1: Сущности (entities)
# ============================================================

ENTITIES_PUML = """@startuml
skinparam classAttributeIconSize 0
skinparam class {
    BorderColor #82b366
    BackgroundColor #d5e8d4
}
skinparam packageStyle rectangle

class general {
    - __code : int
    - __name : str
    --
    + setCode(value)
    + setName(value)
    + getCode() : int
    + getName() : str
}

class department {
    - __employees : int
    --
    + setEmployees(value)
    + getEmployees() : int
}

class expensetype {
    - __description : str
    - __limit : float
    --
    + setDescription(value)
    + getDescription() : str
    + setLimit(value)
    + getLimit() : float
}

class expense {
    - __expensetype : expensetype
    - __department : department
    - __amount : float
    - __date : str
    --
    + setExpenseType(value)
    + getExpenseType() : expensetype
    + getExpenseTypeCode() : int
    + getExpenseTypeName() : str
    + setDepartment(value)
    + getDepartment() : department
    + getDepartmentCode() : int
    + getDepartmentName() : str
    + setAmount(value)
    + getAmount() : float
    + setDate(value)
    + getDate() : str
}

general <|-- department
general <|-- expensetype
general <|-- expense

expense o-- department : агрегация
expense o-- expensetype : агрегация

note bottom of expense
  Расход связывает Вид расхода
  и Отдел через агрегацию.
  Все три сущности наследуют
  code и name от general.
end note

@enduml
"""

# ============================================================
# Диаграмма 2: Слой данных (data layer)
# ============================================================

DATA_PUML = """@startuml
skinparam classAttributeIconSize 0
skinparam class {
    BorderColor #82b366
    BackgroundColor #d5e8d4
}
skinparam package {
    BorderColor #6c8ebf
    BackgroundColor #dae8fc
}
skinparam note {
    BorderColor #d6b656
    BackgroundColor #fff2cc
}

package "Слой данных" {

    class generalList {
        - __list : list
        --
        + clear()
        + findByCode(code)
        + getNewCode() : int
        + getCodes() : list
        + getItems() : list
        + appendItem(value)
        + removeItem(value)
    }

    class departmentList {
        --
        + appendItem(value)
        + createItem(code, name, employees) : department
        + newItem(name, employees) : department
    }

    class expensetypeList {
        --
        + appendItem(value)
        + createItem(code, name, desc, limit) : expensetype
        + newItem(name, desc, limit) : expensetype
    }

    class expenseList {
        --
        + appendItem(value)
        + createItem(code, name, exptype, dept, amount, date) : expense
        + newItem(name, exptype, dept, amount, date) : expense
    }

    class rowCode {
        - __list : list
        --
        + clear()
        + appendRowCode(row, code)
        + updateRow(row)
        + removeRow(row)
        + removeCode(code)
        + getCode(row) : int
        + getCodes() : list
        + getRow(code) : int
    }

    generalList <|-- departmentList
    generalList <|-- expensetypeList
    generalList <|-- expenseList
}

package "Управляющий класс" {
    class accounting {
        - __departmentList : departmentList
        - __expensetypeList : expensetypeList
        - __expenseList : expenseList
        --
        + clear()
        + createDepartment(code, name, employees) : department
        + newDepartment(name, employees) : department
        + removeDepartment(code)
        + getDepartment(code) : department
        + getDepartmentList() : list
        + getDepartmentCodes() : list
        + createExpenseType(code, name, desc, limit) : expensetype
        + newExpenseType(name, desc, limit) : expensetype
        + removeExpenseType(code)
        + getExpenseType(code) : expensetype
        + getExpenseTypeList() : list
        + getExpenseTypeCodes() : list
        + createExpense(...) : expense
        + newExpense(...) : expense
        + removeExpense(code)
        + getExpense(code) : expense
        + getExpenseList() : list
        + getExpenseCodes() : list
    }
}

package "Сериализация" {
    class data {
        - __lib : accounting
        - __inp : str
        - __out : str
        --
        + setLib(value)
        + setInp(value)
        + setOut(value)
        + getLib() : accounting
        + getInp() : str
        + getOut() : str
        + readFile(lib, filename)
        + writeFile(lib, filename)
        + read()
        + write()
    }

    class dataxml {
        --
        + read()
        + write()
    }

    data <|-- dataxml
}

accounting o-- departmentList
accounting o-- expensetypeList
accounting o-- expenseList

dataxml --> accounting : читает/пишет

note right of dataxml
  read(): парсит XML, создаёт
  объекты через accounting,
  восстанавливает связи по кодам.
  write(): сериализует все
  объекты в XML с отступами.
end note

@enduml
"""

# ============================================================
# Диаграмма 3: GUI (графический интерфейс)
# ============================================================

GUI_PUML = """@startuml
skinparam classAttributeIconSize 0
skinparam class {
    BorderColor #82b366
    BackgroundColor #d5e8d4
}
skinparam package {
    BorderColor #6c8ebf
    BackgroundColor #dae8fc
}

package "Базовые виджеты" {

    class libWidget <<mixin>> {
        - __library : accounting
        --
        + getLibrary() : accounting
    }

    class dbTableWidget {
        - __rowCode : rowCode
        --
        + setHeader(value)
        + clearContents()
        + getCodes() : list
        + getCurrentCode() : int
        + setCurrentCode(code)
        + appendRowCode(row, code)
        + update(code)
        + setData()
    }

    class dbComboBox {
        - __rowCode : rowCode
        --
        + clear()
        + addItem(code, text)
        + removeItem(index)
        + getCurrentCode() : int
        + setCurrentCode(code)
        + setCurrentRec(value)
        + getCurrentRec()
        + update()
    }

    class editForm {
        - __grid : QGridLayout
        - __vbox : QVBoxLayout
        - __hbox : QHBoxLayout
        - __currentCode : int
        --
        + addLabel(text, x, y)
        + addNewWidget(widget, x, y)
        + addLeftLayout(layout)
        + setCurrentCode(value)
        + getCurrentCode() : int
        + update()
        + newClick()
        + editClick()
        + delClick()
    }

    class page {
        - __table : dbTableWidget
        - __form : editForm
        - __newButton : QPushButton
        - __editButton : QPushButton
        - __delButton : QPushButton
        --
        + setTable(value)
        + setForm(value)
        + newClick()
        + editClick()
        + delClick()
        + tableClick()
        + setConnect()
        + update()
    }
}

package "Таблицы" {
    class departmentsTable {
        --
        + setData()
    }
    class expensetypesTable {
        --
        + setData()
    }
    class expensesTable {
        --
        + setData()
    }
}

package "Комбо-боксы" {
    class departmentCombo {
        --
        + update()
    }
    class expensetypeCombo {
        --
        + update()
    }
}

package "Формы редактирования" {
    class departmentEditForm {
        - __nameEdit : QLineEdit
        - __employeesSpin : QSpinBox
        --
        + update()
        + newClick()
        + editClick()
        + delClick()
    }
    class expensetypeEditForm {
        - __nameEdit : QLineEdit
        - __descriptionEdit : QLineEdit
        - __limitSpin : QDoubleSpinBox
        --
        + update()
        + newClick()
        + editClick()
        + delClick()
    }
    class expenseEditForm {
        - __expensetypeCombo : expensetypeCombo
        - __departmentCombo : departmentCombo
        - __amountSpin : QDoubleSpinBox
        - __dateEdit : QDateEdit
        --
        + update()
        + newClick()
        + editClick()
        + delClick()
    }
}

package "Страницы" {
    class departmentPage {
        --
        + setTable()
        + setForm()
        + setConnect()
    }
    class expensetypePage {
        --
        + setTable()
        + setForm()
        + setConnect()
    }
    class expensePage {
        --
        + setTable()
        + setForm()
        + setConnect()
    }
}

package "Главное окно" {
    class tabWidget {
        - __departmentPage : departmentPage
        - __expensetypePage : expensetypePage
        - __expensePage : expensePage
        --
        + update()
    }
    class mainWindow {
        - __accounting : accounting
        - dataxml : dataxml
        - tabWidget : tabWidget
        - new : QAction
        - openxml : QAction
        - savexml : QAction
        --
        + newAction()
        + openXMLAction()
        + saveXMLAction()
    }
}

' Наследования
QTableWidget <|-- dbTableWidget
QComboBox <|-- dbComboBox
QWidget <|-- editForm
QWidget <|-- page
QTabWidget <|-- tabWidget
QMainWindow <|-- mainWindow

dbTableWidget <|-- departmentsTable
dbTableWidget <|-- expensetypesTable
dbTableWidget <|-- expensesTable

dbComboBox <|-- departmentCombo
dbComboBox <|-- expensetypeCombo

editForm <|-- departmentEditForm
editForm <|-- expensetypeEditForm
editForm <|-- expenseEditForm

page <|-- departmentPage
page <|-- expensetypePage
page <|-- expensePage

' Примеси
dbTableWidget ..|> libWidget
dbComboBox ..|> libWidget
editForm ..|> libWidget
page ..|> libWidget

' Композиции
departmentPage *-- departmentsTable
departmentPage *-- departmentEditForm
expensetypePage *-- expensetypesTable
expensetypePage *-- expensetypeEditForm
expensePage *-- expensesTable
expensePage *-- expenseEditForm

expenseEditForm --> departmentCombo : использует
expenseEditForm --> expensetypeCombo : использует

tabWidget *-- departmentPage
tabWidget *-- expensetypePage
tabWidget *-- expensePage

mainWindow *-- tabWidget
mainWindow --> accounting : управляет
mainWindow --> dataxml : сохраняет/загружает

@enduml
"""


def save_puml(content, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Создан: {filename}")


if __name__ == "__main__":
    print("Генерация PlantUML-диаграмм...\n")
    save_puml(ENTITIES_PUML, "uml_entities.puml")
    save_puml(DATA_PUML, "uml_data.puml")
    save_puml(GUI_PUML, "uml_gui.puml")
    print()
    print("Способы получить PNG:")
    print("  A) Открыть https://www.plantuml.com/plantuml/uml/")
    print("     Вставить содержимое .puml → Submit → скачать PNG")
    print("  B) plantuml *.puml   (если установлен plantuml)")
    print("  C) В draw.io: Arrange → Insert → Advanced → PlantUML")
    print("     Вставить код → кнопка Insert")
