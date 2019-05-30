class CalUtils:

    def __init__(self):
        self.names = []
        self.heights = []
        self.totalStudentHeight = 0
        self.totalStudentCount = 0
        self.denominator_in_file = "\t"  # name and height is separated with this character(s)
        self.count = 0
        self.file_name = "listOfStudentHeight.txt"
        file = open(self.file_name, "r")
        self.students_unparsed = file.read()
        file.close()

    def calculator(self, name , height):

        for i in self.students_unparsed.split("\n"):
            user_list = i.split("\t")
            height = float(user_list[1])
            self.heights.append(height)
            self.totalStudentCount += 1
            self.totalStudentHeight += height

    def calAvgHeight(self):
        avg = self.totalStudentHeight / self.totalStudentCount
        print("Student average height is {0:.2f} m for {1} students.".format(avg, self.totalStudentCount))
        self.names = []
        self.heights = []
        self.totalStudentHeight = 0
        self.totalStudentCount = 0
        self.count +=1
        self.totalStudentCount += self.count
        exit()

    def addStudent(self, name, height):
        self.names.append(name)
        self.heights.append(height)
        self.totalStudentCount += 1
        self.totalStudentHeight += height


cal_utils = CalUtils()
if __name__ == "__main__":

    while True:
        input_text = input("Add another student? (Y or N):\nTo exit: (Ctrl+C)\n")
        if input_text.upper() == 'Y':
            name , height = input("Name and height separated by tab:\n").split("\t")
            height = float(height)
            file = open("listOfStudentHeight.txt", "a")
            file.write(f"\n{name}\t{height}")
            cal_utils.addStudent(name, height)
            cal_utils.calculator(name, height)
            cal_utils.calAvgHeight()
            file.close()
        else:
            cal_utils.calculator("", "")
            cal_utils.calAvgHeight()