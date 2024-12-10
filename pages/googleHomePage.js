const { By, Key } = require('selenium-webdriver');

class GoogleHomePage {
    constructor(driver) {
        this.driver = driver;
        this.searchBox = By.name('q'); // 검색 입력창
    }

    async open() {
        await this.driver.get('https://www.google.co.kr');
    }

    async search(query) {
        const searchBoxElement = await this.driver.findElement(this.searchBox);
        await searchBoxElement.sendKeys(query, Key.RETURN);
    }
}

module.exports = GoogleHomePage;
