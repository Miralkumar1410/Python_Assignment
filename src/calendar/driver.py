from calendar.util import weekday_name


if __name__ == '__main__':
    m, d, y = map(int, input().split())
    print(weekday_name(m,d,y))