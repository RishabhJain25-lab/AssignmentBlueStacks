@author    Rishabh Jain
*** Settings ***
Library     SeleniumLibrary 
Library     Excel    
Library     OperatingSystem
Library     String
Resource    ../Resource/browser_setup.robot

*** Variable ***
${ExcelName}   GameData.xlsx
${SheetName}   GameDetailSheet
${gameStatusCode}  200

*** Test Cases ***
TC_Initial Suite Setup Keywords Initialization
    [Documentation]    Setting Up Excels.
      Suite Setup Keywords 
     
TC#1 Open Game Website
    Setup Browser 
    Maximize Browser Window
    Go To     https://www.game.tv/
    Wait Until Page Contains Element    //img[@class="logo-img"]   5s 
    Scroll Element Into View    //img[@alt="Garena Free Fire Tournaments"]
    Log To Console  Welcome to Game TV 
    Log To Console  SR.NO-Name of Game-TournamentCount
     
    FOR  ${i}  IN RANGE   1  150
         ${GametilesVisiblity}    Run Keyword And Return Status        Wait Until Page Contains Element   //*[@id="game_list"]/ul/li[${i}]/a/figcaption
         Exit For Loop If    "${GametilesVisiblity}" == "False"
         ${GameName}          Get Text      //*[@id="game_list"]/ul/li[${i}]/a/figcaption
         ${GameName}  Split String   ${GameName}   T    
         #Log To Console   ${Name}    
         Click Element    //*[@id="game_list"]/ul/li[${i}]/a/figcaption
         ${gameUrlVisiblity}    Run Keyword And Return Status   Wait Until Page Contains Element    //span[@class="count-tournaments"]   
         ${gameStatusCode}=  set variable if  "${gameUrlVisiblity}" == "True"
         ...    ${gameStatusCode}
         
         ${gameUrl} =  Execute Javascript  return window.location.href;
           
         ${tournamentCount}  Get Text    //span[@class="count-tournaments"]
         To Append Values    ${SheetName}    ${ExcelName}    ${i}    ${GameName}[0]   ${gameUrl}    ${gameStatusCode}    ${tournamentCount} 
        
         Log To Console  ${i}-${GameName}[0]-${tournamentCount}-${gameurl}-${gameStatusCode}
         Go Back
    END      
    Close Browser
        
*** Keywords ***

Suite Teardown Keywords
    To Save the excel    ${EXCEL_NAME}

To Save the excel
    [Documentation]    Saves the particular excel file by moving it in the Results Directory.
    [Arguments]    ${ExcelFileName}
    ${time}                             Get Time
    ${time}                             Split String                            ${time}           ${SPACE}
    ${time_hr}                          Replace String                          @{time}[1]        :                        -  
    Copy File    ${EXECDIR}${/}${ExcelFileName}    ${EXECDIR}${/}Results${/}${SUITENAME}_@{time}[0]_${time_hr}_${ExcelFileName}
    
To Append Values
    [Documentation]    Testing excel.py code to Add 3 Values to a Excel
    [Arguments]      ${SheetName}    ${ExcelName}    ${Value1}    ${Value2}    ${Value3}     ${Value4}     ${Value5}  
    Check File       ${EXECDIR}${/}${ExcelName}
    Check Sheet      ${SheetName}    ${EXECDIR}${/}${ExcelName}
    Append Values    ${SheetName}    ${EXECDIR}${/}${ExcelName}    ${Value1}    ${Value2}    ${Value3}     ${Value4}     ${Value5}

Add a Value
    [Documentation]    Testing excel.py code to Add Value to a Excel
    [Arguments]    ${SheetName}    ${ExcelName}     ${CellCords}    ${Value} 
    Check File     ${EXECDIR}${/}${ExcelName}
    Check Sheet    ${SheetName}    ${EXECDIR}${/}${ExcelName}
    Add Value      ${SheetName}   ${EXECDIR}${/}${ExcelName}   ${CellCords}    ${Value}

Suite Setup Keywords
    Set Log Level    DEBUG
    Create Excel File    ${SheetName}    ${ExcelName}
    Add a Value    ${SheetName}    ${ExcelName}    A1    SR.NO
    Add a Value    ${SheetName}    ${ExcelName}    B1    Game Name
    Add a Value    ${SheetName}    ${ExcelName}    C1    Page URL
    Add a Value    ${SheetName}    ${ExcelName}    D1    Page Status
    Add a Value    ${SheetName}    ${ExcelName}    E1    Tournament Count
    
    
    
    