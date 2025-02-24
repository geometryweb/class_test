class Student:
    def __init__(self, korean, english, Mathematics, science, social_studies):
        self.__korean = korean
        self.__english = english
        self.__Mathematics = Mathematics
        self.__science = science
        self.__social_studies = social_studies
    def student_sum(self):  
        self.__total = self.__korean + self.__english + self.__Mathematics\
            + self.__science + self.__social_studies 
        return self.__total
    def student_average(self):
        self.__total_number = 5     
        return self.__total/self.__total_number
    def __eq__(self, other):
        return self.student_sum() == other.student_sum()
    def __ne__(self, other):
        return self.student_sum() != other.student_sum()