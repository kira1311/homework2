from src import widget, processing

print_num_account = input()
input_date = input()

transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(processing.filter_by_state(transactions))
print(processing.sort_by_date(transactions))

print(widget.mask_account_card(print_num_account))
print(widget.get_date(input_date))
