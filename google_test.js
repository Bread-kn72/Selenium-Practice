// selenium-webdriver 모듈 가져오기
const { Builder, By, Key, until } = require('selenium-webdriver');

(async function testGoogleSearch() {
  // WebDriver 인스턴스 생성
  const driver = await new Builder().forBrowser('chrome').build();

  try {
    // Google 홈페이지 열기
    await driver.get('https://www.google.com');

    // 검색창이 로드될 때까지 기다림
    await driver.wait(until.elementLocated(By.name('q')), 10000);

    // 검색창에 키워드 입력
    const searchBox = await driver.findElement(By.name('q'));
    await searchBox.sendKeys('Selenium WebDriver', Key.RETURN);

    // 검색 결과가 로드될 때까지 기다림
    await driver.wait(until.titleContains('Selenium WebDriver'), 10000);

    // 현재 페이지 제목 출력
    const title = await driver.getTitle();
    console.log(`현재 페이지 제목: ${title}`);
  } catch (error) {
    console.error(`테스트 중 오류 발생: ${error}`);
  } finally {
    // WebDriver 종료
    await driver.quit();
  }
})();
