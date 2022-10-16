class CV:
    def __init__(self,full_name, birth_year ,phone_number, email_address, city_adress , nationality ,gender, language, language_lavel):
        self.full_name = full_name
        self.birth_year = birth_year
        self.phone_number = phone_number
        self.email_address = email_address
        self.city_adress = city_adress
        self.nationality = nationality
        self.gender = gender
        self.language = language
        self.language_lavel = language_lavel

    def __str__(self):

        bio_part = f"I'm {self.full_name} , I was born in {self.birth_year} , '\n' - Contact me via phone number or e-mail : '\n' {self.phone_number} / {self.email_address} . '\n' - I live in {self.city_adress} , my nationality is {self.nationality}, '\n'-And my gender is {self.gender}"

        line1 = "'\n' ________"

        language_part= f"'\n'- {self.language} language , {self.language_lavel}"

        total_parts = bio_part +line1+ language_part

        return total_parts

    
        



cv1 = CV("noor", 1995, 785131, "eng@gmail.com", "amman", "jordanian","femail", "english", "veryGood")
print (cv1)


class Functional_cv (CV):
    def __init__(self, * , education ,school,city,education_date):
        super().__init__(self)
        self.education = education
        self.school = school
        self.city = city
        self.education_date = education_date

    def func(self):

        education_part = f"I got an {self.education} degree from the {self.school} University in {self.city} and finished my studies in a period of {self.education_date}"

        return education_part

# cv2 = Functional_cv("noor", 1995, 785131, "eng@gmail.com", "amman", "jordanian","femail", "english", "veryGood","engineering" ,"Hashimite", "Zarqa", "4 years")
# print (cv2)


class Combination_cv (Functional_cv):
    def __init__(self, experiance, company, duration, description):
        super().__init__() 
        self.experiance = experiance
        self.company = company
        self.duration = duration
        self.description = description    

class Chronological_Resumes_cv (CV):
    def __init__(self, experiance, company, duration, description):
        super().__init__() 
        self.experiance = experiance
        self.company = company
        self.duration = duration
        self.description = description 
        




