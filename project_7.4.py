def create_calendar_page(month = None, year = None):
    import calendar
    from datetime import datetime
    if month == None:
        month = datetime.today().month 
    if year == None:
        year = datetime.today().year 
    days_abr = calendar.weekheader(2).upper()
    length_header = len(days_abr)
    header_dash = ''
    for i in range(length_header):
        header_dash += '-'
    month_list = calendar.TextCalendar().monthdayscalendar(year, month)
    while month_list[-1][-1] == 0:
        del month_list[-1][-1]
    month_list_str = [['%02d'%(j) for j in i]for i in month_list]
    month_str = []
    for i in month_list_str:
        month_str.append(' '.join(i)) 
    month_str = '\n'.join(month_str)
    month_str = month_str.replace('00', '  ')
    output_str = f'{header_dash}\n{days_abr}\n{header_dash}\n{month_str}\n'
    return output_str


print (create_calendar_page(1))
print (create_calendar_page())
print (create_calendar_page(3))
print (create_calendar_page(4, 1992))