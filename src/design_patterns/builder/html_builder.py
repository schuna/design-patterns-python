class HtmlBuilder:
    def __init__(self, html_root_element):
        self.__root = html_root_element

    def add_child(self, html_element):
        self.__root.elements.append(html_element)

    def add_child_fluent(self, html_element):
        self.__root.elements.append(html_element)
        return self

    def __str__(self):
        return str(self.__root)
