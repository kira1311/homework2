import logging
import os


if not os.path.exists('logs'):
    os.makedirs('logs')

logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('logs/masks.log', mode='w')
logger.setLevel(logging.DEBUG)

file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    logger.info("запуск маскировки номера карт")
    """функция для маскировки номера карты"""
    card_number = str(card_number)
    block1 = card_number[:4]
    block2 = card_number[4:6]
    block3 = "**"
    block4 = "****"
    block5 = card_number[-4:]
    mask_card = f"{block1} {block2}{block3} {block4} {block5}"
    logger.info(f"маскировка пройдена успешно - {mask_card}")
    return mask_card


def get_mask_account(account_number: str) -> str:
    logger.info("запуск маскировки номера счета")
    """функция для маскировки номера счета"""
    block6 = account_number[-4:]
    mask_number = f"**{block6}"
    logger.info(f"маскировка пройдена успешно - {mask_number}")
    return mask_number


print(get_mask_account('12874624812964718260471'))

print(get_mask_card_number('7189237812348121'))
