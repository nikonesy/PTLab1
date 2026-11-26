# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

from DataReader import DataReader
from Types import DataType


class XmlDataReader(DataReader):
    """Читает данные о студентах из файла формата XML.

    Ожидаемая структура файла (см. data/data.xml)::

        <?xml version="1.0" encoding="UTF-8"?>
        <root>
          <student name="Иванов Иван Иванович">
            <subject name="математика" score="91"/>
            <subject name="химия" score="100"/>
          </student>
        </root>
    """

    def read(self, path: str) -> DataType:
        tree = ET.parse(path)
        root = tree.getroot()

        students: DataType = {}
        for student in root.findall("student"):
            name = (student.get("name") or "").strip()
            students[name] = []
            for subject in student.findall("subject"):
                title = (subject.get("name") or "").strip()
                score = int(subject.get("score") or 0)
                students[name].append((title, score))
        return students
