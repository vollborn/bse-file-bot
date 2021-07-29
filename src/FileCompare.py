import json
from src.Course import Course


class FileCompare:
    file = "storage/courses.json"

    def __init__(self):
        self.courses = []

    def load_file(self):
        try:
            f = open(self.file)
            course_dicts = json.load(f)
            f.close()

            for course_dict in course_dicts:
                course = Course(course_dict["name"], course_dict["id"])
                course.resources = course_dict["resources"]
                self.courses.append(course)

        except:
            print("Error while loading course file.")

    def write_file(self, courses):
        f = open(self.file, "w")
        f.write(json.dumps([course.__dict__ for course in courses]))
        f.close()

    def compare(self, current_courses):
        self.load_file()
        self.write_file(current_courses)

        existing_course_ids = []

        for course in self.courses:
            existing_course_ids.append(course.id)

            for current_course in current_courses:
                if course.id == current_course.id:
                    # compare resources
                    to_remove = []
                    for current_resource in current_course.resources:
                        if current_resource in course.resources:
                            to_remove.append(current_resource)
                    
                    for remove in to_remove:
                        current_course.resources.remove(remove)

        # remove courses, that have no resources and existed beforehand
        remove_ids = []

        for course in current_courses:
            if len(course.resources) == 0 and course.id in existing_course_ids:
                remove_ids.append(course.id)

        new_courses = []
        for course in current_courses:
            if course.id not in remove_ids:
                new_courses.append(course)

        return new_courses
