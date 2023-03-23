import domain

test_cases = [
    ('https://www.smokecartel.com/3508253/checkouts/ee6751f27ea600d0c133445710f11db0?_ga=2.208438866.1566561875.1678469276-1096666253.1678469276', 'smokecartel'),
    ('http://abc.hostname.com/somethings/anything/', 'abc.hostname'),
    ('ftp://www.hostname.com/somethings/anything/', 'hostname'),
    ('calendar.google.com', 'calendar.google'),
    ('https://calendar.google.com/calendar/u/0/r/week', 'calendar.google'),
    ('https://www.geeksforgeeks.org/python-os-environ-object/', 'geeksforgeeks'),
    ('google.biz', 'google'),
]

for raw_input,expected_answer in test_cases:
    actual_answer = domain.get_name(raw_input)

    if actual_answer != expected_answer:
        print('🍎', 'expected', expected_answer, 'actual', actual_answer)
    else:
        print('💚', 'expected', expected_answer, 'actual', actual_answer)
