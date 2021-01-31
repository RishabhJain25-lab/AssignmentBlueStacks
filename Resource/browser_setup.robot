*** Settings ***
Documentation     The main interface for interacting with browser. It handles low level stuff like managing the selenium request library.
Library           Collections
Library           OperatingSystem
Library           SeleniumLibrary

*** Variables ***
${HEADLESS}           False
${PROXY}              No
${GLOBAL_SELENIUM_BROWSER}    chrome

*** Keywords ***
Setup Browser
    [Documentation]   Sets up browser based upon the value of ${GLOBAL_SELENIUM_BROWSER}
    Run Keyword If    '${GLOBAL_SELENIUM_BROWSER}' == 'chrome'    Setup Browser Chrome
    Log    Running with ${GLOBAL_SELENIUM_BROWSER}

Setup Browser Chrome
    ${chrome options}=    Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys
    Call Method    ${chrome options}    add_argument    no-sandbox
    Run Keyword If  ${HEADLESS}==True  Call Method    ${chrome options}    add_argument    headless
    ${dc}   Evaluate    sys.modules['selenium.webdriver'].DesiredCapabilities.CHROME  sys
    Set To Dictionary   ${dc}   elementScrollBehavior    1
    Create Webdriver    Chrome       desired_capabilities=${dc}    chrome_options=${chrome_options}  
    Set Global Variable    ${GLOBAL_SELENIUM_BROWSER_CAPABILITIES}    ${dc}
          
Close Agents
    [Documentation]    Closes the currently opened Browser.
    Close Browser    