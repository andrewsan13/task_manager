import calendar


#  https://pythonworld.ru/moduli/modul-calendar.html
class Callend:
    def __init__(self):
        self.formated = [[], [], [], [], []]
        self.cr = calendar.Calendar(firstweekday=0)  # 0 - понедельник, 6 - воскресенье

    def get_callend(self, year, month):
        temp = self.cr.itermonthdays3(year, month)
        new_li = []
        for i in temp:
            new_li.append(i[2])
        for j in range(0, 5):
            self.formated[j].extend(new_li[j * 7: (j + 1) * 7])
        if not self.formated[-1]:
            self.formated[-1].extend([i for i in range(1, 8)])
        return self.formated

# def prev_calendar(self):
#     if self.month == 1:
#         self.month = 12
#         self.year = self.year - 1
#     else:
#         self.month = self.month - 1
#     self.show_calendar(self.year, self.month)
#
# def next_calendar(self):
#     if self.month == 12:
#         self.month = 1
#         self.year = self.year + 1
#     else:
#         self.month = self.month + 1
#     self.show_calendar(self.year, self.month)
#
# def current_calendar(self):
#     self.year = datetime.datetime.today().year
#     self.month = datetime.datetime.today().month
#     self.show_calendar(self.year, self.month)
#
# def show_calendar(self, year, month):
#     self.labelMonth.setText(f"year:{year} month:{month}")
#
#     call = callend.Callend()
#     c = call.get_callend(year, month)
#
#     for i in range(0, 5):
#         for j in range(0, 7):
#             self.calendarTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(c[i][j])))
#     self.calendarTable.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
