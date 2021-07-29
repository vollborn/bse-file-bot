from src.Course import Course
import html
import requests


class FileFetcher:
    base_url = "https://bs-elmshorn.schul-moodle.de"
    session = requests.Session()
    courses = []

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        login_url = self.base_url + "/login/index.php"

        get_response = self.session.get(login_url)

        search_text = '<input type="hidden" name="logintoken" value="'
        if get_response.text.find(search_text) == -1:
            return False
        search_index = get_response.text.index(search_text)

        token_index = search_index + len(search_text)
        token = get_response.text[token_index:token_index + 32]

        post_response = self.session.post(login_url, {
            'anchor': '',
            'username': self.username,
            'password': self.password,
            'logintoken': token
        })

        if post_response.text.find("Ungültige Anmeldedaten") != -1:
            return False

        return True

    def get_courses(self):
        profile_url = self.base_url + "/user/profile.php"
        profile_response = self.session.get(profile_url)

        search_in = profile_response.text

        search_text = "Kursprofile"
        if search_in.find(search_text) == -1:
            return False
        search_in = search_in[search_in.index(search_text):]

        search_text = "</ul>"
        if search_in.find(search_text) == -1:
            return False
        search_in = search_in[:search_in.index(search_text)]

        course_id_begin = 'course='
        course_id_end = '">'
        course_name_end = '</a>'

        while search_in.find(course_id_begin) != -1:
            id_index = search_in.index(course_id_begin) + len(course_id_begin)
            search_in = search_in[id_index:]

            id_end_index = search_in.index(course_id_end)
            id = search_in[:id_end_index]
            search_in = search_in[id_end_index + len(course_id_end):]

            name = search_in[:search_in.index(course_name_end)]

            course = Course(name, id)
            self.get_course_files(course)

            self.courses.append(course)

        return True

    def get_course_files(self, course):
        course_response = self.session.get(self.base_url + "/course/view.php?id=" + course.id)

        course.add_resources_from_string(course_response.text)

        search_in = course_response.text
        cut_at = "section-title"

        sections = []
        section_link_start = 'href="'
        section_link_end = '"'

        while search_in.find(cut_at) != -1:
            search_in = search_in[search_in.index(cut_at):]
            search_in = search_in[search_in.index(section_link_start) + len(section_link_start):]
            end_index = search_in.index(section_link_end)
            section = search_in[:end_index]
            search_in = search_in[end_index:]

            if section.startswith(self.base_url):
                sections.append(section)

        for section in sections:
            url = html.unescape(section)
            section_response = self.session.get(url)
            course.add_resources_from_string(section_response.text)
