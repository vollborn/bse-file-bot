
class Course:

    def __init__(self, name, id):
        self.id = id
        self.name = name
        self.resources = []

    def add_resources_from_string(self, string):
        search_in = string

        resource_begin = 'class="instancename">'
        resource_ends = ['<span', '</span>']
        while search_in.find(resource_begin) != -1:
            search_in = search_in[search_in.index(resource_begin) + len(resource_begin):]

            end_indexes = []
            for resource_end in resource_ends:
                if search_in.find(resource_end) != -1:
                    end_indexes.append(search_in.index(resource_end))

            resource = search_in[:min(end_indexes)]
            if resource not in self.resources:
                self.resources.append(resource)
