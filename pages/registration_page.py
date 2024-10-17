import os

from selene import browser, be, have

from data.users import User


class RegistrationPage:

    def open_form(self):
        browser.open('https://demoqa.com/automation-practice-form')

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

    def should_registered_user(self, user: User):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{user.first_name} {user.last_name}',
                user.email,
                user.gender,
                user.phone,
                f"{user.day} {user.month},{user.year}",
                user.subject,
                user.hobbies,
                user.picture_name,
                user.address,
                f"{user.state} {user.city}"
            )
        )
        return self

    def register_user(self, user: User):
        self.fill_full_name(user.first_name, user.last_name)
        self.fill_email(user.email)
        self.choose_gender(user.gender)
        self.fill_phone(user.phone)
        self.select_date_of_birth(user.day, user.month, user.year)
        self.fill_subject(user.subject)
        self.upload_picture(user.picture)
        self.fill_adress(user.address)
        self.choose_hobby(user.hobbies)
        self.select_state_and_city(user.state, user.city)
        self.submit()
        return self
