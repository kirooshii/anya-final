#!/usr/bin/env python3
"""
Генератор трёх UML-диаграмм в формате draw.io (.drawio).
Запуск: python3 generate_drawio_uml.py
Результат: uml_entities.drawio, uml_data.drawio, uml_gui.drawio
Откройте каждый в draw.io → File → Export as → PNG
"""

import xml.etree.ElementTree as ET
import os

# ============================================================
# Вспомогательные функции для создания mxGraph XML
# ============================================================

def new_cell(id, parent, value, style, x, y, w, h):
    """Создать mxCell с геометрией."""
    cell = ET.Element("mxCell", id=id, parent=parent, value=value, style=style, vertex="1")
    geo = ET.SubElement(cell, "mxGeometry", x=str(x), y=str(y), width=str(w), height=str(h), as_="geometry")
    return cell

def new_edge(id, parent, source, target, style, value="", points=None):
    """Создать ребро (связь)."""
    attrs = {"id": id, "parent": parent, "source": source, "target": target, "style": style, "edge": "1"}
    if value:
        attrs["value"] = value
    edge = ET.Element("mxCell", attrs)
    geo = ET.SubElement(edge, "mxGeometry", relative="1", as_="geometry")
    if points:
        ET.SubElement(geo, "Array", as_="points")
        # точки задаются как дочерние mxPoint
        for pt in points:
            ET.SubElement(geo, "mxPoint", x=str(pt[0]), y=str(pt[1]))
    return edge

def new_root(arrow_size=10):
    """Создать базовую структуру mxGraphModel."""
    model = ET.Element("mxGraphModel", dx="1422", dy="794", grid="1", gridSize="10",
                       guides="1", tooltips="1", connect="1", arrows="1",
                       fold="1", page="0", pageScale="1", pageWidth="827",
                       pageHeight="1169", math="0", shadow="0")
    root = ET.SubElement(model, "root")
    ET.SubElement(root, "mxCell", id="0")
    ET.SubElement(root, "mxCell", id="1", parent="0")
    return model, root

def make_diagram(name, model):
    """Оборачивает модель в diagram и mxfile."""
    diagram = ET.Element("diagram", id="diag", name=name)
    diagram.append(model)
    mxfile = ET.Element("mxfile", host="draw.io", modified="2024-01-01T00:00:00.000Z",
                        agent="manual", version="21.0.0", type="device")
    mxfile.append(diagram)
    return mxfile

def indent(elem, level=0):
    """Форматирует XML с отступами (аналог pretty-print)."""
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def save_diagram(mxfile, filename):
    """Сериализует mxfile в .drawio файл."""
    indent(mxfile)
    tree = ET.ElementTree(mxfile)
    tree.write(filename, encoding="utf-8", xml_declaration=True)
    print(f"  Создан: {filename}")

# ============================================================
# Стили для UML-диаграмм классов
# ============================================================

# Прямоугольник класса: заголовок + разделитель + атрибуты + разделитель + методы
CLASS_STYLE = (
    "whiteSpace=wrap;html=1;align=left;"
    "strokeWidth=1;fillColor=#d5e8d4;strokeColor=#82b366;"
)
CLASS_HEAD_STYLE = CLASS_STYLE + "part=1;"  # только для заголовка, но мы рисуем целый класс

# Наследование (hollow triangle)
INHERIT_STYLE = (
    "edgeStyle=elbowEdgeStyle;elbow=vertical;html=1;endArrow=block;"
    "endFill=0;endSize=16;strokeWidth=1;dashed=0;"
)

# Агрегация (diamond at source end)
AGGREGATE_STYLE = (
    "edgeStyle=elbowEdgeStyle;elbow=vertical;html=1;endArrow=none;"
    "startArrow=diamondThin;startFill=1;startSize=14;strokeWidth=1;"
)

# Ассоциация (простая линия)
ASSOC_STYLE = (
    "edgeStyle=elbowEdgeStyle;elbow=vertical;html=1;endArrow=none;"
    "strokeWidth=1;dashed=0;"
)

# ============================================================
# cell_id counter
# ============================================================
cid = 2  # начинаем после root cells 0 и 1
def next_id():
    global cid
    cid += 1
    return str(cid - 1)

def reset_id():
    global cid
    cid = 2

# ============================================================
# Функция для создания ячейки UML-класса
# ============================================================

def uml_class(root, class_name, attributes, methods, x, y, w=180):
    """
    Рисует UML-класс в виде раскрашенного прямоугольника.
    Формат значения: &lt;&lt;class&gt;&gt;\n<b>ClassName</b>\n──────────\n- attr1\n- attr2\n──────────\n+ method1()\n+ method2()
    """
    lines = []
    lines.append(f"&lt;&lt;class&gt;&gt;")
    lines.append(f"<b>{class_name}</b>")
    lines.append("──────────")
    for a in attributes:
        lines.append(f"- {a}")
    if methods:
        lines.append("──────────")
        for m in methods:
            lines.append(f"+ {m}()")
    value = "\n".join(lines)

    # Вычисляем высоту: примерно 22px на строку
    h = max(60, len(lines) * 22 + 10)
    cell_id = next_id()
    cell = new_cell(cell_id, "1", value, CLASS_STYLE, x, y, w, h)
    root.append(cell)
    return cell_id


# ============================================================
# Диаграмма 1: Сущности (entities)
# ============================================================

def create_entities_diagram():
    global cid
    cid = 2
    model, root = new_root()

    # --- general ---
    g = uml_class(root, "general",
        ["- __code : int", "- __name : str"],
        ["+ setCode(value)", "+ setName(value)", "+ getCode()", "+ getName()"],
        400, 50)

    # --- department ---
    d = uml_class(root, "department",
        ["- __employees : int"],
        ["+ setEmployees(v)", "+ getEmployees()"],
        100, 250)

    # --- expensetype ---
    et = uml_class(root, "expensetype",
        ["- __description : str", "- __limit : float"],
        ["+ setDescription(v)", "+ getDescription()", "+ setLimit(v)", "+ getLimit()"],
        400, 250)

    # --- expense ---
    e_id = next_id()
    e_lines = [
        "&lt;&lt;class&gt;&gt;",
        "<b>expense</b>",
        "──────────",
        "- __expensetype : expensetype",
        "- __department : department",
        "- __amount : float",
        "- __date : str",
        "──────────",
        "+ setExpenseType(v)",
        "+ getExpenseType()",
        "+ getExpenseTypeCode()",
        "+ getExpenseTypeName()",
        "+ setDepartment(v)",
        "+ getDepartment()",
        "+ getDepartmentCode()",
        "+ getDepartmentName()",
        "+ setAmount(v)",
        "+ getAmount()",
        "+ setDate(v)",
        "+ getDate()"
    ]
    e_h = len(e_lines) * 22 + 10
    e_cell = new_cell(e_id, "1", "\n".join(e_lines), CLASS_STYLE, 700, 200, 210, e_h)
    root.append(e_cell)

    # --- Наследование: department → general ---
    inh1 = new_edge(next_id(), "1", d, g, INHERIT_STYLE)
    root.append(inh1)

    # --- Наследование: expensetype → general ---
    inh2 = new_edge(next_id(), "1", et, g, INHERIT_STYLE)
    root.append(inh2)

    # --- Наследование: expense → general ---
    inh3_id = next_id()
    inh3 = new_edge(inh3_id, "1", str(e_id), g, INHERIT_STYLE, "",
                     [(700, 160), (580, 160), (580, 110)])
    root.append(inh3)

    # --- Агрегация: expense → department ---
    agg1 = new_edge(next_id(), "1", str(e_id), d, AGGREGATE_STYLE)
    root.append(agg1)

    # --- Агрегация: expense → expensetype ---
    agg2 = new_edge(next_id(), "1", str(e_id), et, AGGREGATE_STYLE)
    root.append(agg2)

    mxfile = make_diagram("UML Entities", model)
    save_diagram(mxfile, "uml_entities.drawio")


# ============================================================
# Диаграмма 2: Слой данных (data layer)
# ============================================================

def create_data_diagram():
    global cid
    cid = 2
    model, root = new_root()

    # --- generalList ---
    gl = uml_class(root, "generalList",
        ["- __list : list"],
        ["+ clear()", "+ findByCode(code)", "+ getNewCode()", "+ getCodes()",
         "+ getItems()", "+ appendItem(v)", "+ removeItem(v)"],
        750, 40, 200)

    # --- departmentList ---
    dl = uml_class(root, "departmentList",
        [],
        ["+ appendItem(v)", "+ createItem(code,name,emp)", "+ newItem(name,emp)"],
        500, 300, 200)

    # --- expensetypeList ---
    etl = uml_class(root, "expensetypeList",
        [],
        ["+ appendItem(v)", "+ createItem(code,name,desc,lim)", "+ newItem(name,desc,lim)"],
        750, 300, 200)

    # --- expenseList ---
    el = uml_class(root, "expenseList",
        [],
        ["+ appendItem(v)", "+ createItem(...)", "+ newItem(...)"],
        1000, 300, 190)

    # --- Наследование списков от generalList ---
    root.append(new_edge(next_id(), "1", dl, gl, INHERIT_STYLE))
    root.append(new_edge(next_id(), "1", etl, gl, INHERIT_STYLE))
    root.append(new_edge(next_id(), "1", el, gl, INHERIT_STYLE))

    # --- accounting ---
    acc_id = next_id()
    acc_lines = [
        "&lt;&lt;class&gt;&gt;",
        "<b>accounting</b>",
        "──────────",
        "- __departmentList",
        "- __expensetypeList",
        "- __expenseList",
        "──────────",
        "+ clear()",
        "+ createDepartment(...)",
        "+ newDepartment(...)",
        "+ removeDepartment(code)",
        "+ getDepartment(code)",
        "+ getDepartmentList()",
        "+ getDepartmentCodes()",
        "+ createExpenseType(...)",
        "+ newExpenseType(...)",
        "+ removeExpenseType(code)",
        "+ getExpenseType(code)",
        "+ getExpenseTypeList()",
        "+ getExpenseTypeCodes()",
        "+ createExpense(...)",
        "+ newExpense(...)",
        "+ removeExpense(code)",
        "+ getExpense(code)",
        "+ getExpenseList()",
        "+ getExpenseCodes()"
    ]
    acc_h = len(acc_lines) * 22 + 10
    acc_cell = new_cell(acc_id, "1", "\n".join(acc_lines), CLASS_STYLE, 260, 200, 210, acc_h)
    root.append(acc_cell)

    # --- Агрегации: accounting → списки ---
    root.append(new_edge(next_id(), "1", str(acc_id), dl, AGGREGATE_STYLE))
    root.append(new_edge(next_id(), "1", str(acc_id), etl, AGGREGATE_STYLE))
    root.append(new_edge(next_id(), "1", str(acc_id), el, AGGREGATE_STYLE))

    # --- data ---
    data_cls = uml_class(root, "data",
        ["- __lib", "- __inp : str", "- __out : str"],
        ["+ setLib(v)", "+ setInp(v)", "+ setOut(v)",
         "+ getLib()", "+ getInp()", "+ getOut()",
         "+ readFile(lib,fn)", "+ writeFile(lib,fn)",
         "+ read()", "+ write()"],
        30, 470, 200)

    # --- dataxml ---
    dxml = uml_class(root, "dataxml",
        [],
        ["+ read()", "+ write()"],
        280, 470, 180)

    # --- Наследование: dataxml → data ---
    root.append(new_edge(next_id(), "1", dxml, data_cls, INHERIT_STYLE))

    # --- Ассоциация: dataxml → accounting (использует) ---
    # Для красоты сделаем ассоциацию штриховой линией
    assoc_style_dash = "edgeStyle=elbowEdgeStyle;elbow=vertical;html=1;endArrow=open;dashed=1;strokeWidth=1;"
    root.append(new_edge(next_id(), "1", dxml, str(acc_id), assoc_style_dash, "использует",
                          [(370, 500), (370, 550), (470, 550), (470, 400)]))

    # --- rowCode ---
    rc = uml_class(root, "rowCode",
        ["- __list : list"],
        ["+ clear()", "+ appendRowCode(r,c)", "+ updateRow(r)",
         "+ removeRow(r)", "+ removeCode(c)", "+ getCode(r)",
         "+ getCodes()", "+ getRow(c)"],
        1030, 470, 200)

    mxfile = make_diagram("UML Data Layer", model)
    save_diagram(mxfile, "uml_data.drawio")


# ============================================================
# Диаграмма 3: GUI (графический интерфейс)
# ============================================================

def create_gui_diagram():
    global cid
    cid = 2
    model, root = new_root()

    # --- libWidget ---
    lw = uml_class(root, "«mixin»\nlibWidget",
        ["- __library"],
        ["+ getLibrary()"],
        100, 20, 160)

    # --- rowCode ---
    rc = uml_class(root, "rowCode",
        ["- __list"],
        ["+ clear()", "+ appendRowCode(r,c)", "+ getCode(r)", "+ getRow(c)"],
        1050, 20, 180)

    # --- QTableWidget (внешний, Qt) ---
    qtw_id = next_id()
    qtw_cell = new_cell(qtw_id, "1",
        "&lt;&lt;Qt&gt;&gt;\n<b>QTableWidget</b>",
        "whiteSpace=wrap;html=1;align=center;fillColor=#f5f5f5;strokeColor=#666666;fontColor=#999999;dashed=1;",
        340, 20, 140, 50)
    root.append(qtw_cell)

    # --- QComboBox (внешний, Qt) ---
    qcb_id = next_id()
    qcb_cell = new_cell(qcb_id, "1",
        "&lt;&lt;Qt&gt;&gt;\n<b>QComboBox</b>",
        "whiteSpace=wrap;html=1;align=center;fillColor=#f5f5f5;strokeColor=#666666;fontColor=#999999;dashed=1;",
        660, 20, 140, 50)
    root.append(qcb_cell)

    # --- QWidget (внешний, Qt) ---
    qw_id = next_id()
    qw_cell = new_cell(qw_id, "1",
        "&lt;&lt;Qt&gt;&gt;\n<b>QWidget</b>",
        "whiteSpace=wrap;html=1;align=center;fillColor=#f5f5f5;strokeColor=#666666;fontColor=#999999;dashed=1;",
        340, 150, 120, 50)
    root.append(qw_cell)

    # --- QMainWindow (внешний, Qt) ---
    qmw_id = next_id()
    qmw_cell = new_cell(qmw_id, "1",
        "&lt;&lt;Qt&gt;&gt;\n<b>QMainWindow</b>",
        "whiteSpace=wrap;html=1;align=center;fillColor=#f5f5f5;strokeColor=#666666;fontColor=#999999;dashed=1;",
        660, 150, 140, 50)
    root.append(qmw_cell)

    # --- QTabWidget (внешний, Qt) ---
    qtab_id = next_id()
    qtab_cell = new_cell(qtab_id, "1",
        "&lt;&lt;Qt&gt;&gt;\n<b>QTabWidget</b>",
        "whiteSpace=wrap;html=1;align=center;fillColor=#f5f5f5;strokeColor=#666666;fontColor=#999999;dashed=1;",
        660, 260, 140, 50)
    root.append(qtab_cell)

    # --- dbTableWidget ---
    dbtw = uml_class(root, "dbTableWidget",
        ["- __rowCode : rowCode"],
        ["+ setHeader(v)", "+ clearContents()",
         "+ getCodes()", "+ getCurrentCode()",
         "+ setCurrentCode(c)", "+ appendRowCode(r,c)",
         "+ update(code)", "+ setData()"],
        340, 100, 200)

    # --- dbComboBox ---
    dbcb = uml_class(root, "dbComboBox",
        ["- __rowCode : rowCode"],
        ["+ clear()", "+ addItem(code,text)",
         "+ removeItem(idx)", "+ getCurrentCode()",
         "+ setCurrentCode(c)", "+ setCurrentRec(v)",
         "+ getCurrentRec()", "+ update()"],
        660, 100, 200)

    # --- editForm ---
    ef = uml_class(root, "editForm",
        ["- __grid", "- __vbox", "- __hbox", "- __currentCode"],
        ["+ addLabel(text,x,y)", "+ addNewWidget(w,x,y)",
         "+ addLeftLayout(l)", "+ setCurrentCode(c)",
         "+ getCurrentCode()", "+ update()",
         "+ newClick()", "+ editClick()", "+ delClick()"],
        340, 270, 200)

    # --- page ---
    pg = uml_class(root, "page",
        ["- __vbox", "- __hbox", "- __buttonbox",
         "- __newButton", "- __editButton", "- __delButton",
         "- __table", "- __form"],
        ["+ setTable(v)", "+ setForm(v)", "+ newClick()",
         "+ editClick()", "+ delClick()", "+ tableClick()",
         "+ setConnect()", "+ update()"],
        340, 440, 200)

    # --- Наследования ---
    root.append(new_edge(next_id(), "1", dbtw, str(qtw_id), INHERIT_STYLE))
    root.append(new_edge(next_id(), "1", dbtw, lw, "mixin\n──────────────────", []))

    root.append(new_edge(next_id(), "1", dbcb, str(qcb_id), INHERIT_STYLE))
    root.append(new_edge(next_id(), "1", dbcb, lw, "mixin\n──────────────────", []))

    root.append(new_edge(next_id(), "1", ef, str(qw_id), INHERIT_STYLE))
    root.append(new_edge(next_id(), "1", ef, lw, "mixin\n──────────────────", []))

    root.append(new_edge(next_id(), "1", pg, str(qw_id), INHERIT_STYLE))
    root.append(new_edge(next_id(), "1", pg, lw, "mixin\n──────────────────", []))

    # --- Специализированные таблицы (справа) ---
    deps_tbl = uml_class(root, "departmentsTable",
        [], ["+ setData()"], 40, 640, 180)
    expt_tbl = uml_class(root, "expensetypesTable",
        [], ["+ setData()"], 250, 640, 180)
    exp_tbl = uml_class(root, "expensesTable",
        [], ["+ setData()"], 460, 640, 180)

    root.append(new_edge(next_id(), "1", deps_tbl, dbtw, INHERIT_STYLE))
    root.append(new_edge(next_id(), "1", expt_tbl, dbtw, INHERIT_STYLE))
    root.append(new_edge(next_id(), "1", exp_tbl, dbtw, INHERIT_STYLE))

    # --- Специализированные комбо-боксы ---
    dep_combo = uml_class(root, "departmentCombo",
        [], ["+ update()"], 670, 640, 190)
    exptype_combo = uml_class(root, "expensetypeCombo",
        [], ["+ update()"], 900, 640, 190)

    root.append(new_edge(next_id(), "1", dep_combo, dbcb, INHERIT_STYLE))
    root.append(new_edge(next_id(), "1", exptype_combo, dbcb, INHERIT_STYLE))

    # --- Специализированные формы ---
    dep_ef = uml_class(root, "departmentEditForm",
        [], ["+ update()", "+ newClick()", "+ editClick()", "+ delClick()"],
        40, 820, 180)
    expt_ef = uml_class(root, "expensetypeEditForm",
        [], ["+ update()", "+ newClick()", "+ editClick()", "+ delClick()"],
        250, 820, 180)
    exp_ef = uml_class(root, "expenseEditForm",
        ["- __expensetypeCombo", "- __departmentCombo"],
        ["+ update()", "+ newClick()", "+ editClick()", "+ delClick()"],
        460, 820, 180)

    root.append(new_edge(next_id(), "1", dep_ef, ef, INHERIT_STYLE))
    root.append(new_edge(next_id(), "1", expt_ef, ef, INHERIT_STYLE))
    root.append(new_edge(next_id(), "1", exp_ef, ef, INHERIT_STYLE))

    # --- Композиция: expenseEditForm использует комбо-боксы ---
    comp_style = "edgeStyle=elbowEdgeStyle;elbow=vertical;html=1;endArrow=open;dashed=1;strokeWidth=1;"
    root.append(new_edge(next_id(), "1", exp_ef, dep_combo, comp_style, ""))
    root.append(new_edge(next_id(), "1", exp_ef, exptype_combo, comp_style, ""))

    # --- Специализированные страницы ---
    dep_pg = uml_class(root, "departmentPage",
        [], ["+ setTable()", "+ setForm()", "+ setConnect()"],
        40, 1000, 180)
    expt_pg = uml_class(root, "expensetypePage",
        [], ["+ setTable()", "+ setForm()", "+ setConnect()"],
        250, 1000, 180)
    exp_pg = uml_class(root, "expensePage",
        [], ["+ setTable()", "+ setForm()", "+ setConnect()"],
        460, 1000, 180)

    root.append(new_edge(next_id(), "1", dep_pg, pg, INHERIT_STYLE))
    root.append(new_edge(next_id(), "1", expt_pg, pg, INHERIT_STYLE))
    root.append(new_edge(next_id(), "1", exp_pg, pg, INHERIT_STYLE))

    # --- Композиция страниц из таблиц и форм ---
    root.append(new_edge(next_id(), "1", dep_pg, deps_tbl, comp_style, ""))
    root.append(new_edge(next_id(), "1", dep_pg, dep_ef, comp_style, ""))
    root.append(new_edge(next_id(), "1", expt_pg, expt_tbl, comp_style, ""))
    root.append(new_edge(next_id(), "1", expt_pg, expt_ef, comp_style, ""))
    root.append(new_edge(next_id(), "1", exp_pg, exp_tbl, comp_style, ""))
    root.append(new_edge(next_id(), "1", exp_pg, exp_ef, comp_style, ""))

    # --- tabWidget ---
    tabw = uml_class(root, "tabWidget",
        ["- __departmentPage", "- __expensetypePage", "- __expensePage"],
        ["+ update()"],
        680, 350, 200)

    root.append(new_edge(next_id(), "1", tabw, str(qtab_id), INHERIT_STYLE))
    root.append(new_edge(next_id(), "1", tabw, dep_pg, AGGREGATE_STYLE, ""))
    root.append(new_edge(next_id(), "1", tabw, expt_pg, AGGREGATE_STYLE, ""))
    root.append(new_edge(next_id(), "1", tabw, exp_pg, AGGREGATE_STYLE, ""))

    # --- mainWindow ---
    mw = uml_class(root, "mainWindow",
        ["- __accounting : accounting", "- dataxml : dataxml",
         "- tabWidget : tabWidget",
         "- new, openxml, savexml : QAction"],
        ["+ newAction()", "+ openXMLAction()", "+ saveXMLAction()"],
        680, 500, 220)

    root.append(new_edge(next_id(), "1", mw, str(qmw_id), INHERIT_STYLE))
    root.append(new_edge(next_id(), "1", mw, tabw, AGGREGATE_STYLE, ""))

    mxfile = make_diagram("UML GUI Layer", model)
    save_diagram(mxfile, "uml_gui.drawio")


# ============================================================
# Главная программа
# ============================================================
if __name__ == "__main__":
    print("Генерация UML-диаграмм для draw.io...\n")
    create_entities_diagram()
    create_data_diagram()
    create_gui_diagram()
    print("\nГотово. Откройте файлы .drawio в draw.io (app.diagrams.net) и экспортируйте в PNG.")
