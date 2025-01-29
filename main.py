from src import masks

print_num_account = int(input())
print_num_card = int(input())

print(masks.get_mask_account(print_num_account))
print(masks.get_mask_card_number(print_num_card))