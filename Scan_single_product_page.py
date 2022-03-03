import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import service
from selenium.webdriver.support import expected_conditions as EC

#import search_from_colab

#home "C:\\Users\\User\\Desktop\\chromeDriver\\chromedriver.exe"
# school: "C:\\chromedriver.exe"
#
PATH = "C:\\Users\\User\\Desktop\\chromeDriver\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()
driver.get("https://www.zara.com/il/he/%D7%A4%D7%99%D7%92-%D7%9E%D7%94-%D7%A7%D7%98%D7%99%D7%A4%D7%94-%D7%A2%D7%9D-%D7%94%D7%93%D7%A4%D7%A1-%D7%9B%D7%9C%D7%91-p08501528.html?v1=144410020&v2=2022652")

def convert_selenium_tag_to_html_tag():# הופכת סלניום לתגית html
    elem = driver.find_element_by_xpath("//a")
    source_code = elem.get_attribute("outerHTML")
    print(source_code)
#work
def find_add_tag():  # פונקציה המחפשת את כפתור ההוספה לסל מחזירה את הכפתור ו-1 אם מצא תגית הוספה ן- 0 אם לא מכיל
    # מעבר על כל האלמנטים ומציאת תגית ההוספה לסל
    result = []
    amount_of_add_tag = 0
    list_of_buttons = []
    body = driver.find_elements(By.TAG_NAME, "body")[0]
    include_add_tag = 0
    add_tag = ''
    list_of_button_elements = body.find_elements(By.XPATH, '//button') # שליפת כל הכפתורים לתוך רשימה
    print("find buttons")
    for element in list_of_button_elements:  # מעבר על הכפתורים שבדף
        list_of_attributes = element.get_property('attributes')
        for attribute in list_of_attributes:  # מעבר על attributes
            if attribute['value'].__contains__("הוספה לסל") or attribute['value'].__contains__("buy now")or attribute['value'].__contains__("הוסף לסל"):
                include_add_tag = 1
                print(element.tag_name)
                #add_tag = element
                amount_of_add_tag = amount_of_add_tag+1
                list_of_buttons.append(element)
                #break
    print(amount_of_add_tag)
    print("finish: find_add_tag ")
    #result = [include_add_tag, add_tag]
    #return result
    return list_of_buttons

#var_a:WebElement
def flatten(l):
    try:
        return flatten(l[0]) + (flatten(l[1:]) if len(l) > 1 else []) if type(l) is list else [l]
    except IndexError:
        return []
#work
def is_tag_include_picture(element: WebElement):#  מקבלת אלמנט ובודקת האם הוא מכיל תמונהו ומחזיר מערך שמחזיר במקום ה[0] 1 כשיש תמונה ו 0 כשאין תמונה, במקום ה [1] מחזיר את אלמנט התמונה
    #print("entered to : is_tag_include_picture ")
    #time.sleep(3)
    global find_picture_element
    picture_element = "" #מכיל אלמנט תמונה
    children_of_element = []
    flat_list = []

    is_there_is_picture = 0 #מכיל 1 כאשר יש אלמנט תמונה ו 0 כשלא מכיל אלמנט תמונה
    #./ *
    children_of_element = element.find_elements(By.XPATH, ".//*") # קבלת כל הילדים של האלמנט שהתקבל
    flat_list = flatten(children_of_element)# שיטוח הרשימה
    for elem in children_of_element:
        #print(elem.tag_name)
        if elem.tag_name == "img" or elem.tag_name == "src":  # חיפוש באלמנט אחר תגית img  או src
            picture_element = elem
            is_there_is_picture = 1
            print("found pic!!!")
            break

    result = [is_there_is_picture, picture_element]
    return result
# not  work
def check_if_element_include_price(element: WebElement):# מקבלת אלמנט ובודקת האם הוא מכיל מחיר
    print("entered to : check_if_element_include_price ")
    children_of_element = element.find_elements(By.XPATH, "./*")
    is_include_price = 0
    price_element = ''
    for element in children_of_element:
       # print(element)
       # print(element.tag_name)
        innerHTML = element.get_attribute('innerHTML')  # קבלת כל התוכן של אלמנט ה h1
        print(innerHTML)
        '''
        if element.text.__contains__("price") or element.text.__contains__("מחיר") or element.text.__contains__("$") or element.text.__contains__("₪"):
            is_include_price = 1
            price_element = element
                  # In case that we found an element that contains in its free text the next things:price,מחיר,$,₪
        list_of_attributes = element.get_property('attributes')
        for attribute in list_of_attributes:
            if attribute['value'].__contains__("price") or attribute['value'].__contains__("מחיר") or element.text.__contains__("$") or element.text.__contains__("₪"):
                is_include_price = 1
                price_element = element
                '''
    print("finished : check_if_element_include_price ")
    return is_include_price, price_element


#שליפת שם המוצר לא עובדת בטרמינל X לבדוק למה!!!!!!
def check_if_element_include_h1(element: WebElement): #פונקציה המקבלת אלמנט ובודקת אם הוא מכיל תגית h1 מחזיר במקום ה- [0] 1 אם מצא תגיתh1  אם לא מצא תגית h1 מחזיר 0

    print("entered to : check_if_element_include_h1 ")
    h1_element = "" #מכיל אלמנט תמונה
    is_there_is_h1 = 0  # מכיל 1 כאשר יש h1 ו 0 כשלא מכיל אלמנט h1
    children_of_element = element.find_elements(By.XPATH, ".//*")  # קבלת כל הילדים של האלמנט שהתקבל
    flat_list = flatten(children_of_element)

    #print("got the element children")
    #print(children_of_element)
    for elem in children_of_element:
        #print(elem.tag_name)
        if elem.tag_name == 'h1':
            is_there_is_h1 = 1
            h1_element = elem
            print("found h1")
            break
    print("finished : check_if_element_include_h1 ")

    return is_there_is_h1, h1_element
def return_h1_text(element: WebElement):
    innerHTML = element.get_attribute('innerHTML')  # קבלת כל התוכן של אלמנט ה h1
    text = element.text
    print("product name:")
    print(innerHTML)  # הדפסת שם הפריט!!!!
    print(text)  # הדפסת שם הפריט!!!!

    return text
#work
def check_if_element_include_h1_zmaniiiii():
    body = driver.find_elements(By.TAG_NAME, "body")[0]
    list_of_h1_elements = body.find_elements(By.XPATH, '//h1')  # שליפת כל h1 לתוך רשימה

    tag = list_of_h1_elements[0]
    print(tag.tag_name)
    print(tag)

    innerHTML = tag.get_attribute('innerHTML')  # קבלת כל התוכן של אלמנט ה h1
    print(innerHTML)#הדפסת שם הפריט!!!!

#didnt work- check why
def include_everything( add_tag_parent : WebElement):
    time.sleep(3)
    include_everything = 0
    include_everything_tag = " "
    can_be_the_father_element = add_tag_parent
    is_include_price = 0
    is_include_picture =[ ]
    is_include_h1 = [ ]
    insided_element = ""

    # #בדיקה לפני כניסה ל while אולי אנחנו כבר על התגית שמכילה את כולם
    # is_include_price = check_if_element_include_price(can_be_the_father_element)  # נשלח לבדיקת מחיר
    # is_include_picture = is_tag_include_picture(can_be_the_father_element)  # נשלח לבדיקת תמונות
    # is_include_h1 = check_if_element_include_h1(can_be_the_father_element)  # נשלח לבדיקת תיאור -h1
    # if is_include_price[0] == 1 and is_include_picture[0] == 1 and is_include_h1[0] == 1:
    #     include_everything = 1
    #     include_everything_tag = can_be_the_father_element
    #     print("התגית הראשונה שנשלחה מכילה את כל הדברים.")
    # else:
    #     print("התגית הראשונה שנשלחה לא מכילה את כל הדברים.")
    element_name = can_be_the_father_element.tag_name  #קבלת שם האלמנט כמחרוזת

    #מעבר על כל האלמנטים, בכל איטרציה עולים לאבא ובודקים האם הוא מכיל את כולם. במידה ולא עולים לאבא עד שמגיעים לאלמנט שמכיל את כולם או הגענו ל html ולא היה אלמנט שהכיל את כולם.
    while include_everything != 1 and element_name != "html" : # ירוץ כל עוד לא נמצא באב תמונה, מחיר ו- h1 או שהאב הוא html ואנחנו כבר לא מעוניינים לעלות יותר

        can_be_the_father_element = can_be_the_father_element.find_element(By.XPATH,'..') #נסיון 1 # נקבל את איבר האב של האובייקט הנוכחי
        #print("got the parent!!!!!!!!!!")
        #print(can_be_the_father_element.tag_name)

        #is_include_price = check_if_element_include_price(can_be_the_father_element)  # נשלח לבדיקת מחיר
        is_include_picture = is_tag_include_picture(can_be_the_father_element)  # נשלח לבדיקת תמונות
        if(is_include_picture[0]==1):
            #can_be_the_father_element = is_include_picture[1]
            #element_name = can_be_the_father_element.tag_name
            print(is_include_picture[1].tag_name)
            print("include pic")

            is_include_h1 = check_if_element_include_h1(can_be_the_father_element)  # נשלח לבדיקת תיאור -h1
            if is_include_h1[0] == 1:
                print("include h1")
                break

    if is_include_picture[0] == 1 and is_include_h1[0] == 1:
        include_everything = 1
        include_everything_tag = can_be_the_father_element

    # סיבות ליציאה מהwhile :

    # -1- הגענו לתגית הhtml
    # ז"א אין תמונה, מחיר ותיאור
    #-2- נמצאו תמונה, מחיר ותיאור
    #, is_include_price[1]
    result = [include_everything, include_everything_tag , is_include_picture[1], is_include_h1[1]]
    return result

    # מחזירה מערך:
    #[תיאור, מחיר, תמונה, אבא שמכיל את כולם ,האם מכיל את כולם או לא]
'''
def X_on_show_massage_that_jump_sometimes():#פונקציה שבודקת אם קפצה הודעה- ובמידה וכן לוחצת על X
    #list_of_buttons = []
    body = driver.find_elements(By.TAG_NAME, "body")[0]
    include_add_tag = 0
    list_of_button_elements = body.find_elements(By.XPATH, '//button')  # שליפת כל הכפתורים לתוך רשימה
    print("find buttons")
    for button in list_of_button_elements:
        list_of_attributes = button.get_property('attributes')#קבלת האטריביוטס של התגית
        for attribute in list_of_attributes:  # מעבר על attributes
            if attribute['value'].__contains__("action-close"):# אם ה attributes מכיל את הטקסט  "action-close" ללחוץ על הכפתור
              print("found massage box ")
              button.click()
              print("click on X")
              break
'''

def found_X(): #פונקציה שבודקת אם קפצה הודעה- ובמידה וכן מחזירה את כפתור ה X
    time.sleep(3)
    body = driver.find_elements(By.TAG_NAME, "body")[0]
    list_of_button_elements = body.find_elements(By.XPATH, '//button')  # שליפת כל הכפתורים לתוך רשימה
    X_element=''
    print("find buttons")
    for button in list_of_button_elements:
        list_of_attributes = button.get_property('attributes')#קבלת האטריביוטס של התגית
        for attribute in list_of_attributes:  # מעבר על attributes
            if attribute['value'].__contains__("action-close"):# אם ה attributes מכיל את הטקסט  "action-close" ללחוץ על הכפתור
               #print("found massage box that jump ")
               X_element = button
               break

    return X_element

def click_on_X():# פונקציה המחפשת את כפתור ה X כאשר קופצת הודעה ולוחצת עליו
    print("enter to : click_on_X ")
    X_element = found_X()# מציאת כפתור הX
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('useAutomationExtension', False)
    button = WebDriverWait(PATH, 10).until(EC.element_to_be_clickable(X_element))
    button.click()
    print("clicked on X")
    print("finished : click_on_X ")
















def Search_inputs(product_to_search):
    # בדיקה אם חלונית קפצה
    try:
        click_on_X()
    except:
        print("not found massage box!!!!")
    # שליפת כל האינפוטים בדף ובדיקה האם מכילים את המילה חיפוש
    current_url = driver.current_url
    list_of_elements = []
    list_of_attributes = []
    list_of_elements = driver.find_elements(By.XPATH, '//input')
    flag = 0  # דגל שאומר אם מצאנו תיבת חיפוש
    flag_send_keys = 0  # כאשר הערכים נשלחים לחיפוש בהצלחה
    correct_element = None


    for element in list_of_elements:
        #print(element.tag_name)
        if flag == 0 and list_of_elements != []:
            list_of_attributes = element.get_property('attributes')
            attributes = []
            for attribute in list_of_attributes:
                if attribute['value'].__contains__("search") or attribute['value'].__contains__("חיפוש"):
                    correct_element = element
                    flag = 1
                else:
                    break


    if flag == 1:
        correct_element.clear() #למחוק את התוכן שקיים מחיפוש קודם!!!!!
        correct_element.send_keys(product_to_search)
        time.sleep(3)
        correct_element.send_keys(Keys.ENTER)
        print("enter!")

        flag_send_keys = 1
    current_url = driver.current_url
    result = []
    result = flag_send_keys, current_url
    print("is found: ")
    print(result[0])
    return result

def button_to_search_if_search_input_didnt_work(product_to_search):  # פונקציה שמחפשת כפתור של חיפוש ולוחצת עליו במקרה שלא נמצא input של חיפוש
    print("enter to: button_to_search_if_search_input_didnt_work")

    # בדיקה אם חלונית קפצה
    try:
        click_on_X()
    except:
        print("not found massage box!!!!")

    list_of_elements = []
    list_of_attributes = []
    list_of_elements = driver.find_elements(By.XPATH, '//button')  # קבלת כל ה button שבדף
    flag_found_button_search = 0
    flag_search_input_work = [ ]
    correct_element = None

    for element in list_of_elements:  # מעבר על כל הכפתורים שנמצאו. לכל כפתור שולפים את ה attribute שלו
        if flag_found_button_search == 0 and list_of_elements != []:
            list_of_attributes = element.get_property('attributes')
            attributes = []
            for attribute in list_of_attributes:  # עוברים על כל attribute ובודקים אם הוא מכיל "חיפוש" או "search"
                if attribute['value'].__contains__("search") or attribute['value'].__contains__("חיפוש"):
                    correct_element = element  # במידה ונמצא כפתור חיפוש שומרים אותו ויוצאים מהלולאה
                    flag_found_button_search = 1
                else:
                    break

    correct_element.click()  # לוחצים על הכפתור ע"מ שיוכלו להפעיל כעת את הפונקציה שמוצאת את תיבת החיפוש ומקלידה לתוכה ערכים

    flag_search_input_work = Search_inputs(product_to_search)  # הקלדה לאחר הלחיצה

    if flag_search_input_work[0] == 1:
        print("the search work!!!")
    return flag_search_input_work[0], flag_search_input_work[1]
    flag_search_input_work = Search_inputs(product_to_search)

def a_to_search_if_search_input_didnt_work(product_to_search):  # פונקציה שמחפשת a של חיפוש ולוחצת עליו במקרה שלא נמצא input של חיפוש
    print("enter to : a_to_search_if_search_input_didnt_work")

    #בדיקה אם חלונית קפצה
    try:
        click_on_X()
    except:
        print("not found massage box!!!!")


    list_of_elements = []
    list_of_attributes = []
    list_of_elements = driver.find_elements(By.XPATH, '//a')  # קבלת כל ה a שבדף
    flag = 0
    flag_search_input_work = []
    correct_element = None

    for element in list_of_elements:  # מעבר על כל ה -a שנמצאו. לכל a שולפים את ה attribute שלו
        if flag == 0 and list_of_elements != []:
            list_of_attributes = element.get_property('attributes')
            attributes = []
            for attribute in list_of_attributes:  # עוברים על כל attribute ובודקים אם הוא מכיל "חיפוש" או "search"

                if attribute['value'].__contains__("search") or attribute['value'].__contains__("חיפוש"):
                    correct_element = element  # במידה ונמצא a חיפוש שומרים אותו ויוצאים מהלולאה
                    flag = 1
                else:
                    break

    correct_element.click()  # לוחצים על a ע"מ שיוכלו להפעיל כעת את הפונקציה שמוצאת את תיבת החיפוש ומקלידה לתוכה ערכים

    flag_search_input_work = Search_inputs(product_to_search) #הקלדה לאחר הלחיצה

    if flag_search_input_work[0] == 1:
        print("the search work!!!")
        print(flag_search_input_work[1])
    return flag_search_input_work[0], flag_search_input_work[1]

def typing_in_input(product_to_search):# פונקציה שמקלידה גם כאשר יש כפתור ללחוץ עליו קודם או a
    result = []
    print("enter to: typing_in_input")
    try:# אם התיבת טקסט מוצגת
        result = Search_inputs(product_to_search)
        if result[0] == 1:
            result = Search_inputs(product_to_search)[0]
            print("Search_inputs work")
            return result
    except:
        print("Search_inputs not work")
    try:# אם צריך ללחוץ על כפתור ואח"כ למצוא את התיבת טקסט
        result = button_to_search_if_search_input_didnt_work(product_to_search)
        print("button_to_search_if_search_input_didnt_work work")
        return result
    except:
        print("button_to_search_if_search_input_didnt_work not work")
    try:# אם צריך ללחוץ על a ואח"כ למצוא את התיבת טקסט
        result = a_to_search_if_search_input_didnt_work(product_to_search)
        print("a_to_search_if_search_input_didnt_work work")
        return result
    except:# בכל מקרה אחר
        print("nothing work")
        #return 0,0###

def loop_on_site_main(product_to_search):#פונקציה שעוברת על כל האתרים ובעבור כל אחד מקלידה את שם המוצר ומחזירה רשימה של קישורים לכל האתרים במידה ונמצאו תוצאות
    print("enter to : loop_on_site_main")
    list_of_site_after_search = []# מחזיר 3 קישורים לאתרים לאחר החיפוש שמשם צריך לשלוף את המוצרים היחידים
    driver.get("https://www.castro.com/")
    try:
        click_on_X()
    except:
        print("not found massage box!!!!")
    ans = typing_in_input(product_to_search)
    #print(ans[1])
    list_of_site_after_search.append(ans[1])
    print("searched in CASTRO")# הכנסת הקישור של תוצאות החיפוש למקום הראשון במערך

    #search_message_box_not_found_result()
    driver.get("https://www.hoodies.co.il/")
    try:
        click_on_X()
    except:
        print("not found massage box!!!!")
    ans = typing_in_input(product_to_search)
    #print(ans[1])
    list_of_site_after_search.append(ans[1])# הכנסת הקישור של תוצאות החיפוש למקום השני במערך

    #search_message_box_not_found_result()
    driver.get("https://www.terminalx.com/")
    try:
        click_on_X()
    except:
        print("not found massage box!!!!")
    ans = typing_in_input(product_to_search)
    #print(ans[1])
    list_of_site_after_search.append(ans[1])# הכנסת הקישור של תוצאות החיפוש למקום השלישי במערך
    print("finished : loop_on_site_main")
    return list_of_site_after_search

list_of_add_tags = find_add_tag()  # חיפוש ההוספה לסל
print(list_of_add_tags)
add_tag = list_of_add_tags[-1]# לקיחת תגית ההוספה לסל האחרונה

is_there_is_everything = include_everything(add_tag)# בדיקה אם אנחנו על מוצר יחיד
print("is_there_is_everything:")

print(is_there_is_everything[3].tag_name)
product_to_search = return_h1_text(is_there_is_everything[3]) # שליפת שם המוצר מתוך תגית ה h1
print(product_to_search)
urls_after_search = []
#url_after_search = typing_in_input(product_to_search)
#print(url_after_search[1])
urls_after_search =loop_on_site_main(product_to_search)
print("URLS after search")
print(urls_after_search)#קישורים ל-תוצאות החיפוש ב-3 האתרים




driver.close()


'''
product_to_search = return_h1_text(is_there_is_everything[3])
#product_to_search = is_there_is_everything[2]
typing_in_input(product_to_search)
'''







