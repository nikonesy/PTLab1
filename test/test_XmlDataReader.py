# -*- coding: utf-8 -*-
import pytest

from src.Types import DataType
from src.XmlDataReader import XmlDataReader


class TestXmlDataReader:

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        text = (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<root>\n'
            '  <student name="Иванов Иван Иванович">\n'
            '    <subject name="математика" score="91"/>\n'
            '    <subject name="химия" score="100"/>\n'
            '  </student>\n'
            '  <student name="Петров Петр Петрович">\n'
            '    <subject name="русский язык" score="87"/>\n'
            '    <subject name="литература" score="78"/>\n'
            '  </student>\n'
            '</root>\n'
        )

        data: DataType = {
            "Иванов Иван Иванович": [
                ("математика", 91), ("химия", 100)
            ],
            "Петров Петр Петрович": [
                ("русский язык", 87), ("литература", 78)
            ]
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, DataType],
                          tmp_path) -> tuple[str, DataType]:
        p = tmp_path / "my_data.xml"
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = XmlDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]

    def test_read_real_data_file(self) -> None:
        data = XmlDataReader().read("data/data.xml")
        assert len(data) == 10
        assert data["Абрамов Петр Сергеевич"] == [
            ("математика", 80), ("русский язык", 76),
            ("программирование", 100)
        ]
