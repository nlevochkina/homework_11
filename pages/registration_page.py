import os

from selene import browser, be, have


class RegistrationPage:

    def open_form(self):
        browser.open('/automation-practice-form')

        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def fill_full_name(self, first_name, last_name):
        browser.element('#firstName').should(be.blank).type(first_name)
        browser.element('#lastName').should(be.blank).type(last_name)

    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)

    def choose_gender(self, value):
        browser.element(f"//label[text()='{value}']").click()

    def fill_phone(self, value):
        browser.element('#userNumber').should(be.blank).type(value)

    def select_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(f'//*[text()="{month}"]').click()

        browser.element('.react-datepicker__year-select').click()
        browser.element(f'//*[text()={year}]').click()
        browser.element(f'//div[text()={day}]').click()

    def fill_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def fill_adress(self, value):
        browser.element('#currentAddress').should(be.blank).type(value)

    def choose_hobby(self, value):
        browser.element(f"//label[text()='{value}']").click()

    def upload_picture(self, path):
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        image_path = os.path.join(project_root, path)
        browser.element('#uploadPicture').send_keys(image_path)

    def select_state_and_city(self, state, city):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.text(state)).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.text(city)).click()

    def submit(self):
        browser.element('#submit').press_enter()

    def should_registered_user_with(self, fill_full_name, fill_email, choose_gender, fill_phone, select_date_of_birth,
                                    fill_subject, fill_adress, choose_hobby, upload_picture, select_state_and_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                fill_full_name,
                fill_email,
                choose_gender,
                fill_phone,
                select_date_of_birth,
                fill_subject,
                upload_picture,
                fill_adress,
                choose_hobby,
                select_state_and_city
            )
        )
        return self
