const { Builder } = require('selenium-webdriver');
const GoogleHomePage = require('../pages/googleHomePage');
const GoogleSearchResultPage = require('../pages/googleSearchResultPage');

(async function runGoogleSearchTest() {
    // WebDriver 초기화
    let driver = await new Builder().forBrowser('chrome').build();

    try {
        // Page Object 생성
        const googleHomePage = new GoogleHomePage(driver);
        const googleSearchResultPage = new GoogleSearchResultPage(driver);

        // 테스트 실행
        await googleHomePage.open();
        await googleHomePage.search('javascript');
        await googleSearchResultPage.waitForResults();
        await googleHomePage.open(); // 다시 Google 홈페이지로 이동
    } catch (error) {
        console.error('테스트 중 오류 발생:', error);
    } finally {
        // WebDriver 종료
        await driver.quit();
    }
})();
