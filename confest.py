from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def main() -> None:
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.google.com")

        search_box = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "q"))
        )
        search_box.send_keys("Python Selenium")
        search_box.submit()

        WebDriverWait(driver, 10).until(
            lambda browser: "Python Selenium" in browser.title
            or "/sorry/" in browser.current_url
        )
        if "/sorry/" in driver.current_url:
            raise RuntimeError(
                "Google returned an automated-traffic challenge; "
                "search results are unavailable."
            )

        print(driver.title)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
