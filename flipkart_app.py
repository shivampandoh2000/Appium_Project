from appium import webdriver

desired_cap = {
    "appium:deviceName": "Android Emulator",
    "platformName": "Android",
    "appium:app": "C:\\Users\\USER\\Downloads\\Flipkart-7.18.apk",
    "appium:appPackage": "com.flipkart.android",
    "appium:appWaitActivity": "com.flipkart.android.activity.FirstLaunchActivity"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)

driver.implicitly_wait(30)


# UTILS: XPATH's
xpath_for_Lang_eng = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout" \
                     "/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget" \
                     ".RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[" \
                     "1]/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[" \
                     "6]/android.widget.RelativeLayout "

xpath_for_switch_to_email = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget" \
                            ".FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget" \
                            ".FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android" \
                            ".widget.LinearLayout/android.widget.RelativeLayout[" \
                            "2]/android.widget.LinearLayout/android.widget.TextView "


# Step1: Language Select
driver.find_element_by_xpath(xpath_for_Lang_eng).click()

driver.find_element_by_id("com.flipkart.android:id/select_btn").click()


# Step2: Use email-id login
driver.find_element_by_xpath(xpath_for_switch_to_email).click()
driver.implicitly_wait(30)

# Step3: Enter Email [Before Running: Enter Valid Email]
driver.find_element_by_id("com.flipkart.android:id/phone_input").send_keys("")

driver.find_element_by_id("com.flipkart.android:id/button").click()
driver.implicitly_wait(30)

#  Step4: Enter Passcode[Before Execution: Enter Valid Passcode]
driver.find_element_by_id("com.flipkart.android:id/phone_input").send_keys("")

driver.find_element_by_id("com.flipkart.android:id/button").click()
