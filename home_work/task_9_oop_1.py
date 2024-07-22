from python_training.task_9_checks import Checks


class Input:

    def __init__(self, loc, text):
        super().__init__()
        self.loc = loc
        self.text = text


search = Input('input#search', 'Введите ФИО')
search2 = Checks('input#search')
print(search.loc)
print(search.text)
print(search2.check_text())


class Button:

    def __init__(self, loc, text):
        super().__init__()
        self.loc = loc
        self.text = text


btn = Button('xpath=//button', 'Text Box')
btn2 = Checks('xpath=//button')
print(btn.loc)
print(btn.text)
print(btn2.check_text())


class Title:

    def __init__(self, loc, text):
        super().__init__()
        self.loc = loc
        self.text = text


title = Title('xpath=//title', 'Заголовок статьи')
title2 = Checks('xpath=//title')
print(title.loc)
print(title.text)
print(title2.check_text())


class Link:

    def __init__(self, loc, text):
        super().__init__()
        self.loc = loc
        self.text = text


link = Link('xpath=//href', 'https://demoqa.com/text-box')
link2 = Checks('xpath=//href')
print(link.text)
print(link.loc)
print(link2.check_text())

