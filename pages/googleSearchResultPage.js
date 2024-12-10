const { until } = require('selenium-webdriver');

class GoogleSearchResultPage {
    constructor(driver) {
        this.driver = driver;
    }

    async waitForResults() {
        await this.driver.wait(until.titleContains('javascript'), 5000);
    }
}

module.exports = GoogleSearchResultPage;
