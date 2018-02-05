import pyexcel

a_list_of_dictionaries = [
    {
        "title": "SU25",
        "link": "https://google.com.vn"
    },
    {
        "title": "SU25-2",
        "link": "https://google-2.com.vn"
    },
    {
        "title": "SU25-3",
        "link": "https://google-3.com.vn"
    }
]

pyexcel.save_as(records=a_list_of_dictionaries, dest_file_name="excel.xlsx")
