import PySimpleGUI as simple_gui

main_menu_layout = [[simple_gui.Image('assets/wizard_hat.png')],
                    [simple_gui.Text('Welcome to this simple main menu!', font=('Any 20'), key="_TextFieldMenu_")],
                    [simple_gui.Button('Optie A', size=(10, 1))],
                    [simple_gui.Button('Optie B', size=(10, 1))],
                    [simple_gui.Button('Optie C', size=(10, 1))],
                    [simple_gui.Button('Cancel', size=(10, 1))]
                    ]

main_menu = simple_gui.Window(title='Example Application',
                              layout=main_menu_layout,
                              size=(500, 300),
                              element_justification="c")

answers = ["Ja", "Nee", "Misschien"]


def open_second_window():
    main_menu.Hide()
    question_layout = [[simple_gui.Text('Vraag 1: Vind je programmeren leuk?', font=("Any 20"))],
                       [simple_gui.Radio(answer, 1, size=(10, 1), enable_events=True) for answer in answers],
                       [simple_gui.Button('Next')]]

    questions_window = simple_gui.Window(title='Example Application',
                                         layout=question_layout,
                                         size=(500, 300),
                                         element_justification="c")
    while True:
        event, values = questions_window.read()
        if event == simple_gui.WIN_CLOSED or event == 'Next':
            questions_window.close()
            main_menu.UnHide()
            break
        print(values)


while True:
    event, values = main_menu.read()
    if event == simple_gui.WIN_CLOSED or event == 'Cancel':
        break
    elif event == "Optie A":
        main_menu["_TextFieldMenu_"].update("Welcome to this simple main menu!")
        print("We are going for option A!")
    elif event == "Optie B":
        open_second_window()
    elif event == "Optie C":
        main_menu["_TextFieldMenu_"].update("Text is now changed?")

main_menu.close()
