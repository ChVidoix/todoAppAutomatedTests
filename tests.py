import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def run_tests(items_num):
    driver = webdriver.Chrome()
    # driver.get("http://localhost:3000/")
    driver.get("http://localhost:5173/")

    task_name_input = driver.find_element(by=By.CSS_SELECTOR, value="input[data-testid='new-task-input']")
    add_task_btn = driver.find_element(by=By.CSS_SELECTOR, value="button[data-testid='new-task-button']")

    ############## ADDING ITEMS ##############

    start = time.time()

    for i in range(items_num):
        task_name_input.send_keys(f'task{i}')
        add_task_btn.click()

    end_adding = time.time()

    print('added {} items in:\t\t'.format(items_num), end_adding-start)

    ############## MARKING ITEMS AS DONE ##############

    start_marking = time.time()

    for i in reversed(range(items_num)):
        toggle_task_btn = driver.find_element(by=By.CSS_SELECTOR, value="button[data-testid='toggle-btn-{}']".format(i))
        toggle_task_btn.click()

    end_marking = time.time()

    print('marked {} items in:\t\t'.format(items_num), end_marking-start_marking)

    ############## REMOVING ITEMS ##############

    start_removing = time.time()

    for i in reversed(range(items_num)):
        delete_task_btn = driver.find_element(by=By.CSS_SELECTOR, value="button[data-testid='delete-btn-{}']".format(i))
        delete_task_btn.click()

    end = time.time()

    print('removed {} items in:\t'.format(items_num), end-start_removing)
    print('executed all tests in: \t', end-start)

    driver.close()


if __name__ == "__main__":
    run_tests(300)
