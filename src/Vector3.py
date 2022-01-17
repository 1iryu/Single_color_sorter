import re


class Vector3:

    #Vector3("x, y, z")
    def __init__(self, text: str):
        vector3 = self.convert_text_to_vector3(text)
        self.x = vector3[0]
        self.y = vector3[1]
        self.z = vector3[2]

    def convert_text_to_vector3(self, text: str):
        pattern = re.compile(r',')
        result = pattern.split(text.replace(' ', ''))
        int_result = []
        for vector in result:
            int_result.append(int(vector))
        return int_result
